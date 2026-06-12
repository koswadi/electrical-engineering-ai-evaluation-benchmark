"""
Complete Benchmark Workflow Example
"""

from src.evaluation.benchmark_pipeline import (
    BenchmarkPipeline
)


def main():

    pipeline = BenchmarkPipeline()

    ground_truth = (
        "Power factor is the ratio "
        "of real power to apparent power."
    )

    ai_answer = (
        "Power factor greater than 1."
    )

    result = pipeline.evaluate_row(
        ground_truth,
        ai_answer
    )

    print("\nBenchmark Result")

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()