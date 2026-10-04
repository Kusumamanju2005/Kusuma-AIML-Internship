from crewai import Agent, Crew, LLM, Process, Task
from crewai_tools import SerperDevTool

# ============================================================
# W9D5 - AUTOMATED RESEARCH REPORT AGENT
# ============================================================

# Gemini LLM
llm = LLM(
    model="gemini/gemini-3.5-flash-lite"
)

# Web search tool
search_tool = SerperDevTool()


# ============================================================
# AGENTS
# ============================================================

researcher = Agent(
    role="Research Specialist",
    goal=(
        "Research the assigned topic using reliable web information "
        "and collect accurate, relevant, and organized findings."
    ),
    backstory=(
        "You are an experienced research specialist who investigates "
        "technical topics carefully and provides factual information "
        "for report generation."
    ),
    llm=llm,
    tools=[search_tool],
    verbose=True
)


writer = Agent(
    role="Technical Report Writer",
    goal=(
        "Convert research findings into a clear, structured, "
        "professional research report."
    ),
    backstory=(
        "You are a technical writer who can transform complex "
        "research findings into simple and readable reports."
    ),
    llm=llm,
    verbose=True
)


reviewer = Agent(
    role="Report Reviewer",
    goal=(
        "Review the research report for accuracy, clarity, "
        "completeness, and logical structure."
    ),
    backstory=(
        "You are a quality reviewer who carefully checks reports "
        "and identifies factual or structural improvements."
    ),
    llm=llm,
    verbose=True
)


# ============================================================
# TASKS
# ============================================================

research_task = Task(
    description=(
        "Research the topic: 'How Generative AI is transforming "
        "software development'. Investigate AI coding assistants, "
        "code generation, automated testing, debugging, developer "
        "productivity, security concerns, accuracy, and future trends. "
        "Use web search and organize the findings clearly."
    ),
    expected_output=(
        "A structured research summary containing key findings, "
        "benefits, challenges, examples, and future trends."
    ),
    agent=researcher
)


writing_task = Task(
    description=(
        "Using the research findings, create a professional report "
        "about how Generative AI is transforming software development. "
        "Include an introduction, applications, benefits, challenges, "
        "and future outlook."
    ),
    expected_output=(
        "A well-structured research report with clear headings "
        "and easy-to-understand explanations."
    ),
    agent=writer
)


review_task = Task(
    description=(
        "Review the generated research report. Check accuracy, "
        "clarity, completeness, logical flow, and whether the report "
        "addresses the research topic properly. Provide a final "
        "quality assessment and improvement suggestions."
    ),
    expected_output=(
        "A concise review containing strengths, weaknesses, "
        "and recommended improvements."
    ),
    agent=reviewer
)


# ============================================================
# CREW
# ============================================================

research_crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)


# ============================================================
# RUN PROJECT
# ============================================================

if __name__ == "__main__":
    print("\n==============================================")
    print("W9D5 AUTOMATED RESEARCH REPORT AGENT")
    print("==============================================")

    result = research_crew.kickoff()

    print("\n==============================================")
    print("FINAL AUTOMATED RESEARCH REPORT")
    print("==============================================")

    print(result)