from ragas_evaluation import evaluate_report


def test_report_not_empty():
    report = "This is a sample research report."
    assert len(report.strip()) > 0


def test_report_evaluation():
    report = """
    Introduction

    Generative AI provides benefits for software development.

    Challenges include accuracy and security.

    Future development will include more AI-assisted tools.
    """

    score = evaluate_report(report)

    assert score > 0
    assert score <= 1


def test_report_contains_required_sections():
    report = """
    Introduction
    Benefits
    Challenges
    Future
    """

    assert "Introduction" in report
    assert "Benefits" in report
    assert "Challenges" in report
    assert "Future" in report