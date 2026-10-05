from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver


# -----------------------------
# State definition
# -----------------------------

class ConversationState(TypedDict):
    user_input: str
    category: str
    response: str
    conversation_count: int


# -----------------------------
# Node 1: Classify
# -----------------------------

def classify(state: ConversationState):

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

    print(f"[Classify] Category: {category}")

    return {
        "category": category
    }


# -----------------------------
# Node 2: Route
# -----------------------------

def route(state: ConversationState):

    print(f"[Route] Routing: {state['category']}")

    return {}


# -----------------------------
# Node 3: Respond
# -----------------------------

def respond(state: ConversationState):

    category = state["category"]
    count = state["conversation_count"] + 1

    if category == "technical":

        response = (
            "I can help you with Python, programming, "
            "and LangGraph."
        )

    elif category == "greeting":

        response = "Hello! How can I help you today?"

    else:

        response = (
            "This is a general question. "
            "I will try to help you."
        )

    print(f"[Respond] {response}")

    return {
        "response": response,
        "conversation_count": count
    }


# -----------------------------
# Conditional routing
# -----------------------------

def route_condition(state: ConversationState):

    return state["category"]


# -----------------------------
# Build LangGraph
# -----------------------------

builder = StateGraph(ConversationState)

builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("respond", respond)

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

builder.add_edge("respond", END)


# -----------------------------
# Persistent memory
# -----------------------------

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# -----------------------------
# Test conversation
# -----------------------------

if __name__ == "__main__":

    print("\n======================================")
    print("W10D3 LANGGRAPH + MEMORY")
    print("======================================")

    config = {
        "configurable": {
            "thread_id": "w10d3-demo"
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
                "conversation_count": 0,
            },
            config
        )

        print(f"Final Response: {result['response']}")
        print(
            f"Conversation Count: "
            f"{result['conversation_count']}"
        )

    print("\n======================================")
    print("5 TESTS COMPLETED")
    print("======================================")