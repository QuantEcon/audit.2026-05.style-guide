# Style Audit — equalizing_difference

- **Series:** lecture-python-intro
- **File:** `lectures/equalizing_difference.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1/H2/H3 conventions OK; some longer paragraphs. |
| Math         | 8/10  | Clean math; no transpose needed; equation labels via `(label)`. |
| Code         | 9/10  | Unicode Greek (`γ`, `R`, etc.) used throughout (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 7/10  | All 3 `ax.set_title` calls inside solution blocks (exception applies); one axis label "Career length $T$" with leading uppercase (line 572); no figure `:name:`. |
| References   | 7/10  | `{cite}` used; "Chapter 4 of Jennifer Burns {cite}\`Burns_2023\`" (line 25) is in-text and should be `{cite:t}`. |
| Links        | N/A   | no cross-series links |
| Admonitions  | 9/10  | Solutions use `:class: dropdown` + exercise labels; gated form throughout (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W1** — Several multi-sentence paragraphs (e.g. lines 22–25, 30–35).
- **[qe-ref-001]** — In-text citation should use `{cite:t}`. *Example:* `lectures/equalizing_difference.md:25` ("Chapter 4 of Jennifer Burns {cite}\`Burns_2023\`"). *Count:* 1 occurrence (with additional adjacent `{cite}` that may also need review).

### Low severity
- **W7** — Inconsistent quotes: uses both `''equalizing difference''` (line 32) and `"equalizing"` (line 139).
- **W4** — "**equalizing difference**" bold for definition (good); "**free college** special case" minor.
- **[qe-fig-006]** — Axis label "Career length $T$" (line 572) starts with uppercase; should be "career length $T$".
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Headings comply with W2/W3.
- Clean equation labels and `{eq}` references.
- Bold used for definitions.
- Unicode Greek in code (qe-code-002 OK).
- All 4 solutions gated, dropdown, linked.

## Recommended actions
1. Break compound paragraphs in Overview into one-sentence units.
2. Normalize quote style (replace `''...''` with `"..."`).
3. Convert "Chapter 4 of Jennifer Burns {cite}" → `{cite:t}` form (line 25).
4. Lowercase axis label "Career length" → "career length".
