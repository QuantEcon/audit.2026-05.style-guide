# functions

- **Series:** lecture-python-programming
- **File:** `lectures/functions.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×13; `qe-writing-005` ×7; `qe-writing-002` ×3, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-008` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 5. *Lines:* 178, 293, 316, 348, 377. *Example:* plot() without lw=.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 7. *Lines:* 137, 183, 185, 263, 322, 384, 450. *Example:* the lecture bolds exactly one term (`**built-in**`, 57) and italicises every other definition: the function body (137), a keyword argument (183), positional arguments (185), anonymous (263), bound (322), callable (384), and frame and stack together at 450 - seven definitions in italic, which the rule reserves for emphasis.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 13. *Lines:* 47, 55, 80, 94, 100, 168, 213, 227, 266, 279, …. *Example:* H2 Title Case: 'Function Basics' (Basics).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 112, 605, 685. *Example:* trailing whitespace after `f(1)` at 112 (W291); whitespace immediately inside the parentheses at 605, `count = count + ( 1 if U < 0.5 else 0 )` (E201/E202), where the equivalent line at 585 is written correctly; and `recursion_factorial` indented three spaces instead of four at 685-688 (E111).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 283, 307, 336, 368. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 28, 38, 404. *Example:* 28 is a truncated sentence - "Functions are an extremely useful construct provided by almost all programming" is missing its noun; 38 reads "learn to do is build our own user-defined functions"; and 404 is a 41-word sentence that restates what 386-388 has just said about binding names to callables.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 224. *Example:* "The Flexibility of Python Functions" (213-225) lists four capabilities and promises "We will give examples of how straightforward it is to pass a function to a function in the following sections" (224), but functions defined inside other functions (220) and functions returning functions (222) are never exemplified anywhere in the lecture.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 386. *Example:* 2 spaces.


## Strengths

- The `lambda` motivation is genuine rather than illustrative: `quad(lambda x: x**3, 0, 2)` (260) needs a function object where naming one would be pure overhead, so the reader sees why anonymous functions exist.
- `generate_data` is refactored in four steps - inline loop (283-295), function (307-318), conditional argument (336-350), callable argument (368-379) - and each step is motivated by a stated limitation of the one before ("Our function `generate_data()` is rather limited", 329).
- The recursion section is honest about itself: it flags its own example as contrived and says the iterative version would normally be preferred (456), instead of selling recursion.
- Rebinding `max` to `m` (396-399) is a two-line demonstration that functions are objects - the cheapest possible illustration of the claim at 221.
- Five exercises use gated `exercise-start`/`solution-start` with dropdown solutions, and two of them build on named earlier targets (`factorial_exercise` at 461, referenced at 672).

## Recommended actions

1. Sentence-case the 13 headings (47, 55, 80, 94, 100, 168, 213, 227, 266, 279 ...) - the largest single fix and what floors Writing at 5.
2. Move the seven italicised definitions (137, 183, 185, 263, 322, 384, 450) to bold; `**built-in**` at 57 is the one that already gets it right.
3. Fix the two broken sentences: 28 ("provided by almost all programming" - the noun is missing) and 38 ("learn to do is build our own user-defined functions").
4. Add mystnb caption/name to the four code-cell figures (283, 307, 336, 368) and `lw=2` to the five plot calls (178, 293, 316, 348, 377).
5. Either give examples of the two claims at 220 and 222 or drop the promise at 224.
6. Cut 404 to its point, delete the double space at 386 (qe-writing-008), and add the missing full stop at 85.
7. Run the code cells through pycodestyle for the three-space indent at 685-688, the bracket spacing at 605 and the trailing whitespace at 112.
