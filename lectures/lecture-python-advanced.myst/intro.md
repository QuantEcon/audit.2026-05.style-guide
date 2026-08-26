# intro

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/intro.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
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

- A 17-line landing page that does one job - name the series and emit `{tableofcontents}` - and adds nothing a style rule could catch.
- The H1 "Advanced Quantitative Economics with Python" is correctly title-cased for a lecture title (qe-writing-006), and it is the only heading in the file.
- The single description sentence sits alone in its own paragraph, so qe-writing-001 holds by construction.

## Recommended actions

1. Add the missing newline at end of file - line 17 (```` ``` ````) ends without one, which trips POSIX line-oriented tooling and shows as `\ No newline at end of file` in every diff.
2. Consider two or three more sentences of orientation before `{tableofcontents}`: what background the series assumes, and how it relates to `lecture-python.myst` and `lecture-python-programming`; one sentence is thin for the front door of a 60-lecture series.
3. Otherwise leave this file alone - it needs no style remediation and is a useful reference for what a clean MyST page looks like.
