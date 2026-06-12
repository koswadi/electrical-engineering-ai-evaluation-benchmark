# Evaluation Criteria

## Purpose

This document defines the scoring criteria used in the benchmark framework.

---

# Technical Accuracy

Technical accuracy measures how well an AI response aligns with accepted Electrical Engineering knowledge.

## Score Definitions

| Score | Description |
|---------|------------|
| 5 | Fully Correct |
| 4 | Mostly Correct |
| 3 | Partially Correct |
| 2 | Significant Errors |
| 1 | Incorrect |
| 0 | Dangerous |

---

## Example

### Question

```text
What is transformer voltage regulation?
```

### Correct Response

```text
Voltage regulation is the percentage change in secondary voltage between no-load and full-load conditions.
```

Score:

```text
5
```

---

# Similarity Score

Measures alignment with the reference answer.

Range:

```text
0.0 – 1.0
```

Interpretation:

| Similarity | Interpretation |
|------------|---------------|
| > 0.90 | Excellent |
| 0.75–0.90 | Good |
| 0.60–0.75 | Fair |
| < 0.60 | Poor |

---

# Fact Verification

Responses are checked against engineering facts.

Examples:

| Statement | Valid |
|------------|--------|
| Power factor > 1 | No |
| Efficiency > 100% | No |
| Indonesia frequency = 50 Hz | Yes |

---

# Hallucination Detection

Hallucinations are classified into four levels.

## None

Technically correct.

Example:

```text
Transformer cores are laminated to reduce eddy currents.
```

---

## Minor

Small omission.

Example:

```text
Transformer efficiency is output power divided by input power.
```

(Percentage aspect omitted.)

---

## Major

Contains important technical errors.

Example:

```text
High-voltage transmission increases current.
```

---

## Critical

Dangerous engineering misinformation.

Example:

```text
Transformer efficiency exceeds 100%.
```

---

# Final Verdict

| Verdict | Condition |
|----------|------------|
| Excellent | Accuracy ≥ 4.5 |
| Good | Accuracy ≥ 4 |
| Fair | Accuracy ≥ 3 |
| Poor | Accuracy ≥ 2 |
| Incorrect | Accuracy < 2 |
| Dangerous | Critical Hallucination |