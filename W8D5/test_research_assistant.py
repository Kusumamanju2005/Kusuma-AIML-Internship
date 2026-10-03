from research_assistant import (
    load_research_notes,
    search_research_notes,
    create_research_report,
)


def test_research_notes_exist():
    """Verify that the local knowledge base can be loaded."""

    notes = load_research_notes()

    assert len(notes) > 0


def test_search_returns_machine_learning_information():
    """Verify that ML-related information can be retrieved."""

    notes = load_research_notes()

    results = search_research_notes(
        "machine learning",
        notes,
    )

    assert len(results) > 0
    assert any(
        "Machine Learning" in result
        for result in results
    )


def test_report_contains_retrieved_information():
    """Verify that the research report contains retrieved content."""

    results = [
        "Machine Learning allows computers to learn patterns from data."
    ]

    report = create_research_report(
        "What is machine learning?",
        results,
    )

    assert "What is machine learning?" in report
    assert "Machine Learning" in report