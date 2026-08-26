# os_egm

- **Series:** lecture-python.myst
- **File:** `lectures/os_egm.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×4; `qe-writing-003` ×3; `qe-writing-002` ×2, +3 more. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 4. *Lines:* 62, 84, 105, 221. *Example:* H2 Title Case: 'Key Idea' (Idea).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 202, 240, 341, 237. *Example:* 202-204 declare three required callables as optional - `u_prime: Callable = None`, `f_prime: Callable = None`, `u_prime_inv: Callable = None` - and `K` calls all three unconditionally (247, 250), so omitting any one of them produces a `TypeError: 'NoneType' object is not callable` from inside the operator rather than a clear failure at construction; either make them positional or validate in `create_model`. Six lambdas are bound to names (240, 272, 273, 274, 275, 276), which is E731 - for the five one-line formulas at 272-276 the rule's mathematical-notation exemption is arguable, since `u = lambda c: np.log(c)` really does sit close to $u(c) = \ln c$, but 240 (`σ = lambda x: np.interp(x, x_in, c_in)`) is a closure over two captured arrays rather than a formula and a nested `def` would document what it captures. 341 is a bare expression relying on the notebook to auto-display an unlabelled float, `np.max(np.abs(c - σ_star(x, model.α, model.β)))`, where the sibling lecture prints the same quantity with a label (`` {doc}`os_egm_jax` ``:240-241). And 237 unpacks all eleven fields of `Model` to use seven: `u`, `μ` and `ν` are bound and never read - which is what makes the drafted `qe-code-002` finding actively dangerous rather than merely wrong (see actions).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 248, 250. *Example:* spelled-out `mu`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 81, 129, 100. *Example:* the defining integral is written with measure notation in the displays and density notation in the code that implements it: $\phi(dz)$ at 81 and 131 against `ϕ(z)dz` in the comment at 246 (and at `` {doc}`os_egm_jax` ``:156). Second, `` {eq}`egm_getc` `` at 128-132 uses `\left\{ ... \right\}` as the argument delimiter of $(u')^{-1}$, in a lecture that otherwise reserves braces for sets - $\{x_i\}$ (94), $\{(x_i, c_i)\}$ (100), $\{s_i\}$ (122) - so the one place braces are not a set is the place a reader is most likely to be parsing carefully. Third, the pair set loses its inner parentheses halfway through the section that introduces it: $\{(x_i, c_i)\}$ at 100 and 137, then $\{x_i, c_i\}$ at 139.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 351, 102. *Example:* 351-353 makes one point in two sentences and repeats the operative word: "EGM is faster than time iteration because it avoids numerical root-finding. / Instead, we invert the marginal utility function directly, which is much more efficient" - "much more efficient" adds nothing to "faster", and the causal clause is already in the first sentence. 102 is not a sentence: "Iteration then continues..." closes the exogenous-grid section on an ellipsis where the parallel section closes properly at 139-141.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 351, 149, 155. *Example:* the lecture's headline claim is the one thing it never measures. 351 states "EGM is faster than time iteration because it avoids numerical root-finding" and the only timing in the file is of EGM alone (346-348); no time-iteration number appears anywhere, and the comparison quoted at 41 ("We found time iteration to be significantly more accurate and efficient") was made in a different lecture against a different method. The note at 260-264 then pulls the other way - "The routine is still not particularly fast because we are using pure Python loops" - so within ninety lines the reader is told the routine is fast because it avoids root-finding and slow because it uses Python loops, with nothing reconciling the two and no number attached to either. Second, the production function is never written down: 149 says only "the function $f$ has a Cobb-Douglas specification", the displays at 81 and 131 give $f$ one argument ($f(x-c)$, $f(s_i)$), and the code's $f$ takes two - `f = lambda k, α: k**α` at 275, called as `f(s, α)` at 247 - so the algebra and the implementation disagree about the arity of the model's central function and $f(k) = k^\alpha$ is never displayed. Third, `v_star` (155-163) is defined with a docstring and never called, so the analytical *value* function is computed nowhere, while 152 promises "This will allow us to make comparisons with the analytical solutions" - only the policy comparison happens (331, 341).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 122, 325. *Example:* the lecture is named after a grid transformation and no figure shows a grid. 122-135 sets out the whole idea in three steps - fix a uniform exogenous $\{s_i\}$, compute $c_i$ from `` {eq}`egm_getc` ``, then set $x_i = c_i + s_i$ - and 141 says the method's name comes from $\{x_i\}$ being determined endogenously. One panel putting the uniform $s$ grid above the resulting non-uniform $x$ grid, or plotting $s_i$ and $x_i$ against $i$ on the same axes, would show what "endogenous grid" means in a glance; the array is already in hand at 320, and the sibling lecture later has to *explain in prose* that the endogenous grid shifts with the policy (`` {doc}`os_egm_jax` ``:402-404), which is exactly what such a figure would have made unnecessary. Second, the one figure the lecture does have (325-335) shows that the approximation is good, and the informative version of it is the error: the next cell collapses $c - \sigma^*(x)$ to a single number (341), so plotting that deviation across the grid instead would show *where* the approximation is worst - presumably near the lower bound $s = 10^{-4}$ (210), where the interpolation has least support.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 75, 123. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 325. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 141. *Example:* 141 uses bold for emphasis - "the grid $\{x_i\}$ is determined **endogenously**" - where the lecture's own emphasis on the opposite term nineteen lines earlier is correctly italic: 122, "we fix an *exogenous* grid $\{s_i\}$ for savings". The two words are a matched contrast and are set two different ways. The file's only other emphasis span, **endogenous grid method** at 43, is a definition and correctly bold.


## Strengths

- The method is motivated by the specific cost it removes, and the removal is then pointed out where it happens: 107-111 says the exogenous-grid strategy needs a root-finder and that root-finding is expensive because it takes many function evaluations, 113-114 names the one assumption EGM needs in exchange ($u'$ invertible), and 258 says plainly "Note the lack of any root-finding algorithm" immediately below the operator.
- The three-step construction at 120-137 is written so each step is one line and the non-obvious step is flagged: after $x_i = c_i + s_i$, line 137 says "Importantly, each $(x_i, c_i)$ pair constructed in this manner satisfies `` {eq}`egm_coledef` ``" - which is the fact that makes the whole trick legitimate and the fact a reader would otherwise have to supply.
- The exogenous-grid method is restated in full (86-102) before the endogenous one, using the same symbols and the same `` {eq}`egm_coledef` ``, so the difference between the two is a difference of two paragraphs rather than a difference of two lectures.
- The lecture places itself precisely: 36-41 lists the two previous methods with `{doc}` links and states what was concluded from them, 68 says the model and notation are inherited from `` {doc}`os_time_iter` `` rather than restating them, and 52 and 355-359 name what the next lecture adds.
- Reproducibility is handled and said out loud: `create_model` seeds a `default_rng` and stores the shock draws in the model (212-214, with the comment "with a seed, so results are reproducible"), so every application of $K$ integrates against the same draws - which is what makes the fixed-point iteration converge rather than wander.
- The `Model` `NamedTuple` documents every field with an inline comment (178-188), including which callables are derivatives of which, and `K`'s signature does the same for its three arguments (226-230) - so the operator can be read without scrolling back.
- Timing uses the `quantecon` `Timer` context manager (347) rather than a `%%time` cell magic, which is what `qe-code-004` asks for, and it re-solves with `verbose=False` so the timing is not contaminated by printing.

## Recommended actions

1. Do not act on the two drafted `qe-code-002` findings at 248 and 250 - and this one is worth stating in the report, because the rename the rule asks for introduces a bug. `mu` there is a local abbreviation for the *marginal utility* being averaged, as the comment on 246 says ("Approximate marginal utility"), and `μ` is already bound in the same function two lines earlier: 237 unpacks the shock location parameter as `μ`. Renaming `mu` to `μ` at 248 would silently overwrite it inside the loop. Rename `mu` to `expected_mu` or `Emu` instead, if anything (see scanner_doubts).
2. Time the sibling method in this lecture, or drop the comparison at 351. As written the claim that EGM beats time iteration rests on a timing that lives in `` {doc}`os_time_iter` ``, and 261 says the routine is slow for an unrelated reason - one extra cell calling the `os_time_iter` solver on the same grid would settle both sentences.
3. Add a figure of the two grids - uniform $s_i$ against the induced non-uniform $x_i$ - so that the thing the method is named after is visible. The array is available at 320.
4. Write $f(k) = k^\alpha$ where 149 currently only says "Cobb-Douglas", and reconcile the arity: the displays at 81 and 131 give $f$ one argument, the code gives it two (275, 247). Then settle $\phi(dz)$ against `ϕ(z)dz` (81, 131 versus 246).
5. Either call `v_star` (155) or delete it: the analytical value function is defined and never used, while 152 promises comparisons "with the analytical solutions" and only the policy comparison is made.
6. Make the three callables in `create_model` required (202-204): as optional keyword arguments defaulting to `None` they turn a missing argument into a `NoneType` error raised from inside `K`.
7. Sentence-case the four Title Case headings (62 "Key Idea", 84 "Exogenous Grid", 105 "Endogenous Grid", 221 "The Operator"); italicise **endogenously** at 141 to match *exogenous* at 122; add `mystnb: figure: caption`/`name` metadata to the figure cell at 325; close the two double spaces (75, 123); print the deviation at 341 with a label; and replace the ellipsis at 102 with a sentence.
8. Sync the `lecture-dp` mirror rather than editing it: `lecture-dp/lectures/os_egm.md` differs from this file in exactly two places and both are staler there - it still uses the legacy global-state RNG (`np.random.seed(seed)` / `np.random.randn(...)`) where this file uses `np.random.default_rng(seed)` / `rng.standard_normal(...)`, and it has no `!pip install quantecon` cell at all, which is why the mirror carries a `qe-code-003` finding this file does not. The usual advice for the duplicated lectures is to fix upstream and let both clear; here upstream is already correct and the copy needs the update.
