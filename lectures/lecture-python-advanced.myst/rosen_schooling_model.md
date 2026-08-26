# rosen_schooling_model

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/rosen_schooling_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-001` ×2; `qe-writing-003` ×3; `qe-writing-005` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×4; `qe-fig-005` ×4; `qe-fig-008` ×14, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 161, 244, 248, 294, 295, 318, 319, 320. *Example:* comma spacing is applied inconsistently within the same file: 161 writes `['a22', 'c2','ub','ud']` with no space after two of three commas while 162 and 163 space theirs; 294 and 295 write `ax1.plot(econ1.c_irf,label=...)` with no space before the keyword argument, where 299, 300, 312-314 and 434-435 do have it; and 318-320 index `econ1.h_irf[:,0]` where 299, 300, 435 and 530 write `[:, 0]`. 244 writes `np.zeros((1, k+1))` where the identical expression at 192, 256, 404 and 498 is `k + 1`. 248 names a variable `Pref3` in CapWords among `pref1`, `pref2` and `pref4`, and 249 then passes `Pref3` where its three siblings pass lowercase names.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 14. *Lines:* 294, 295, 299, 300, 312, 313, 314, 318, 319, 320, …. *Example:* plot() without lw=.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 293, 311, 425, 519. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 297, 302, 316, 322. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 292, 310, 390, 485. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 383, 447. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 145, 26, 271. *Example:* the algebra and the code disagree about $C_2$. The display at 143-146 sets $C_2 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \\ 0 & 1\end{bmatrix}$, but every code cell writes `c2 = np.array([[0, 0], [10, 0], [0, 10]])` (214, 416, 510) - a factor of ten on the shock loadings, so a reader who checks the impulse responses against the stated matrix gets answers ten times too small. Second, the lecture has no overview: 26-27 opens with "This lecture is yet another part of a suite of lectures that use the quantecon DLE class" and then goes straight to equations at 49, so nothing states the question the Ryoo-Rosen model answers - and the mechanism that in fact explains every figure, the $(\beta\rho_d)^k$ discount on a wage premium that has to survive $k$ years of schooling, is developed only at 366-386, inside a dropdown solution most readers will not open. Third, 271-290 gives six paragraphs interpreting "the first figure" before the cell that draws it at 292-303, so the reader is told what to see well before there is anything to see.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 292, 310. *Example:* none of the eight panels in the four figures (292-303, 310-323, 425-441, 519-536) carries an axis label. The horizontal axis is time in periods and the vertical is the impulse response, and neither is stated anywhere - which matters more here than usual because the lecture's whole subject is a $k$-period delay. The second figure (310-323) compares $k=4$, $k=7$ and $k=10$ precisely to show that delay, and nothing marks $t=4$, $t=7$ or $t=10$ on the axis, so the one feature the figure exists to display has to be counted off by eye against an unlabelled tick sequence. A labelled time axis plus a vertical rule at each $k$ would make the point the prose asserts at 326-332 directly visible.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 29, 136, 332. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 27. *Example:* {cite} in narrative flow: '{cite}`'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 343. *Example:* 343 sets **persistence of the demand shock** in bold as emphasis ("Now investigate how the **persistence of the demand shock** matters") where the rule asks for italic - and the same exercise uses italic correctly for emphasis three times, at 353 (*why*), 377 (*survives the $k$ periods of schooling*) and 385 (*no*), so the bold is the odd one out rather than a consistent house style.


## Strengths

- The exercise solution at 360-386 supplies the analytical spine the body lacks: it isolates $(\beta\rho_d)^k$ as "the decisive term" (376-377), explains it in one sentence - what matters is how much of the wage premium survives the $k$ periods of schooling - and then takes the limit $\rho_d \to 0$ to show the response vanishes entirely, which is the sharpest possible statement of the time-to-build mechanism.
- That analysis is then checked against numbers rather than left as intuition: 447-452 computes $(\beta \times 0.2)^4 \approx 0.0013$ against $(\beta \times 0.95)^4 \approx 0.67$ and reports the ratio as "about two tenths of one percent", which is exactly the gap the reader sees in the plotted curves.
- The three `namedtuple` definitions at 161-163 carry the same names as the three subsections that specify them - Preferences (93), Technology (119), Information (134) - so the matrices written out at 96-107, 124-130 and 139-155 map onto the constructor arguments at 218-222 by name rather than by position.
- The comment at 185 preserves a fact that would otherwise be unrecoverable: `# Use of ε_1 is a trick to acquire detectability, see HS2013 p. 228 footnote 4` - naming the page and the footnote for a $10^{-7}$ that would otherwise look like a typo.
- The economics of the first figure is built one step per paragraph and each step follows from the one before (275-290): the shock raises wages, wages draw entrants, entrants raise $N_t$, a larger $\alpha_d$ makes that rise depress wages more, and entry therefore turns negative.
- The second exercise (461-472) varies $\alpha_s$, the one parameter the body never touches, and is structured as prediction then test - the intuition is stated at 478-483 before any code, and 539-541 reports whether it held.
- Both solutions rebuild the model from scratch (391-421, 486-515) rather than inheriting the names left over from the body cells, where `k`, `λ_1`, `δ_h` and `θ_h` have been mutated three times over by 261 - so a reader who runs only a solution still gets the intended parameterisation.

## Recommended actions

1. Reconcile $C_2$ between the algebra and the code: 143-146 shows unit loadings, all three code cells (214, 416, 510) use 10 - one of them has to move, and until it does no impulse response in the lecture can be checked against the stated matrices.
2. Label the time axis on all eight panels and mark $t=k$ with a vertical rule on the $k$-comparison figure at 310-323, so the delay the lecture is about is visible in the figure rather than only asserted at 326-332.
3. Give the lecture an Overview that says what the Ryoo-Rosen model explains and promote the $(\beta\rho_d)^k$ argument from the dropdown at 366-386 into the body, where it can do the work of interpreting all four figures.
4. Fix the three notation slips: `k` outside math mode at 55 ("It takes k periods of schooling"), the missing space in `\psi_1i_t = g_t` at 129, and the bare `\mathbb{E}` at 75 against `\mathbb{E}_t` at 363 for the same conditional expectation.
5. Clean the PEP8 items: comma spacing at 161, 294, 295 and 318-320, `k + 1` at 244, and rename `Pref3` to `pref3` at 248-249.
6. Italicise the emphasis at 343 to match 353, 377 and 385.
7. Sweep the figures: `lw=2` on the fourteen `plot` calls, move the eight `set_title` calls (297, 302, 316, 322, 438, 440, 533, 535) into `mystnb: figure: caption/name` metadata on the four figure cells (292, 310, 390, 485), and drop the four `figsize=(12, 4)` overrides.
8. Split the two-sentence paragraphs at 383 and 447 and remove the double spaces at 29, 136 and 332.
