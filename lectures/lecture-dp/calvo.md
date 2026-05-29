# Style Audit — calvo

- **Series:** lecture-dp
- **File:** `lectures/calvo.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 5.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2 sentence case throughout; some long paragraphs. |
| Math         | 8/10  | `\vec` used for sequences; otherwise clean. |
| Code         | 5/10  | Duplicate `!pip install` (lines 33 and 82); Unicode Greek; figsize used 5×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 5/10  | Two embedded `ax.set_title`/`fig.suptitle`; 5 figsize; 3 lowercase axis labels. |
| References   | 4/10  | Twelve narrative-author `{cite}` patterns ("Calvo {cite}…", "Chang {cite}…", etc.). |
| Links        | 5/10  | Four raw markdown links to `python-intro.quantecon.org`. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-003]** — Duplicate `!pip install --upgrade quantecon` cells: at top (line 33) and again at line 82. Pip install should appear once at the top of the lecture.
- **[qe-ref-001]** — Twelve narrative-author citations using parenthetical `{cite}` rather than `{cite:t}`. *Examples:* "Calvo {cite}`Calvo1978`" (38, 244, 249, 1424), "Cagan {cite}`Cagan`" (63, 107), "Chang {cite}`chang1998credible`" (75, 153, 244, 249), "Sargent and Wallace's {cite}`sargent1973stability`" (107).

### Medium severity
- **[qe-math-004]** — `\vec \mu`, `\vec \theta`, `\vec v` used extensively (lines 150, 207, 209, 265, 267, 304, 337, 338, 341, 346, 715, 756). *Count:* 23 occurrences.
- **[qe-fig-003]** — Embedded matplotlib titles: `ax.set_title(fr'$\beta$={clq.β}, $c$={clq.c}')` (line 1263), `fig.suptitle(...)` (line 1463).
- **[qe-link-002]** — Four raw markdown links to `python-intro.quantecon.org` (lines 67, 193, 288, 765). Should be `{doc}` form.
- **[qe-fig-001]** — `figsize=` set 5 times.

### Low severity
- **[qe-writing-001]** — A few multi-sentence paragraphs (lines 38-39, 211-218).
- **[qe-writing-005]** — Double-backtick quotes (line 227: ` ``bliss level`` `).

## Strengths
- Lecture title in correct Title Case.
- All H2 headings sentence case.
- Matrices use `bmatrix` consistently (9 matrix blocks).
- Definitions bolded ("**time inconsistency**", "**Definition**", "**square summable**", "**Insight**", "**Ramsey plan**").
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent; Unicode Greek (β, μ, σ) in code.
- No transpose, no `\tag`, no `align`-inside-`$$` issues.

## Recommended actions
1. Remove the duplicate `!pip install` cell (line 82). Keep only the top-of-lecture install.
2. Switch all 12 narrative `Author {cite}…` references to `{cite:t}` form.
3. Remove `\vec` from sequence symbols.
4. Drop the embedded matplotlib titles.
5. Replace 4 raw cross-series markdown URLs with `{doc}` form.
6. Replace ``\`\`bliss level\`\``` with `**bliss level**`.
7. Reduce unnecessary `figsize=` usage.
