from conversation_memory import graph


config = {
    "configurable": {
        "thread_id": "persistent-demo"
    }
}


print("\n======================================")
print("W10D3 PERSISTENT MEMORY TEST")
print("======================================")


# First conversation turn
result = graph.invoke(
    {
        "user_input": "Hello bro",
        "category": "",
        "response": "",
        "conversation_count": 0,
    },
    config
)

print("\nTurn 1:")
print("User:", "Hello bro")
print("Assistant:", result["response"])
print("Conversation Count:", result["conversation_count"])


# Second conversation turn using SAME thread
result = graph.invoke(
    {
        "user_input": "How can I learn Python?",
        "category": "",
        "response": "",
        "conversation_count": 0,
    },
    config
)

print("\nTurn 2:")
print("User:", "How can I learn Python?")
print("Assistant:", result["response"])
print("Conversation Count:", result["conversation_count"])


# Read the saved state
saved_state = graph.get_state(config)

print("\nSaved State:")
print(saved_state.values)


print("\n======================================")
print("PERSISTENT MEMORY TEST COMPLETED")
print("======================================")