"""
Example Report Generation

Generate all benchmark reports.
"""

from src.reports.generate_benchmark_report import (
    generate_report as benchmark_report
)

from src.reports.generate_accuracy_report import (
    generate_report as accuracy_report
)

from src.reports.generate_hallucination_report import (
    generate_report as hallucination_report
)


def main():

    print(
        "\nGenerating Benchmark Report..."
    )

    benchmark_report()

    print(
        "\nGenerating Technical Accuracy Report..."
    )

    accuracy_report()

    print(
        "\nGenerating Hallucination Analysis Report..."
    )

    hallucination_report()

    print(
        "\nAll reports generated successfully."
    )

    print(
        "\nGenerated Files:"
    )

    print(
        "- reports/benchmark_report.pdf"
    )

    print(
        "- reports/technical_accuracy_report.pdf"
    )

    print(
        "- reports/hallucination_analysis.pdf"
    )


if __name__ == "__main__":
    main()