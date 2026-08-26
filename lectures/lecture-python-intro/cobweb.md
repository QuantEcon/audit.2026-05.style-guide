# cobweb

- **Series:** lecture-python-intro
- **File:** `lectures/cobweb.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-005` ×3; `qe-writing-002` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-002` ×4; `qe-code-001` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×2; `qe-fig-003` ×1; `qe-fig-008` ×7, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 81, 144, 145, 286, 296, 452, 576. *Example:* plot() without lw=.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 4. *Lines:* 562, 567, 569, 592. *Example:* spelled-out `alpha`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 443, 567. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 453. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 75, 139. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 17, 195, 396. *Example:* the three definitions that organize the lecture are all in plain text: the model itself at line 17 ('The cobweb model is a model of prices and quantities...'), naive expectations at line 195 ('which refers to the case where producers expect...'), and adaptive expectations at lines 396-400. The only bold in the file, at line 529, is a pseudo-heading for the third scheme inside an exercise, and the italics at lines 22 and 102 are correctly doing emphasis.

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 349. *Example:* line 349 writes the keyword default as `y_b= 12`, with a space after the equals sign and none before; the parameter beside it on the same line (`y_a=3`) uses the correct form.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 1. *Lines:* 102. *Example:* line 102 is a 32-word sentence carrying three clauses - why supply is dated at t, what it depends on, and the notation for it - where the surrounding prose keeps to one idea per sentence.


## Strengths

- The 45-degree diagram helper at lines 240-313 draws the cobweb itself - vertical and horizontal arrows tracing p_0 to p_1 to p_2, with the x-ticks relabelled $p_0$, $p_1$, ... - so the reader follows the dynamics by eye instead of being told a cycle exists.
- The soybean narrative at lines 26-51 establishes the whole mechanism (planting lag, supply flood, price drop, exit, price climb) in nine short sentences before a single symbol is introduced.
- The history section replicates Figure 2 of the paper it cites - actual 1924-1959 hog prices at lines 74-87 - so the cyclical pattern the model predicts is shown in real data before the model is built.
- All three expectation schemes run through the same `Market` class and the same time-series plotting helper, which makes the comparison across naive, adaptive and backward-looking average expectations genuinely like-for-like.
- Both exercises use the gated `{exercise-start}`/`{exercise-end}` and `{solution-start}`/`{solution-end}` form with `:class: dropdown`, so solutions are collapsed by default.

## Recommended actions

1. Add mystnb figure metadata (name and caption) to the seven figure cells at lines 75, 139, 239, 346, 441, 488 and 561 - the 45-degree diagram in particular deserves a name so the text at lines 324-342 can cross-reference it (qe-fig-005).
2. Set `lw=2` on the six plot calls that genuinely lack it: lines 81, 144, 145, 286, 296 and 576. Lines 271, 362 and 504 already set `lw=2` on a continuation line and need no change (see scanner doubt).
3. Bold the three definitions at lines 17, 195 and 396, so the model and its two expectation schemes are marked the way the third one is at line 529.
4. Move the two author-position citations at lines 67 and 69 into the parenthetical form the style guide asks for (qe-ref-001).
5. Drop the `figsize=` overrides at lines 443 and 567 (qe-fig-001) and move the embedded title at line 453 into a caption (qe-fig-003).
6. Split line 102 into two sentences, and fix `y_b= 12` at line 349 and the singular 'naive expectation' at line 465.
