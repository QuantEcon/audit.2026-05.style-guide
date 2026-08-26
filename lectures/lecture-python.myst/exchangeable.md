# exchangeable

- **Series:** lecture-python.myst
- **File:** `lectures/exchangeable.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×8; `qe-writing-001` ×2; `qe-writing-003` ×3, +3 more. |
| Math         | 7/10  | `qe-math-010` (proposed) ×2; `qe-math-015` (proposed) ×3. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 424, 425, 429, 712, 713, 714, 719. *Example:* seven functions are bound by assigning a lambda to a name, which PEP8 rules out explicitly in favour of `def` (E731); `def f(w): return p(w, F_a, F_b)` reads the same and gives the function a name in tracebacks. The single-letter names themselves are fine here - `l` for the likelihood ratio $l(w)$ is the mathematical-notation exception the rule allows.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 700. *Example:* bare expectation `E\left[`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 114, 148, 166, 172, 193, 219, 223, 239. *Example:* bold is used for emphasis at least eight times: '**nothing to learn**' at 114 and again at 148, '**either** ... **or**' at 166 and 172, the four bolded verbs in the bullet list at 193-195 ('**knows**', '**doesn't know**', '**acting as if**', '**thinking that**'), '**conditional on nature having selected**' at 219 and 223, and '**not**' at 239. The file uses italic correctly for emphasis elsewhere (51, 58, 175, 299-303, 602) and bold correctly for the terms it defines (83, 89-96, 265, 274, 281, 592), so these are inconsistent with its own practice.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 290. *Example:* H2 Title Case: "Bayes' Law" (Law).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 62. *Lines:* 31, 36, 43, 44, 48, 58, 60, 83, 94, 99, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 446, 479, 534. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 685. *Example:* .set(xlabel='$t$', title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 683, 684, 721. *Example:* plot() without lw=.
- **[qe-math-015 (proposed)]** *(reviewer)* — Lowercase for densities/PMFs, uppercase for CDFs. *Count:* 3. *Lines:* 166, 391, 721. *Example:* line 162 sets up the case convention explicitly - $F$ and $G$ are the cumulative distribution functions, $f$ and $g$ their densities - and the lecture then uses the two cases for the same object. Nature 'selects **either** $f$ **or** $g$' at 166 but draws 'from **either** $F$ **or** $G$' at 172; $\pi$ is defined as $\mathbb{P}\{q = f\}$ at 311 and 322 but described as 'the probability $\pi$ put on distribution $F$' at 391 and 'under true distribution $F$' at 512; and the same experiment is labelled 'F generates' in the figure at 683-684 and 'f generates' at 721.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 640, 659. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 148, 191, 195. *Example:* line 148 repeats line 114 verbatim, bold and all - 'there is **nothing to learn** about the densities of future random variables from past random variables' - and 150 then repeats 112 as well. The bullet list at 191-197 re-lists the three facts that 178-189 have just stated in prose, with no new content. Its third bullet (195-196) is a 51-word item that hedges twice over ('by **acting as if** or **thinking that**').
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 579, 589, 757. *Example:* the three subsections under '## Appendix' (579-757) are the lecture's payoff - the sample-path ensembles, the convergence rates and the ensemble dynamics - so the strongest exhibits sit under a heading that tells the reader they are optional. Line 589-590 asserts that 'outcomes depend on a peculiar property of likelihood ratio processes' and points at `` {doc}`advanced:additive_functionals` `` without saying what the property is, and 610-611 restates the same non-explanation. The third case is computed at 756 and then the lecture ends at 759 with no reading of the figure, unlike the two cases before it, which each get one (736-737, 749).

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 681. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Every probability is written as an event in braces - $\mathbb{P}\{q = f\}$ (311), $\mathbb{P}\{q = f \mid w^t\}$ (322), and the three-way Bayes statement at 348-356 - so the proposed qe-math-014 (proposed) convention holds throughout.
- The three graphs are assembled from one `create_model` (418-432) that returns $f$, $g$ and the two roots of $l(w) = 1$, so 'Another instance' at 571-574 is three lines of reuse rather than three new plotting functions.
- The odds form of Bayes' Law is derived (596-607) and then actually exploited: the simulator computes the whole ensemble with one `np.cumprod` (626) precisely because the belief path is a running product of likelihood ratios.
- The claim that the mixture is not IID is settled by writing the non-factorisation out at 244-255 instead of asserting it, which is what makes the exchangeable-but-not-IID distinction land.
- Every reused equation is labelled and cited by `` {eq} ``: `eq_definetti` (233) at 278, `eq_Bayes102` (341) at 344, 368 and 594, `eq_Bayes103` (379) at 394 and 464, `eq_odds` (597) at 602, and `π` is written in unicode in the code (525, 617, 715) to match the mathematics.

## Recommended actions

1. Convert the eight bold emphases at 114, 148, 166, 172, 193-195, 219, 223 and 239 to italic, keeping bold for the defined terms it already marks correctly.
2. Honour the $F$/$f$ distinction announced at 162: pick the CDF or the density for each statement and stay with it at 166, 172, 311, 388-391, 512 and in the figure labels at 683-684 and 721 (qe-math-015 (proposed), proposed).
3. Cut the redundancy in the setup: delete the bullet list at 191-197, which restates 178-189, and the repetition of 112-114 at 148-150.
4. Brace the two bare expectation operators at 700: `E\left[` becomes `\mathbb{E}\left[` (qe-math-010 (proposed), proposed).
5. Replace the seven lambda assignments at 424, 425, 429, 712, 713, 714 and 719 with `def` statements.
6. Figure hygiene: add mystnb name/caption metadata to the cell at 681 (qe-fig-005), move the embedded `title='convergence'` at 685 into a caption (qe-fig-003), add `lw=2` at 683, 684 and 721 (qe-fig-008), and drop `figsize=` at 446, 479 and 534 (qe-fig-001).
7. Structural and prose tidy-up: promote the '## Appendix' subsections (579-757) into the body or say why they are an appendix, say what the third instance at 756 shows, split the two-sentence paragraphs at 640 and 659 (qe-writing-001), and sweep the 62 double-space runs (31, 36, 43, 44, 48, 58, 60, 83, 94, 99, ...).
