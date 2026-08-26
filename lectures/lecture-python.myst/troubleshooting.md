# troubleshooting

- **Series:** lecture-python.myst
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, figures, links  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-001` ×1; `qe-writing-008` ×1. |
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
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 29, 65. *Example:* H2 Title Case: 'Fixing Your Local Environment' (Your, Local, Environment).

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 36. *Example:* raw link to python-programming.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 69. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 56. *Example:* {image} without :name:.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 69. *Example:* 2 spaces.


## Strengths

- The page states its own scope in its first sentence (27, "This page is for readers experiencing errors when running the code from the lectures") and then states the assumption that makes troubleshooting possible at all as a two-item numbered list (31-34) - executed in a Jupyter notebook, on a machine with the latest Anaconda - so within four lines a reader can tell whether their situation is one this page addresses.
- The remedies are ordered by how likely each is to work, and the most likely one is named as such rather than left for the reader to infer: 38 says "the most common source of problems for our readers is that their Anaconda distribution is not up to date", then 40-41 links the article on updating, 43 gives the blunt fallback ("simply remove Anaconda and reinstall"), 45 moves on to the external libraries, 54 leaves the local machine entirely, and only 60 reaches reporting a bug.
- Every step is an action the reader can execute rather than a description of one, and the one distinction a beginner actually gets wrong is spelled out: 49-50 gives both forms of the upgrade command and says where each belongs - `pip install --upgrade quantecon` on the command line, `!pip install --upgrade quantecon` inside a notebook.
- The single image on the page (56) is the Launch Notebook icon, placed immediately after the sentence that tells the reader to click it (54) - a screenshot doing the one job prose cannot do, which is show what a button looks like.
- Both escalation paths point at something live rather than at an instruction to get in touch: 67 links the issue tracker of this series' own repository, and 72 is a working `mailto:` to contact@quantecon.org.
- The request for a bug report is specific enough to act on - 69-70 names the two things a maintainer needs ("Tell us where the problem is and as much detail about your local set up as you can provide") - rather than asking the reader to "provide details".
- The prerequisite is linked at the point where a reader might be missing it (36) instead of assumed, and the register stays plain throughout: ten of the twelve content paragraphs are a single sentence, and the page carries no jargon, no math and no code cell it would have to keep working.

## Recommended actions

1. Lower-case the two H2 headings to sentence case per `qe-writing-006`: "Fixing your local environment" (29) and "Reporting an issue" (65).
2. Replace the raw URL at 36 with a `{doc}` link to the programming series' `getting_started` page, per `qe-link-002` - this is the page most likely to be reached by a reader whose environment is broken, so the cross-series link is worth having resolved rather than hard-coded.
3. Give the `{image}` at 56 a `:name:` and `:alt:` - it is a screenshot of a button the preceding sentence tells the reader to click, so a reader using a screen reader currently gets nothing where the instruction is.
4. Split the two sentences at 69-70 into separate paragraphs and remove the double space after "possible.", closing the one `qe-writing-001` and one `qe-writing-008` finding.
