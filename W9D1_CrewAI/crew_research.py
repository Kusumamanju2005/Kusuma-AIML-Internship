from crewai import Agent, LLM
from crewai_tools import SerperDevTool
llm = LLM(
    model="gemini/gemini-3.5-flash"
)
search_tool = SerperDevTool()
# Researcher Agent
researcher = Agent(
    role="Researcher",
    goal="Find accurate and useful information about the research topic using web search.",
    backstory="You are a careful researcher who collects clear and relevant information from the web.",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# Writer Agent
writer = Agent(
    role="Writer",
    goal="Write a clear and well-structured article using the researcher's information.",
    backstory="You are a skilled technical writer who explains complex topics in simple language.",
    verbose=True,
    llm=llm
)

# Reviewer Agent
reviewer = Agent(
    role="Reviewer",
    goal="Review the written content for accuracy, clarity, and completeness.",
    backstory="You are a quality reviewer who checks research content and suggests improvements.",
    verbose=True,
    llm=llm
)

print("Three CrewAI agents created successfully!")
from crewai import Task

# Research Task
research_task = Task(
    description=(
        "Research the topic of Artificial Intelligence. "
        "Find important concepts, applications, benefits, and challenges."
    ),
    expected_output=(
        "A clear research summary containing key concepts, "
        "applications, benefits, and challenges of Artificial Intelligence."
    ),
    agent=researcher
)

# Writing Task
writing_task = Task(
    description=(
        "Using the researcher's findings, write a clear and "
        "well-structured article about Artificial Intelligence."
    ),
    expected_output=(
        "A well-structured article about Artificial Intelligence "
        "written in simple and understandable language."
    ),
    agent=writer
)

# Review Task
review_task = Task(
    description=(
        "Review the article for accuracy, clarity, completeness, "
        "and logical structure. Suggest improvements if required."
    ),
    expected_output=(
        "A review containing the strengths, weaknesses, "
        "and suggested improvements for the article."
    ),
    agent=reviewer
)

print("Three CrewAI tasks created successfully!")
from crewai import Crew, Process

# Create the research crew
research_crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

print("Crew created successfully!")
# Run the crew
if __name__ == "__main__":
    result = research_crew.kickoff()
    print("\n===== FINAL RESEARCH OUTPUT =====")
    print(result)