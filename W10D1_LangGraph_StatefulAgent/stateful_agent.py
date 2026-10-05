from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# ============================================================
# STATE
# ============================================================

class AgentState(TypedDict):
    user_input: str
    category: str
    response: str


# ============================================================
# NODE 1 — CLASSIFY
# ============================================================

def classify(state: AgentState):
    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["python", "code", "programming"]):
        category = "technical"

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        category = "greeting"

    else:
        category = "general"

    print(f"[Classify] Category: {category}")

    return {
        "category": category
    }


# ============================================================
# NODE 2 — ROUTE
# ============================================================

def route(state: AgentState):
    category = state["category"]

    print(f"[Route] Routing to: {category}")

    return {}


# ============================================================
# NODE 3 — RESPOND
# ============================================================

def respond(state: AgentState):
    category = state["category"]

    if category == "technical":
        response = "This is a technical question. I can help with Python and programming."

    elif category == "greeting":
        response = "Hello! How can I help you today?"

    else:
        response = "This is a general question. I will try to help you."

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# ============================================================
# CONDITIONAL ROUTING
# ============================================================

def route_condition(state: AgentState):
    return state["category"]


# ============================================================
# BUILD GRAPH
# ============================================================

builder = StateGraph(AgentState)

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
    }
)

builder.add_edge("respond", END)

graph = builder.compile()


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    test_inputs = [
        "Hello bro",
        "How can I learn Python?",
        "Write a programming program",
        "What is your name?",
        "Hey, can you help me?"
    ]

    print("\n==============================================")
    print("W10D1 STATEFUL LANGGRAPH AGENT")
    print("==============================================")

    for user_input in test_inputs:

        print(f"\nInput: {user_input}")

        result = graph.invoke({
            "user_input": user_input,
            "category": "",
            "response": ""
        })

        print(f"Final Response: {result['response']}")

    print("\n==============================================")
    print("5 TESTS COMPLETED")
    print("==============================================")
from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    user_input: str
    category: str
    response: str


# Node 1: Classify the user input
def classify(state: AgentState):
    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["python", "code", "programming"]):
        category = "technical"
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        category = "greeting"
    else:
        category = "general"

    print(f"[Classify] Category: {category}")

    return {"category": category}


# Node 2: Route based on classification
def route(state: AgentState):
    print(f"[Route] Routing: {state['category']}")
    return {}


# Node 3: Generate response
def respond(state: AgentState):
    category = state["category"]

    if category == "technical":
        response = "This is a technical question. I can help with Python and programming."
    elif category == "greeting":
        response = "Hello! How can I help you today?"
    else:
        response = "This is a general question. I will try to help you."

    print(f"[Respond] {response}")

    return {"response": response}


# Conditional routing
def route_condition(state: AgentState):
    return state["category"]


# Build graph
builder = StateGraph(AgentState)

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

graph = builder.compile()


# Test with 5 inputs
if __name__ == "__main__":

    test_inputs = [
        "Hello bro",
        "How can I learn Python?",
        "Write a programming program",
        "What is your name?",
        "Hey, can you help me?",
    ]

    print("\n==============================================")
    print("W10D1 STATEFUL LANGGRAPH AGENT")
    print("==============================================")

    for user_input in test_inputs:

        print(f"\nInput: {user_input}")

        result = graph.invoke(
            {
                "user_input": user_input,
                "category": "",
                "response": "",
            }
        )

        print(f"Final Response: {result['response']}")

    print("\n==============================================")
    print("5 TESTS COMPLETED")
    print("==============================================")