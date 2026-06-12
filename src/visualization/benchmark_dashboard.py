"""
Benchmark Dashboard
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


class BenchmarkDashboard:

    def __init__(self):

        self.base_dir = (
            Path(__file__).resolve().parents[2]
        )

        self.file_path = (
            self.base_dir
            / "data"
            / "processed"
            / "evaluation_results.csv"
        )

        self.output_dir = (
            self.base_dir
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

        summary = (
            df.groupby("model_name")
            .agg({
                "technical_accuracy_score": "mean",
                "similarity_score": "mean"
            })
        )

        plt.figure(
            figsize=(8, 5)
        )

        summary[
            "technical_accuracy_score"
        ].plot(
            kind="bar"
        )

        plt.title(
            "Average Technical Accuracy by Model"
        )

        plt.ylabel(
            "Average Score"
        )

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            self.output_dir
            / "benchmark_overview.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(
            "[SUCCESS] benchmark_overview.png generated"
        )

    def domain_performance(self):

        df = pd.read_csv(
            self.file_path
        )

        performance = (
            df.groupby("category")
            ["technical_accuracy_score"]
            .mean()
            .sort_values(
                ascending=False
            )
        )

        plt.figure(
            figsize=(10, 5)
        )

        performance.plot(
            kind="bar"
        )

        plt.title(
            "Domain Performance"
        )

        plt.ylabel(
            "Average Accuracy"
        )

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(
            self.output_dir
            / "domain_performance.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(
            "[SUCCESS] domain_performance.png generated"
        )


if __name__ == "__main__":

    dashboard = BenchmarkDashboard()

    dashboard.generate()

    dashboard.domain_performance()