"""
Engineering Hallucination Detection
"""

class HallucinationDetector:

    CRITICAL_PATTERNS = [
        "efficiency above 100",
        "power factor greater than 1",
        "negative resistance transformer",
        "transformer generates energy",
        "slack bus always zero voltage"
    ]

    def detect(
        self,
        answer
    ):

        answer = answer.lower()

        for pattern in self.CRITICAL_PATTERNS:

            if pattern in answer:

                return "Critical"

        return "None"


if __name__ == "__main__":

    detector = HallucinationDetector()

    result = detector.detect(
        "Transformer efficiency above 100 percent"
    )

    print(result)