from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import MemorySaver


# ============================================================
# STATE
# ============================================================

class HumanState(TypedDict):
    user_input: str
    human_approval: str
    response: str


# ============================================================
# NODE 1 — HUMAN REVIEW
# ============================================================

def human_review(state: HumanState):

    decision = interrupt(
        "Human review required. Type APPROVE or REJECT."
    )

    return {
        "human_approval": decision
    }


# ============================================================
# NODE 2 — RESPOND
# ============================================================

def respond(state: HumanState):

    if str(state["human_approval"]).upper() == "APPROVE":
        response = f"Request approved: {state['user_input']}"
    else:
        response = f"Request rejected: {state['user_input']}"

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# ============================================================
# BUILD GRAPH
# ============================================================

builder = StateGraph(HumanState)

builder.add_node("human_review", human_review)
builder.add_node("respond", respond)

builder.add_edge(START, "human_review")
builder.add_edge("human_review", "respond")
builder.add_edge("respond", END)


# MemorySaver allows the workflow to pause and resume
memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# ============================================================
# TEST HUMAN-IN-THE-LOOP
# ============================================================

if __name__ == "__main__":

    print("\n==============================================")
    print("W10D1 HUMAN-IN-THE-LOOP TEST")
    print("==============================================")

    config = {
        "configurable": {
            "thread_id": "w10d1-demo"
        }
    }

    # --------------------------------------------------------
    # STEP 1 — START WORKFLOW
    # --------------------------------------------------------

    result = graph.invoke(
        {
            "user_input": "Generate a research report",
            "human_approval": "",
            "response": ""
        },
        config
    )

    print("\nWorkflow paused.")
    print("Human approval is required.")

    # --------------------------------------------------------
    # STEP 2 — HUMAN INPUT
    # --------------------------------------------------------

    human_input = input(
        "\nEnter APPROVE or REJECT: "
    )

    # --------------------------------------------------------
    # STEP 3 — RESUME WORKFLOW
    # --------------------------------------------------------

    result = graph.invoke(
        Command(resume=human_input),
        config
    )

    print("\nWorkflow resumed successfully.")

    print("\nFinal Response:")
    print(result["response"])

    print("\n==============================================")
    print("HUMAN-IN-THE-LOOP TEST COMPLETED")
    print("==============================================")