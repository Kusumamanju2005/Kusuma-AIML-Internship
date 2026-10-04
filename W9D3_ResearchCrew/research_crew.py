from crewai import Agent, LLM, Task, Crew, Process
from crewai_tools import SerperDevTool

# Gemini LLM
llm = LLM(
    model="gemini/gemini-3.5-flash-lite"
)

# Web search tool
search_tool = SerperDevTool()

print("W9D3 CrewAI setup loaded successfully!")
# Researcher Agent
researcher = Agent(
    role="Lead Researcher",
    goal=(
        "Research the assigned topic using web search and collect "
        "accurate, relevant, and well-organized information."
    ),
    backstory=(
        "You are an experienced research analyst. "
        "You investigate topics carefully and provide useful findings "
        "that another agent can use to create a high-quality article."
    ),
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# Writer Agent
writer = Agent(
    role="Technical Writer",
    goal=(
        "Transform the research findings into a clear, structured, "
        "and easy-to-understand article."
    ),
    backstory=(
        "You are a technical writer who specializes in converting "
        "complex research into simple and readable content."
    ),
    verbose=True,
    llm=llm
)

# Reviewer Agent
reviewer = Agent(
    role="Quality Reviewer",
    goal=(
        "Evaluate the article for accuracy, clarity, completeness, "
        "logical flow, and usefulness."
    ),
    backstory=(
        "You are a quality assurance reviewer. "
        "You carefully inspect research content and identify areas "
        "that need correction or improvement."
    ),
    verbose=True,
    llm=llm
)

print("Researcher, Writer, and Reviewer agents created successfully!")
# Research Task
research_task = Task(
    description=(
        "Research how Generative AI is changing software development. "
        "Use web search to find current information about AI coding assistants, "
        "automated testing, code generation, debugging, developer productivity, "
        "and important challenges such as security, accuracy, and over-reliance. "
        "Organize the findings clearly for the Writer."
    ),
    expected_output=(
        "A structured research report covering current applications, "
        "benefits, challenges, and future impact of Generative AI "
        "on software development."
    ),
    agent=researcher
)

# Writing Task
writing_task = Task(
    description=(
        "Using the Researcher's findings, write a well-structured article "
        "explaining how Generative AI is changing software development. "
        "Use simple language and organize the article with clear headings."
    ),
    expected_output=(
        "A clear article with an introduction, major applications, "
        "benefits, challenges, and future outlook."
    ),
    agent=writer
)

# Review Task
review_task = Task(
    description=(
        "Review the Writer's article carefully. Check factual accuracy, "
        "clarity, completeness, logical flow, and whether the article "
        "properly reflects the research findings. Provide specific "
        "improvement suggestions."
    ),
    expected_output=(
        "A concise quality review listing strengths, weaknesses, "
        "and specific improvements required."
    ),
    agent=reviewer
)

print("Research, writing, and review tasks created successfully!")
# Create the Research Crew
research_crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

print("W9D3 Research Crew created successfully!")


# Run the Crew
if __name__ == "__main__":
    result = research_crew.kickoff()

    print("\n===== W9D3 FINAL RESEARCH OUTPUT =====")
    print(result)