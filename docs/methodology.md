# Methodology

## Overview

This project evaluates AI-generated responses in Electrical Engineering domains using a benchmark-based assessment framework.

The evaluation process consists of:

1. Question Selection
2. Ground Truth Development
3. AI Response Collection
4. Similarity Assessment
5. Hallucination Detection
6. Fact Verification
7. Technical Accuracy Scoring
8. Benchmark Reporting

---

## Evaluation Workflow

```text
Question
    ↓
Ground Truth Answer
    ↓
AI Generated Response
    ↓
Similarity Analysis
    ↓
Fact Checking
    ↓
Hallucination Detection
    ↓
Technical Accuracy Scoring
    ↓
Final Evaluation
```

---

## Data Sources

The benchmark dataset consists of Electrical Engineering questions covering:

- Electrical Fundamentals
- Transformers
- Power Systems
- Protection Systems
- Electrical Machines

Each question is paired with a reference answer developed from standard engineering knowledge.

---

## Similarity Analysis

Ground truth answers are compared with AI-generated answers.

Current implementation uses:

- Sequence Similarity
- Text Matching

Future improvements may include:

- Sentence Embeddings
- Semantic Similarity Models
- LLM-as-a-Judge Evaluation

---

## Fact Verification

Engineering facts are checked against known technical constraints.

Examples:

| Statement | Expected |
|------------|-----------|
| Transformer efficiency | < 100% |
| Power factor | 0 to 1 |
| Indonesia grid frequency | 50 Hz |

---

## Hallucination Detection

The framework identifies technically incorrect engineering statements.

Hallucinations are classified as:

- None
- Minor
- Major
- Critical

---

## Technical Accuracy Scoring

Scores range from 0 to 5.

| Score | Description |
|---------|------------|
| 5 | Fully Correct |
| 4 | Mostly Correct |
| 3 | Partially Correct |
| 2 | Significant Errors |
| 1 | Incorrect |
| 0 | Dangerous Misinformation |

---

## Outputs

The framework generates:

- Evaluation Results
- Visualizations
- Performance Metrics
- PDF Reports

---

## Future Work

- Larger benchmark datasets
- Transformer-specific evaluation
- Power system reasoning benchmarks
- LLM-as-a-Judge integration
- Automated engineering fact retrieval