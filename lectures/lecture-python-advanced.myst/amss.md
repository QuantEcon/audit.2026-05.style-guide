# amss

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/amss.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×6; `qe-writing-001` ×2; `qe-writing-003` ×3, +3 more. |
| Math         | 4/10  | `qe-math-010` (proposed) ×16; `qe-math-003` ×2; `qe-math-009` ×1. |
| Code         | 7/10  | `qe-code-001` ×7; `qe-code-004` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×3; `qe-fig-008` ×3, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 86, 91, 866, 996, 1081, 1082, 1087. *Example:* five lines in the interpolation cell carry trailing whitespace (86, 96, 105, 115, 121); 91-92 and 100-101 use backslash line continuations with a two-space hanging indent (`slope = (y_values[1] - y_values[0]) \` then `  / (x_nodes[1] - x_nodes[0])`) where parentheses would wrap the expression cleanly; 866 and 999 write `) ** 2` with spaces around the exponentiation operator, which the rule explicitly asks to be written `a**b`; 996 leaves a space before a closing bracket, `np.hstack([1 - g, np.ones(S)]) ]).T`; 1081 puts a backslash continuation *inside* the parentheses of `zip(...)` and 1082 indents the continuation to a flat 8 spaces; and 1087 omits the space after the comma in `('Complete Markets','Incomplete Markets')`, where the identical call at 1043 has it.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 16. *Lines:* 302, 313, 335, 344, 353, 378, 403, 405, 408, 451, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 6. *Lines:* 33, 245, 294, 585, 677, 930. *Example:* the assignment of bold and italic is inconsistent in both directions. Definitions appear in bold in some places (**natural debt limit** 221, **measurability constraints** 249, **marketable subspace** 327, **continuation Ramsey planner** 601, **state variable degeneracy** 710) and in italic in others (*implementability constraints* 294, *measurability constraints* 585 - the same term as 249, *risk-adjusted martingale* 677, *martingale convergence theorem* 732). Emphasis likewise appears in bold (**without** 33, **purchases**/**sells** 920-921, **low** twice at 930 and again at 932, **increase**/**reduction** 949-950) and occasionally in italic (*only* 306, *increase* 384, *same* 922). Line 245 sets an entire sentence in bold.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 67. *Lines:* 27, 31, 33, 146, 149, 170, 181, 198, 293, 297, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 2. *Lines:* 879, 1012. *Example:* %%time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 900, 1036, 1079. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 909, 1040, 1084. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 889, 1022, 1071. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 907, 1039, 1083. *Example:* plot() without lw=.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 802, 815. *Example:* pmatrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 513, 1092. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 191, 327, 368, 921. *Example:* 327 is a 50-word sentence with three levels of nesting ("In a language used in the literature on incomplete markets models, it can be said that the AMSS model requires that at each $(t,s^t)$ what would be the present value of ... must belong to the **marketable subspace** ..."); 368-369 is 44 words before reaching its main verb; 191 is 40 words comparing three papers in one breath; and 921-922 says it twice - "the Ramsey planner designs these purchases and sales designed so that".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 221, 815, 1056. *Example:* the displayed expenditure vector at 815 is $g = (0.1, 0.1, 0.1, 0.1, 0.2, 0.1)$, putting the war value in the fifth state, which matches the state list at 794 where state 5 is $(3, g_h)$ - but the code at 846 writes `g = np.array([0.1, 0.1, 0.1, 0.2, 0.1, 0.1])`, putting it in the fourth, and 891-892 then treat index 3 as the war history; so the algebra and the code disagree about which state is the war state and a reader checking one against the other is stopped cold. Line 221 introduces the **natural debt limit** that 262 then invokes to derive `` {eq}`TS_gov_wo3` ``, deferring it to "a forthcoming lecture" that is never named or linked. And 1056 says "the following figure" but two further paragraphs (1059, 1061) intervene before the cells that draw it at 1063-1089.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 645, 790, 836. *Example:* the same all-caps caveat `# WARNING: DO NOT EXPECT THE CODE TO WORK IF YOU CHANGE PARAMETERS` is pasted into five code cells (836, 864, 890, 982, 1024) - an important, repeated warning about the fragility of the grid bounds, hidden in comments where one `{warning}` admonition in the prose would carry it once and be visible to a reader who is not reading the source. Second, the section that carries the lecture's central theoretical claim - $V_x(x,s)$ is a risk-adjusted martingale under the twisted matrix $\check\Pi$ (645-718) - never plots $V_x$, even though the code already computes $V$ on a 300-point grid (850, 990); the figures show consumption, labor, debt, taxes, spending and output, but not the one object the theory is about. Third, the six-state $(t,g)$ construction at 790-810, with the war branch opening at $t=3$, is presented only as a $6\times 6$ matrix where a small transition diagram would make the trick immediately legible.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 612. *Example:* the state space is written `{\cal S}` at 612 and 624 where a plain $S$ would do - and the lecture itself uses plain `S` for exactly that object in code at 856 and 995 (`S = len(Π)`), so the calligraphic form is decoration that also breaks the correspondence between the algebra and the implementation.


## Strengths

- The lecture is organised around one difference and keeps saying which side of it the reader is on: 138-140 opens with "let's start with things that are identical", 187 marks the exact point where AMSS departs from Lucas-Stokey, and 319-327 and 454-468 each give an explicit item-by-item comparison of the two models' first-order conditions.
- The derivation of the measurability constraints is done step by step and the step that matters is called out in its own line: 242-249 points out that the right side of `` {eq}`TS_gov_wo2` `` depends on $s^t$ while the left depends only on $s^{t-1}$, and says that this - not an assumption bolted on later - is what risk-free debt means.
- Almost every displayed equation is labelled and genuinely cited later - `TS_gov_wo` at 232, `TS_gov_wo2` at 247 and 251, `TS_gov_wo3` at 275, 293 and 492, `AMSS_44_2` at 293 and 454, `AMSS_44`/`AMSS_46` at 363, 369, 384 and 395, `eqn:AMSSapp1` at 528, `eqn:AMSSapp2b` at 576, 580 and 585, `eqn:AMSSapp5`-`eqn:AMSSapp9` throughout 659-677.
- The two examples are chosen to isolate one effect each - a single anticipated one-period war (764-950) to show that history dependence appears at all, then a perpetual 50/50 war risk (952-1089) to show it accumulating - and both are plotted against the complete-markets benchmark on the same axes with a stated line convention (829-833).
- Numba-compatible interpolation is written out and collapsed rather than imported from nowhere (71-132), so the interpolation the value-function iteration depends on is auditable.
- The exercise at 688-696 asks the reader to verify that the twisted matrix $\check\Pi$ is a genuine transition density, which is exactly the check the martingale claim rests on.

## Recommended actions

1. Reconcile the war state between the algebra and the code: 815 and 794 put $g_h = 0.2$ in state 5, the code at 846 puts it in index 3, and 891-892 simulate the war history through index 3 - one of the three has to move.
2. Replace the five pasted `# WARNING: DO NOT EXPECT THE CODE TO WORK IF YOU CHANGE PARAMETERS` comments (836, 864, 890, 982, 1024) with a single `{warning}` admonition in the prose that says which parameters the hand-tuned grid bounds `x_min`/`x_max` (848-849, 988-989) depend on.
3. Fix the LaTeX in the Lagrangian at 399-414: line 405 opens `\Bigl[` and 406 closes with `\biggr\}`, so the bracket is never matched; and rename the labels carrying stray semicolons (`AMSS_lagr;a`, `AMSS_lagr;`, `AMSS_foc;a`, `AMSS_foc;b`) and the triple-M typo in `eqn:AMMSSapp101` at 640.
4. Settle bold for definitions and italic for emphasis - the same term, *measurability constraints*, is bolded at 249 and italicised at 585 - and un-bold the whole-sentence emphasis at 245.
5. Plot $V_x$ along one of the simulated histories so the risk-adjusted-martingale claim of 645-686 is visible, and add a transition diagram for the six-state $(t,g)$ construction at 790-810.
6. Convert the two `%%time` magics at 879 and 1012 to the `quantecon` `Timer` context manager (qe-code-004), add `mystnb: figure: caption/name` metadata to the three figure cells (889, 1022, 1071), move the `set(title=)` calls at 909, 1040 and 1084 into those captions, set `lw=2` at 907, 1039 and 1083, and drop the three `figsize=(14, 10)` overrides.
7. Sweep the remaining items: 67 runs of double spaces, the two `pmatrix`/`\begin{matrix}` displays at 802 and 815 recast with `bmatrix` (qe-math-003), the seven PEP8 items above, "This pattern facilities smoothing" at 924, the garbled sentence at 470-471, and name the lecture that 221 defers the natural debt limit to.
