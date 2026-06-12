"""
Generate Benchmark Report PDF
"""

import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


INPUT_FILE = "data/processed/evaluation_results.csv"
OUTPUT_FILE = "reports/benchmark_report.pdf"


def generate_report():

    df = pd.read_csv(INPUT_FILE)

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(OUTPUT_FILE)

    content = []

    content.append(
        Paragraph(
            "Electrical Engineering AI Evaluation Benchmark",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Benchmark Report",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Total Evaluation Records: {len(df)}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Number of Models: {df['model_name'].nunique()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    avg_accuracy = round(
        df["technical_accuracy_score"].mean(),
        2
    )

    avg_similarity = round(
        df["similarity_score"].mean(),
        2
    )

    content.append(
        Paragraph(
            f"Average Technical Accuracy: {avg_accuracy}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Average Similarity Score: {avg_similarity}",
            styles["Normal"]
        )
    )

    content.append(
        PageBreak()
    )

    content.append(
        Paragraph(
            "Model Comparison",
            styles["Heading1"]
        )
    )

    summary = (
        df.groupby("model_name")
        .agg({
            "technical_accuracy_score": "mean",
            "similarity_score": "mean"
        })
    )

    for model, row in summary.iterrows():

        content.append(
            Paragraph(
                f"{model}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"Accuracy: {row['technical_accuracy_score']:.2f}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Similarity: {row['similarity_score']:.2f}",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    doc.build(content)

    print("Benchmark report generated.")


if __name__ == "__main__":

    generate_report()