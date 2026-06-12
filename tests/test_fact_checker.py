"""
Unit Tests

Fact Checker
"""

import unittest

from src.evaluation.fact_checker import (
    FactChecker
)


class TestFactChecker(
    unittest.TestCase
):

    def setUp(self):

        self.checker = FactChecker()

    def test_valid_fact(self):

        result = self.checker.check(
            "Frequency Indonesia 50 Hz"
        )

        self.assertEqual(
            result,
            "Pass"
        )

    def test_invalid_fact(self):

        result = self.checker.check(
            "Power factor greater than 1"
        )

        self.assertEqual(
            result,
            "Fail"
        )

    def test_efficiency_error(self):

        result = self.checker.check(
            "Efficiency above 100"
        )

        self.assertEqual(
            result,
            "Fail"
        )

    def test_unknown_statement(self):

        result = self.checker.check(
            "Transformer uses copper windings"
        )

        self.assertEqual(
            result,
            "Pass"
        )


if __name__ == "__main__":
    unittest.main()