"""
Unit Tests

Technical Accuracy Evaluator
"""

import unittest

from src.evaluation.technical_accuracy import (
    TechnicalAccuracyEvaluator
)


class TestTechnicalAccuracyEvaluator(
    unittest.TestCase
):

    def setUp(self):

        self.evaluator = (
            TechnicalAccuracyEvaluator()
        )

    def test_score_5(self):

        score = self.evaluator.evaluate(
            similarity_score=0.95,
            hallucination_level="None"
        )

        self.assertEqual(
            score,
            5
        )

    def test_score_4(self):

        score = self.evaluator.evaluate(
            similarity_score=0.80,
            hallucination_level="None"
        )

        self.assertEqual(
            score,
            4
        )

    def test_score_3(self):

        score = self.evaluator.evaluate(
            similarity_score=0.65,
            hallucination_level="None"
        )

        self.assertEqual(
            score,
            3
        )

    def test_score_2(self):

        score = self.evaluator.evaluate(
            similarity_score=0.45,
            hallucination_level="None"
        )

        self.assertEqual(
            score,
            2
        )

    def test_critical_hallucination(self):

        score = self.evaluator.evaluate(
            similarity_score=0.95,
            hallucination_level="Critical"
        )

        self.assertEqual(
            score,
            0
        )


if __name__ == "__main__":
    unittest.main()