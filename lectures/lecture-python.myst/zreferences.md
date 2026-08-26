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

- The entire page is one `{bibliography}` directive against `_static/quant-econ.bib` (15-16), so the reference list cannot drift out of step with the `{cite}` roles that populate it - there is no hand-maintained list to fall behind.
- The `(references)=` anchor sits directly above the H1 (12-13), so cross-series links target the page rather than a heading inside it.

## Recommended actions

1. Consider dropping the `jupytext` and `kernelspec` front matter (1-10): the page has no code cells, so the declared Python 3 kernel is never used and the file is still converted to an executable notebook at build time.
