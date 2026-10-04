import mlflow


def track_research_run(report):
    mlflow.set_tracking_uri("sqlite:///mlflow.db")

    with mlflow.start_run(
        run_name="W9D5_Automated_Research_Agent"
    ):

        mlflow.log_param(
            "project",
            "Automated Research Report Agent"
        )

        mlflow.log_param(
            "topic",
            "Generative AI in Software Development"
        )

        mlflow.log_param(
            "frameworks",
            "CrewAI, LangGraph, MLflow"
        )

        mlflow.log_metric(
            "report_length",
            len(report)
        )

        mlflow.log_metric(
            "word_count",
            len(report.split())
        )

        print("\nMLflow tracking completed.")
        print("Report length:", len(report))
        print("Word count:", len(report.split()))