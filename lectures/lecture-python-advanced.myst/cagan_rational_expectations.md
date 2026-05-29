# Style Audit — cagan_rational_expectations

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/cagan_rational_expectations.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case (with `?`); sentence-case headings; one-sentence paragraphs. |
| Math         | 7/10  | Bare `E_t` used 14 times; otherwise clean (uses `\top` for transpose; no `\mathcal{N}`; uses `aligned`). |
| Code         | 8/10  | Unicode Greek heavily used (11 occurrences vs 18 spelled mostly in legacy code); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 8/10  | Modern lecture with mystnb captions and `name: fig-...` fields; 2 `figsize=`; 1 `ax.set_title`. |
| References   | 9/10  | 13 `{cite}` and 10 `{cite:t}` correctly distinguished. |
| Links        | 8/10  | 3 `{doc}` (incl. `intro:cagan_ree`); no raw cross-series URLs. |
| Admonitions  | 8/10  | 3 gated exercises and 3 solutions with `:class: dropdown`. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-A1]** — Bare `E_t` used 14 times instead of `\mathbb{E}_t`. *Example:* `lectures/cagan_rational_expectations.md:155`, `:158`, `:167`. *Count:* 14 occurrences.

### Medium severity
- **[qe-fig-003]** — 1 `ax.set_title` occurrence.
- **[qe-math-003]** — 2 `\begin{pmatrix}` occurrences should use `\begin{bmatrix}`.
- **[qe-fig-006]** — `set_xlabel("...")` with capitalised content (e.g. "Mean") — 2 occurrences.

### Low severity
- **[qe-code-002]** — Mixed spelled and unicode Greek in code (18 spelled vs 11 unicode); ratio is shifting toward unicode.
- **[qe-fig-001]** — 2 `figsize=` settings.

## Strengths
- Title in Title Case with question mark (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- Heavy correct use of `{cite:t}` for narrative author refs (qe-ref-001).
- `{doc}\`intro:cagan_ree\`` and `{doc}\`muth_kalman\`` style intersphinx (qe-link-002).
- `\top` used for transpose (qe-math-002).
- Sequences `\{ ... \}` (qe-math-005).
- Equation labels with `:label:` and `{eq}` references (qe-math-007).
- Modern figure metadata with `mystnb: figure: caption: ... name: fig-...` (qe-fig-005).
- Exercises gated; solutions with `:class: dropdown` (qe-admon-001, qe-admon-002).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Convert bare `E_t` to `\mathbb{E}_t` (qe-math-A1).
2. Remove `ax.set_title` (qe-fig-003).
3. Convert 2 `\begin{pmatrix}` to `\begin{bmatrix}` (qe-math-003).
4. Lowercase axis labels (qe-fig-006).
5. Standardise on unicode Greek in code (qe-code-002).
