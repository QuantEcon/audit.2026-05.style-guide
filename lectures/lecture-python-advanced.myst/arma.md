# arma

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arma.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | Sentence-case headings; clean one-sentence paragraphs. |
| Math         | 8/10  | `\mathbf 1` for indicator (qe-math-008 spirit). |
| Code         | 6/10  | Spelled Greek (`alpha`, `beta`, etc.) used heavily (17 occurrences); install cell with `hide-output`. |
| JAX          | N/A   | not a JAX lecture |
| Figures      | 7/10  | 5 `figsize=`; no `:name:` fields; one `{only} latex` directive present (good for plotly-ish placeholder). |
| References   | 8/10  | 15 `{cite}` consistently used; never uses `{cite:t}`. |
| Links        | 7/10  | One raw `python-programming.quantecon.org` URL (L874); one raw `python-intro.quantecon.org` URL (L50). |
| Admonitions  | N/A   | no exercises, solutions, or proof-family directives. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Raw cross-series URLs instead of `{doc}`. *Example:* `lectures/arma.md:50` (`python-intro.quantecon.org/linear_models.html`), `:874` (`python-programming.quantecon.org/python_advanced_features.html#descriptors`). *Count:* 2 occurrences.
- **[qe-code-002]** — Spelled-out Greek (`alpha`, `beta`, `phi`, `theta`) in code parameters instead of unicode (17 occurrences across code cells).

### Low severity
- **[qe-math-008]** — `\mathbf 1\{k = 0\}` used for the indicator function. *Example:* `lectures/arma.md:134`, `:136`. *Count:* 2 occurrences.
- **[qe-fig-005]** — Figures lack `:name: fig-...` fields.
- **[qe-fig-001]** — `figsize=` set 5 times.
- **[qe-ref-001]** — `{cite:t}` never used; some narrative refs (e.g. "Sargent 1987") would benefit.

## Strengths
- Title uses Title Case via `{index}` directive (qe-writing-006).
- Sentence-case subheadings (qe-writing-006).
- Sequences in curly brackets `\{X_t\}` (qe-math-005).
- `\mathbb Z`, `\mathbb R` notation correct.
- One-sentence paragraph rule respected (qe-writing-001).
- Install cell at top with `hide-output` (qe-code-003).

## Recommended actions
1. Switch `\mathbf 1` to `\mathbb{1}` for the indicator and add a one-line explanation (qe-math-008).
2. Convert raw cross-series URLs to `{doc}\`intermediate:linear_models\`` / `{doc}\`programming:python_advanced_features\`` (qe-link-002).
3. Convert spelled Greek to unicode in code (qe-code-002).
4. Add `:name: fig-...` fields to figures (qe-fig-005).
