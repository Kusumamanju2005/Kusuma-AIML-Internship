from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import MemorySaver


class HumanState(TypedDict):
    user_input: str
    approval: str
    response: str


def human_review(state: HumanState):

    decision = interrupt(
        "Human review required. Enter APPROVE or REJECT."
    )

    return {
        "approval": decision
    }


def respond(state: HumanState):

    if str(state["approval"]).upper() == "APPROVE":
        response = f"Request approved: {state['user_input']}"
    else:
        response = f"Request rejected: {state['user_input']}"

    print(f"[Respond] {response}")

    return {
        "response": response
    }


builder = StateGraph(HumanState)

builder.add_node("human_review", human_review)
builder.add_node("respond", respond)

builder.add_edge(START, "human_review")
builder.add_edge("human_review", "respond")
builder.add_edge("respond", END)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


if __name__ == "__main__":

    print("\n======================================")
    print("W10D2 HUMAN-IN-THE-LOOP TEST")
    print("======================================")

    config = {
        "configurable": {
            "thread_id": "w10d2-demo"
        }
    }

    result = graph.invoke(
        {
            "user_input": "Generate a research report",
            "approval": "",
            "response": ""
        },
        config
    )

    print("\nWorkflow paused.")
    print("Human approval is required.")

    human_input = input(
        "\nEnter APPROVE or REJECT: "
    )

    result = graph.invoke(
        Command(resume=human_input),
        config
    )

    print("\nWorkflow resumed successfully.")

    print("\nFinal Response:")
    print(result["response"])

    print("\n======================================")
    print("HUMAN-IN-THE-LOOP TEST COMPLETED")
    print("======================================")