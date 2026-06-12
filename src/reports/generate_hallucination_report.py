"""
Generate Hallucination Analysis Report
"""

import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


INPUT_FILE = "data/processed/evaluation_results.csv"
OUTPUT_FILE = "reports/hallucination_analysis.pdf"


def generate_report():

    df = pd.read_csv(INPUT_FILE)

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        OUTPUT_FILE
    )

    content = []

    content.append(
        Paragraph(
            "Engineering Hallucination Analysis",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    hallucination_counts = (
        df["hallucination_level"]
        .value_counts()
    )

    content.append(
        Paragraph(
            "Hallucination Distribution",
            styles["Heading1"]
        )
    )

    for level, count in hallucination_counts.items():

        content.append(
            Paragraph(
                f"{level}: {count}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Critical Cases",
            styles["Heading1"]
        )
    )

    critical_cases = df[
        df["hallucination_level"]
        == "Critical"
    ]

    if len(critical_cases) == 0:

        content.append(
            Paragraph(
                "No critical hallucinations detected.",
                styles["Normal"]
            )
        )

    else:

        for _, row in critical_cases.head(10).iterrows():

            content.append(
                Paragraph(
                    (
                        f"Model: {row['model_name']} | "
                        f"Category: {row['category']}"
                    ),
                    styles["Normal"]
                )
            )

    doc.build(content)

    print(
        "Hallucination report generated."
    )


if __name__ == "__main__":

    generate_report()