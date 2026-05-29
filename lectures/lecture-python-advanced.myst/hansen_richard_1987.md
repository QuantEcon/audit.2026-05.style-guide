# Style Audit — hansen_richard_1987

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hansen_richard_1987.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 6/10  | 58 bare `E(`/`E[`; `\mathbb{R}` used; no transpose primes detected. |
| Code         | 6/10  | Spelled Greek (6); no install cell (uses numpy/scipy — OK). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 1 `figsize=`; modern figure metadata with captions and names. |
| References   | 9/10  | 8 `{cite}` and 8 `{cite:t}` correctly distinguished. |
| Links        | 8/10  | 3 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 10/10 | 26 `{prf:...}` directives — exemplary proof-family use (qe-admon-004); 1 gated exercise and 1 solution. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-A1]** — 58 bare `E(`/`E[` instead of `\mathbb{E}`. *Count:* 58 occurrences.

### Medium severity
- **[qe-code-002]** — Spelled-out Greek (6 occurrences) in code parameters.

### Low severity
- **[qe-fig-001]** — 1 `figsize=` setting.

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- Heavy correct use of `{cite:t}` and `{cite}` (qe-ref-001) — both 8 occurrences.
- Heavy correct use of `{prf:theorem}`, `{prf:lemma}`, `{prf:definition}`, etc. (qe-admon-004) — 26 occurrences total, exemplary.
- Modern figure metadata with captions and `name: fig-...` (qe-fig-005).
- Exercise gated; solution with `:class: dropdown` (qe-admon-001, qe-admon-002).
- `{doc}` for cross-series references (qe-link-002).

## Recommended actions
1. Convert bare `E(`/`E[` to `\mathbb{E}` notation (qe-math-A1).
2. Convert spelled Greek to unicode in code (qe-code-002).
