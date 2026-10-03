from crewai import Agent, LLM, Task, Crew, Process
from crewai.tools import tool
from crewai_tools import SerperDevTool

# Gemini LLM
llm = LLM(
    model="gemini/gemini-3.5-flash-lite"
)

# Web search tool
search_tool = SerperDevTool()
@tool("Python Calculator")
def python_calculator(expression: str) -> str:
    """Calculate a basic mathematical expression."""
    try:
        allowed = "0123456789+-*/(). "
        if not all(char in allowed for char in expression):
            return "Invalid expression. Only basic arithmetic is allowed."

        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"

print("CrewAI tools loaded successfully!")
# Researcher Agent
researcher = Agent(
    role="Researcher",
    goal="Find accurate information about the research topic using web search.",
    backstory="You are a careful researcher who collects useful and reliable information.",
    verbose=True,
    llm=llm,
    tools=[search_tool, python_calculator]
)

# Writer Agent
writer = Agent(
    role="Writer",
    goal="Write a clear and well-structured article using the researcher's findings.",
    backstory="You are a skilled writer who explains technical topics in simple language.",
    verbose=True,
    llm=llm
)

# Reviewer Agent
reviewer = Agent(
    role="Reviewer",
    goal="Check the article for accuracy, clarity, completeness, and quality.",
    backstory="You are a strict reviewer who identifies mistakes and suggests improvements.",
    verbose=True,
    llm=llm
)

print("Researcher, Writer, and Reviewer agents created successfully!")
# Research Task
research_task = Task(
   description=(
    "Research the topic of Python programming using the web search tool. "
    "Find important concepts, real-world applications, benefits, and current trends. "
    "Also use the Python Calculator tool to calculate and verify this example: "
    "the percentage increase from 50 to 75. "
    "Include the calculation and result in your research findings."
),
    expected_output=(
        "A clear research summary about Python programming "
        "covering concepts, applications, benefits, and current trends."
    ),
    agent=researcher
)

# Writing Task
writing_task = Task(
    description=(
        "Use the researcher's findings to write a clear and "
        "well-structured article about Python programming."
    ),
    expected_output=(
        "A simple, well-structured article about Python programming "
        "that is easy for beginners to understand."
    ),
    agent=writer
)

# Review Task
review_task = Task(
    description=(
        "Review the Python article for accuracy, clarity, completeness, "
        "and logical structure. Identify errors and suggest improvements."
    ),
    expected_output=(
        "A review report containing strengths, weaknesses, "
        "and specific suggestions for improving the article."
    ),
    agent=reviewer
)

print("Research, writing, and review tasks created successfully!")
# Create Crew
research_crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

print("Crew created successfully!")


# Run Crew
if __name__ == "__main__":
    result = research_crew.kickoff()

    print("\n===== FINAL W9D2 OUTPUT =====")
    print(result)