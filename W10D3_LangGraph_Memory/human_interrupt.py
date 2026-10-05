from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


class ApprovalState(TypedDict):
    user_input: str
    approval: str
    response: str


def ask_for_approval(state: ApprovalState):

    print("\n[Human Review Required]")

    decision = interrupt(
        "Do you approve this request? Type yes or no."
    )

    return {
        "approval": decision
    }


def respond(state: ApprovalState):

    if state["approval"].lower() == "yes":
        response = "Request approved successfully."
    else:
        response = "Request rejected by human reviewer."

    print(f"[Respond] {response}")

    return {
        "response": response
    }


builder = StateGraph(ApprovalState)

builder.add_node("approval", ask_for_approval)
builder.add_node("respond", respond)

builder.add_edge(START, "approval")
builder.add_edge("approval", "respond")
builder.add_edge("respond", END)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


if __name__ == "__main__":

    config = {
        "configurable": {
            "thread_id": "w10d3-human-review"
        }
    }

    print("\n======================================")
    print("W10D3 HUMAN-IN-THE-LOOP TEST")
    print("======================================")

    result = graph.invoke(
        {
            "user_input": "Create a deployment",
            "approval": "",
            "response": "",
        },
        config
    )

    print("\nGraph paused for human approval.")
    print("Interrupt information:")
    print(result)

    print("\nResuming with approval: yes")

    result = graph.invoke(
        Command(resume="yes"),
        config
    )

    print("\nFinal Response:")
    print(result["response"])

    print("\n======================================")
    print("HUMAN-IN-THE-LOOP TEST COMPLETED")
    print("======================================")