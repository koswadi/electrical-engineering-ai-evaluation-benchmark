"""
Ground Truth Similarity
"""

from difflib import SequenceMatcher


class SimilarityScorer:

    def calculate(
        self,
        ground_truth,
        ai_answer
    ):
        """
        Similarity score between 0 and 1.
        """

        score = SequenceMatcher(
            None,
            str(ground_truth).lower(),
            str(ai_answer).lower()
        ).ratio()

        return round(score, 3)


if __name__ == "__main__":

    scorer = SimilarityScorer()

    result = scorer.calculate(
        "Voltage regulation is percentage voltage change",
        "Voltage regulation is voltage change"
    )

    print(result)