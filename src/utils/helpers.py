"""
Utility Functions
"""

import os
import pandas as pd


def create_directory(path):
    """
    Create directory if it does not exist.
    """

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def load_csv(file_path):
    """
    Load CSV file.
    """

    return pd.read_csv(file_path)


def save_csv(dataframe, file_path):
    """
    Save DataFrame to CSV.
    """

    dataframe.to_csv(
        file_path,
        index=False
    )

    print(
        f"File saved: {file_path}"
    )


def normalize_text(text):
    """
    Basic text normalization.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    text = text.lower()

    text = text.strip()

    return text


def word_count(text):
    """
    Count words in text.
    """

    return len(
        str(text).split()
    )


def calculate_percentage(
    numerator,
    denominator
):
    """
    Calculate percentage safely.
    """

    if denominator == 0:
        return 0

    return round(
        (numerator / denominator) * 100,
        2
    )


def print_section(title):
    """
    Print formatted section title.
    """

    print("\n" + "=" * 50)

    print(title.upper())

    print("=" * 50)


def summarize_dataset(df):
    """
    Dataset summary.
    """

    summary = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values":
            int(df.isnull().sum().sum())
    }

    return summary


def export_summary(
    summary_dict,
    output_file
):
    """
    Save summary report.
    """

    summary_df = pd.DataFrame(
        summary_dict.items(),
        columns=[
            "Metric",
            "Value"
        ]
    )

    summary_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Summary exported to {output_file}"
    )


if __name__ == "__main__":

    print_section(
        "Utility Test"
    )

    sample_text = (
        "Transformer Efficiency Analysis"
    )

    print(
        normalize_text(sample_text)
    )

    print(
        word_count(sample_text)
    )

    print(
        calculate_percentage(
            18,
            20
        )
    )