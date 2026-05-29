# laffer_adaptive

- **Series:** lecture-python-intro
- **File:** `lectures/laffer_adaptive.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | H1 Title Case (with double-space), H2 sentence case OK; multi-sentence paragraphs throughout. |
| Math         | 8/10  | Mostly clean; correct sequences, no transpose violations. |
| Code         | 8/10  | Unicode Greek (`π`, `α`, `δ`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 366, 531; 2 `ax.set_title(...)` inside solution blocks (OK by exception). |
| References   | 6/10  | 7 `{cite}` usages; 2 are clearly in-text ("used by {cite}", "studied by {cite}") — should be `{cite:t}`. |
| Links        | 9/10  | `{doc}` cross-references used (9 occurrences). |
| Admonitions  | 9/10  | Solutions gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Multiple multi-sentence paragraphs in Overview (lines 33, 44–46) and several places. *Count:* ~6 paragraphs.
- **[qe-ref-001]** — In-text citations using `{cite}` instead of `{cite:t}`. *Examples:* `lectures/laffer_adaptive.md:23` ("used by {cite}\`Cagan\` and {cite}\`Friedman1956\`"), 42 ("studied by {cite}\`bruno1990seigniorage\`"). *Count:* 2 sentences.
- **[qe-fig-001]** — `figsize=` overrides on lines 366, 531. *Count:* 2 occurrences.

### Low severity
- **W2** — H1 has trailing space "Laffer Curves  with Adaptive Expectations " (line 14).
- **W7** — Quoted phrases ("old time religion", "rational expectations", "perfect foresight") sometimes paired inconsistently.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Equation labels and `{eq}` cross-references used correctly (M14).
- Section headings comply with W3.
- Math notation generally clean.
- Unicode Greek in code (qe-code-002 OK).
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert in-text `{cite}` usages on lines 23, 42 to `{cite:t}`.
2. Remove `figsize=` overrides.
3. Split multi-sentence paragraphs per W1.
4. Trim trailing whitespace from H1.
