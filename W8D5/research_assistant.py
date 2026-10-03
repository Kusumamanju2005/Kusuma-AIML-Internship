from pathlib import Path


DATA_FILE = Path("data/research_notes.txt")


def load_research_notes():
    """Load research information from the local knowledge base."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Knowledge base not found: {DATA_FILE}"
        )

    return DATA_FILE.read_text(
        encoding="utf-8"
    )


def search_research_notes(
    query,
    notes,
    top_k=3
):
    """Retrieve relevant lines using keyword matching."""

    query_words = set(
        query.lower()
        .replace("?", "")
        .split()
    )

    scored_lines = []

    for line in notes.splitlines():
        if not line.strip():
            continue

        line_words = set(
            line.lower()
            .replace(".", "")
            .split()
        )

        score = len(
            query_words.intersection(line_words)
        )

        if score > 0:
            scored_lines.append(
                (score, line)
            )

    scored_lines.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        line
        for _, line in scored_lines[:top_k]
    ]


def generate_summary(
    query,
    retrieved_information
):
    """Generate a concise local research summary."""

    if not retrieved_information:
        return (
            "No relevant information was found "
            "in the local knowledge base."
        )

    summary_parts = []

    for information in retrieved_information:
        summary_parts.append(information)

    return " ".join(summary_parts)


def create_research_report(
    query,
    retrieved_information
):
    """Create a structured research report."""

    summary = generate_summary(
        query,
        retrieved_information
    )

    report = [
        "===== AI Research Assistant =====",
        f"Research topic: {query}",
        "",
        "Summary:",
        summary,
        "",
        "Sources from local knowledge base:"
    ]

    for index, information in enumerate(
        retrieved_information,
        start=1
    ):
        report.append(
            f"{index}. {information}"
        )

    return "\n".join(report)


def main():
    """Run the local AI research assistant."""

    print("===== Local AI Research Assistant =====")

    query = input(
        "Enter your research topic: "
    ).strip()

    if not query:
        print("Please enter a research topic.")
        return

    notes = load_research_notes()

    retrieved_information = search_research_notes(
        query,
        notes
    )

    report = create_research_report(
        query,
        retrieved_information
    )

    print("\n" + report)


if __name__ == "__main__":
    main()