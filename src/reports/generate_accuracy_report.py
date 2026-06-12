"""
Generate Technical Accuracy Report
"""

import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


INPUT_FILE = "data/processed/evaluation_results.csv"
OUTPUT_FILE = "reports/technical_accuracy_report.pdf"


def generate_report():

    df = pd.read_csv(INPUT_FILE)

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        OUTPUT_FILE
    )

    content = []

    content.append(
        Paragraph(
            "Technical Accuracy Assessment Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    accuracy_stats = (
        df["technical_accuracy_score"]
        .describe()
    )

    for metric, value in accuracy_stats.items():

        content.append(
            Paragraph(
                f"{metric}: {round(value,2)}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Domain Performance",
            styles["Heading1"]
        )
    )

    domain_scores = (
        df.groupby("category")
        ["technical_accuracy_score"]
        .mean()
    )

    for category, score in domain_scores.items():

        content.append(
            Paragraph(
                f"{category}: {score:.2f}",
                styles["Normal"]
            )
        )

    doc.build(content)

    print(
        "Technical accuracy report generated."
    )


if __name__ == "__main__":

    generate_report()