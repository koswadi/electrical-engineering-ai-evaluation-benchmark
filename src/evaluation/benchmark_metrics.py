"""
Benchmark Performance Metrics
"""

import pandas as pd


class BenchmarkMetrics:

    def average_accuracy(
        self,
        dataframe
    ):
        return round(
            dataframe[
                "technical_accuracy_score"
            ].mean(),
            2
        )

    def average_similarity(
        self, 
        df
    ):
        return (
            df[
                "similarity_score"
            ].mean()
         )

    def hallucination_rate(
        self,
        dataframe
    ):

        total = len(dataframe)

        hallucinations = len(
            dataframe[
                dataframe[
                    "hallucination_level"
                ] != "None"
            ]
        )

        return round(
            hallucinations / total * 100,
            2
        )

    def fact_error_rate(
        self,
        dataframe
    ):

        total = len(dataframe)

        failures = len(
            dataframe[
                dataframe[
                    "fact_check"
                ] == "Fail"
            ]
        )

        return round(
            failures / total * 100,
            2
        )


if __name__ == "__main__":

    df = pd.read_csv(
        "../../data/processed/evaluation_results.csv"
    )

    metrics = BenchmarkMetrics()

    print(
        metrics.average_accuracy(df)
    )

    print(
        metrics.average_similarity(df)
    )

    print(
        metrics.hallucination_rate(df)
    )

    print(
        metrics.fact_error_rate(df)
    )