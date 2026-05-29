# `qe-math-013` — Reference equations via `` {eq}`label` ``

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § end](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-013
**Type:** rule  
**Title:** Reference equations via {eq}`label`

**Description:**  
When an equation has a label (via `$$ ... $$ (label)` per `qe-math-007`), references to that equation must use the `` {eq}`label` `` role. Do not use manual numeric references like "equation (3)" or "(eq. above)" or "see (5)".

This rule is the positive counterpart of `qe-math-007` (which bans `\tag{}` for manual numbering). Together they make the auto-numbered / role-referenced workflow complete.

**Check for:**
- Manual references like "(3)", "(eq. 5)", "see equation (2)", "from (4)" appearing in proximity to labelled equations
- `[…](#equation-label)` or other markdown-style anchor references when `{eq}` should be used
- Cross-references that bypass MyST's auto-numbering

**Examples:**
````markdown
<!-- ✅ Correct -->
$$
x^2 + y^2 = r^2
$$ (pythagoras)

Then by {eq}`pythagoras`, ...

The recursion {eq}`bellman` admits a unique solution.

<!-- ❌ Incorrect -->
$$
x^2 + y^2 = r^2
$$ (pythagoras)

Then by equation (1) above, ...

The recursion (3) admits a unique solution.

See equation (eq. pythagoras) for the identity.
````

**Implementation note:**  
Partial-deterministic candidate. Detect numeric references (e.g., `"equation (\d+)"`, `"\(\d+\)"`, `"see (\d+)"`) within a window of labelled equations in the same document. False-positive guard needed: references to other content (page numbers, footnotes) shouldn't be flagged.
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> [Equation numbering example with label]
> 
> which can be referenced using the role
> 
> `and here is the reference to {eq}\`label\``

`qe-math-007` already bans `\tag{}` for manual equation numbering. The complementary positive rule — *use `{eq}`label`` for references* — is not separately encoded today, leaving a gap where authors might still write "see equation (3)" manually.

**Corpus evidence (May 2026 audit):** Moderate. The audit observed manual numeric references in several older lectures alongside labelled equations. One concrete broken reference was found: [`lecture-python.myst/cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) — `` {eq}`eq:Kalman102} `` has mismatched braces.

**Why partial:** Detecting "this looks like a manual numeric ref to an equation" requires proximity / context analysis. Regex flags candidates; an LLM or stricter parser confirms intent.
