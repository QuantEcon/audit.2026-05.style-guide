# hs_invertibility_example

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/hs_invertibility_example.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×2; `qe-writing-003` ×4; `qe-writing-002` ×3, +2 more. |
| Math         | 7/10  | `qe-math-003` ×8; `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×6; `qe-fig-005` ×3; `qe-fig-008` ×12, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 160, 174, 267, 305, 306. *Example:* the rule permits capitals for matrices and the setup cell declines them in exactly the places where the correspondence with the display would help: 174-179 names $A_{22}$, $C_2$, $U_b$, $U_d$ as `a22`, `c2`, `ub`, `ud` while the neighbouring objects keep their symbols (`ϕ_c`, `ϕ_g`, `ϕ_i`, `δ_k`, `θ_k`, `π_h`). Worse, `γ` at 160 is the technology *matrix* $\Gamma$ assembled from the scalar `γ_1` of 159, which is the $\gamma$ of equation 91 - so the two names differ by a subscript while the objects differ in rank. 305 is a no-op self-assignment, `ma_coefs = ma_coefs`. 306 sets `jj = 50` five lines after 301 has already passed `50` to `stationary_coefficients(50, 'ma')`, so the loop bound and the number of coefficients requested have to be kept equal by hand. And 267 writes `econ1.d_irf[:,0].reshape(40,1)` with no space after either comma where the identical line at 275 has both spaces, and both hardcode the `ts_length=40` set at 263 (as 295 hardcodes the state dimension in `reshape(1, 8)`).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 6. *Lines:* 269, 277, 328, 333, 370, 375. *Example:* .set_title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 12. *Lines:* 266, 267, 274, 275, 325, 326, 330, 331, 368, 369, …. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 8. *Lines:* 110, 115, 124, 132, 202, 205, 224, 227. *Example:* array used as matrix.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 9. *Lines:* 29, 50, 53, 62, 65, 72, 235, 253. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 265, 324, 367. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 260, 294, 349. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 77, 195, 212. *Example:* the conditioning information set is attached with a bare `|` placed outside every delimiter: 77 is $-\frac{1}{2}\mathbb{E}\sum_{t=0}^\infty \beta^t[(c_t - b_t)^2 + l_t^2]|J_0$ and 195 is $\mathbb{E}\sum_{j=0}^\infty \beta^j (c_{t+j} - d_{t+j})|J_t = \beta^{-1}k_{t-1}$, so in both the bar sits after the closing bracket of the summand and reads as applying to the whole expression rather than as conditioning inside the expectation; $\mathbb{E}_0$ and $\mathbb{E}_t$ - the form the sibling DLE lectures use - is both simpler and unambiguous. Separately, 212 and 241 write the zero row vector as `[0\,\,\,0]`, three stacked thin spaces faking a matrix, where $\sigma_2(\beta) = 0$ (or a `bmatrix`) says it.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 29, 235, 257. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 56, 64, 337. *Example:* 56-59 is a 44-word single sentence that has to carry the lecture's central definition: "the invertibility problem indicates a situation in which histories of the shocks in an econometrician's autoregressive or Wold moving average representation span a smaller information space than do the shocks that are seen by the agents inside the econometrician's model". 64-65 drops its noun - "A shock-invertibility that is technically close to the one studied here is discussed by ..." - where 67 gets the same construction right ("A distinct shock-invertibility issue"). And 337-341 and 343-347 each break one sentence across a paragraph and a bullet, leaving the paragraph without terminal punctuation and starting the bullet in lower case ("... in the econometrician's Wold representation" / "- this is the object that would be recovered from a high order vector autoregression").
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 72, 175, 180, 370. *Example:* 72 says the endowment process is "the sum of two orthogonal autoregressive processes", but 155-156 states the opposite about the second one - "$d_{1t}$ is a first-order AR process, while $d_{2t}$ is a third-order pure moving average process" - and 152 confirms it, $d_{2t} = 4w_{2t} + 0.8(4w_{2t-1}) + 0.6(4w_{2t-2}) + 0.4(4w_{2t-3})$, an MA(3) with no lagged $d$; 138-139 gets it right by saying only "two orthogonal processes", so 72 is the sentence to fix. Second, the third figure's titles at 370 and 375 are the strings 'Response to $w_{1t}$' and 'Response to $w_{2t}$', character-for-character the titles already used at 269 and 277 for the *first* figure, even though 379-380 says the third one shows something else entirely (the responses of $u_t$ to $w_t$, not of $c_t$ and $c_t - d_t$) - two of the lecture's three figures are labelled identically for different content. Third, the $6 \times 6$ information matrix displayed at 110-113 is realised in code only by the fancy-indexed assignment at 176, whose comment is `# Chase's great trick`, so the one line that has to be checked against the display gives the reader nothing to check with. And 180 sets `x0 = np.array([[5], [150], [1], [0], [0], [0], [0], [0]])` with no word anywhere about what the eight entries are - $h_{-1} = 5$ and $k_{-1} = 150$ in particular, the latter being the household's initial asset position, which the level of the deficit path in every figure depends on.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 191, 285. *Example:* the terms the lecture introduces are bolded in the Overview - **news and noise** (51), **shock-invertibility** (53), **fiscal foresight** (65) - and then in quotation marks once the Model section starts: "expected present-value budget balance" at 191 is being defined right there, by the display at 195 that immediately follows ("in the sense that"), and gets quotes instead of bold; "random walk" (285) and "old news" (392) are the same treatment for two more terms of art. The one italic in the file is used correctly for emphasis (*smaller*, 242).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 260, 343. *Example:* the lecture exists to show that two sets of impulse responses do not resemble each other, and it never puts them side by side: the $w$-responses (260-279, Fig 8.E.1) and the $u$-responses (294-335, Fig 8.E.2) are drawn in separate cells on separate scales, so the comparison 235-239 promises ("do not resemble the impulse response functions that depict the response of consumption and the net-of-interest deficit to innovations $w_t$") has to be made from memory across two pictures - a 2x2 grid, or the two consumption responses on one set of axes, would show it in one glance. Second, the reading of the second figure at 343-347 - "Consumption responds only to the first innovation" - is a claim about a line being flat at zero, which is exactly the sort of thing a reader mis-sees on an autoscaled axis and which nothing in the figure marks; and the lecture's central caution at 61-62 ("An econometrician who is unaware of the problem would misinterpret shocks and likely responses to them") is left in running prose where a `{note}` would carry it.

### Low severity
_None found._


## Strengths

- The abstract HS2013 matrices are immediately cashed out as the scalar processes they encode: after the $6 \times 6$ $A_{22}$ and the $U_d$ of 108-136, lines 144-152 write $d_t = 5 + d_{1t} + d_{2t}$, $d_{1t} = 0.9 d_{1t-1} + w_{1t}$ and the third-order MA for $d_{2t}$ out in full, so the matrix rows can be checked one at a time.
- The invertibility claim is made three times at increasing sharpness and each version is then shown: informally at 56-59, as the exact restriction $\sigma_2(\beta) = [0\ 0]$ at 211-212, and as its consequence $u_t = \sum_{j=0}^\infty \alpha_j w_{t-j}$ at 245-250 - which is precisely what the third figure (349-377) plots.
- The three information sets the argument turns on are separated into three bullets at 214-221 and never conflated afterwards: the consumer sees the histories of $d_{1t}$ and $d_{2t}$, the econometrician has only $[c_t, d_t]$, and what the econometrician can therefore estimate is a Wold representation for $[c_t, c_t - d_t]$.
- Every figure names the exact page it reproduces - `# This is Fig 8.E.1 from p.188 of HS2013` (261), `Fig 8.E.2 from p.189` (303), `Fig 8.E.3 from p.189` (350) - so the replication is verifiable against the book rather than asserted.
- 318-322 says why the responses are rescaled and does it properly: the comment `# This scales the impulse responses to match those in the book` followed by multiplication by the stationary innovation standard deviations from `hs_kal.stationary_innovation_covar()`, so the comparison with HS2013's figures is like-for-like.
- 296 explains the one line of the Kalman setup a reader would otherwise stall on, in a comment on the line itself: `H_HS = 1e-8 * np.eye(2)  # Set very small so there is no measurement error` - which is what makes the whitener a Wold representation of the observed pair.
- 343-347 reads the right thing off the second figure and names the mechanism rather than the picture: consumption responds only to the first innovation because Hall's model imposes Granger causality from $c_t$ to $c_t - d_t$ with no reverse causality.

## Recommended actions

1. Fix 72 - "the sum of two orthogonal autoregressive processes" contradicts 152 and 155-156, where $d_{2t}$ is a third-order pure moving average; 138-139 already says it correctly.
2. Give the third figure titles of its own (370, 375): they currently duplicate the first figure's (269, 277) while plotting the responses of $u_t$ to $w_t$ rather than of $c_t$ and $c_t - d_t$.
3. Write the conditioning as $\mathbb{E}_0[\cdot]$ and $\mathbb{E}_t[\cdot]$ at 77 and 195 instead of hanging `|J_0` and `|J_t` outside the brackets, and replace `[0\,\,\,0]` at 212 and 241 with a `bmatrix` or a plain $0$.
4. Say what `x0` is at 180 - eight entries, with $h_{-1} = 5$ and $k_{-1} = 150$ - and either explain or zero the $\delta_h = 0.9$, $\theta_h = 0.1$ of 170-171, which are dead given $\Lambda = 0$ at 168 and the $s_t = c_t$ of 81.
5. Replace the `# Chase's great trick` comment at 175 with a line saying which rows of `` {eq} `` at 108-120 the index arrays at 176 and 178 fill in, or build the matrix literally as `ud` is built at 172.
6. Clean the three code cells: drop the no-op `ma_coefs = ma_coefs` at 305, derive `jj` at 306 from the 50 passed at 301 rather than repeating it, and replace the hardcoded `reshape(40, 1)` at 267 and 275 and `reshape(1, 8)` at 295 with the `ts_length` of 263 and the state dimension; add the missing spaces after the commas at 267.
7. Rename `γ` at 160 to `Γ` (it is the matrix of 91, built from the scalar `γ_1`) and restore the capitals on `a22`, `c2`, `ub`, `ud` at 174-179.
8. Label the $u_t = \sum_j \alpha_j w_{t-j}$ display once at 248-250 so 382-384 can `{eq}`-reference it instead of repeating it verbatim, and restore the dropped noun at 64.
9. Sweep the measured items: the eight `\left[ {\begin{array}...} \right]` displays at 110, 115, 124, 132, 202, 205, 224 and 227 recast as `bmatrix` (qe-math-003), the six `set_title` calls (269, 277, 328, 333, 370, 375) moved into `mystnb` captions with `name`s on the three figure cells (260, 294, 349), `lw=2` on the twelve plot calls, the three `figsize=(12, 4)` overrides dropped, and the nine double spaces.
