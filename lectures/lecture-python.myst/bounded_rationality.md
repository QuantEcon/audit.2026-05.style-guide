# bounded_rationality

- **Series:** lecture-python.myst
- **File:** `lectures/bounded_rationality.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.6 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×7; `qe-writing-002` ×4; `qe-writing-003` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-004` ×1, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 7. *Lines:* 71, 145, 156, 334, 396, 479, 840. *Example:* the lecture italicises for emphasis about thirty times and correctly bolds about a dozen defined terms (**Individual rationality** 73, **Mutual consistency** 75, **bounded rationality** 101, **best-response map** 230, **relaxation algorithm** 283, **relaxation parameter** 293, **adaptive expectations** 381, **perceived law of motion** 486, **actual law of motion** 498), and then reaches for bold to emphasise as well: **two** (71), **selecting** and **computing** (145), **too many equilibria** (156), **diverges** (334), the whole bolded question at 395-396, **forecasting scheme itself** (479) and **replace the rational agents with adaptive ones** (839-840). None of the seven is a definition, and each has an italic counterpart doing the same job elsewhere in the same file.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 350, 665, 723, 801. *Example:* four code lines exceed 79 characters - 81 at 350, 83 at 665, 82 at 723 and 91 at 801, where the comment `# money demand, with p* = p since prices are constant` pushes the line well past the limit and would read better on its own line above the statement.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 313, 455, 690, 1036. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 317, 323. *Example:* .set_title.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 40, 854, 858, 864. *Example:* the series is previewed twice in near-identical terms 660 lines apart: line 854 ("least squares learning selects the *opposite* equilibrium from the one the rational expectations dynamics converge to, and human experimental subjects side with the adaptive model") restates 179-180; 858-862 restates 186-188 on the exchange rate depending on initial conditions; 864-866 restates 191-192 on the search economy. Separately, lines 40-42 are a 44-word sentence carrying three fields of research, the assumption they share and the kind of setting they were built for.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 34, 59, 101. *Example:* 2 spaces.

### Low severity
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 1. *Lines:* 683. *Example:* caption of 7 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 1035. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 522. *Example:* line 517 claims "The relaxation algorithm carries over unchanged", but `` {eq}`t_relaxation` `` at 519-523 does not parallel `` {eq}`relaxation` ``: it iterates on $H^*_k$, the *actual* law of motion defined at 499-502, and applies $T$ to it, whereas the static version at 287-291 iterates on the *perceived* value $X^*_k$ and applies the best-response map to that. With $T$ defined at 507-510 as the map from perceived to actual, the iteration should read $H_k = H_{k-1} + \lambda(T(H_{k-1}) - H_{k-1})$; as written the starred and unstarred objects have swapped roles between the two displays the text says are the same.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 295. *Example:* line 295 names the cobweb ("With $\lambda = 1$ this is simple iteration on $h$, the classic cobweb") and the figure that follows at 297-332 plots $X^*_k$ against iteration count $k$ instead - two time-series panels. The picture the whole section is about, $h(X)$ against the 45-degree line with $X^*$ at the crossing and the staircase spiralling out of it, is never drawn, even though the section is titled "Rational expectations as a fixed point", $h$ is affine and two lines and a staircase would carry both the fixed point (253) and the divergence (334) in one panel.


## Strengths

- The note at 414-427 disarms the lecture's worst notational hazard before it bites: it says that Sargent uses $\lambda$ for both the smoothing weight and the moving-average coefficient, that this lecture writes the second as $\theta$ to keep $\lambda = 1 - \theta$ visible, that $\lambda$ and $\gamma$ mean different things again in the money model, and that the code therefore names them `λ_m` and `γ_m`.
- Muth's theorem is not asserted but tested: 434-467 simulates the MA(1) process at three values of $\theta$, sweeps 97 smoothing weights, marks $1 - \theta$ with a dashed line on each curve, and the prose at 470-473 checks both the location of the minimum and its value against $\mathbb{V}[\epsilon_t] = 1$.
- The indeterminacy claim is verified rather than trusted: 652-668 prints `max |demand - supply|` for four different bubble constants and 670 reads the result back ("Money demand equals money supply exactly, at every date, for every $c$").
- The exercise 1 solution does something unusual and valuable - it explains the *discrepancy* between the numerical and analytical stability boundaries (919-928) instead of hiding it, deriving the size of the gap from the 400-iteration, $10^{-8}$-tolerance test itself and confirming the prediction in a second table.
- Exercise 3 is designed to break its own earlier result: the two-currency table at 804-808 shows the real allocation invariant to $e$, and the exercise then sets $\mu_1 \neq \mu_2$ to show that this was a knife-edge (1047-1058), separating the nominal indeterminacy that survives from the real invariance that does not.

## Recommended actions

1. Switch the seven bolded emphases at 71, 145, 156, 334, 396, 479 and 840 to italic; the lecture already has a consistent italic-for-emphasis convention and these are the only departures from it.
2. Add the $(X, h(X))$ cobweb diagram the fixed-point section is about, alongside or in place of the iteration-count panels at 297-332.
3. Fix `` {eq}`t_relaxation` `` at 519-523 so the iterate is the perceived law $H$, not the actual law $H^*$ - as written the display contradicts the sentence above it and the static analogue it is said to reproduce.
4. Move the four embedded matplotlib titles into figure captions - `axes[0].set_title("undamped")` and `axes[1].set_title("damped")` at 317 and 323 (qe-fig-003, 2 occurrences).
5. Cut "Where this leaves us" (828-871) back to the argument that is new - the three responses to indeterminacy and why adaptive agents can select where rational expectations cannot (833-849); the results survey at 851-871 repeats the series map at 175-194.
6. Drop the four `figsize=` overrides at 313, 455, 690 and 1036 (qe-fig-001, 4 occurrences), add `mystnb: figure: caption/name` metadata to the figure at 1035 (qe-fig-005), and shorten the seven-word caption at 683-688 (qe-fig-004).
7. Sweep the small items: collapse the double spaces at 34, 59 and 101 (qe-writing-008, 3 occurrences), wrap the four over-length code lines at 350, 665, 723 and 801, and add the missing sentence-ending period at line 493.
