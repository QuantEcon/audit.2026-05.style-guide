# estspec

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/estspec.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-005` ×5; `qe-writing-001` ×2; `qe-writing-003` ×3, +2 more. |
| Math         | 9.5/10 | `qe-math-009` ×3. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-005` ×7; `qe-fig-006` ×2; `qe-fig-003` ×1, +3 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 301, 488, 540, 547, 551, 555. *Example:* 301 mixes spacing conventions inside one expression - `0.5 - 0.5 * np.cos(2 * np.pi * n/(M-1))` spaces every operator except the `/` and the `-` in the subscript arithmetic - and binds the comprehension variable to `n`, the name the whole lecture uses for the sample size (224, 489). 488 writes `## Data` with a doubled hash. 540 writes `figsize=(10,12)` with no space after the comma, where the identical call at 495 has `figsize=(10, 12)`. And the three `semilogy` calls at 547-548, 551-552 and 555-556 break their argument list onto a continuation line indented to a flat 8 spaces rather than aligned to the opening parenthesis, so `label=` sits under the middle of the call.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 223, 243, 299, 338, 458, 487, 535. *Example:* {figure} without :name:.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 76, 114, 157, 374. *Example:* the lecture contains no bold at all, and every definition it makes is italicised instead: the *periodogram* at 76 ("the *periodogram* of $X_0,\ldots,X_{n-1}$, which is defined as"), the *Fourier frequencies* at 114, and *pre-filtering*, *pre-whitening* and *recoloring* at 374 - the three names for the steps of the recipe just given at 369-372, and the ones a reader will scan back for. The remaining defined term, "plug-in estimator", is set in double quotes at 157 and 159 rather than in either. Since italic is never used for emphasis anywhere in the file, the fix is a straight substitution of bold at these five sites.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 306, 495, 540. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 243, 338, 458. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 308. *Example:* .set_title.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 309, 310. *Example:* axis label `Weights`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 129, 190, 199. *Example:* the same complex exponential is written two ways, sometimes within one display: 82 and 136-138 use `e^{i t \omega}` / `e^{i t \omega_j}`, while 129 writes both forms side by side (`\sum e^{i t \omega_j} = \sum \exp\left\{ i 2\pi j \frac{t}{n}\right\}`), and 190 and 199 use only the longer `\exp\left\{\cdot\right\}` form. Since $\omega_j := 2\pi j/n$ is defined at 117, the displays at 190 and 199 could carry the shorter `e^{i t \omega_j}` that the reader has already been trained on.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 323, 444. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 365, 436, 331. *Example:* the symbol $I$ is redefined mid-lecture. It is introduced at 81-84 as the periodogram of the raw data $X_0,\ldots,X_{n-1}$, and used that way through 164-169, 274-286 and 385-393; then 436-439 writes "the recoloring step, which constructs an estimate $I$ of $f$ from $I_0$" and sets $I(\omega) = |1/(1-\hat\phi e^{i\omega})|^2 I_0(\omega)$ - a different object, and one that is precisely *not* the periodogram of the data. With $I_S$ already taken at 286 for the smoothed version, the section that most needs distinct names for three estimators reuses the first one. Second, 365 promises "First, we describe the basic idea, and after that we give the code", but no code follows in that section - 444 only links out to GitHub, as 209, 321 and 361 already had. Third, 331 says "the next three figures", 335 says "from the top figure to bottom" and 342-346 refers to "the middle figure" and "the first window length", but 337-340 is a single `{figure}` of three stacked panels, which 455 then calls "the three subfigures".
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 321, 323, 329, 404. *Example:* 2 spaces.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 307. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 376. *Example:* the pre-filtering section (361-395) makes an entirely visual argument in words and never draws it: the claim is that the residual periodogram $I_0$ is flat enough that heavy smoothing costs little bias (384-395), and that recoloring by $|1/(1-\hat\phi e^{i\omega})|^2$ recovers $f$ (436-439). Nothing in the lecture shows $I_0$, so the reader sees the smoothed and AR-smoothed results side by side at 458 without ever seeing the flat intermediate object that makes the trick work - the one plot that would justify the whole section. The Hanning window figure at 299-311 is exactly the right instinct applied one section earlier.


## Strengths

- The algebra from the definition of the periodogram to "$I(\omega_j)$ is just a sample analog of $f(\omega_j)$" is carried out in full and signposted at both ends: 121-123 asks the question and warns it "does involve some algebra", 125-166 does it in five displays, and 168-169 lands it against the expression for $f$ given at 68, with an explicit `{ref}` back to it.
- Every claim that could be taken on faith is instead handed to the reader to check - 99-105 asks them to verify that $I$ on $[0,\pi]$ pins down $I$ on all of $\mathbb R$, and the two exercises at 470-481 and 517-529 ask for the two static figures to be reproduced, with the model, window type, window length and sample size all restated so the exercise is self-contained.
- The `{note}` at 205-207 pre-empts the exact doubt a reader has at 203 - whether `np.abs` on a complex array does the right thing - at the point the expression `np.abs(fft(X))**2 / len(X)` appears rather than in a footnote.
- The Hanning window figure at 299-311 is generated rather than asserted, and 295-297 tells the reader what to look for in it before it is drawn ("smaller weights towards the edges and larger weights in the center"), tying it back to the sum in {eq}`estspec_ws`.
- The three symbols of the pre-whitening argument are defined together as a bulleted list at 424-426 - $g$ the spectral density of the shock, $I_0$ the periodogram of the residuals, $f$ the target - each with a clause saying what role it plays, before the relation {eq}`ar_sdsc` between them is stated.
- The lecture is honest about what it cannot do: 348-350 says that in real problems the true spectral density is invisible and the smoothing choice rests on judgement, immediately after using the visible truth at 342-346 to pick the middle window.

## Recommended actions

1. Rename the recolored estimate at 436-439 - $I$ there collides with the raw periodogram of 81-84 while $I_S$ (286) and $I_0$ (425) are already taken; $\hat f$ or $I_{AR}$ would keep the three estimators distinct in the one section that compares them.
2. Add a figure to the pre-filtering section showing the residual periodogram $I_0$ next to the raw periodogram for the same series, so the flatness that justifies heavy smoothing (384-395) is visible before the recoloring formula at 439.
3. Bold the five definitions currently in italic (76, 114, 374 x3) and the quoted "plug-in estimator" at 157.
4. Either show `ar_periodogram()` inline as 365 promises, or reword 365 and 361 - "we showed three functions" at 361 describes a GitHub link, not anything shown in the lecture.
5. Fix the figure-vs-subfigure language: 331 and 335 call the panels of the single `{figure}` at 337-340 "three figures", 455 calls the same construct "subfigures".
6. Clean the PEP8 items: `## Data` at 488, `figsize=(10,12)` at 540, the continuation indents at 547, 551 and 555, the operator spacing at 301, and rename the comprehension variable at 301 so it does not shadow the sample size `n`.
7. Sweep the figures: give the three static PNGs at 243, 338 and 458 `:name:` targets, add `mystnb: figure: caption/name` metadata to the four code-cell figures (223, 299, 487, 535), lowercase the axis labels at 309-310, move the `set_title` at 308 into a caption, add `lw=2` at 307, and drop the `figsize` overrides at 306, 495 and 540.
