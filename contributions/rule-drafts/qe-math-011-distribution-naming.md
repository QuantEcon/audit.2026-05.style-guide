# `qe-math-011` — Plain letters for distribution names

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § Distribution names](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-011
**Type:** rule  
**Title:** Plain letters for distribution names; \mathrm{...} for multi-letter

**Description:**  
Use plain letters for named distributions — not `\mathcal`, `\mathbb`, or other decorative fonts. For multi-letter distribution names use `\mathrm`:

- Normal: `N(\mu, \sigma^2)` — not `\mathcal{N}` or `{\cal N}` or `\mathbb{N}`
- Uniform: `U(a, b)` — not `\mathcal{U}`
- Beta: `\mathrm{Beta}(\alpha, \beta)` — not `\text{Beta}`, `\operatorname{Beta}`, or `Beta`
- Bernoulli: `\mathrm{Bernoulli}(p)`
- Multinomial: `\mathrm{Multinomial}(n, p)`

**Check for:**
- `\mathcal{N}` for the normal distribution
- `{\cal N}` (plain TeX form)
- `\mathbb{N}` for the normal distribution (also wrong because $\mathbb{N}$ means natural numbers)
- `\text{Beta}`, `\operatorname{Beta}`, `\mathrm{ Beta}` (loose spacing) for multi-letter distributions

**Examples:**
```markdown
<!-- ✅ Correct -->
$X \sim N(\mu, \sigma^2)$
$\theta \sim \mathrm{Beta}(\alpha, \beta)$
$Y \sim U(0, 1)$
$Z \sim \mathrm{Bernoulli}(p)$

<!-- ❌ Incorrect -->
$X \sim \mathcal{N}(\mu, \sigma^2)$
$X \sim {\cal N}(0, I)$
$\theta \sim \text{Beta}(\alpha, \beta)$
$Z \sim \operatorname{Bernoulli}(p)$
```

**Implementation note:**  
Regex patterns:
- `\\mathcal\{N\}` — flag for distribution context (sim N, ~ N)
- `\{\\cal N\}` — flag for distribution context
- `\\text\{[A-Z][a-z]+\}|\\operatorname\{[A-Z][a-z]+\}` near `\sim` — flag

False-positive guard: `\mathcal{N}` may legitimately denote a set (e.g., natural numbers in some texts) — context matters. Look for distribution context: `\sim`, `\mid`, conditional notation.
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> Use plain letters for named distributions — not `\mathcal` or `\mathbb`. For multi-letter distribution names use `\mathrm`:
> 
> `$X \sim N(\mu, \sigma^2)$, $\theta \sim \mathrm{Beta}(\alpha, \beta)$`

**Corpus evidence (May 2026 audit):** ~30 lectures. Distribution:

- `lecture-python-advanced.myst`: 14 / 55
- `lecture-dp`: 9 / 50
- `lecture-python.myst`: 6 / 110

Affected files include `affine_risk_prices`, `merging_of_opinions`, `likelihood_var`, `measurement_models`, `ross_recovery`, `wald_friedman`, `smoothing`, `markov_jump_lq`, `tax_smoothing_*`.

**Why mechanical:** The `\mathcal{N}` → `N` case is unambiguous in distribution context (preceded by `\sim`). Multi-letter forms have known token patterns. Phase 4.3 candidate.
