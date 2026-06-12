"""
Example Evaluation

Demonstrates how to evaluate
an AI-generated Electrical Engineering response.
"""

from src.evaluation.similarity_score import (
    SimilarityScorer
)

from src.evaluation.hallucination_detector import (
    HallucinationDetector
)

from src.evaluation.fact_checker import (
    FactChecker
)

from src.evaluation.technical_accuracy import (
    TechnicalAccuracyEvaluator
)


def main():

    question = (
        "What is transformer voltage regulation?"
    )

    ground_truth = (
        "Voltage regulation is the percentage "
        "change in secondary voltage from "
        "no-load to full-load conditions."
    )

    ai_answer = (
        "Voltage regulation is the change "
        "in transformer secondary voltage "
        "between no-load and full-load conditions."
    )

    print("=" * 60)
    print("ELECTRICAL ENGINEERING AI EVALUATION")
    print("=" * 60)

    print(f"\nQuestion:\n{question}")

    print(f"\nGround Truth:\n{ground_truth}")

    print(f"\nAI Answer:\n{ai_answer}")

    similarity = SimilarityScorer()

    similarity_score = similarity.calculate(
        ground_truth,
        ai_answer
    )

    hallucination_detector = (
        HallucinationDetector()
    )

    hallucination_level = (
        hallucination_detector.detect(
            ai_answer
        )
    )

    fact_checker = FactChecker()

    fact_result = fact_checker.check(
        ai_answer
    )

    accuracy_evaluator = (
        TechnicalAccuracyEvaluator()
    )

    accuracy_score = (
        accuracy_evaluator.evaluate(
            similarity_score,
            hallucination_level
        )
    )

    print("\nRESULTS")
    print("-" * 60)

    print(
        f"Similarity Score: "
        f"{similarity_score}"
    )

    print(
        f"Hallucination Level: "
        f"{hallucination_level}"
    )

    print(
        f"Fact Check: "
        f"{fact_result}"
    )

    print(
        f"Technical Accuracy Score: "
        f"{accuracy_score}/5"
    )

    print("-" * 60)


if __name__ == "__main__":
    main()