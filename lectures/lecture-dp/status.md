# status

- **Series:** lecture-dp
- **File:** `lectures/status.md`
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

- Every environment fact on the page is produced by a live cell rather than typed in - `{nb-exec-table}` (16-17), `!python --version` (25-27), `!conda list` (31-33) - so the page cannot go stale.
- The `!conda list` cell carries `:tags: [hide-output]` (32), keeping a several-hundred-line dump out of the rendered page while leaving it in the notebook.
- The machine-details region carries an explicit `(status:machine-details)=` anchor (19), so other pages can link straight at it.

## Recommended actions

1. Give the machine-details region a heading - `(status:machine-details)=` at 19 anchors a bare paragraph, so a `{ref}` to it lands on text with no visible target.
2. Tag the cells `ipython3` rather than `ipython` (25, 31) to match the `python3` kernel declared at 9.
3. Reconcile the five series' copies of this page: `lecture-python-programming` and `lecture-python.myst` carry a 47-line version with GPU and JAX-backend probes, while this file, `lecture-python-intro` and `lecture-dp` carry a 33-line one - the page is hand-maintained in five places and has already diverged.
4. Drop the trailing space at the end of line 21. This copy is the 33-line variant plus a newline at end of file, so it differs from `lecture-python-intro` and `lecture-python-advanced.myst` in exactly that one character - the other two already lack the newline, so fixing it in all three is the smaller change.
