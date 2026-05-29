# Style Audit — smoothing_tax

- **Series:** lecture-dp
- **File:** `lectures/smoothing_tax.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 mostly sentence case. |
| Math         | 7/10  | `\mathbb E_t` bare; one bare `E` (line 910). |
| Code         | 8/10  | Unicode Greek; pip install at top; PEP8; figsize 2×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 4/10  | Three `plt.title(...)` / `ax.set_title(...)` calls; 5 Title-Case `'Periods'`/`'Cumulative return'` xlabels/ylabels. |
| References   | 3/10  | Eight narrative-author `{cite}` patterns ("Barro {cite}…", "Hall {cite}…", "Lucas and Stokey {cite}…"). |
| Links        | 8/10  | `{doc}` used 10×; one raw `python.quantecon.org` link. |
| Admonitions  | 8/10  | Two `{exercise}` directives. |

## Issues

### Critical
_None found._

### High severity
- **[qe-ref-001]** — Eight narrative-author citations using parenthetical `{cite}` rather than `{cite:t}`. *Examples:* "Lucas and Stokey {cite}`LucasStokey1983`", "Barro {cite}`Barro1979`", "Hall {cite}`Hall1978`", "Albert Gallatin (1807) {cite}`Gallatin`".

### Medium severity
- **[qe-math-A1]** — `\mathbb E_t` written without braces (lines 877, 884, 892, 898); bare `E` on line 910.
- **[qe-fig-003]** — Three matplotlib title calls. *Lines:* 585 (`plt.title('Tax collection paths')`), 593 (`plt.title('Government debt paths')`), 604 (`ax.set_title('Cumulative return path (complete markets)')`).
- **[qe-fig-006]** — Five Title-Case axis labels (`'Periods'` ×4, `'Cumulative return'`, `'Government expenditures'`). *Lines:* 255, 263, 289, 298, 607, 608, 613.
- **[qe-link-002]** — One raw markdown link to `python.quantecon.org` (in narrative).

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` set 2 times.

## Strengths
- Lecture title in correct Title Case.
- H2/H3 headings mostly sentence case.
- Matrices use `bmatrix`.
- "IID" used correctly.
- Definitions bolded ("**complete markets**", "**incomplete markets**", "**Convention**", "**Returns**").
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors, no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- pip install at top; Unicode Greek; `{doc}` used.

## Recommended actions
1. Switch the 8 narrative `Author {cite}…` references to `{cite:t}` form.
2. Standardise `\mathbb E_t` → `\mathbb{E}_t`; replace bare `E` on line 910 with `\mathbb{E}`.
3. Remove the 3 matplotlib title calls.
4. Lowercase Title-Case axis labels.
5. Convert raw `python.quantecon.org` markdown link to `{doc}` form.
