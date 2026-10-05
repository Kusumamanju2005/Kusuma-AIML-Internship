from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# ---------------------------------
# State
# ---------------------------------

class AgentState(TypedDict):
    user_input: str
    category: str
    response: str


# ---------------------------------
# Node 1: Classify
# ---------------------------------

def classify(state: AgentState):

    user_input = state["user_input"].lower()

    if any(word in user_input for word in [
        "python",
        "code",
        "programming",
        "langgraph"
    ]):
        category = "technical"

    elif any(word in user_input for word in [
        "hello",
        "hi",
        "hey"
    ]):
        category = "greeting"

    else:
        category = "general"

    print(f"[Classify] {category}")

    return {
        "category": category
    }


# ---------------------------------
# Node 2: Route
# ---------------------------------

def route(state: AgentState):

    print(f"[Route] Sending request to: {state['category']}")

    return {}


# ---------------------------------
# Node 3: Respond
# ---------------------------------

def respond(state: AgentState):

    category = state["category"]

    if category == "technical":
        response = (
            "This is a technical request. "
            "I can help with Python and LangGraph."
        )

    elif category == "greeting":
        response = "Hello! How can I help you today?"

    else:
        response = (
            "This is a general request. "
            "I will try to help you."
        )

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# ---------------------------------
# Conditional routing
# ---------------------------------

def route_condition(state: AgentState):

    return state["category"]


# ---------------------------------
# Human-in-the-loop
# ---------------------------------

def human_approval(state: AgentState):

    decision = interrupt(
        f"Human approval required for: {state['user_input']}. "
        "Type yes to approve or no to reject."
    )

    if str(decision).lower() == "yes":
        response = "Request approved successfully."
    else:
        response = "Request rejected by human reviewer."

    return {
        "response": response
    }


# ---------------------------------
# Build graph
# ---------------------------------

builder = StateGraph(AgentState)

builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("respond", respond)
builder.add_node("human_approval", human_approval)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")

builder.add_conditional_edges(
    "route",
    route_condition,
    {
        "technical": "respond",
        "greeting": "respond",
        "general": "respond",
    },
)

builder.add_edge("respond", "human_approval")
builder.add_edge("human_approval", END)


# ---------------------------------
# Memory / Checkpoint
# ---------------------------------

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# ---------------------------------
# Test
# ---------------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("W10D4 HUMAN-IN-THE-LOOP LANGGRAPH")
    print("======================================")

    config = {
        "configurable": {
            "thread_id": "w10d4-demo"
        }
    }

    test_inputs = [
        "Hello bro",
        "How can I learn Python?",
        "What is LangGraph?",
        "What is your name?",
        "Hey bro, can you help me?"
    ]

    for user_input in test_inputs:

        print(f"\nInput: {user_input}")

        result = graph.invoke(
            {
                "user_input": user_input,
                "category": "",
                "response": "",
            },
            config
        )

        print("Graph paused for human approval.")
        print("Interrupt:", result)

        result = graph.invoke(
            Command(resume="yes"),
            config
        )

        print("Human Decision: yes")
        print("Final Response:", result["response"])

    print("\n======================================")
    print("W10D4 TEST COMPLETED")
    print("======================================")