# multi_hyper

- **Series:** lecture-python.myst
- **File:** `lectures/multi_hyper.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 6.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-002` ×5; `qe-writing-001` ×2; `qe-writing-005` ×3, +4 more. |
| Math         | 6.5/10 | `qe-math-010` (proposed) ×4; `qe-math-009` ×4; `qe-math-014` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 271, 324, 390, 411, 414. *Example:* 411 and 412 are 110 and 113 characters; 414 and 427 write `'$k_{' +str(i+1) +'}$'`, putting the space on the wrong side of `+` in four places; 324 writes `[5, 5, 4 ,1]` with the space before the comma rather than after; 271 and 331 leave one space before an inline comment (`k_arr = [2, 2, 2] # array of number of observed successes`, `n = 6 # number of draws`) where PEP8 asks two; and `count` at 390-398 is decorated `@jit` and loops with `prange` but is never given `parallel=True`, so `prange` silently degrades to `range`, while the function reads the module-level `sample` at 392 even though `vec1` and `vec2` are passed in, and its local `size` shadows the global `size` set at 348. Line 411 also bins with `np.arange(0, n, 1)`, which stops at $n-1$ and so drops the largest realised value from the marginal histograms.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 4. *Lines:* 140, 147, 153, 157. *Example:* non-blackboard `\Pr`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 29, 59, 71, 104, 366. *Example:* the opening sentence says the administrator wanted "to access the fairness of a procedure" (29) where the word is *assess* - the lecture's thesis sentence contains a typo that reverses its meaning. Line 71 is 44 words and contains "independent of continent of the author's continent of residence". Lines 100-105 run to 60 words with a dangling dash pair carrying a stray comma before the closing dash ("a $4 \times 1$ vector of integers recording the numbers of blue, green, yellow, and black balls, respectively, - contains evidence") and end on "which here means *color blind* and truly are random draws", which does not agree. Line 366 is a single 51-word sentence that names the multivariate hypergeometric distribution three times. And 59 restates 55 ("Then $n$ balls are drawn randomly") as "Thus, the selection procedure is supposed randomly to draw $n$ balls from the urn".
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 13. *Lines:* 29, 34, 57, 59, 61, 77, 104, 128, 276, 366, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 414, 427. *Example:* .set_title.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 97, 133, 147, 259. *Example:* the moment formulas at 147, 153 and 157 are pasted MediaWiki source and still carry its markup: `{\displaystyle \operatorname {E} (X_{i})=n{\frac {K_{i}}{N}}}`, with a `\displaystyle` wrapper that does nothing inside `$$`, a space between `\operatorname` and its argument, and every fraction wrapped in redundant braces; 141 has the same style. Line 259 is worse: `{{{5 \choose 2}{10 \choose 2}{15 \choose 2}} \over {30 \choose 6}}=0.079575596816976` uses the plain-TeX `\over` instead of `\frac`, triple-nests braces, and quotes the probability to fifteen significant digits. Across those four displays the same operators appear four ways - `\Pr` (140), `\operatorname{E}`/`\operatorname{Var}`/`\operatorname{Cov}` (147, 153, 157), a bare `P(` (259) - and the binomial coefficient three ways: `{m \choose q}` (133), `\binom{K_i}{k_i}` (141), `{5 \choose 2}` (259). The two matrices at 74 and 97 use the plain-TeX row separator `\cr` rather than `\\`, and 97 writes a four-entry column as $k_1, k_2, \vdots, k_4$, so the vertical ellipsis stands for the single omitted entry $k_3$.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 254, 440. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 133, 320, 331, 465. *Example:* line 133 defines the notation the whole lecture rests on incorrectly: "${m \choose q} = \frac{m!}{(m-q)!}$" is the permutation count, not the binomial coefficient - the $q!$ is missing - and `` {eq} ``-less display at 141 then uses $\binom{K_i}{k_i}$ as though 133 had defined it. The section titled "Back to the administrator's problem" (300) silently changes the sample size: 90-92 fix the administrator's problem at $n = 15$, the `pmf` calls at 316 and 324 all pass outcome vectors summing to 15, and then 328 says "when $n=6$" and 331 sets `n = 6`, so the moments (332), the ten-million-draw simulation (349), the normal-approximation figure (401-429) and both normality tests (452, 461) are all computed for a six-ball draw the administrator never makes. Line 320 says the outcomes are stacked in "a 3-dimensional arrays `k_arr`" where 276 correctly called the two-row version 2-dimensional - the array is 2-dimensional with three rows. And 465 ends the lecture on "the normal approximation is imperfect", never returning to the question posed at 77-105: the pmf of the realized $(10,1,4,0)$ is printed at 317 and nothing says whether that number is evidence against colour blindness.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 268. *Example:* mid-sentence 'Class'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 77, 104, 131. *Example:* **color blind** is defined in bold at 57, then bolded twice more in the single sentence at 77-78 as emphasis, and then set in *italic* at 104 - three formats for one term inside fifty lines. Lines 131, 137, 144 and 150 use bold one-word paragraphs (`**Notation**`, `**Probability mass function**`, `**Mean**`, `**Variances and covariances**`) as section headings, where `####` headings would put them in the contents tree; 133 then bolds **binomial coefficients** correctly as a definition in the very next line, so the two uses of bold sit next to each other.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 4. *Lines:* 84, 316, 403, 449. *Example:* the lecture's own question never gets a picture. The realized outcome $(10, 1, 4, 0)$ is evaluated at 316-317 as a bare probability, and the ten-million-draw sample at 349 contains exactly what is needed to place it - a histogram of the blue-ball count with the observed value marked would answer 77-105 in one panel - but no such figure is drawn. The urn itself (238 balls in four colours, 15 drawn) is described across five one-line paragraphs at 84-92 where a single bar chart would carry it. The one figure that does exist is a 4x4 grid at 403 with `figsize=(14, 14)`: the twelve off-diagonal panels are six pairs plotted twice with the axes swapped, so half the figure is redundant and the prose at 440 has to tell the reader which axis is which, and none of the sixteen panels has an axis label. And 449 uses a bare markdown blockquote (`> \`normaltest\` returns an array of p-values ...`) where a `{note}` belongs - the lecture has no admonition anywhere.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 403. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 401. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 1. *Lines:* 259. *Example:* line 140 gets it right - `\Pr \{X_{i}=k_{i} \ \forall i\}` writes an event as a logical condition inside braces - and line 259 writes the same kind of event with parentheses instead, `P(2{\text{ black}},2{\text{ white}},2{\text{ red}})`, so the lecture's two probability statements disagree with each other about the convention as well as about the operator.


## Strengths

- The balls-and-colours metaphor is introduced with an explicit reason at 42-43 - to forget details that are none of the reader's business and to protect anonymity - and then held consistently: every subsequent quantity is given both readings ($K_i$ balls/proposals at 45, $c$ colours/continents at 47, drawn balls as funded proposals at 61).
- The real problem is instantiated with real numbers before any code: 84-92 gives $N = 238$, the four colour counts $(157, 11, 46, 24)$, and $n = 15$, so the reader knows the scale of the administrator's question before meeting the `Urn` class.
- `Urn` is exactly three methods matching the three displays it implements - `pmf` (179-199) is the mass function at 140-141, `moments` (201-221) is the mean at 147 and the variance-covariance at 153-157 assembled as `np.diag(p) - np.outer(p, p)`, `simulate` (223-244) draws from it - and each carries a numpy-style docstring naming its parameters.
- `pmf` accepts either one outcome or a stack of them via `np.atleast_2d` (191) and infers $n$ from the row sum (192), so the same call works for `[2, 2, 2]` at 272 and for the three-row array at 324 without a separate interface.
- `simulate` takes an explicit `seed` and constructs its own `Generator(PCG64(seed))` (241) rather than touching global numpy state, so a reader can reproduce a sample exactly.
- The normal approximation is not merely displayed but tested: 452-462 runs D'Agostino-Pearson on both the hypergeometric sample and a normal sample of the same mean and covariance, and reports that the first rejects and the second does not - which is what makes the visual comparison at 435 into a claim rather than an impression.
- The moment-matching check at 345-362 draws ten million samples and compares `np.mean(sample, 0)` and `np.cov(sample.T)` against the closed-form $\mu$ and $\Sigma$ computed at 332, so the class is validated against its own algebra before it is used.

## Recommended actions

1. Fix the binomial coefficient at 133 - it is missing the $q!$ in the denominator, and it is the notation the mass function at 141 relies on.
2. Decide whether the administrator's problem is $n = 15$ or $n = 6$ and make one choice hold from 300 to 465: 90-92, 316 and 324 use 15, while 328-331 and everything downstream (349, 401-429, 452, 461) uses 6.
3. Close the loop the lecture opens: use the sample at 349 to place the realized outcome $(10, 1, 4, 0)$ in the distribution and say whether it is evidence against the colour-blind hypothesis of 77-78.
4. Retype the pasted Wikipedia displays at 141, 147, 153, 157 and 259 in plain LaTeX - drop `{\displaystyle ...}`, use `\mathbb{E}`, `\mathbb{V}` and `\mathbb{P}` with braces per qe-math-010 (proposed), use `\frac` rather than `\over`, use `\\` rather than `\cr` at 74 and 97, and round the 15-digit constant at 259.
5. Make the probability notation consistent: 140 uses `\Pr\{...\}` for an event and 259 uses `P(...)` for the same kind of event (qe-math-014 (proposed)); pick `\mathbb{P}\{...\}` and apply it in both places.
6. Turn the four bold heading lines at 131, 137, 144 and 150 into real headings, settle **color blind** on one format (bold at 57, bold again at 77-78, italic at 104), lowercase "Class" at 268, and split the two-sentence blocks at 254 and 440.
7. Clean the figure and code: give the 4x4 grid axis labels and drop the redundant transposed half, move the two `set_title` calls at 414 and 427 into `mystnb` figure metadata with a `name:` (qe-fig-003, qe-fig-005), reconsider `figsize=(14, 14)` at 403, add `parallel=True` to the `@jit` at 390 or drop `prange`, fix the `np.arange(0, n, 1)` binning at 411-412 that omits the top value, wrap lines 411-412 under 80 characters, and remove the thirteen double spaces (29, 34, 57, 59, 61, 77, 104, 128, 276, 366, 440) and the comment typo "distrbution" at 424.
