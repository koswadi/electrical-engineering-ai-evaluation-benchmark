"""
End-to-End Benchmark Pipeline
"""

import pandas as pd

from similarity_score import SimilarityScorer
from hallucination_detector import HallucinationDetector
from technical_accuracy import TechnicalAccuracyEvaluator
from fact_checker import FactChecker


class BenchmarkPipeline:

    def __init__(self):

        self.similarity = SimilarityScorer()

        self.hallucination = (
            HallucinationDetector()
        )

        self.accuracy = (
            TechnicalAccuracyEvaluator()
        )

        self.fact_checker = (
            FactChecker()
        )

    def evaluate_row(
        self,
        ground_truth,
        answer
    ):

        similarity_score = (
            self.similarity.calculate(
                ground_truth,
                answer
            )
        )

        hallucination_level = (
            self.hallucination.detect(
                answer
            )
        )

        fact_check = (
            self.fact_checker.check(
                answer
            )
        )

        accuracy_score = (
            self.accuracy.evaluate(
                similarity_score,
                hallucination_level
            )
        )

        return {
            "similarity_score":
                similarity_score,

            "hallucination_level":
                hallucination_level,

            "fact_check":
                fact_check,

            "technical_accuracy_score":
                accuracy_score
        }


if __name__ == "__main__":

    pipeline = BenchmarkPipeline()

    result = pipeline.evaluate_row(

        "Power factor is ratio of real power to apparent power",

        "Power factor greater than 1"
    )

    print(result)