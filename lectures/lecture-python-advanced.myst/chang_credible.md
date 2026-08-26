# chang_credible

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/chang_credible.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-001` ×5; `qe-writing-005` ×8; `qe-writing-004` ×2, +4 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 5. *Lines:* 459, 612, 725, 792, 797. *Example:* 2 sentences in one paragraph.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 170, 328, 330, 339, 385, 429, 561, 679. *Example:* the two uses are exactly inverted throughout this lecture. Every term is defined in *italic* where the rule asks for bold - *value of money* (170), *government policy* / *price system* / *allocation* (330-332), *competitive equilibrium* (339), *credible* (385), *sustainable plan* (429), *outer hyperplane approximation algorithm* (679), and earlier *Ramsey planner* (43), *sustainable plan* (53), *credible public policy* (54), *sustainable* (78-79) - while bold is used for the block labels that should be `{prf:definition}` / `{prf:proposition}` directives instead: **Definition:** (328, 336), **A credible government policy with a recursive representation** (349), **Proposition:** (561, 566), **Step 1**-**Step 4** (693, 695, 725, 771).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 21. *Lines:* 38, 41, 43, 60, 69, 91, 93, 103, 134, 215, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 829, 855, 868, 869. *Example:* line 829 names a function parameter `ChangModel` - CapWords for a parameter, and it shadows the class of the same name that the calls at 818 and 868 instantiate; 855's continuation (`R[1]), fontsize=18)`) is indented to the `xytext` line rather than to the open paren it continues (E128); 868 writes `h_max=1/0.8` with no spaces around the operator while the same call spaces nothing else ambiguously; and 869 continues that call at a flat 4-space indent instead of aligning under the opening paren.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 319, 403, 423, 725. *Example:* 319-321 delays its verb for twenty words ("The observation that the one dimensional promised marginal utility of real balances $\theta_{t+1}$ functions in this way is an important step in ..."); 403-405 spends 33 words asking the reader to "note the subtle change in arguments" without saying what the change is, which the next paragraph then does; 423-424 is garbled - "For a credible government plan, we the two-dimensional state vector $(w_t, \theta_t)$ encodes history dependence"; and 725-728 packs two sentences and 40 words into one paragraph, the second restating the first.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 435, 447, 594. *Example:* $CE_\pi$ is used at 435 and $CE_\pi^0$ at 477, 509, 528 and 638 without being defined anywhere in this lecture, as are $\Omega$ (459) and $\Theta$ (441 defines $\Theta$ but in terms of the undefined $CE$); each set-builder definition is then split across separate display blocks with prose wedged between the braces - $S$ opens `\Bigl\{` at 448 and closes `\Bigr\}` at 456 with "with value" in between, $\tilde D(Z)$ opens at 508 and closes at 551 across six independently-labelled `{math}` blocks, and $E(Z)$ opens at 648 and closes at 672 across eight; and because of that fragmentation the sentence at 598, "Chang (1998) provides a method for dealing with the final three constraints", refers to constraints the reader cannot count.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 726, 765. *Example:* mid-sentence 'Step'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 242, 768. *Example:* the lecture improvises a diagram in math mode at 467 - `$(h,x) \rightarrow m=q M \rightarrow y = c$` - which is the tell that the within-period timing protocol described at 242-259 wants a real figure; that protocol is the one thing this lecture changes relative to {doc}`chang_ramsey`, and it is the only mechanism here with no picture. Second, 768-769 says the algorithm "constructs a sequence of progressively smaller sets $S_{t+1} \subset S_t \subset S_{t-1} \cdots \subset S_0$" and the reader is shown only the final set at 860 and 879; one plot of two or three successive iterates would show the outer hyperplane approximation actually working.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 833. *Example:* figsize=.


## Strengths

- The lecture states its own delta precisely: 34-51 says it assumes the environment of {doc}`chang_ramsey` and that the *only* change is the within-period timing protocol, and 554-559 then says exactly what the new operator adds - $\tilde D$ is $D$ plus the deterrence condition {eq}`eqn_chang14`.
- The timing protocol is presented as a mechanism rather than a convention: 256-263 explains that the within-period order is what creates the government's temptation and therefore what the new operator has to price.
- Chang's simplification is motivated before it is used - 604-610 argues that only the best deviation and the harshest punishment matter, which is what makes the scalar $BR(Z)$ enough to replace three constraints.
- The punchline is delivered visually and twice with one parameter changed: at $\beta = 0.3$ the Ramsey point $R$ lies outside the blue sustainable set (860, 863) and at $\beta = 0.8$ it lies inside (879, 882), using the same `plot_equilibria` function both times so the comparison is honest.
- The algorithm is given first as a four-step loop (681-691) and then each step is expanded into the linear program that implements it (695-772), so the code that follows can be read against a named step.

## Recommended actions

1. Reassemble the three set definitions into single display blocks: $S$ (447-457), $\tilde D(Z)$ (504-552) and $E(Z)$ (647-673) each open a `\Bigl\{` in one block and close the `\Bigr\}` in another, with prose and separately-numbered equations in between - which is also why "the final three constraints" at 598 cannot be identified.
2. Fix the sign error at 625: the constraint reads `m(h)(u'(f(x(h))) + v'(m(h))) \leq \beta \theta'(h)` where 547 and 666 both have a minus, and the line also carries a stray closing `\}`.
3. Replace the bold block labels with `{prf:definition}` and `{prf:proposition}` directives (328, 336, 349, 561, 566) and bold the terms they define instead of italicising them (170, 330-332, 339, 385, 429, 679); also drop the stray full stops at 429 ("...*sustainable plan* (SP) if.") and 566 ("**Proposition:**.").
4. Define $CE$, $CE_\pi^0$, $\Omega$ and $\Theta$ in this lecture or link them explicitly to where {doc}`chang_ramsey` defines them - they carry the whole of 431-568 and appear here without introduction.
5. Add a figure for the within-period timing protocol (242-259); the arrow chain improvised in math at 467 is doing a diagram's job. And plot two or three successive iterates $S_t$ so the shrinking claimed at 768 is visible.
6. Add `mystnb: figure: caption/name` metadata to the two figure-producing cells (828, 878) and drop the `figsize=(7, 5)` at 833, so the two equilibrium-set plots can be captioned and cross-referenced.
7. Sweep the mechanical items: 21 runs of double spaces, the five two-sentence paragraphs at 459, 612, 725, 792 and 797, the mid-sentence "Step" capitals at 726 and 765, and the four PEP8 items above.
