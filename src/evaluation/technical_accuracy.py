"""
Technical Accuracy Evaluation
"""

class TechnicalAccuracyEvaluator:
    """
    Score AI responses from 0 to 5.
    """

    def evaluate(
        self,
        similarity_score,
        hallucination_level
    ):
        """
        Evaluate technical accuracy.
        """

        if hallucination_level == "Critical":
            return 0

        if similarity_score >= 0.90:
            return 5

        if similarity_score >= 0.75:
            return 4

        if similarity_score >= 0.60:
            return 3

        if similarity_score >= 0.40:
            return 2

        return 1


if __name__ == "__main__":

    evaluator = TechnicalAccuracyEvaluator()

    score = evaluator.evaluate(
        similarity_score=0.92,
        hallucination_level="None"
    )

    print(score)