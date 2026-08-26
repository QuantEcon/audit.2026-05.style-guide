# zreferences

- **Series:** lecture-python.myst
- **File:** `lectures/zreferences.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, links  *(JAX out of scope)*
- **Overall score:** 10.0 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 10/10 | no mechanical violations detected. |
| Math         | N/A   | no mathematical content. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
_None found._

### Low severity
_None found._


## Strengths

- **Not reviewable against the eight judgment rules, and the empty `judgment` list above is that finding, not an omission.** `zreferences.md` is 17 lines, of which 10 are jupytext front matter: the whole page is an anchor, an H1 and a single `{bibliography}` directive pointing at `_static/quant-econ.bib` (12-16). It contains no prose sentence, no code cell, no mathematics, no figure and no emphasis of any kind, so there is literally nothing for `qe-writing-002`, `qe-writing-003`, `qe-writing-005`, `qe-writing-007`, `qe-math-009`, `qe-code-001`, `qe-math-014` (proposed) or `qe-math-015` (proposed) to read - the rendered reference list is generated from the `{cite}` roles in the other 130 lectures. The drafted score of 10.0 is therefore correct but vacuous: it records that nothing violated a rule because nothing was there to violate one. The single action below is the only thing worth changing on the page.
- The entire page is one `{bibliography}` directive against `_static/quant-econ.bib` (15-16), so the reference list cannot drift out of step with the `{cite}` roles that populate it - there is no hand-maintained list to fall behind.
- The `(references)=` anchor sits directly above the H1 (12-13), so cross-series links target the page rather than a heading inside it.

## Recommended actions

1. Consider dropping the `jupytext` and `kernelspec` front matter (1-10): the page has no code cells, so the declared Python 3 kernel is never used and the file is still converted to an executable notebook at build time.
