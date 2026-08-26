# troubleshooting

- **Series:** lecture-python-programming
- **File:** `lectures/troubleshooting.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, figures, links  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-001` ×1; `qe-writing-003` ×1, +1 more. |
| Math         | N/A   | no mathematical content. |
| Code         | N/A   | no executable code cells. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 25, 61. *Example:* H2 Title Case: 'Fixing Your Local Environment' (Your, Local, Environment).

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 65. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 52. *Example:* {image} without :name:.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 56. *Example:* the 'report an issue' branch is opened inside '## Fixing Your Local Environment' (56-59: 'Second, you can report an issue, so we can try to fix your local set up') and then opened again from scratch as its own section at 61-63 ('One way to give feedback is to raise an issue through our issue tracker'). The reader is given the same instruction twice, and the first telling carries no pointer to the section that actually explains it.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 65. *Example:* 2 spaces.


## Strengths

- The remedies are ordered by effort - update Anaconda (34-39), upgrade the external libraries (41-46), then run on a remote machine (50-54) - so a reader stops as soon as their problem is solved.
- The Launch Notebook instruction is paired with a screenshot of the button itself (50-54) rather than described in words.
- The Anaconda prerequisite is a `{doc}` cross-reference to `getting_started` (32) rather than a bare URL.
- The page ends with two concrete routes to a human - the issue tracker (63) and a mailto address (68) - instead of a vague invitation to get in touch.

## Recommended actions

1. Lower-case the two Title Case H2s: 'Fixing your local environment' (25) and 'Reporting an issue' (61) - qe-writing-006, 2 occurrences.
2. Move 56-59 under '## Reporting an Issue', or replace them with a `{ref}` to it, so the reporting instructions appear once.
3. Wrap the two commands at 45-46 in inline code - `conda upgrade quantecon` and `!conda upgrade quantecon` are the only copy-and-paste text on the page and are currently plain prose.
4. Add a `:name:` and a caption to the `{image}` at 52 so it can be cross-referenced (qe-fig-005, 1 occurrence).
5. Split the two-sentence paragraph at 65 and close the double space in 'possible.  Tell' (qe-writing-001 and qe-writing-008, 1 occurrence each).
6. Consider making the rhetorical question at 32 ('You have installed Anaconda, haven't you...?') a plain statement - a reader who arrives on this page is already stuck.
