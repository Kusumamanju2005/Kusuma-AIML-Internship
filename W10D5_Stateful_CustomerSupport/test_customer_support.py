from customer_support_agent import graph
from langgraph.types import Command


def run_test(user_input, decision=None, thread_id="test-thread"):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("\n------------------------------------------")
    print("Customer:", user_input)

    result = graph.invoke(
        {
            "user_input": user_input,
            "category": "",
            "response": "",
            "conversation_history": [],
            "needs_human": False,
        },
        config
    )

    if "__interrupt__" in result:

        print("Human review required: YES")

        result = graph.invoke(
            Command(resume=decision or "yes"),
            config
        )

    else:
        print("Human review required: NO")

    print("Final Response:", result["response"])
    print("Memory:", result["conversation_history"])

    return result


if __name__ == "__main__":

    print("\n==========================================")
    print("W10D5 CUSTOMER SUPPORT TESTS")
    print("==========================================")

    run_test(
        "I want a refund for my order",
        "yes",
        "refund-test"
    )

    run_test(
        "My payment was charged twice",
        "yes",
        "payment-test"
    )

    run_test(
        "I forgot my password",
        thread_id="account-test"
    )

    run_test(
        "Where is my order?",
        thread_id="order-test"
    )

    run_test(
        "I need help",
        thread_id="general-test"
    )

    print("\n==========================================")
    print("5 CUSTOMER SUPPORT TESTS COMPLETED")
    print("==========================================")