from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# State definition
class AgentState(TypedDict):
    user_input: str
    category: str
    response: str


# Node 1: Classify input
def classify(state: AgentState):
    user_input = state["user_input"].lower()

    if any(word in user_input for word in ["python", "code", "programming"]):
        category = "technical"
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        category = "greeting"
    else:
        category = "general"

    print(f"[Classify] {category}")

    return {
        "category": category
    }


# Node 2: Route input
def route(state: AgentState):
    print(f"[Route] {state['category']}")

    return {}


# Node 3: Generate response
def respond(state: AgentState):
    category = state["category"]

    if category == "technical":
        response = "I can help you with Python, coding, and programming."

    elif category == "greeting":
        response = "Hello! How can I help you?"

    else:
        response = "This is a general question. I will try to help you."

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# Conditional routing function
def route_condition(state: AgentState):
    return state["category"]


# Create StateGraph
builder = StateGraph(AgentState)

# Add nodes
builder.add_node("classify", classify)
builder.add_node("route", route)
builder.add_node("respond", respond)

# Start -> Classify
builder.add_edge(START, "classify")

# Classify -> Route
builder.add_edge("classify", "route")

# Conditional edges
builder.add_conditional_edges(
    "route",
    route_condition,
    {
        "technical": "respond",
        "greeting": "respond",
        "general": "respond",
    },
)

# Respond -> End
builder.add_edge("respond", END)

# Compile graph
graph = builder.compile()


# Test the state machine
if __name__ == "__main__":

    test_inputs = [
        "Hello bro",
        "How can I learn Python?",
        "Write a programming program",
        "What is your name?",
        "Hey, can you help me?",
    ]

    print("\n======================================")
    print("W10D2 LANGGRAPH STATE MACHINE")
    print("======================================")

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

    print("\n======================================")
    print("5 TESTS COMPLETED")
    print("======================================")