# kesten_processes

- **Series:** lecture-python.myst
- **File:** `lectures/kesten_processes.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-004` ×4; `qe-writing-003` ×3; `qe-writing-002` ×3, +2 more. |
| Math         | 5/10  | `qe-math-010` (proposed) ×21; `qe-math-009` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×4; `qe-fig-008` ×3. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 21. *Lines:* 132, 190, 227, 253, 255, 264, 285, 289, 291, 293, …. *Example:* missing braces: `\mathbb P`.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 104, 331, 448, 726. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 112, 349, 469. *Example:* plot() without lw=.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 227, 368, 449. *Example:* four letters do double duty. Line 227 is the clearest case: `\int \mathbb P\{ R_{t+1} s w + y_{t+1} \leq y\} F^*(dw)` uses $s$ for the savings fraction (148-157), $y_{t+1}$ for labor income (150) and $y$ for the argument of the distribution function (219) - three meanings for two letters inside one integral. Then 368 makes $s_t$ firm size while $s$ is still the savings fraction at 264, and 612 adds the threshold $\bar s$. And 449-451 introduces $\alpha_0$, $\alpha_1$ as GARCH parameters while $\alpha$ is the Pareto tail index at 286-305, alongside $\sigma_t$ as volatility (129-144) against $\sigma$, $\sigma_a$, $\sigma_b$, $\sigma_e$ as lognormal scale parameters (333, 534, 650-654).
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 317, 357, 497. *Example:* 313-327 uses six one-sentence paragraphs to make two points: 317 and 321 both restate the role of $\mathbb E \ln a_t < 0$ ("has a large amount of probability mass below 1", then "gives us existence of the stationary condition"), and 319 and 323 both restate the role of $\mathbb E a_t^\alpha = 1$ - and 321 misnames its own subject, since what the condition delivers is a stationary *distribution*, not a stationary condition. 497-499 is broken and unpunctuated: "Gibrat's law is generally found to be a reasonable approximation for large firms than for small firms" is missing its comparative and its full stop, and it garbles what 389-390 said correctly. 357 packs a cross-reference, two size measures and two citations into 33 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 329, 408, 421. *Example:* 329 says "the following simulation, which generates 10 paths when $a_t$ and $b_t$ are lognormal" - but the lecture's Kesten process is $X_{t+1} = a_{t+1}X_t + \eta_{t+1}$ and $b_t$ has not been introduced; it first appears at 398, seventy lines later, as the additive term in the firm-size law, and the code at 339 uses `b` for what the surrounding text calls $\eta$. 408 opens "### Heavy tails" inside the firm-dynamics section although "## Heavy tails" is already an H2 at 266, so the table of contents lists the same title twice. And 421-422 promises "We also try to illustrate why the Pareto tail finding is significant for quantitative analysis" - none of the four exercises does that; kp_ex1 simulates GARCH, kp_ex2 compares growth laws, kp_ex3 solves for $\alpha$ and kp_ex4 produces the rank-size plot.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 281, 309, 359, 414. *Example:* mid-sentence 'Theorem'.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 307. *Example:* "### Intuition" (307-327) exists to explain why the two Kesten-Goldie conditions pull in opposite directions - $\mathbb E \ln a_t < 0$ putting mass below one, $\mathbb E a_t^\alpha = 1$ requiring mass at or above one - and delivers that explanation in six prose sentences with no picture, in a lecture that is otherwise willing to plot. Both halves are one-liners to draw: the lognormal density of $a_t$ with a vertical rule at $a = 1$ showing the mass on each side, and the curve $\alpha \mapsto \mathbb E a_t^\alpha = \exp(\alpha\mu + \alpha^2\sigma^2/2)$ crossing one at $\alpha = -2\mu/\sigma^2$, which is exactly the root that exercise kp_ex3 derives at 571-574. The second plot would also show at a glance why the tail gets heavier as $\mu \to 0$.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 494. *Example:* 2 spaces.


## Strengths

- Every probability in the lecture puts its event in braces - `\mathbb P\{a_{t+1} x + \eta_{t+1} \leq y\}` (190), `\mathbb P\{R_{t+1} s w + y_{t+1} \leq y\}` (227), `\mathbb P\{a_t x + \eta_t = x\}` (285), `\mathbb P\{X^* > x\}` (302) - so proposed qe-math-014 (proposed) holds without exception.
- $F^*$ is uppercase for the distribution function throughout and is used as a measure where integration is meant, `F^*(dx)` at 190 and `F^*(dw)` at 227, rather than switching to a density partway - proposed qe-math-015 (proposed) satisfied, and 224 explains the measure notation in words ("the fraction of households with wealth in interval $dw$ is $F^*(dw)$") before using it.
- The lecture shows the phenomenon in real data before modelling it: the Nasdaq returns plot at 104-117 is anchored with `(ndcode)=` and exercise kp_ex1 sends the reader back to it by `{ref}` at 436 to compare the simulated GARCH path against the real one.
- Empirical claims carry their own citations one by one - 386 and 387 attach a separate reference to each of the two findings that contradict Gibrat's law, 390 cites the case in which it survives, and 589 names the paper behind the entry-exit extension - rather than a single bulk citation at the end of a paragraph.
- "IID" is written in the correct form all nine times it appears (82, 92, 93, 132, 142, 162, 376, 401, 610), and bold is reserved for the three terms the lecture actually coins (**Kesten process** 74, **stationary** 171, **nonarithmetic** 277) with the only italic being the Latin *ceteris paribus* at 215.
- All eight labelled equations are cited where they are used, several of them repeatedly - `firm_dynam` at 404, 412, 418, 481, 500, 503, 584 and 618, `wealth_dynam` at 162, 208 and 263, `kp_stat_cond` at 283 - so the argument refers back precisely instead of restating.
- The kp_ex4 solution is a textbook JAX composition: a pure `update` for one firm (691-697), `lax.scan` over the 500 periods and `vmap` over a million firms (703-714), with `T` and `M` marked `static_argnames` so the whole cross-section compiles once.

## Recommended actions

1. Add braces to the 21 blackboard operators - `\mathbb P` -> `\mathbb{P}`, `\mathbb E` -> `\mathbb{E}`, `\mathbb V` -> `\mathbb{V}` at 132, 190, 227, 253, 255, 264, 285, 289, 291, 293 and 11 more - by far the largest fix in this lecture (qe-math-010 (proposed), proposed).
2. Fix the axis label at 471: `garch_ts` returns the returns series `r` (462), not the variance, so `ylabel="$\\sigma_t^2$"` mislabels the plot the exercise asks the reader to compare against the Nasdaq returns at 104 - it should read $r_t$, and the string wants to be a raw `r'...'`.
3. Introduce $b_t$ where it is first used at 329, or write $\eta_t$ there and in the code at 339 to match `` {eq}`kesproc` ``; and rename the "### Heavy tails" H3 at 408 so it does not repeat the H2 at 266.
4. Add the two intuition figures described above to section 307-327, and `mystnb: figure: caption`/`name` metadata to the four un-named figures (104, 331, 448, 726) - the rank-size plot at 726 is the lecture's punchline and 737 refers to it only as "the plot".
5. Rename one member of each colliding pair: the savings fraction $s$ (148-157, 264) against firm size $s_t$ (368-398), and the GARCH parameters $\alpha_0$, $\alpha_1$ (129) against the tail index $\alpha$ (286-305); also give the CDF argument at 219-227 a letter other than $y$, which is labor income in the same display.
6. Compress 313-327 to two sentences, one per condition, dropping the duplicates at 321 and 323 and correcting "stationary condition" to "stationary distribution"; and repair the sentence at 497-499.
7. Lower-case "Theorem" mid-sentence at 281, 309, 359 and 414 (qe-writing-004), add `lw=2` at 112, 349 and 469, close the double space at 494, move the JAX imports from 675-678 up to the opening import cell at 59, and replace the deprecated `jax.random.PRNGKey` at 705 with `jax.random.key`.
