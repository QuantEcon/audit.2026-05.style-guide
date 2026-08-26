# back_prop

- **Series:** lecture-python.myst
- **File:** `lectures/back_prop.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×5; `qe-writing-003` ×2; `qe-writing-002` ×3, +4 more. |
| Math         | 7.5/10 | `qe-math-003` ×6. |
| Code         | 7.5/10 | `qe-code-001` ×6; `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-010` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 49, 342, 418, 430, 442, 453. *Example:* fifteen code lines exceed 79 characters, several badly: 98 at line 49, 100 at 418, 104 at 452, 108 at 430 (`jnp.block([dx.reshape((-1, 1)) for dx_tuple in grad(loss)(params, x, y) for dx in dx_tuple ])`, which also has a space before the closing bracket, as does 407); the continuation line at 443 is indented to column 10 under a bracket opened at column 11; fifteen lines carry trailing whitespace (357, 359, 364, 373, 379, 381, 386, 453, 455, 457, 458, 460, 507, 508, 519); and the two top-level `def`s at 340 and 345 are separated by one blank line where PEP8 asks for two.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 258, 262, 266, 272, 277, 299. *Example:* array used as matrix.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 72, 153, 211, 312, 538. *Example:* H2 Title Case: 'A Deep (but not Wide) Artificial Neural Network' (Deep, Wide, Artificial, Neural).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 59, 60, 69, 74, 78, 80, 84, 90, 121, 123, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-010]** — Plotly figures require latex directive. *Count:* 1. *Lines:* 1. *Example:* plotly used with no {only} latex directive.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 3 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 78, 156, 231. *Example:* line 78 defines width as "the number of right hand side variables on the right hand side of the function being approximated" - the same phrase twice in one clause; lines 156-162 restate the model that 92-151 has just built ("As mentioned above, for a given input $x_1$, our approximating function $\hat f$ evaluated at $x_1$ equals the 'output' $x_{N+1}$ ... computed by iterating on $x_{i+1}=h_i(w_i x_i + b_i)$" is `` {eq}`eq:recursion` `` again in words); and line 231 is a one-word paragraph ("Here goes.") followed by five blank lines.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 328, 538. *Example:* lines 328-470 are fourteen consecutive code cells with no prose between them at all - the reader goes from "The update rule `` {eq}`eq:sgd` `` ... amounts to a stochastic gradient descent algorithm" (326) straight to `jnp.block([[δ * xs[:-1]], [δ]])` (411), `L = jnp.diag(δ * ws, k=-1)` (415) and `D = jax.scipy.linalg.block_diag(...)` (418) with nothing saying that these are the $D$ and $L$ of the display at 262-282, and the two verification cells at 423-435 have only a comment to explain what is being checked against what. Separately, "How Deep?" (538-545) is placed between the two examples but its content belongs to Example 2, which is the one that actually compares one-, two- and three-layer networks (566-610) - and its third bullet asserts a one-layer identity network "would probably work best" for Example 1 without ever running it.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 92, 101, 262. *Example:* the lecture promises to describe "a neuron", "a network of neurons" and "a neural network as a composition of functions" (65-68) and then does all of it in formulas: the layer definition at 92-98, the composition at 134 and the recursion at 145 have no node-and-arrow diagram anywhere in the file, in a lecture whose subject is a graph; the three activation functions at 101-119 (sigmoid, ReLU, identity) are given as three formulas and never plotted, though three curves on one axes is a two-line cell; and the lower-triangular structure that the whole back-propagation argument turns on (262-282, $D$ and $L$) is shown only as a 25-line `array` display where a sparsity sketch would carry it. The two figures the lecture does have (528, 606) are approximation plots.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 519. *Example:* %%time.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 54. *Example:* line 54 bolds **machine learning** and **artificial intelligence**, neither of which the lecture defines - they are field names being emphasised, and the rule reserves bold for definitions; the lecture uses no italic anywhere, so emphasis has nowhere else to go.


## Strengths

- The linear-algebra route to back-propagation is verified against automatic differentiation rather than asserted: `jnp.max(jnp.abs(dxs_ad_mat - dxs_la))` at 426 checks the derivative matrices agree and 435 checks the loss gradients agree, so the $(I-L)^{-1}D$ identity at 293 is demonstrated numerically.
- The `{youtube}` directive at 227 embeds the source of the triangular-matrix idea directly in the page and attributes it in the preceding line, rather than leaving a bare URL.
- The whole derivation is set up so the reader can see why lower-triangularity matters: 213-223 states the two ingredients (chain and product rules, triangular matrices) and the two operations they buy (one triangular inversion plus one multiplication) before any algebra appears.
- Example 2 compares one-, two- and three-layer networks on the same axes with distinct trace names (600-610), which is the right way to show the depth question the lecture raises.

## Recommended actions

1. Convert the six `\begin`` {array}` matrix displays at 258, 262, 266, 272, 277 and 299 to ` ``bmatrix` (qe-math-003, 6 occurrences) and replace the `h'` transpose-style prime at 246 with explicit derivative notation (qe-math-002).
2. Fix the four mathematical errors in the derivation, which currently make it unfollowable: `w_i x_i + bI` at line 96 should be `w_i x_i + b_i`; the composition at 134 repeats `l_1` where `l_{N-1}` belongs; the differential at 252 has `+ b_i` where it needs `+ db_i`; and `e_N` at 305 is used with no definition.
3. Write prose into the fourteen bare code cells at 328-470 tying `L` (415), `D` (418) and `dxs_la` (420) back to the matrices named at 262-282, and say what each of the two verification cells (423, 433) is checking.
4. Add a diagram of the width-one depth-$N$ network, and plot the three activation functions at 101-119 - a lecture that introduces neural networks currently shows the reader no network.
5. Sentence-case the five Title Case H2s at 72, 153, 211, 312 and 538, and collapse the 42 double spaces (qe-writing-008, 42 occurrences, the largest mechanical item here).
6. Fix the training loop at 501-508: `key, _ = random.split(key)` discards the new key and line 504 permutes with the fixed `random.key(1)`, so all 300 (or 500) epochs see the identical permutation and the `epoch` variable is unused.
7. Wrap the fifteen over-length code lines, strip the fifteen trailing-whitespace lines, replace `%%time` at 519 with the `quantecon` `Timer` context manager (qe-code-004), split the three-sentence paragraph at 33, and unify `\mathcal{L}` (167, 199) with `{\mathcal L}` (176, 202).
