from typing import TypedDict, List

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command


# ==========================================
# STATE
# ==========================================

class SupportState(TypedDict):
    user_input: str
    category: str
    response: str
    conversation_history: List[str]
    needs_human: bool


# ==========================================
# NODE 1: CLASSIFY CUSTOMER QUERY
# ==========================================

def classify_query(state: SupportState):

    user_input = state["user_input"].lower()

    if any(word in user_input for word in [
        "refund",
        "money back",
        "return"
    ]):
        category = "refund"

    elif any(word in user_input for word in [
        "payment",
        "charged",
        "transaction",
        "billing"
    ]):
        category = "payment"

    elif any(word in user_input for word in [
        "password",
        "login",
        "account",
        "sign in"
    ]):
        category = "account"

    elif any(word in user_input for word in [
        "order",
        "delivery",
        "shipping",
        "track"
    ]):
        category = "order"

    else:
        category = "general"

    print(f"[Classify] Category: {category}")

    return {
        "category": category
    }


# ==========================================
# NODE 2: ROUTE CUSTOMER REQUEST
# ==========================================

def route_query(state: SupportState):

    category = state["category"]

    # Sensitive requests require human review.
    needs_human = category in ["refund", "payment"]

    print(f"[Route] Category: {category}")
    print(f"[Route] Human review required: {needs_human}")

    return {
        "needs_human": needs_human
    }


# ==========================================
# NODE 3: GENERATE SUPPORT RESPONSE
# ==========================================

def generate_response(state: SupportState):

    category = state["category"]

    if category == "refund":
        response = (
            "Your refund request has been received. "
            "A support representative will review it."
        )

    elif category == "payment":
        response = (
            "Your payment issue has been received. "
            "A support representative will review the transaction."
        )

    elif category == "account":
        response = (
            "For account issues, please verify your login details "
            "and use the password reset option if required."
        )

    elif category == "order":
        response = (
            "I can help with your order. "
            "Please provide your order details to check the status."
        )

    else:
        response = (
            "Thank you for contacting customer support. "
            "Please provide more details so I can help you."
        )

    print(f"[Respond] {response}")

    return {
        "response": response
    }


# ==========================================
# NODE 4: HUMAN REVIEW
# ==========================================

def human_review(state: SupportState):

    if not state["needs_human"]:
        return {}

    decision = interrupt(
        f"Human review required for this {state['category']} request: "
        f"{state['user_input']}. "
        "Type yes to approve or no to reject."
    )

    if str(decision).lower() == "yes":

        response = (
            state["response"]
            + " Human review approved the request."
        )

    else:

        response = (
            "The request was not approved by the human reviewer."
        )

    return {
        "response": response
    }


# ==========================================
# NODE 5: UPDATE CONVERSATION MEMORY
# ==========================================

def update_memory(state: SupportState):

    history = list(state.get("conversation_history", []))

    history.append(
        f"User: {state['user_input']}"
    )

    history.append(
        f"Agent: {state['response']}"
    )

    print(f"[Memory] Conversation turns stored: {len(history)}")

    return {
        "conversation_history": history
    }


# ==========================================
# CONDITIONAL ROUTING
# ==========================================

def human_review_condition(state: SupportState):

    if state["needs_human"]:
        return "human_review"

    return "memory"


# ==========================================
# BUILD LANGGRAPH
# ==========================================

builder = StateGraph(SupportState)

builder.add_node("classify", classify_query)
builder.add_node("route", route_query)
builder.add_node("respond", generate_response)
builder.add_node("human_review", human_review)
builder.add_node("memory", update_memory)

builder.add_edge(START, "classify")
builder.add_edge("classify", "route")
builder.add_edge("route", "respond")

builder.add_conditional_edges(
    "respond",
    human_review_condition,
    {
        "human_review": "human_review",
        "memory": "memory"
    }
)

builder.add_edge("human_review", "memory")
builder.add_edge("memory", END)


# ==========================================
# MEMORY CHECKPOINT
# ==========================================

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)


# ==========================================
# DEMO
# ==========================================

if __name__ == "__main__":

    print("\n==========================================")
    print("W10D5 STATEFUL CUSTOMER SUPPORT AGENT")
    print("==========================================")

    config = {
        "configurable": {
            "thread_id": "customer-support-demo"
        }
    }

    user_input = input("\nCustomer: ")

    initial_state = {
        "user_input": user_input,
        "category": "",
        "response": "",
        "conversation_history": [],
        "needs_human": False
    }

    result = graph.invoke(
        initial_state,
        config
    )

    # Check whether LangGraph paused for human review.
    if "__interrupt__" in result:

        print("\n[Human Review Required]")
        print(result["__interrupt__"])

        decision = input("\nHuman decision (yes/no): ")

        result = graph.invoke(
            Command(resume=decision),
            config
        )

    print("\n------------------------------------------")
    print("FINAL CUSTOMER SUPPORT RESPONSE")
    print("------------------------------------------")

    print(result["response"])

    print("\n------------------------------------------")
    print("CONVERSATION MEMORY")
    print("------------------------------------------")

    for item in result["conversation_history"]:
        print(item)

    print("\n==========================================")
    print("W10D5 DEMO COMPLETED")
    print("==========================================")