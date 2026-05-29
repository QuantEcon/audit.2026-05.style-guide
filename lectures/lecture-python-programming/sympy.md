# Style Audit — sympy

- **Series:** lecture-python-programming
- **File:** `lectures/sympy.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Some H2 in sentence case; H3 mostly sentence case; H2 stragglers remain. |
| Math         | 6/10  | Bare `E(X)` used as expectation violates qe-math-A1. |
| Code         | 8/10  | Only Anaconda packages (sympy, numpy, matplotlib); Greek unicode (λ) used as a SymPy `Symbol` per qe-code-002; `from sympy import *` is a star-import — pedagogically common in SymPy intros but technically discouraged by PEP8 (qe-code-001 nit). |
| JAX          | out of scope | — |
| Figures      | N/A   | No matplotlib figures (SymPy's own `plot()` is used but produces inline output, no figure metadata). |
| References   | N/A   | No citations. |
| Links        | 7/10  | Two bare URLs to sibling series. *Examples:* line 200 `[trigonometry and complex numbers](https://python.quantecon.org/complex_and_trig.html)`, line 313 `[geometric series](https://intro.quantecon.org/geom_series.html...)`, line 664 `[Maximum likelihood estimation (MLE)](https://python.quantecon.org/mle.html)` — should be `{doc}` links with intersphinx prefix per qe-link-002. |
| Admonitions  | 8/10  | Two `{exercise-start}` and two `{exercise}` (line 612, 661) gated/non-gated mix; two `{solution-start}` with `:class: dropdown` and `:label:` per qe-admon-005. |

## Issues

### Critical
_None found._

### High severity
- **[qe-link-002]** — Three bare URLs to sibling lecture series. *Examples:* line 200 (`python.quantecon.org/complex_and_trig.html`), line 313 (`intro.quantecon.org/geom_series.html`), line 664 (`python.quantecon.org/mle.html`) — should use `` {doc}`intermediate:complex_and_trig` ``, `` {doc}`intro:geom_series` ``, `` {doc}`intermediate:mle` ``. *Count:* 3 occurrences.

### Medium severity
- **[qe-writing-006]** *(carry-forward W3)* — A few H2 headings use Title Case. *Examples:* line 45 `## Getting Started`, line 371 `## Symbolic Calculus`, line 470 `## Plotting`, line 515 `## Application: Two-person Exchange Economy`, line 610 `## Exercises`. *Count:* 5 occurrences.
- **[qe-math-A1]** *(carry-forward M7)* — Bare `E(X)` used for expectation rather than `\mathbb{E}[X]`. *Example:* line 349 `E(X) = \sum_{x=0}^{\infty} x f(x)`. *Count:* 1 occurrence in display math (plus `E(X)` echoed at line 368 in code — but that is a SymPy `E` *symbol*, which is intentionally what `from sympy.stats import E` provides).

### Low severity
- **[qe-writing-004]** *(carry-forward W7)* — Mixed casing inside `## Application: Two-person Exchange Economy` (line 515).
- **[qe-code-001]** — `from sympy import *` (line 50) is a star-import; common in SymPy tutorials but discouraged by PEP8.
- **[qe-admon-001]** — Two exercises use bare `{exercise}` rather than gated syntax (lines 612, 661); bodies are prose-only.

## Strengths
- Lecture title "SymPy" follows qe-writing-006.
- Many H2 headings already use sentence case ("Symbolic algebra"); H3 mostly sentence case.
- Lowercase `f` for densities/PMFs per qe-math-A4 (lines 323, 412).
- Sequences correctly use `\{...\}` (e.g., `\{\xi_t\}`) per qe-math-005.
- Greek unicode (λ) used as a SymPy `Symbol` per qe-code-002.
- Exercise/solution pairs use `:class: dropdown` and `:label:` per qe-admon-002/qe-admon-005.

## Recommended actions
1. Convert the three bare quantecon.org URLs (lines 200, 313, 664) to `{doc}` cross-series links.
2. Convert remaining Title Case H2 headings to sentence case ("Getting started", "Symbolic calculus", "Application: two-person exchange economy").
3. Replace narrative `E(X) = \sum ...` with `\mathbb{E}[X] = \sum ...` (the SymPy code `E(X)` may remain since it's the SymPy function name).
4. Optionally replace `from sympy import *` with explicit named imports.
