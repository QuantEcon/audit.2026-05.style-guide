# hoist_failure

- **Series:** lecture-python.myst
- **File:** `lectures/hoist_failure.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-002` ×3; `qe-writing-006` ×1; `qe-writing-008` ×25, +2 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×2; `qe-math-014` (proposed) ×2; `qe-math-009` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-004` ×2; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 168, 174. *Example:* non-blackboard `\Pr`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 356. *Example:* H3 Title Case: 'The Fast Fourier Transform' (Fast, Transform).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 25. *Lines:* 41, 381, 489, 544, 545, 549, 552, 554, 560, 567, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 285, 616, 777. *Example:* line 284-285 wraps the density with a backslash continuation and then over-indents the second line (E127) where parentheses would do; line 616 leaves one space before the inline comment `# Component type 7 (appears 8 times)` where PEP8 asks two (E261); line 777 under-indents the continuation of the `results.append([...])` call (E128). Trailing whitespace at 607 and 712.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 325, 430, 449, 684. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 235, 250. *Example:* caption of 7 words.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 383, 498. *Example:* the Fourier transform is defined at 363 as $x(\omega_j)$ - the same letter as the sequence, with the argument carrying the meaning - and then written as $F(\omega)$, $G(\omega)$, $H(\omega)$ at 383-385 for the transforms of $\{f_k\}$ and $\{g_k\}$, which is a different convention two paragraphs later. Similarly the probability operator is `\Pr` at 168 and 174 and plain `P` from 498 onward.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 2. *Lines:* 168, 174. *Example:* $f_j = \Pr(X = j)$ (168) and $g_j = \Pr(Y = j)$ (174) put an event - a condition on a random variable - inside parentheses, where the proposed convention asks for braces: $\mathbb{P}\{X = j\}$. The set-valued arguments later in the lecture, $P(A \cup B)$ and $P(A \cap B)$ at 498-510, are correctly parenthesised, so the two cases are already distinguished in the file - just the wrong way round for the event.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 352, 571, 591. *Example:* lines 591-595 repeat 583-587 across the '### Model specification' heading almost word for word: '$n = 14$', 'estimates the annual failure rate of a critical hoist at a nuclear waste facility', 'a regulatory agency wants/requires the system to be designed so that the top event failure rate is small with high probability'. Line 571 ('The analyst assumes that the random variables $P(A_i)$ are statistically mutually independent') repeats 565, in a passage where nine consecutive sentences open with 'The analyst'. Line 352 repeats what 194-196 established, that `fftconvolve` is faster and will be used throughout.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 797. *Example:* exercise `hoist_ex2` asks the reader to judge the rare event approximation by comparing the expected system failure rate with the sum of component expected values - and its own solution says at 832 that 'the expected value of the sum equals the sum of the expected values (by linearity of expectation), so these should match closely regardless of the rare event approximation'. The exercise as posed cannot answer the question it asks, and the solution says so rather than fixing the question.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 481. *Example:* '## Fault tree analysis' promises at 485 to 'describe the model that connects constituent events to the *top* end whose failure rate we seek to quantify' - that model is a tree, and no tree is drawn. The lecture reproduces the source paper's Figure 5 (the CDF) and Table 11, but not its fault tree, so the fourteen components, the seven identically distributed pairs (599-601) and the top event $F$ exist only as a list of parameter tuples at 609-617. Eight figures elsewhere in the lecture show the author is willing to draw.


## Strengths

- All eight figure cells carry mystnb `caption` and `name` metadata (206-212, 235-241, 250-256, 314-320, 420-426, 442-448, 672-678), so every exhibit is addressable.
- Every approximation is checked against something independent: the discretised density against a 25,000-draw histogram (314-333), the discretised mean against $e^{\mu+\sigma^2/2}$ (335-343), and both convolutions against their sample histograms and theoretical means (420-478).
- The final answer is validated against the source: the CDF is presented as a counterpart to Figure 5 of `` {cite:t}`Greenfield_Sargent_1993` `` (670) and the quantiles against its Table 11 (699-716), with an explicit list of why small discrepancies remain (718-721).
- Both timing comparisons use the `quantecon.Timer` context manager (400-409, 662-667, 767) rather than `time.time()` - the convention `qe-code-004` asks for, and rare in this corpus.
- The `{note}` at 75-80 pre-empts the standard confusion between a lognormal's parameters and its moments, and the `{warning}` at 117-119 states the single fact that motivates the whole lecture: the product of lognormals is lognormal, the sum is not.
- Densities and mass functions are lowercase throughout - $f$, $g$, $h$, $f_j$, $g_j$, $h_n$ (125-177) - with the cumulative object kept in prose and code as `cdf`, so the proposed qe-math-015 (proposed) case convention holds.

## Recommended actions

1. Draw the fault tree: the fourteen components, the seven identically distributed pairs and the top event $F$ are currently only a list of tuples, and the tree is what the section at 481-540 is about.
2. Delete the duplicated opening at 591-595, which repeats 583-587 verbatim across the section heading, and the restatements at 571 and 352.
3. Rewrite exercise `hoist_ex2` so the question is answerable - for example compare $\sum_i P(A_i)$ with $1 - \prod_i (1 - P(A_i))$, or compare quantiles rather than means - since the current comparison holds by linearity whatever the approximation error is.
4. Stop rebinding `μ` and `σ` in the loops at 652 and 757: they overwrite the lognormal parameters set at 214 and used at 269 and 340, so after the fault-tree cell the names silently mean component type 6's parameters.
5. Write probabilities as `\mathbb{P}` with braces for events: `\Pr(X = j)` at 168 and 174 become `\mathbb{P}\{X = j\}` (qe-math-010 (proposed), proposed; qe-math-014 (proposed), proposed), and the plain `P(\cdot)` from 498 onward becomes `\mathbb{P}(\cdot)`.
6. Sentence-case '### The Fast Fourier Transform' at 356 (qe-writing-006) and settle the capitalisation of 'fast Fourier transform', which is lowercase at 387 and Title Case at 356 and 416.
7. Housekeeping: drop `figsize=` at 325, 430, 449 and 684 (qe-fig-001), shorten the captions at 235 and 250 (qe-fig-004), fix the PEP8 items above, replace the placeholder-free f-strings at 466 and 476, reconcile the body's `p = 15` (645) with the exercise solution's recommendation of `p = 13` (788), and sweep the 25 double-space runs.
