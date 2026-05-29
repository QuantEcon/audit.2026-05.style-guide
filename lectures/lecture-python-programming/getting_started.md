# Style Audit — getting_started

- **Series:** lecture-python-programming
- **File:** `lectures/getting_started.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6.5/10| Section headings systematically use Title Case. |
| Math         | N/A   | No math. |
| Code         | 8/10  | Single demo code cell uses Greek unicode (θ) per qe-code-002; no non-Anaconda packages. |
| JAX          | out of scope | — |
| Figures      | 7/10  | Many `{figure}` directives for installer screenshots (lines 154, 182, 195, 207, 230, 320, 338, 357, 363, 378, 397). All lack `name:` and `caption:` metadata. |
| References   | N/A   | No citations. |
| Links        | 9/10  | External links only; no improper cross-series URL patterns. |
| Admonitions  | 8/10  | One `{exercise-start}`/`{exercise-end}` block correctly gated; `{note}` and `{index}` directives used cleanly. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** *(carry-forward W3)* — Section headings use Title Case rather than sentence case. *Examples:* line 50 `## Python in the Cloud`, line 67 `## Local Install`, line 77 `### The Anaconda Distribution`, line 105 `### Installing Anaconda`, line 167 `### Starting the Jupyter Notebook`, line 213 `### Notebook Basics`, line 302 `### Working with the Notebook`, line 367 `### Debugging Code`, line 403 `### Sharing Notebooks`, line 432 `### QuantEcon Notes`, line 440 `## Installing Libraries`, line 492 `## Working with Python Files`, line 515 `### Editing and Execution`, line 558 `## Exercises`. *Count:* 14+ occurrences.

### Medium severity
- **[qe-fig-005]** — All eleven `{figure}` directives lack a `name:` field, preventing `{numref}` cross-referencing. *Lines:* 154, 182, 195, 207, 230, 320, 338, 357, 363, 378, 397.

### Low severity
- **[qe-writing-001]** *(carry-forward W1)* — A handful of multi-sentence paragraphs in installation prose, mostly justified by the procedural nature.
- **[qe-fig-004]** — Most screenshots have no caption text; appropriate for procedural installer screenshots but slightly inconsistent with a captioning-encouraged style.

## Strengths
- Lecture title "Getting Started" follows qe-writing-006.
- Clean lists, code-cell examples, inline `code` formatting.
- Index roles (`{index}`) used correctly.
- Greek unicode (θ) used in the test program per qe-code-002.
- Exercise uses gated `exercise-start`/`exercise-end` syntax per qe-admon-001.

## Recommended actions
1. Convert section headings to sentence case ("Python in the cloud", "Local install", "The Anaconda distribution", "Installing Anaconda", "Notebook basics", "Working with the notebook", "Debugging code", "Sharing notebooks", "Installing libraries", "Working with Python files", "Editing and execution").
2. Add `name:` (e.g., `fig-jp-demo`, `fig-starting-nb`, …) to each `{figure}` directive for future cross-referencing.
