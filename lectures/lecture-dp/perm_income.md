# Style Audit — perm_income

- **Series:** lecture-dp
- **File:** `lectures/perm_income.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.3 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Many Title Case H2/H3/H4 headings. |
| Math         | 5/10  | Apostrophe transpose for matrices throughout the math. |
| Code         | 8/10  | Unicode Greek; no pip install needed; PEP8; figsize used 3×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 6/10  | One `ax.set_title(...)` with f-string; Title-Case `'Time'` xlabel; 3 figsize calls. |
| References   | 5/10  | Three narrative-author `{cite}` patterns (e.g. "Hall {cite}…", "Friedman {cite}…") — should be `{cite:t}`. |
| Links        | 8/10  | Mostly `{doc}` and clean external URLs; one Wikipedia link to "cointegration" (OK). |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Systemic Title Case in H2/H3/H4 headings. *Examples:* `## The Savings Problem` (56), `### Preliminaries` (64), `### The Decision Problem` (107), `### Assumptions` (140), `### First-Order Conditions` (186), `### The Optimal Decision Rule` (217), `#### Responding to the State` (274), `#### A State-Space Representation` (331), `#### A Simple Example with IID Income` (421), `## Alternative Representations` (525), `### Hall's Representation` (530), `### Cointegration` (599), `### Cross-Sectional Implications` (635), `### Impulse Response Functions` (683), `### Moving Average Representation` (691), `## Two Classic Examples` (733), `## Further Reading` (945), `## Appendix: The Euler Equation` (957). *Count:* 20+ headings.

### Medium severity
- **[qe-math-002]** — Apostrophe transpose `'` used in displayed math. *Lines:* 158 (`w_t w_t'`), 394 (`(x_t - \mu_t)'`), 406 (`\tilde A'`, `\tilde C'`), 417 (`\tilde U'`), 669 (`CC'`, `(I-\beta A')`, `U'`). *Count:* 6+ blocks.
- **[qe-ref-001]** — Narrative-author citations using parenthetical `{cite}` rather than `{cite:t}`. *Count:* 3 occurrences ("Milton Friedman {cite}`Friedman1956`", "Robert Hall cast Friedman's model {cite}`Hall1978`", "Hall {cite}`Hall1978` suggested…", "Engle and Granger {cite}`EngleGranger1987`").
- **[qe-fig-003]** — One f-string `ax.set_title(f'Impulse response: {title} income shock')` (line 833).
- **[qe-fig-006]** — Title-Case `xlabel('Time')` on line 501.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 3 times.

## Strengths
- Lecture title in correct Title Case (via `{index}`).
- Definitions bolded ("**random walk**").
- `\mathbb{E}`, `\mathbb{E}_t`, `\mathbb{E}_0` used correctly with braces.
- Matrices use `bmatrix` (M4 compliant).
- "IID" used correctly throughout.
- Equation labels and `{eq}` references used cleanly.
- No `\tag`, no `align`-inside-`$$`, no bold vectors.
- Unicode Greek; PEP8 code.

## Recommended actions
1. Convert all H2/H3/H4 headings to sentence case.
2. Replace every `'` used as transpose with `^\top`.
3. Switch narrative `Author {cite}…` to `{cite:t}` form.
4. Remove the f-string `ax.set_title(...)`.
5. Lowercase the `'Time'` axis label.
