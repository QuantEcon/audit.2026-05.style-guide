# troubleshooting

- **Series:** lecture-python-intro
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
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

- The page states its own scope in one sentence and never exceeds it: line 23, "This page is for readers experiencing errors when running the code from the lectures", and the two sections that follow are exactly the two things such a reader can do - fix the environment (25-59) or report the problem (61-68).
- 27-30 makes the lectures' maintained assumption explicit as a numbered pair - code should execute in a Jupyter notebook on a machine with the latest Anaconda - which is what turns a support page into a diagnostic: a reader who fails either condition knows immediately which one.
- The remedies are ordered by cost to the reader: update Anaconda (34-37), reinstall it (39), update the external libraries (41-46), fall back to a remote machine (50-54), and only then report an issue (56). Nothing is asked of the reader before the cheaper fix has been offered.
- 50-54 pairs the instruction with the screenshot it refers to: the sentence names the "Launch Notebook icon available for each lecture" and the `{image}` immediately below shows what that icon looks like, which is the one place on this page where a figure is doing real work.
- 58-59 and 68 give two different routes for feedback - the issue tracker for reproducible problems, a mailto address for everything else - and say that feedback is wanted, which is the right note to end a support page on.
- There is no maths, no code cell, no admonition and no citation on the page, and it does not manufacture any: the drafted report correctly scores four categories `N/A`, and there is nothing here for the eight judgment rules to bite on.

## Recommended actions

1. Point the issue tracker at the right repository: line 63 links to `https://github.com/QuantEcon/lecture-python/issues`, which is the intermediate series, while this page ships with `lecture-python-intro` - so a reader following the instruction files an intro-series bug in the wrong tracker. It should be `https://github.com/QuantEcon/lecture-python-intro/issues`.
2. Replace the raw cross-series URL at 32 with a `{doc}` reference - `` {doc}`programming:getting_started` `` - which is the one mechanical Links finding on the page (qe-link-002).
3. Put the two install commands in inline code at 45-46: `conda install -y quantecon` and `!conda install -y quantecon` currently sit in plain prose, so the leading `!` that distinguishes the notebook form from the shell form reads as punctuation.
4. Split the two-sentence paragraph at 65-66 into two blocks (qe-writing-001), which also removes the double space after "possible." (qe-writing-008), and add the missing full stop at the end of 68.
5. Convert the `{image}` at 52-54 to a `{figure}` with a `:name:` and a short caption such as "the Launch Notebook icon" (qe-fig-005), and give the path a leading slash - `/_static/lecture_specific/troubleshooting/launch.png` - to match the fifteen other image and figure directives in this series; only this file and `long_run_growth.md:34` use the relative form.
6. Leave the rest as it is. Two comparable support pages in other series returned no judgment findings, and this one should too: the page is 69 lines, one sentence per paragraph almost throughout, with no term to define and no result to visualise.
