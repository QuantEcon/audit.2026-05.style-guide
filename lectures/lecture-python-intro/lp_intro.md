# lp_intro

- **Series:** lecture-python-intro
- **File:** `lectures/lp_intro.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 9/10  | H1 Title Case OK; H2/H3 sentence case; one-sentence paragraphs. |
| Math         | 8/10  | Equations use `aligned`; uses `\mbox` (older LaTeX style); minor `^\top` consistency. |
| Code         | 8/10  | `!pip install ortools` at top with `hide-output` (qe-code-003 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 8/10  | No `figsize=` / `ax.set_title` violations; no `{figure}` directives. |
| References   | 6/10  | 2 `{cite}` usages, **both in-text** ("created by {cite}", "posed and solved by {cite}") — should be `{cite:t}`. |
| Links        | 9/10  | `{doc}` link present (1 occurrence). |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-ref-001]** — Both in-text citations should use `{cite:t}`. *Examples:* `lectures/lp_intro.md:64` ("created by {cite}\`bertsimas_tsitsiklis1997\`"), 197 ("posed and solved by {cite}\`hu_guo2018\`"). *Count:* 2 occurrences.

### Low severity
- **W1** — A few short two-sentence paragraphs (e.g. lines 175, 182).
- **W7** — Uses `\mbox{subject to}` (line 91); modern usage prefers `\text{subject to}`.

## Strengths
- Section headings sentence case (W3 OK).
- Bold for definitions (**Linear programming**, **primal**, **dual**).
- Italic for emphasis (*maximization*, *minimization*).
- `!pip install ortools` at top with `hide-output` (qe-code-003 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert in-text `{cite}` on lines 64, 197 to `{cite:t}` form.
2. Replace `\mbox` with `\text` per modern LaTeX.
