# intro

- **Series:** lecture-dp
- **File:** `lectures/intro.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
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

- A seven-line landing page that does exactly one job: name the series, say what it covers, and emit `{tableofcontents}` - there is no structure here for a rule to catch.
- The H1 'Dynamic Programming with Python' is correctly title-cased for a lecture title (qe-writing-006) and is the only heading in the file.
- The single sentence at line 14 sits alone between blank lines, so qe-writing-001 holds by construction, and it is 15 words - well inside the qe-writing-002 guideline.

## Recommended actions

1. Lowercase 'Economists' at line 14 - it is a common noun in mid-sentence position, and it is the only mark on the file (qe-writing-004; the scanner's curated noun list does not carry this word, see scanner_doubts).
2. Expand the orientation to two or three sentences: what background the series assumes (the `lecture-python-intro` and `lecture-python-programming` series), what the reader will be able to do at the end, and that roughly half the series is shared with `lecture-python.myst` - a single sentence is thin for a 52-lecture landing page.
3. Add a `{doc}` link to `status` from this page, so the execution table is reachable from the entry point rather than only from the sidebar.
4. Otherwise leave the file alone - it needs no style remediation and is a useful reference for what a clean MyST landing page looks like.
