"""
Project Constants

Electrical Engineering AI Evaluation Benchmark
"""

# =====================================================
# DATA PATHS
# =====================================================

RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"
FIGURES_PATH = "figures"
REPORTS_PATH = "reports"

# =====================================================
# EVALUATION PARAMETERS
# =====================================================

SIMILARITY_EXCELLENT = 0.90
SIMILARITY_GOOD = 0.75
SIMILARITY_FAIR = 0.60
SIMILARITY_POOR = 0.40

MAX_ACCURACY_SCORE = 5
MIN_ACCURACY_SCORE = 0

# =====================================================
# HALLUCINATION LEVELS
# =====================================================

HALLUCINATION_NONE = "None"
HALLUCINATION_MINOR = "Minor"
HALLUCINATION_MAJOR = "Major"
HALLUCINATION_CRITICAL = "Critical"

# =====================================================
# FACT CHECK STATUS
# =====================================================

FACT_PASS = "Pass"
FACT_FAIL = "Fail"

# =====================================================
# FINAL VERDICTS
# =====================================================

VERDICT_EXCELLENT = "Excellent"
VERDICT_GOOD = "Good"
VERDICT_FAIR = "Fair"
VERDICT_POOR = "Poor"
VERDICT_INCORRECT = "Incorrect"
VERDICT_DANGEROUS = "Dangerous"

# =====================================================
# ENGINEERING DOMAINS
# =====================================================

DOMAINS = [
    "Electrical Fundamentals",
    "Transformer",
    "Power System",
    "Protection",
    "Electrical Machines",
    "Transmission",
    "Distribution",
    "Renewable Energy"
]

# =====================================================
# BENCHMARK CATEGORIES
# =====================================================

DIFFICULTY_LEVELS = [
    "Easy",
    "Medium",
    "Hard"
]

# =====================================================
# KNOWN ENGINEERING FACTS
# =====================================================

KNOWN_FACTS = {
    "maximum transformer efficiency": "<100%",
    "power factor range": "0 to 1",
    "indonesia frequency": "50 Hz",
    "synchronous speed formula": "120f/P",
    "ohms law": "V = IR"
}