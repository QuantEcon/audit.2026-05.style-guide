# bayes_nonconj

- **Series:** lecture-python.myst
- **File:** `lectures/bayes_nonconj.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-005` ×6; `qe-writing-001` ×4; `qe-writing-002` ×4, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-003` ×2; `qe-fig-005` ×4; `qe-fig-008` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 39, 114, 203, 260, 384, 445. *Example:* the lecture uses italic correctly for emphasis in about fifteen places (*same* 33, *compute* 128, *declaration* 130, *reads* 132, *single* 142, *zero* 310, *joint* 454, *within the guide family* 513, ...) but then reaches for bold for the same job six times: **not** (39), **small** (114), **four** (203), **not** (260), **scale** (384), and **minimizing**/**maximizing** (445); none of these is a term being defined.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 2. *Lines:* 160, 277. *Example:* two code lines exceed the PEP8 79-character limit with no mathematical justification: the `run_nuts` signature at line 160 is 84 characters and the four keyword defaults would split cleanly across lines, and `prior_pdf = np.where(...)` at line 277 is 83 characters.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 287, 485. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 228, 238, 480, 493. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 55. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 178, 325, 425, 436. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 51, 53, 218, 396. *Example:* four sentences run to 40+ words, each carrying two joined ideas: line 51 (41 words) defines NUTS as Hamiltonian Monte Carlo and then explains accept/reject in one breath; line 53 (41 words) joins the gradient-proposal mechanism to the automatic step-length tuning with a semicolon; the middle sentence of line 218 (42 words) explains autocorrelation, the length-N comparison and the bulk/tail split together; line 396 (40 words) states both halves of the MCMC-versus-VI rule of thumb in one sentence.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 482. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 439. *Example:* the ELBO derivation (398-452) is the one section of an otherwise well-illustrated lecture with no visual support; the decomposition at 439-441 - $\log p(Y)$ fixed, split into the KL divergence plus the ELBO, so maximising one closes the gap on the other - is exactly the relationship a single stacked-bar or bound diagram makes obvious, and the sentence at 452 ("the ELBO is a lower bound on $\log p(Y)$ - hence its name") is asking for one.


## Strengths

- The lecture validates the machinery before trusting it: the conjugate beta case is run through NUTS first (192-252) precisely so the sampler can be checked against a posterior known in closed form, and the plan at 58-62 says so up front.
- Convergence diagnostics are taught, not just printed - `r_hat` and `ess_bulk`/`ess_tail` are each explained in their own bullet (216-218) and the trace plot at 228 is preceded by a description of what a well-mixed chain looks like (226).
- The four priors reuse one `binomial_model` and one `plot_prior_posterior` helper, and the recipe is stated as three numbered steps at 264-266 before the first of them - so each subsequent subsection is three lines of code and the reader's attention stays on the prior.
- The restrictive uniform prior on $[0.5, 0.95]$ (308-321) is a deliberately chosen counterexample: it excludes the true $\theta = 0.4$, and the lecture draws the lesson explicitly at 321 rather than leaving the reader to notice the piling-up at the boundary.
- The masking comment at 274-275 explains *why* `prior.support` is needed (`dist.Uniform.log_prob` returns its constant outside the support), which is the kind of NumPyro trap a reader would otherwise hit alone.

## Recommended actions

1. Add `mystnb: figure: caption/name` metadata to the four bare code-cell figures at 228, 238, 480 and 493 so they can be captioned and cross-referenced (qe-fig-005, 4 occurrences).
2. Move the two embedded matplotlib titles into figure captions: `ax.set_title(title)` at 287 (fed by the `title=` argument of `plot_prior_posterior`, so all four prior figures are affected) and `ax.set_title("SVI convergence")` at 485 (qe-fig-003, 2 occurrences).
3. Switch bold to italic in the six emphasis-only places listed above (39, 114, 203, 260, 384, 445); the lecture already uses italic correctly everywhere else, so this is an internal-consistency fix.
4. Split the four one-paragraph pairs at 178, 325, 425 and 436 into one sentence per paragraph, and while doing so break the 40+ word sentences at 51, 53, 218 and 396 (qe-writing-001, 4 occurrences).
5. Replace the raw URL at line 55 with a `{doc}` cross-series reference to the MCMC lecture (qe-link-002).
6. Set `lw=2` on the loss-curve plot at line 482 - the only `ax.plot` in the lecture without it (qe-fig-008).
7. Wrap the two over-long code lines at 160 and 277, and consider giving `plot_prior_posterior` a `{numref}`-able name per figure rather than a `title=` string.
