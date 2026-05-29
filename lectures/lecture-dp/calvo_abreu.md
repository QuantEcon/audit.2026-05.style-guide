# Style Audit — calvo_abreu

- **Series:** lecture-dp
- **File:** `lectures/calvo_abreu.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2/H3 sentence case throughout; some long paragraphs. |
| Math         | 8/10  | `\vec` used for sequences; otherwise clean. |
| Code         | 8/10  | Unicode Greek; pip install at top (line 278) — but late in file; figsize 1×. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 9/10  | No matplotlib titles; no spine; figsize 1×; no Title-Case labels. |
| References   | 4/10  | Seven narrative-author `{cite}` patterns. |
| Links        | 9/10  | Five `{doc}` references; no raw cross-series URLs. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-ref-001]** — Seven narrative-author citations using parenthetical `{cite}` rather than `{cite:t}`. *Examples:* "Guillermo Calvo {cite}`Calvo1978`" (35), "Cagan {cite}`Cagan`" (49), "Calvo {cite}`Calvo1978`" (49), "Chang {cite}`chang1998credible`" (49, 117), "Abreu {cite}`Abreu`" (51), "Stokey {cite}`stokey1989reputation`" (51), "Stokey {cite}`Stokey1991`" (154).

### Medium severity
- **[qe-math-004]** — `\vec \mu`, `\vec \theta` used 22 times in narrative. *Lines:* 35, 37, 115, 116, etc.
- **[qe-code-003]** — `!pip install --upgrade quantecon` placed mid-lecture (line 278) rather than at top.

### Low severity
- **[qe-writing-001]** — Several multi-sentence paragraphs (e.g. 35-42, 46-52).
- **[qe-math-005]** — Sequence written with parentheses elsewhere mostly OK; one `(c_t)_{t=0}` style.

## Strengths
- Lecture title in correct Title Case.
- All H2/H3 headings sentence case ("Model components", "Another timing protocol", "Government decisions", "Temptation to deviate from plan", "Sustainable or credible plan", "Abreu's self-enforcing plan", "Abreu's carrot-stick plan").
- Definitions bolded ("**time inconsistency**", "**Stackelberg**", "**Ramsey planner**", "**credible government policy**", "**sustainable plan**").
- Equation labels and `{eq}` references used cleanly.
- No transpose, no bold vectors (apart from `\vec`), no matrix-bracket, no `\tag`, no `align`-inside-`$$` issues.
- `{doc}` used for cross-series references; no raw URLs.

## Recommended actions
1. Switch narrative `Author {cite}…` to `{cite:t}` form (7 occurrences).
2. Remove `\vec` arrows from sequence symbols.
3. Move `!pip install` to the very top of the lecture.
4. Tighten multi-sentence paragraphs.
