# Style Audit — tax_smoothing_1

- **Series:** lecture-dp
- **File:** `lectures/tax_smoothing_1.md`
- **Audit date:** 2026-05-28
- **Spec version:** v2
- **Categories audited:** writing, math, code, jax, figures, references, links, admonitions
- **Overall score:** 6.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H2 sentence case. |
| Math         | 6/10  | `\cal N`; bare `E_0`; apostrophe transpose. |
| Code         | 5/10  | `!pip install` placed mid-lecture (line 162) not at top; Unicode Greek elsewhere; no figsize. |
| JAX          | out of scope | not a JAX lecture. |
| Figures      | 8/10  | No matplotlib titles, no figsize, no Title-Case labels in matplotlib. |
| References   | 4/10  | Many narrative-author `{cite}` patterns (Barro mentioned repeatedly with `{cite}`). |
| Links        | 8/10  | `{doc}` used 5×; one raw markdown URL. |
| Admonitions  | N/A   | No exercises / proofs. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-003]** — `!pip install --upgrade quantecon` placed mid-lecture (line 162) rather than at the top.
- **[qe-ref-001]** — Many narrative-author `{cite}` patterns: "{cite}`Barro1979` model" repeated, "{cite}`barro1999determinants`", "{cite}`barro2003religion`". Should be `{cite:t}` form for narrative use. *Count:* ~13 occurrences.

### Medium severity
- **[qe-math-A3]** — Multivariate normal written as `{\cal N}(0,I)` (line 220).
- **[qe-math-A1]** — Bare `E_0` for expectation in display equations (lines 70, 203). Should be `\mathbb{E}_0`.
- **[qe-math-002]** — Apostrophe transpose in LQ section. *Count:* ~6 occurrences in later derivation.
- **[qe-link-002]** — One raw markdown link to `python.quantecon.org` (line).

### Low severity
- **[qe-writing-A1]** — Smart quotes ’ in narrative.
- **[qe-writing-001]** — Several multi-sentence paragraphs.

## Strengths
- Lecture title in correct Title Case.
- All H2 headings sentence case.
- Matrices use `bmatrix` (6 matrix blocks).
- Definitions bolded.
- Equation labels and `{eq}` references used cleanly.
- "IID"/Greek-letter conventions consistent.
- No `\tag`, no bold vectors, no `align`-inside-`$$` issues.
- `{doc}` used for cross-series; no matplotlib titles.

## Recommended actions
1. Move the `!pip install` to the top of the lecture.
2. Switch narrative `Author {cite}…` to `{cite:t}` form throughout.
3. Replace `{\cal N}` with plain `N`.
4. Replace bare `E_0` with `\mathbb{E}_0`.
5. Replace apostrophe transpose with `^\top`.
6. Convert raw `python.quantecon.org` markdown link to `{doc}` form.
7. Normalise smart-quotes.
