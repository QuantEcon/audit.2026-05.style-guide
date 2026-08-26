# intro

- **Series:** lecture-python.myst
- **File:** `lectures/intro.md`
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

- A five-line landing page that does one job - name the series and emit `{tableofcontents}` - so there is no surface for a style rule to catch.
- The H1 "Intermediate Quantitative Economics with Python" is correctly Title Case for a lecture title and is the only heading in the file.
- The single description sentence sits alone between blank lines, satisfying qe-writing-001 by construction, and carries no repeated spaces.

## Recommended actions

1. Expand line 14 into two or three sentences of orientation: who the series is for, what `lecture-python-intro` background it assumes, and how it differs from `lecture-python-advanced.myst` - one sentence is thin for the landing page of a 200-lecture series.
2. If that orientation is added, keep each sentence in its own paragraph block so the page stays qe-writing-001 clean.
3. Otherwise leave the file untouched; it needs no style remediation and is a useful reference for what a clean MyST page looks like.
