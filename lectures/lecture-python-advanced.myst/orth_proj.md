# Style Audit — orth_proj

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/orth_proj.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 6.4 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | Title in Title Case; sentence-case headings; clean one-sentence paragraphs. |
| Math         | 3/10  | Systemic primes as transpose; `\begin{array}` blocks for matrices. |
| Code         | 8/10  | 4 spelled Greek; no install cell (numpy only — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 6/10  | 6 `{figure}` directives reference static PNGs; no `:name:` fields. |
| References   | 9/10  | 1 `{cite}` used. |
| Links        | 9/10  | No cross-series URL links; self-contained. |
| Admonitions  | 9/10  | 3 gated exercises and 3 solutions with `:class: dropdown`; 18 `{prf:...}` directives — exemplary proof-family use. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-002]** — Prime `'` used systematically as transpose. *Example:* `P = X (X' X)^{-1} X' y`, `U' U = I`, `(R' R)^{-1} R'`. *Count:* ~47 occurrences.
- **[qe-math-003]** — `\begin{array}{c}` (and `{cccc}`) used for matrices instead of `\begin{bmatrix}`. *Example:* `lectures/orth_proj.md:535`, `:545`, `:560`, `:569`, `:777`. *Count:* 6 occurrences.

### Medium severity
- **[qe-fig-002]** — 6 `{figure}` directives reference static schematic PNGs.

### Low severity
- **[qe-math-010 (proposed)]** — Two `\mathbb{E}` occurrences (per scan).
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-code-002]** — 4 spelled Greek in code.

## Strengths
- Title in Title Case (qe-writing-006).
- Subheadings sentence case (qe-writing-006).
- Sentence-case definitions in bold (e.g. `**orthogonal**`, `**orthogonal complement**`) follow qe-writing-005.
- One-sentence paragraph rule respected (qe-writing-001).
- Heavy correct `prf:` directive use (qe-admon-004) — 18 occurrences.
- Exercises gated; solutions use `:class: dropdown` (qe-admon-001, qe-admon-002).

## Recommended actions
1. Replace prime `'` with `^\top` for transpose throughout (qe-math-002).
2. Convert `\begin{array}` blocks to `\begin{bmatrix}` (qe-math-003).
3. Add `:name: fig-...` fields (qe-fig-005).
