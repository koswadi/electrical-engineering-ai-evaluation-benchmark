"""
Unit Tests

Hallucination Detector
"""

import unittest

from src.evaluation.hallucination_detector import (
    HallucinationDetector
)


class TestHallucinationDetector(
    unittest.TestCase
):

    def setUp(self):

        self.detector = (
            HallucinationDetector()
        )

    def test_no_hallucination(self):

        result = self.detector.detect(
            "Voltage regulation is the change in secondary voltage."
        )

        self.assertEqual(
            result,
            "None"
        )

    def test_critical_efficiency(self):

        result = self.detector.detect(
            "Transformer efficiency above 100 percent."
        )

        self.assertEqual(
            result,
            "Critical"
        )

    def test_power_factor_error(self):

        result = self.detector.detect(
            "Power factor greater than 1."
        )

        self.assertEqual(
            result,
            "Critical"
        )

    def test_slack_bus_error(self):

        result = self.detector.detect(
            "Slack bus always zero voltage."
        )

        self.assertEqual(
            result,
            "Critical"
        )


if __name__ == "__main__":
    unittest.main()