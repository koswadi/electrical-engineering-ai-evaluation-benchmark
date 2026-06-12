"""
Preprocessing utilities for benchmark data.
"""

import pandas as pd


class BenchmarkPreprocessor:
    """
    Prepare datasets for evaluation.
    """

    def clean_text(self, text):
        """
        Basic text cleaning.
        """

        if pd.isna(text):
            return ""

        text = str(text)

        text = text.lower()
        text = text.strip()

        return text

    def merge_datasets(
        self,
        questions_df,
        ground_truth_df,
        ai_answers_df
    ):
        """
        Merge benchmark datasets.
        """

        merged = pd.merge(
            questions_df,
            ground_truth_df,
            on="id",
            how="inner"
        )

        merged = pd.merge(
            merged,
            ai_answers_df,
            on="id",
            how="inner"
        )

        return merged

    def preprocess_dataset(
        self,
        benchmark_df
    ):
        """
        Apply preprocessing steps.
        """

        benchmark_df["question"] = (
            benchmark_df["question"]
            .apply(self.clean_text)
        )

        benchmark_df["ground_truth"] = (
            benchmark_df["ground_truth"]
            .apply(self.clean_text)
        )

        benchmark_df["answer"] = (
            benchmark_df["answer"]
            .apply(self.clean_text)
        )

        return benchmark_df

    def save_processed_dataset(
        self,
        dataframe,
        output_path
    ):
        """
        Save processed dataset.
        """

        dataframe.to_csv(
            output_path,
            index=False
        )

        print(
            f"Dataset saved to {output_path}"
        )


if __name__ == "__main__":

    from data_loader import DataLoader

    loader = DataLoader()

    questions = loader.load_questions()
    ground_truth = loader.load_ground_truth()
    answers = loader.load_ai_answers()

    processor = BenchmarkPreprocessor()

    benchmark = processor.merge_datasets(
        questions,
        ground_truth,
        answers
    )

    benchmark = processor.preprocess_dataset(
        benchmark
    )

    print(
        benchmark.head()
    )

    processor.save_processed_dataset(
        benchmark,
        "../data/processed/benchmark_dataset.csv"
    )