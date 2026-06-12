"""
Unit Tests

Benchmark Metrics
"""

import unittest
import pandas as pd

from src.evaluation.benchmark_metrics import (
    BenchmarkMetrics
)


class TestBenchmarkMetrics(
    unittest.TestCase
):

    def setUp(self):

        self.metrics = (
            BenchmarkMetrics()
        )

        self.df = pd.DataFrame({

            "technical_accuracy_score": [
                5,
                4,
                3,
                0
            ],

            "similarity_score": [
                0.95,
                0.80,
                0.65,
                0.10
            ],

            "hallucination_level": [
                "None",
                "None",
                "Major",
                "Critical"
            ],

            "fact_check": [
                "Pass",
                "Pass",
                "Fail",
                "Fail"
            ]
        })

    def test_average_accuracy(self):

        result = (
            self.metrics
            .average_accuracy(
                self.df
            )
        )

        self.assertEqual(
            result,
            3.0
        )

    def test_average_similarity(self):

        result = (
            self.metrics
            .average_similarity(
                self.df
            )
        )

        self.assertAlmostEqual(
    result,
    0.625,
    places=2
)

    def test_hallucination_rate(self):

        result = (
            self.metrics
            .hallucination_rate(
                self.df
            )
        )

        self.assertEqual(
            result,
            50.0
        )

    def test_fact_error_rate(self):

        result = (
            self.metrics
            .fact_error_rate(
                self.df
            )
        )

        self.assertEqual(
            result,
            50.0
        )


if __name__ == "__main__":
    unittest.main()