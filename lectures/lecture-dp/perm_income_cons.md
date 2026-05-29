# Style Audit — perm_income_cons

- **Series:** lecture-dp
- **File:** `lectures/perm_income_cons.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | Title Case in many H2/H3/H4 headings. |
| Math         | 4/10  | Apostrophe transpose throughout LQ section; bare `E_0`/`E_t`. |
| Code         | 7/10  | Unicode Greek; pip install at top; PEP8; figsize used 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 8/10  | No matplotlib titles; no Title-Case labels; 3 figsize calls. |
| References   | 5/10  | `Hall {cite}`Hall1978`` and similar narrative-author cases (2×) — should be `{cite:t}`. |
| Links        | 4/10  | One raw markdown link to `python-intro.quantecon.org/perm_income.html` instead of `{doc}`. |
| Admonitions  | N/A   | No exercises. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Apostrophe `'` used as transpose throughout the LQ derivation. *Lines:* 228, 240, 244, 247, 249, 251, 280, and matrix sections through to 720. *Count:* 25+ occurrences.
- **[qe-writing-006]** — Systemic Title Case H2/H3/H4 headings. *Examples:* `### Digression on a Useful Isomorphism` (137), `### A Specification of the Nonfinancial Income Process` (165), `## The LQ Approach` (201), `### The LQ Problem` (221), `### Mapping into the LQ Framework` (253), `### The Exogenous Nonfinancial Income Process` (328), `### Comparison with the Difference Equation Approach` (407), `## Two Example Economies` (472), `### First Set of Initial Conditions` (494), `### Population and Sample Panels` (508), `### A "Borrowers and Lenders" Closed Economy` (721). *Count:* 12+ headings.

### Medium severity
- **[qe-math-A1]** — Expectation written as plain `E_0`, `E_t` rather than `\mathbb{E}` (lines 94, 115). *Count:* 2.
- **[qe-ref-001]** — Author-name narrative citations using parenthetical `{cite}` instead of textual `{cite:t}`. *Count:* 2 occurrences ("Hall {cite}…", "Robert Hall {cite}…" patterns).
- **[qe-link-002]** — Raw markdown link to `python-intro.quantecon.org/perm_income.html` (line) where `{doc}` is preferred.
- **[qe-fig-001]** — `figsize=` set 3 times.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- Matrices use `bmatrix` (lines 180-200, 259-269).
- "IID" used correctly (line 240).
- Equation labels and `{eq}` references used cleanly.
- pip install correctly at top.
- Unicode Greek in code cells.
- No matplotlib titles, no Title-Case axis labels.
- No `\tag`, no `align`-inside-`$$`, no bold vectors.

## Recommended actions
1. Replace every `'` used as transpose with `^\top` (or restructure the matrix-math).
2. Replace bare `E_0`/`E_t` with `\mathbb{E}_0`/`\mathbb{E}_t`.
3. Convert all H2/H3/H4 headings to sentence case.
4. Switch narrative `Author {cite}…` to `{cite:t}` form.
5. Convert raw `python-intro.quantecon.org` markdown link to `{doc}` form.
