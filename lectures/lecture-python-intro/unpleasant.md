# Style Audit — unpleasant

- **Series:** lecture-python-intro
- **File:** `lectures/unpleasant.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.6 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | Several H2 use Title Case (W3); some multi-sentence paragraphs. |
| Math         | 7/10  | Uses `{\mathcal S}` for a map (W8 — could use `S`); otherwise clean `aligned`, labels. |
| Code         | 8/10  | Unicode Greek (`α`, `β`, `π`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 6/10  | `figsize=` on lines 475, 564; 1 `ax.set_title(titles[i])` (line 482) outside exercise context; 3 set_title inside solution blocks (OK by exception). |
| References   | 8/10  | 4 `{cite}` usages, parenthetical, no clear in-text mis-use. |
| Links        | 9/10  | `{doc}` cross-references used (6 occurrences). |
| Admonitions  | 9/10  | `{prf:remark}`, `{prf:algorithm}` directives used (qe-admon-004 OK); solutions gated, dropdown, exercise-linked. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **W3** — "## Monetary-Fiscal Policy" (line 78), "## Example Calculations" (line 303) use Title Case; should be sentence case.
- **W1** — Several multi-sentence paragraphs (lines 26–30, 33–35, 78–80, 308–311).
- **W8** — `{\mathcal S}` (lines 289, 292, 297) used for a mapping where simpler `S` would do.
- **[qe-fig-001]** — `figsize=` on lines 475, 564. *Count:* 2 occurrences.
- **[qe-fig-003]** — `ax.set_title(titles[i])` (line 482) outside exercise context. *Count:* 1 occurrence.

### Low severity
- **W2** — H1 has trailing whitespace.
- **W7** — Inconsistent capitalization in subsections (e.g. "Before time $T$").
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Equation labels and `{eq}` references used throughout.
- `aligned` used inside `$$` correctly (M12).
- `prf:remark` / `prf:algorithm` directives used for structure (qe-admon-004 OK).
- Bold for definitions (**fiscal policy**, **monetary policy**, **open market operation**).
- Unicode Greek in code.
- `{doc}` cross-references used (qe-link-002 OK).
- Solutions all gated, dropdown, linked.

## Recommended actions
1. Convert "Monetary-Fiscal Policy" and "Example Calculations" to sentence case.
2. Consider replacing `{\mathcal S}` with `S` per W8.
3. Move `set_title` on line 482 to mystnb/figure metadata.
4. Remove `figsize=` overrides.
5. Split multi-sentence paragraphs.
