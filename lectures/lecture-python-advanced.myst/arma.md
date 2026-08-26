# arma

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/arma.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-005` ×8; `qe-writing-003` ×3; `qe-writing-002` ×4, +3 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×3. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×4; `qe-fig-003` ×1; `qe-fig-008` ×6, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 236, 474, 523, 563, 757. *Example:* figsize=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 243, 528, 535, 568, 575, 746. *Example:* plot() without lw=.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 118, 119, 133. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 107, 116, 121, 131, 138, 287, 321, 341. *Example:* the two uses are inverted lecture-wide. Every term is defined in italic where the rule asks for bold: *stationary* (107), *covariance stationary* (116), *autocovariance function* (121), *white noise process* (131), *general linear processes* (143), *linear filter* (157), *autoregressive moving average process* (273), *lag operator* (285), *impulse response function* (331), *spectral density* (341), *real part* / *imaginary part* (351), *modulus* (353), *imaginary unit* (359), *inverse Fourier transform* (600), *Fourier coefficients* (642). The three uses of bold, meanwhile, are emphasis - **building blocks** (138) and **always assume** (321) - or a block label, `**Def.**` at 287, which wants a `{prf:definition}` directive.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 105, 159, 291, 292, 313, 369, 380, 389, 402, 415, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 559, 715, 720, 721. *Example:* line 720 writes `xlim=(-0.5)`, which is a parenthesised scalar rather than the two-element tuple `xlim` expects, and writes `min(yi)-0.1` / `max(yi)+0.1` unspaced; 721's continuation is indented to column 18 against an opening paren at column 12, where the equivalent calls at 729-730 and 738-739 are correctly aligned; the five top-level `def`s at 715, 724, 733, 742 and 750 are separated by a single blank line where PEP8 asks for two; and 559 mixes conventions inside one expression, `np.cos(np.pi * k/3)`, spacing the multiplication but not the division.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 747. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 234, 468, 515, 555. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 50, 874. *Example:* raw link to python-intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 415. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 105, 699, 770, 869. *Example:* four sentences are broken rather than merely long: 105 ends "allowing us to learn from as data arrive", with the object of "learn from" missing; 770 reads "let's make sure things look right when we for the pure white noise model"; 780 has "which is at it should be"; and 869-872 splits one conditional across a paragraph break with a full stop in the middle - "If the user decides to change the value of either `theta` or `phi` ex-post by assignments such as ... ." and then a new paragraph beginning "then `ma_poly` and `ar_poly` should update automatically". Line 699 is separately a 40-word sentence carrying an em-dash aside and three links.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 169, 573, 867. *Example:* line 161 derives the autocovariance of a general linear process ("With some manipulations, it is possible to confirm that ... is `` {eq}`ma_inf_ac` ``") and then 169 says the same result follows "by the Cauchy-Schwartz inequality" - Cauchy-Schwarz gives the finiteness of the sum, not the formula, so the second justification both repeats and misattributes the first; the second three-panel cell (555-588) is a copy of the first (515-548) with `np.cos(np.pi * k)` changed to `np.cos(np.pi * k/3)`, and the copy carries the stale comment "# Cycles at frequency π" at 573 for a figure about $\pi/3$; and the Explanation section switches API names midway - 831, 843-844 and 846 correctly say `ϕ`, `θ`, `σ`, while 867 and 869-870 talk about `phi` and `theta`, which are not what `qe.ARMA` is called with at 775.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 345. *Example:* the "Complex numbers" section (345-375) is the one part of this figure-rich lecture with nothing to look at, and it is the most visual material in it: real and imaginary parts as coordinates in $\mathbb R^2$ (351), the modulus as a Euclidean norm (353), and the polar form $re^{i\omega} = r(\cos\omega + i\sin\omega)$ (369-375). One Argand-plane diagram would carry all four definitions, and it is exactly the picture a reader coming to spectral analysis needs before meeting $e^{-i\omega k}$ at 385.


## Strengths

- The hardest intuition in the lecture - why the spectral density is large at $\omega = \pi$ for $\phi = -0.8$ - is built as three stacked panels showing $\gamma(k)$, $\cos(\pi k)$ and their product (515-548), and then repeated for $\omega = \pi/3$ (555-588) so the reader sees the matched and the unmatched case side by side.
- The lecture is honest about which parts are optional and says where to jump: 347 offers to "skip to the next section", and 624 states that the Hilbert-space section is for readers who want more insight and that "none of this material is necessary to progress to computation".
- The plotting machinery is sanity-checked on white noise before it is trusted (770-786): the spectrum should be flat at $10^0$, the variance should equal $1 = \frac{1}{2\pi}\int_{-\pi}^{\pi} 1\, d\omega$, and the text says so and then checks the picture against it.
- All four Ljungqvist-Sargent models (791-825) are pushed through the same `quad_plot` helper, so the four quartets of impulse response, spectral density, autocovariance and sample path are directly comparable rather than each drawn its own way.
- The frequency-domain and time-domain views are tied together in both directions - the forward transform at 385, the inverse at 607 (`ift`), and then 878-913 shows how `np.fft.ifft` actually recovers $\gamma(k)$ from $f$, so the theory and the implementation meet.

## Recommended actions

1. Factor the two duplicated three-panel cells (515-548 and 555-588) into one function of $\omega$; they differ only in the cosine argument, and the copy has already gone stale - the comment at 573 still says "Cycles at frequency π" and 566 reverts to a spelled-out `phi`.
2. Bold the defined terms and reserve italic for emphasis: every definition listed above is currently italic, while **building blocks** (138) and **always assume** (321) are bold; and replace `**Def.**` at 287 with a `{prf:definition}` directive.
3. Add `mystnb: figure: caption/name` metadata to the four figure cells (234, 468, 515, 555), drop the five `figsize=(10, ...)` overrides (236, 474, 523, 563, 757), set `lw=2` on the six plot calls (243, 528, 535, 568, 575, 746), and move the embedded title at 747 into the caption.
4. Add an Argand-plane figure to the "Complex numbers" section (345), and fix the slip at 375 - $\omega = \arctan(y/z)$ should be $\arctan(y/x)$, as the same line's $\tan(\omega) = y/x$ confirms.
5. Repair the broken sentences: 105 ("learn from as data arrive"), 770 ("when we for the pure white noise model"), 780 ("which is at it should be"), 415 (two sentences in one paragraph), and the split conditional at 869-872.
6. Brace the three expectation operators - `\mathbb E X_t` (118), `\mathbb E (X_t - \mu)...` (119) and `\mathbb E \epsilon_t` (133) should be `\mathbb{E}` (qe-math-010 (proposed), proposed) - and fix the Cauchy-Schwarz attribution at 169.
7. Cite or drop the four dead equation labels `ar1_rep` (211), `ar_acov` (226), `arma_sd_cos` (394) and `arma_fc` (631); convert the raw URLs at 50 and 874 to `{doc}` references (qe-link-002 ×2); align the prose at 867-870 with the `ϕ`/`θ` names the code actually uses; and strip the 19 runs of double spaces.
