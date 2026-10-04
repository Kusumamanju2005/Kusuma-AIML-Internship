from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from automated_research import research_crew
from mlflow_tracking import track_research_run
from ragas_evaluation import evaluate_report


# ============================================================
# LANGGRAPH STATE
# ============================================================

class ResearchState(TypedDict):
    topic: str
    report: str


# ============================================================
# CREWAI NODE
# ============================================================

def run_research(state: ResearchState):
    print("\n[LangGraph] Starting CrewAI research workflow...")

    result = research_crew.kickoff()

    return {
        "report": str(result)
    }


# ============================================================
# BUILD LANGGRAPH
# ============================================================

builder = StateGraph(ResearchState)

builder.add_node("research", run_research)

builder.add_edge(START, "research")
builder.add_edge("research", END)

research_graph = builder.compile()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    print("\n==============================================")
    print("W9D5 LANGGRAPH + MLFLOW WORKFLOW")
    print("==============================================")

    result = research_graph.invoke({
        "topic": "How Generative AI is transforming software development",
        "report": ""
    })

    report = result["report"]

    evaluation_score = evaluate_report(report)

    print("\n==============================================")
    print("LANGGRAPH WORKFLOW COMPLETED")
    print("==============================================")

    print(report)

    # MLflow tracking
    track_research_run(report)

    print("\nEvaluation score:", evaluation_score)

    print("\n==============================================")
    print("MLFLOW TRACKING COMPLETED")
    print("==============================================")