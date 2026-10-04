def evaluate_report(report):
    """
    Lightweight evaluation for the generated research report.
    """

    report_text = report.strip()

    checks = {
        "not_empty": len(report_text) > 0,
        "has_introduction": "introduction" in report_text.lower(),
        "has_benefits": "benefit" in report_text.lower(),
        "has_challenges": "challenge" in report_text.lower(),
        "has_future": "future" in report_text.lower(),
    }

    passed = sum(checks.values())
    total = len(checks)

    score = passed / total

    print("\n==============================================")
    print("RAGAS-STYLE REPORT EVALUATION")
    print("==============================================")

    for check, result in checks.items():
        print(f"{check}: {'PASS' if result else 'FAIL'}")

    print(f"\nEvaluation score: {score:.2f}")

    return score