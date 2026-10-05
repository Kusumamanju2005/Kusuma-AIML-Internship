from stateful_agent import graph


def test_greeting():
    result = graph.invoke({
        "user_input": "Hello bro",
        "category": "",
        "response": ""
    })

    assert result["category"] == "greeting"


def test_technical():
    result = graph.invoke({
        "user_input": "How can I learn Python?",
        "category": "",
        "response": ""
    })

    assert result["category"] == "technical"


def test_general():
    result = graph.invoke({
        "user_input": "What is your name?",
        "category": "",
        "response": ""
    })

    assert result["category"] == "general"


def test_five_inputs():
    inputs = [
        "Hello",
        "Learn Python",
        "Write code",
        "What is your name?",
        "Hey bro"
    ]

    for user_input in inputs:
        result = graph.invoke({
            "user_input": user_input,
            "category": "",
            "response": ""
        })

        assert result["response"] != ""