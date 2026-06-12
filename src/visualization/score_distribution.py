"""
Score Distribution Visualization

Creates:
figures/accuracy_distribution.png
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


class ScoreDistributionChart:

    def __init__(self):

        self.root_dir = (
            Path(__file__).resolve().parents[2]
        )

        self.file_path = (
            self.root_dir
            / "data"
            / "processed"
            / "evaluation_results.csv"
        )

        self.output_dir = (
    self.root_dir
    / "results"
    / "figures"
)

        self.output_dir.mkdir(
    parents=True,
    exist_ok=True
)

    def generate(self):

        df = pd.read_csv(
            self.file_path
        )

        plt.figure(figsize=(8, 5))

        df[
            "technical_accuracy_score"
        ].hist(
            bins=6
        )

        plt.title(
            "Technical Accuracy Score Distribution"
        )

        plt.xlabel(
            "Accuracy Score"
        )

        plt.ylabel(
            "Frequency"
        )

        plt.tight_layout()

        output_file = (
            self.output_dir
            / "accuracy_distribution.png"
        )

        plt.savefig(
            output_file,
            dpi=300
        )

        plt.close()

        print(
            f"Saved: {output_file}"
        )


if __name__ == "__main__":

    chart = (
        ScoreDistributionChart()
    )

    chart.generate()