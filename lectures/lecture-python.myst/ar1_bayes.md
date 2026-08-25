# ar1_bayes

- **Series:** lecture-python.myst
- **File:** `lectures/ar1_bayes.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7/10  | `qe-writing-003` ×3; `qe-writing-002` ×3. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 6/10  | `qe-code-002` ×8; `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8/10  | `qe-fig-005` ×3; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 470, 485, 522, 525, 537. *Example:* five code lines exceed the PEP8 79-character limit, two of them badly: `numpyro.infer.MCMC(NUTS_kernel, num_samples=50000, num_warmup=10000, progress_bar=False)` is 95 characters at line 485 and 96 at line 537, and the `numpyro.sample(...)` calls at 470, 522 and 525 run to 82-84; none of the five is close to a mathematical expression, so nothing here overrides PEP8.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 8. *Lines:* 244, 250, 327, 334, 337. *Example:* spelled-out `sigma`.

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 220, 383, 557. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 39, 47. *Example:* raw link to intro.quantecon.org.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 315, 426, 504. *Example:* the stationary density $y_0 \sim N(0, \sigma_x^2/(1-\rho^2))$ is set as an unlabelled display three separate times - lines 85-87, 314-316 and 503-505 - each time preceded by a "recall that" sentence; labelling it once and citing it with `{eq}` would remove two displays and two lead-ins. Line 426 is a 36-word sentence that comma-splices three separate NumPyro-versus-PyMC correspondences (function versus `with` block, `numpyro.sample` versus a `pm` variable, `obs=` versus `observed=`) into one span.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 461, 479, 510. *Example:* the NumPyro half silently rebinds three names the PyMC half established: `AR1_model` is a `pm.Model()` object from line 238 until line 461 turns it into a plain function, `AR1_model_y0` likewise at 321 versus 510, and line 479 rebinds `y` from the NumPy array built at 215 to a JAX array; nothing in the prose at 418-428 warns the reader, and after line 479 none of the PyMC cells at 277-373 can be re-executed.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 441. *Example:* figsize=.


## Strengths

- The two assumptions are named once ("conditioning assumption", "stationary assumption" at 77 and 83) and then used by name for the rest of the lecture, so the reader never has to re-derive which is which.
- The second PyMC model differs from the first by exactly one line (337), the prose says so at 340, and the note at 342-348 draws the consequence explicitly - "any difference between the two posteriors comes entirely from this one term".
- The mechanism behind the result is spelled out step by step at 404-416 rather than asserted: extreme $y_0$, low stationary likelihood, Bayes' law seeking parameters that make it plausible, $\rho \to 1$ inflating $\sigma_x^2/(1-\rho^2)$.
- The PyMC and NumPyro posteriors are overlaid at 557-567 as an explicit cross-library check, matching the promise made at line 107.
- The Hurwicz small-sample bias is named and cited ({cite:t}`hurwicz1950least`, {cite}`Orcutt_Winokur_69`) rather than left as an unexplained gap between the posterior mode and the true 0.5.

## Recommended actions

1. Rename the spelled-out Greek in the NumPyro and PyMC cells - `sigma=` keyword values aside, the identifiers `sigma` and `rho` used as PyMC/NumPyro variable *names* at 243, 244, 326, 327, 463, 464, 512, 513 are the lecture's own choice and should be `'ρ'`/`'σ'` or at least consistent with the `ρ`, `σ` Python names bound to them (qe-code-002, 8 occurrences).
2. Fix the density-versus-random-variable conflation at 154-155: `f(y_t \mid y_{t-1}) \sim N(\rho y_{t-1}, \sigma_x^2)` says a density is normally distributed; it should read `y_t \mid y_{t-1} \sim N(\rho y_{t-1}, \sigma_x^2)`.
3. Give the stationary density one equation label and cite it with `{eq}` at 312 and 501 instead of restating the display (315, 504).
4. Rename `AR1_model`/`AR1_model_y0` in the NumPyro section so they do not shadow the PyMC model objects, and keep the NumPy `y` distinct from the JAX `y` created at 479.
5. Convert the two raw `intro.quantecon.org` links at 39 and 47 into `{doc}` cross-series references (qe-link-002, 2 occurrences).
6. Add `mystnb: figure: caption/name` metadata to the three code-cell figures at 220, 383 and 557 (qe-fig-005, 3 occurrences) and drop the `figsize=(17, 6)` override at 441 (qe-fig-001).
7. Wrap the five over-length code lines at 470, 485, 522, 525 and 537, and delete the four assigned-but-unused bindings `y_like` (250), `y_data` (334, 470, 522) and `y0_data` (337, 525) - the `pm.Normal`/`numpyro.sample` calls register with the model by side effect, so the names are noise.
