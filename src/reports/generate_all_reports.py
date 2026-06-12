"""
Generate All Reports

Creates:

- benchmark_report.pdf
- technical_accuracy_report.pdf
- hallucination_analysis.pdf
"""

from generate_benchmark_report import generate_report as benchmark_report
from generate_accuracy_report import generate_report as accuracy_report
from generate_hallucination_report import generate_report as hallucination_report


def generate_all():

    print(
        "Generating benchmark report..."
    )
    benchmark_report()

    print(
        "Generating accuracy report..."
    )
    accuracy_report()

    print(
        "Generating hallucination report..."
    )
    hallucination_report()

    print(
        "\nAll reports generated successfully."
    )


if __name__ == "__main__":
    generate_all()