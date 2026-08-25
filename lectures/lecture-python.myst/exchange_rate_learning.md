# exchange_rate_learning

- **Series:** lecture-python.myst
- **File:** `lectures/exchange_rate_learning.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-005` ×9; `qe-writing-002` ×8; `qe-writing-003` ×1, +1 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×5; `qe-fig-004` ×2; `qe-fig-001` ×4, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 5. *Lines:* 310, 318, 324, 591, 595. *Example:* .set_title.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 8. *Lines:* 37, 79, 476, 601, 637, 651, 667, 818. *Example:* one-sentence-per-paragraph discipline is perfect here, which leaves the length inside the sentence as the only place complexity can go, and eight sentences run 40-54 words with two or three clauses hung off em-dashes and colons: 49 words at 37-40, 41 at 79-81, 54 at 476-479 (three GA operators plus a fourth defined mid-sentence), 41 at 601-603, 41 at 637-639, 42 at 651-653, 48 at 667-670 and 45 at 818-820.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 9. *Lines:* 47, 57, 62, 243, 627, 635, 665, 700, 751. *Example:* bold is doing emphasis work throughout: the two signposts '**First**' (47) and '**Second**' (62), and then '**determinate**' (57), '**flat in $\lambda$**' (243), '**converges**' (627), '**does not converge**' (635), '**asymmetrically**' (665), '**not**' (700) and '**raises**' (751). The file already uses italic correctly for exactly this job (38, 52, 150, 335, 371, 380, 402, 602, 616, 653, 722), and bold correctly for the terms it defines (79, 251, 388, 438, 442, 450, 476-478, 559), so the nine bolded emphases are inconsistent with the file's own practice.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 306, 361, 534, 588. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 351, 562. *Example:* caption of 7 words.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 429, 615. *Example:* the lecture's two empirical claims are the only ones with no exhibit. Lines 429-432 describe Arifovic's laboratory exchange rate in words - 'fluctuated persistently, roughly within a band from $0.5$ to $2$', 'the amplitude grew across sessions' - where every model claim in the file gets a figure or a printed diagnostic; and 615-617 compares the simulated spectrum with the spectra of real hard-currency pairs 'except *without* the dip at zero frequency' with nothing to look at, although the simulated spectrum is plotted immediately above at 588-598.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 362. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 203. *Example:* $R$ is introduced at 203 as the running estimate of the Hessian, and sixteen lines later at 219-220 $R_1$ and $R_2$ are the gross currency returns - two unrelated objects on one letter, in adjacent displays, and the collision carries into the code where `R` is the list of Hessian estimates (265, 282-283) while `R1, R2` are returns (279-280). Naming the second-moment matrix anything else would remove the clash at no cost.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 166. *Example:* '### The indeterminacy, recalled' is a mathematical subsection that ends, at 166-168, with a paragraph about code organisation - carrying parameters in a container 'rather than leaving them lying about as globals'. It belongs with the cell it justifies, not inside the derivation of the indeterminacy.


## Strengths

- All four figure cells carry mystnb `caption` and `name` metadata (297-302, 352-357, 525-530, 563-568), so every figure in the lecture is addressable - unusual in this corpus and worth keeping.
- Every claim in the narrative is followed by a printed check rather than left as an assertion: the two limits at 339-342, the arbitrage rest point at 391-400, the early-versus-late volatility windows at 548-554, and the zero-frequency dip tested as a boolean at 608-613.
- The two economies' parameters are kept apart as named `Params` instances - Sargent's `kw` at 183, Arifovic's `arifovic` at 455 - with the rational expectations saving rate derived as a property (177-180) rather than restated as a literal.
- The three exercises each attack a distinct claim the lecture made (whole-initial-condition dependence, the election operator's destabilising role, the near-unit-root coefficient), all gated with exercise-start/exercise-end and dropdown solutions.
- {eq}`xr_utility` and {eq}`xr_prices` are labelled once and then cited by reference at every reuse (142, 200, 425, 446, 449, 764) - the lecture never says 'the equation above'.

## Recommended actions

1. Convert the nine bold emphases at 47, 57, 62, 243, 627, 635, 665, 700 and 751 to italic, leaving bold to the definitions it already marks well - this is the one systemic style deviation in an otherwise clean file.
2. Fix the printing bug at 341: the loop iterates over both experiments but reads saving from `s1[-1][0]` in both rows, so experiment 2's reported $s$ is experiment 1's.
3. Figure hygiene, the largest mechanical block: move the five embedded titles at 310, 318, 324, 591 and 595 into the cells' captions (qe-fig-003), shorten the two captions at 351 and 562 (qe-fig-004), drop `figsize=` at 306, 361, 534 and 588 (qe-fig-001), and set `lw=2` on the plot at 362 (qe-fig-008).
4. Rename the Hessian estimate so that $R$ and $R_1, R_2$ no longer share a letter, in both the math (203-217) and the code (265, 282-283).
5. Break the eight 40-plus-word sentences listed above into the one-idea-per-sentence form the rest of the file already uses.
6. Give '## Evidence from the laboratory' an exhibit - the experimental path if it can be reproduced from {cite:t}`Arifovic1996`, otherwise a note admonition stating the band and the trend - and attribute the block quote at 409-410 with a {cite} and a page, since it opens with 'Put differently' and currently stands without a source.
7. Rename the `lam` variables to `λ` for consistency with `κ` (257), `μ`, `φ` (802) and `λ0_grid` (358), move the code-organisation paragraph at 166-168 next to its cell, and replace the placeholder-free f-strings at 186, 397 and 398 with plain strings.
