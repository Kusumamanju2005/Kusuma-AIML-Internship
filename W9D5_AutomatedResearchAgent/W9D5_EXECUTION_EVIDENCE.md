# W9D5 Execution Evidence

## Project

Automated Research Report Agent

## Topic

How Generative AI is transforming software development

## Workflow

LangGraph
↓
CrewAI Research Agent
↓
Web Search
↓
Research Findings
↓
Technical Report Writer
↓
Report Reviewer
↓
Report Evaluation
↓
MLflow Tracking

## Frameworks Used

- CrewAI
- LangGraph
- MLflow
- Ragas-style evaluation
- Python
- SerperDevTool
- Gemini

## Successful Execution

The automated research workflow completed successfully.

Final status:

MLFLOW TRACKING COMPLETED

## Evaluation

The generated report was evaluated using the project's report evaluation
function.

## Automated Tests

Command:

pytest -v

Result:

3 passed in 0.05s

Tests:

- test_report_not_empty — PASSED
- test_report_evaluation — PASSED
- test_report_contains_required_sections — PASSED

## MLOps Evidence

MLflow tracking was successfully completed using a local SQLite tracking
database.

## Final Result

The W9D5 Automated Research Report Agent successfully completed its
research, report generation, evaluation, and MLflow tracking workflow.
