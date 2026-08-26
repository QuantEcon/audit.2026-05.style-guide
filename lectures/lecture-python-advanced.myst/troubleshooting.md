# troubleshooting

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, figures, links  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8.5/10 | `qe-writing-001` ×1; `qe-writing-008` ×1. |
| Math         | N/A   | no mathematical content. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 32. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 65. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 52. *Example:* {image} without :name:.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 65. *Example:* 2 spaces.


## Strengths

- The page fixes its own scope in one sentence at 23 and then states the assumption the whole lecture series rests on as a two-item list at 27-30, so a reader can tell within four lines whether their problem is one this page can solve.
- The remedies are ordered cheapest-first and in the order they are actually likely to be the cause - update Anaconda (34-37), reinstall it (39), update the external libraries (41-46), then the two escapes at 48-56 - rather than as an undifferentiated list.
- Every remedy is executable rather than described: 36 links the update article, 45-46 gives the upgrade command in both forms a reader might need (`pip install --upgrade quantecon` at the shell and the `!`-prefixed form inside a notebook), and 50-54 shows a screenshot of the Launch Notebook icon instead of describing where on the page it sits.
- The reporting section asks for what actually makes a report usable - 65-66 names the two things ("where the problem is and as much detail about your local set up as you can provide") - and gives two channels with concrete targets, the issue tracker at 63 and a mailto at 68, so the reader is never left to guess where feedback goes.
- 58-59 frames the report as something the authors want rather than an imposition ("We like getting feedback on the lectures so please don't hesitate to get in touch"), which is the right note on a page reached by someone whose code has just failed.

## Recommended actions

1. Fix the issue-tracker URL at 63: it points at `https://github.com/QuantEcon/lecture-python-advanced/issues`, but this series lives in `QuantEcon/lecture-python-advanced.myst` - the one link on the page whose entire job is to receive bug reports is aimed at a different repository name.
2. Check the Anaconda update article at 36 (`https://www.anaconda.com/keeping-anaconda-date/`) - the slug reads as though "up-to" has been dropped, and a dead link here removes the page's first remedy.
3. Put the two commands at 45-46 in inline code - they are currently plain narrative text ("use pip install --upgrade quantecon on the command line"), so the `--upgrade` flag and the leading `!` render without any typographic signal that they are to be typed verbatim.
4. Replace the raw URL at 32 with a `{doc}` cross-reference to the getting-started lecture (qe-link-002).
5. Split the two-sentence paragraph at 65-66 and remove the double space after "possible." (qe-writing-001, qe-writing-008).
6. Give the screenshot at 52 an `:alt:` describing the Launch Notebook icon and convert it to a `{figure}` with a `:name:` so it can be referenced (qe-fig-005).
