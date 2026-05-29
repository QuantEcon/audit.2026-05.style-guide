# os_time_iter

- **Series:** lecture-dp
- **File:** `lectures/os_time_iter.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | Title Case in H2/H3 headings. |
| Math         | 8/10  | `\mathscr P` instead of plain `P`; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles, no figsize, no Title-Case labels. |
| References   | 10/10 | Single `{cite}` parenthetical. |
| Links        | 9/10  | `{doc}` used 9×; no raw cross-series URLs. |
| Admonitions  | 9/10  | One `{exercise}` + `solution-start` with `:label:` and dropdown. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-writing-006]** — Title Case in H2/H3 headings. *Examples:* `## The Euler Equation` (68), `### The Coleman-Reffett Operator` (161), `### Is the Coleman-Reffett Operator Well Defined?` (215), `### Comparison with VFI (Theory)` (237), `### Testing` (403). *Count:* 5 headings.
- **[qe-writing-004]** — `\mathscr P` used for the set of policies (lines 181, 222, 234, 235); prefer plain letter.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 37-47).

## Strengths
- Lecture title in correct Title Case (via `{index}` directive).
- Definitions bolded correctly ("**time iteration**", "**Inada conditions**", "**envelope condition**", "**Euler equation**", "**Coleman-Reffett operator**").
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- "IID"/Greek-letter conventions consistent; Unicode Greek in code.
- pip install at top.
- `{doc}` used for cross-series.
- Exercise uses `{exercise}` + `solution-start` with dropdown.

## Recommended actions
1. Convert H2/H3 headings to sentence case.
2. Consider replacing `\mathscr P` with plain `P` (or another simple letter).
