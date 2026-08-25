# debugging

- **Series:** lecture-python-programming
- **File:** `lectures/debugging.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-006` ×6; `qe-writing-005` ×3; `qe-writing-002` ×2, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-008` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 76, 117, 196, 217, 234. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 65, 183, 247, 260, 390, 402. *Example:* H3 Title Case: 'The `debug` Magic' (Magic).

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 27. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 157, 291. *Example:* 157-181 pastes the entire `ipdb> h` command table - 25 lines reproducing every pdb command - when the sentence at 154-155 plus the link is what the reader needs, and the lecture only ever uses `n`, `q` and `h c`; and 291 ("In this section, we'll discuss different types of errors in Python and techniques to handle potential errors in our programs") restates the Overview's own sentence at 44.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 209, 297, 354. *Example:* all three of the lecture's defined terms avoid bold: a "break point" is introduced in scare quotes (209), the two-way split "syntax errors and exceptions" is set in plain text (297), and "In Python, these errors are called *exceptions*" (354) puts the definition in italic - the exact inversion the rule names.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 209. *Example:* 2 spaces.


## Strengths

- The bug is introduced deliberately and then debugged live: `plt.subplots(2, 1)` at 74 raises a real `AttributeError`, so the traceback the reader sees is the traceback the text discusses at 88-90.
- The lecture teaches both failure modes and gives each its own tool - an exception you can see (69-80, handled with `%debug`) and a silent wrong answer you cannot (`np.logspace` for `np.linspace` at 195, handled with `breakpoint()`).
- Every error-raising cell is tagged `raises-exception` (71, 98, 112, 191, 306, 317, 326, 335, 344, 380), so the book builds while still showing the reader the real traceback.
- The `try`/`except` progression is stepwise and ends with the right warning: one exception type (408-415), then two (437-446), then a bare `except` followed by "In general it's better to be specific" (487).
- The Kernighan epigraph (26-30) earns its place - the claim that clever code is code you cannot debug is the lecture's actual argument, not decoration.

## Recommended actions

1. Sentence-case the six H3 headings (65, 183, 247, 260, 390, 402).
2. Cut the verbatim `ipdb> h` dump at 157-181 down to the three commands the lecture uses, and keep the documentation link.
3. Show the reader the correct plot: `plot_log` appears broken (74), wrong-but-silent (195) and never right, so the section that sets out "to plot the `log` function over the interval [1, 2]" (82) never shows that plot.
4. Bold the defined terms - "break point" (209) and "syntax errors and exceptions" (297) - and change *exceptions* (354) from italic to bold.
5. Add `lw=2` to the five plot calls (76, 117, 196, 217, 234).
6. Attach the "be specific" advice at 487 to the bare `except:` cell at 464-471 as a `{warning}`, rather than leaving it as the last line of the section.
7. Delete the double space at 209 and the trailing space at 64; fix the parenthetical at 86, which has no closing full stop.
