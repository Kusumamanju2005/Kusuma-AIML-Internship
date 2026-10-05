from human_loop_graph import graph
from langgraph.types import Command


config = {
    "configurable": {
        "thread_id": "w10d4-test"
    }
}


print("\n======================================")
print("W10D4 HUMAN-IN-THE-LOOP TEST")
print("======================================")


test_inputs = [
    "Hello bro",
    "How can I learn Python?",
    "What is LangGraph?",
    "What is your name?",
    "Hey bro, can you help me?"
]


for i, user_input in enumerate(test_inputs, start=1):

    print(f"\nTest {i}")
    print("Input:", user_input)

    result = graph.invoke(
        {
            "user_input": user_input,
            "category": "",
            "response": "",
        },
        config
    )

    print("Graph paused for human approval.")
    print("Interrupt detected:", "__interrupt__" in result)

    resumed_result = graph.invoke(
        Command(resume="yes"),
        config
    )

    print("Human Decision: yes")
    print("Final Response:", resumed_result["response"])


print("\n======================================")
print("5 TESTS COMPLETED")
print("======================================")