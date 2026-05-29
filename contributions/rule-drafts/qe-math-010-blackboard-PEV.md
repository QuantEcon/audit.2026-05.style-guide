# `qe-math-010` — Use `\mathbb{P}`, `\mathbb{E}`, `\mathbb{V}` for probability, expectation, variance

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § Probability, expectation, and variance](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-010
**Type:** rule  
**Title:** Use \mathbb{P}, \mathbb{E}, \mathbb{V} for probability, expectation, variance

**Description:**  
Use blackboard-bold operators with braces for probability, expectation, and variance:
- `\mathbb{P}` for probability
- `\mathbb{E}` for expectation
- `\mathbb{V}` for variance

Subscripts and superscripts attach to the operator: `\mathbb{E}_t`, `\mathbb{E}_{x \sim p}`. Always use **curly braces** around the symbol — never bare `\mathbb E`.

**Check for:**
- Bare `E[`, `E(`, `E_t`, `E_0` for expectation in math environments
- `\mathbb E` (no braces) for expectation
- `\Pr(`, `Pr(`, `\Prob(` for probability
- `\Var(`, `Var(`, `\text{Var}(` for variance
- Use of `\operatorname{E}` / `\operatorname{Var}` instead of the blackboard form

**Examples:**
```markdown
<!-- ✅ Correct -->
$\mathbb{E}[X]$, $\mathbb{E}_t[X_{t+1}]$, $\mathbb{V}[X]$, $\mathbb{P}\{X = 5\}$, $\mathbb{P}(B)$

The conditional expectation $\mathbb{E}_t[\,\cdot\,]$ denotes the expectation given information at time $t$.

<!-- ❌ Incorrect -->
$E[X]$              (bare E)
$E_t[X_{t+1}]$      (bare E)
$\mathbb E_t[X]$    (no braces around E)
$\Pr(B)$            (use \mathbb{P}(B))
$\operatorname{Var}(X)$  (use \mathbb{V}[X])
```

**Note on events vs sets:** when using `\mathbb{P}`, events take braces `\{...\}` and sets take parentheses `(...)`:
- `\mathbb{P}\{X = 5\}` — event
- `\mathbb{P}\{X \leq x\}` — event
- `\mathbb{P}(B)` — set
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> Use `\mathbb{P}` for probability, with braces `\{...\}` for events and parentheses `(...)` for sets […]
> Use `\mathbb{E}` for expectation and `\mathbb{V}` for variance

**Corpus evidence (May 2026 audit):** **~60 lectures** — the single most common math-style violation in the corpus that isn't already a coded rule. Distribution:

- `lecture-python.myst`: 21 / 110
- `lecture-python-advanced.myst`: 17 / 55
- `lecture-dp`: 17 / 50
- `lecture-python-programming`: 5 / 26

Concentrated in expectation-heavy lectures (LQ, Ramsey, IFP, tax-smoothing).

**Why mechanical:** Regex with awareness of math-environment boundaries. The braces-vs-parentheses sub-rule (events vs sets) is judgment-y, so this rule covers the operator form; a separate `qe-math-014` could address the event/set distinction if the team wants finer granularity.
