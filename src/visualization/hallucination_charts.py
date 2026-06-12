"""
Hallucination Visualization
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


class HallucinationCharts:

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

        hallucination_counts = (
            df["hallucination_level"]
            .fillna("None")
            .value_counts()
        )

        plt.figure(
            figsize=(8, 5)
        )

        hallucination_counts.plot(
            kind="bar"
        )

        plt.title(
            "Hallucination Distribution"
        )

        plt.xlabel(
            "Hallucination Level"
        )

        plt.ylabel(
            "Count"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir
            / "hallucination_distribution.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        total = len(df)

        none_count = (
            df["hallucination_level"]
            .fillna("None")
            .eq("None")
            .sum()
        )

        hallucination_rate = (
            (total - none_count)
            / total
            * 100
        )

        plt.figure(
            figsize=(6, 5)
        )

        plt.bar(
            ["Hallucination Rate"],
            [hallucination_rate]
        )

        plt.ylabel(
            "Percentage (%)"
        )

        plt.title(
            "Hallucination Rate"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir
            / "hallucination_rate.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(
            "[SUCCESS] Hallucination charts generated"
        )


if __name__ == "__main__":

    charts = HallucinationCharts()

    charts.generate()