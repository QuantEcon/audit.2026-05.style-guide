# Style Audit — hansen_jagannathan_1991

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hansen_jagannathan_1991.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.6 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Title in Title Case; sentence-case headings; one-sentence paragraphs. |
| Math         | 6/10  | 36 bare `E(`/`E[`; `\mathbb{R}` used; `\top` for transpose (13 occurrences). |
| Code         | 6/10  | Mixed unicode/spelled Greek (13 vs 17); no install cell (uses numpy/scipy/yfinance — yfinance not in Anaconda). |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 6 `figsize=`; modern figure metadata with captions and names. |
| References   | 9/10  | 2 `{cite}` and 1 `{cite:t}`; correctly distinguished. |
| Links        | 8/10  | 4 `{doc}` references; no raw cross-series URLs. |
| Admonitions  | 8/10  | 1 gated exercise and 1 solution with `:class: dropdown`; 2 `{prf:...}` directives (correct prefix). |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-A1]** — 36 bare `E(`/`E[` instead of `\mathbb{E}`. *Count:* 36 occurrences.
- **[qe-code-006]** — `yfinance` is not in Anaconda; no install cell with `hide-output` at top — missing install.

### Medium severity
- **[qe-fig-001]** — 6 `figsize=` settings.
- **[qe-code-002]** — Mixed unicode/spelled Greek (17 unicode vs 13 spelled).

### Low severity
_None found._

## Strengths
- Title in Title Case (qe-writing-006).
- Sentence-case headings (qe-writing-006).
- One-sentence paragraph rule followed (qe-writing-001).
- `\top` used for transpose (13 occurrences) (qe-math-002).
- `\mathbb{R}` correctly used.
- Modern figure metadata with `caption:` and `name: fig-...` (qe-fig-005).
- Correct `prf:` prefix on proof directives (qe-admon-004).
- Exercise gated; solution with `:class: dropdown` (qe-admon-001, qe-admon-002).
- `{doc}` for cross-series references (qe-link-002).

## Recommended actions
1. Convert bare `E(`/`E[` to `\mathbb{E}` notation (qe-math-A1).
2. Add install cell with `!pip install yfinance` and `hide-output` tag (qe-code-003, qe-code-006).
3. Reduce `figsize=` usage (qe-fig-001).
4. Standardise on unicode Greek in code (qe-code-002).
