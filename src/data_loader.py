"""
Data loading utilities.
"""

import pandas as pd


class DataLoader:
    """
    Load benchmark datasets.
    """

    def __init__(self, data_dir="../data"):
        self.data_dir = data_dir

    def load_questions(self):
        """
        Load question dataset.
        """
        return pd.read_csv(
            f"{self.data_dir}/raw/electrical_qa_dataset.csv"
        )

    def load_ground_truth(self):
        """
        Load ground truth answers.
        """
        return pd.read_csv(
            f"{self.data_dir}/raw/ground_truth_answers.csv"
        )

    def load_ai_answers(self):
        """
        Load AI-generated answers.
        """
        return pd.read_csv(
            f"{self.data_dir}/raw/ai_generated_answers.csv"
        )

    def load_benchmark_dataset(self):
        """
        Load processed benchmark dataset.
        """
        return pd.read_csv(
            f"{self.data_dir}/processed/benchmark_dataset.csv"
        )

    def load_evaluation_results(self):
        """
        Load processed evaluation results.
        """
        return pd.read_csv(
            f"{self.data_dir}/processed/evaluation_results.csv"
        )


if __name__ == "__main__":

    loader = DataLoader()

    questions = loader.load_questions()

    print(questions.head())