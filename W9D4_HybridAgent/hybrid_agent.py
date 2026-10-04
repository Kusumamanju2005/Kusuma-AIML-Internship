from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Ollama LLM
llm = OllamaLLM(model="llama3.2:1b")

# Prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple language for a beginner."
)

# Output parser
parser = StrOutputParser()

# LangChain chain
chain = prompt | llm | parser

# Test the chain with 5 inputs
test_inputs = [
    "Python",
    "Artificial Intelligence",
    "Machine Learning",
    "APIs",
    "Docker"
]

print("\n===== 5 CHAIN TESTS =====")

for topic in test_inputs:
    result = chain.invoke({"topic": topic})
    print(f"\nTopic: {topic}")
    print(f"Response: {result}")
    from langchain_core.messages import HumanMessage, AIMessage

# Conversation history
conversation_history = []

def chat_with_memory(user_input):
    messages = [
        HumanMessage(content=message["user"])
        for message in conversation_history
    ]

    messages.append(HumanMessage(content=user_input))

    memory_prompt = PromptTemplate(
        input_variables=["history", "question"],
        template=(
            "You are a helpful AI assistant.\n\n"
            "Conversation history:\n{history}\n\n"
            "Current question: {question}\n\n"
            "Answer based on the conversation history when useful."
        )
    )

    history_text = "\n".join(
        f"User: {item['user']}\nAI: {item['ai']}"
        for item in conversation_history
    )

    memory_chain = memory_prompt | llm | parser

    response = memory_chain.invoke({
        "history": history_text,
        "question": user_input
    })

    conversation_history.append({
        "user": user_input,
        "ai": response
    })

    return response


# Test conversation memory with 5 turns
print("\n===== 5-TURN CONVERSATION MEMORY TEST =====")

questions = [
    "My name is Kusuma.",
    "What is Python?",
    "What can I build with it?",
    "Which skill should I learn first?",
    "What is my name?"
]

for question in questions:
    answer = chat_with_memory(question)
    print(f"\nUser: {question}")
    print(f"AI: {answer}")
    # ============================================================
# TWO-TOOL AGENT
# ============================================================

from langchain_core.tools import tool


@tool
def web_search_stub(query: str) -> str:
    """Return a simulated web search result for a query."""
    return (
        f"Web search result for '{query}': "
        "Generative AI is widely used for code generation, "
        "testing, documentation, and developer assistance."
    )


@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    try:
        allowed = "0123456789+-*/(). "
        if not all(char in allowed for char in expression):
            return "Invalid expression."

        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


print("\n===== TWO TOOLS CREATED =====")
print("Web Search Stub: Ready")
print("Calculator: Ready")
# ============================================================
# LANGCHAIN TWO-TOOL AGENT
# ============================================================

from langchain.agents import create_agent

# Chat model for tool-calling agent
chat_llm = ChatOllama(
    model="llama3.2:1b"
)

agent = create_agent(
    model=chat_llm,
    tools=[web_search_stub, calculator],
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use the calculator tool for arithmetic questions. "
        "Use the web search tool when information lookup is needed. "
        "Give clear and simple answers."
    )
)

print("\n===== TWO-TOOL AGENT CREATED =====")
system_prompt=(
        "You are a helpful AI assistant. "
        "Use the calculator tool for arithmetic questions. "
        "Use the web search tool when information lookup is needed. "
        "Give clear and simple answers."
    )


print("\n===== TWO-TOOL AGENT CREATED =====")
# ============================================================
# TEST AGENT WITH 3 TASKS
# ============================================================

agent_tasks = [
    "Calculate 125 * 8 and give me the answer.",
    "Use the web search tool to find information about Generative AI in software development.",
    "Calculate (500 + 250) / 5."
]

print("\n===== 3 AGENT TASKS =====")

for i, task in enumerate(agent_tasks, start=1):
    print(f"\n--- Task {i} ---")
    print(f"Task: {task}")

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": task}
        ]
    })

    final_message = result["messages"][-1].content
    print(f"Answer: {final_message}")