# `qe-math-015` — Lowercase for densities/PMFs, uppercase for CDFs

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § Density and mass functions](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

> ⚠️ **Weaker-evidence proposal.** Documented in the style guide but with limited corpus evidence. The team may prefer to defer this until a future audit confirms it as a real source of inconsistency.

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-015
**Type:** style  
**Title:** Lowercase for densities/PMFs, uppercase for CDFs

**Description:**  
Use lowercase letters (e.g., `f`, `g`, `p`) for probability density functions and probability mass functions. Use uppercase letters (e.g., `F`, `G`) for cumulative distribution functions.

**Check for:**
- Uppercase letter used as a density (e.g., `P(x)` for a PMF — should be `p(x)`)
- Lowercase letter used as a CDF (e.g., `f(x) = \mathbb{P}\{X \leq x\}` — should be `F(x)`)

**Guidance:**  
This requires understanding which function is being referenced — judgment, not pattern matching. Look at the surrounding definition or context to determine the intended function.

**Examples:**
```markdown
<!-- ✅ Correct -->
Let $f$ denote the density of $X$, so $\mathbb{P}\{X \in A\} = \int_A f(x)\,dx$.

Let $F$ denote the CDF of $X$, i.e., $F(x) = \mathbb{P}\{X \leq x\}$.

The PMF $p(k) = \mathbb{P}\{X = k\}$.

<!-- ❌ Incorrect -->
Let $P$ denote the density of $X$, so $\mathbb{P}\{X \in A\} = \int_A P(x)\,dx$.   (uppercase for density)

Let $f$ denote the CDF of $X$, i.e., $f(x) = \mathbb{P}\{X \leq x\}$.   (lowercase for CDF)
```
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> Use lowercase letters (e.g., $f$, $g$, $p$) for density and mass functions, uppercase for CDFs:
> 
> `$f(x)$ for the density, $F(x)$ for the CDF`

**Corpus evidence (May 2026 audit):** Limited. The rule was identified during the audit (under provisional ID `qe-math-A4`) but few clean violations were tallied. Inconsistency exists but it's a small fraction of the corpus.

**Recommendation:**

1. **Defer** — wait until evidence of systemic deviation accumulates.
2. **Document only** — add to the rules file but don't enforce; useful as a reference for future contributors.
3. **Add as `style` type** — flag for human review when an obvious violation is spotted, no auto-fix.

**Why judgment:** Determining whether `P(x)` means a density or a CDF requires reading the surrounding text and definitions. Not a Phase 4.3 candidate.
