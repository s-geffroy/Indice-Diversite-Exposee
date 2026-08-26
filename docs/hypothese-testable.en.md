# The underlying hypothesis, in refutable form

!!! warning "This chapter measures nothing"
    Everything else in this repository publishes measurements. This one publishes a
    **protocol**: what the underlying question lacked was a form in which it could be lost. It is
    written to be run by others, and to say in advance what would refute it.

The [audit](limites.en.md) ends on a caveat untouched since day one:

> Nothing demonstrates that human opinion **obeys** statistical mechanics.

That was not a prudent conclusion, it was an admission: the hypothesis had never been stated in a
form that could fail. Here is that form.

## 1. What the hypothesis is not

It is not "opinions resemble spins". A resemblance cannot be refuted.

Nor is it "an Ising model fits the data". A two-parameter model fits almost any bimodal
distribution, and a good fit says nothing about the underlying mechanics — the very error this
repository made four times on other subjects.

What separates statistical mechanics from a thermodynamic metaphor is a **consistency
constraint** between two quantities measurable separately: what a system does **on its own**, and
what it does **when pushed**.

## 2. The decisive statement — fluctuation and response

For an equilibrium system described by a free energy and a temperature $T$, the spontaneous
variance of the order parameter and the response to an external field are not independent:

$$\chi = \frac{N \, \mathrm{Var}(\bar{x})}{T}, \qquad
\chi \equiv \frac{\partial \langle \bar{x} \rangle}{\partial h}$$

where $\bar{x}$ is the mean opinion of a group of $N$ people and $h$ an exogenous field — an
exposure intervention of known intensity.

Both sides are measured **separately**: $\mathrm{Var}(\bar{x})$ by doing nothing, $\chi$ by
intervening. Their ratio defines an estimated temperature:

$$\hat{T} = \frac{N \, \mathrm{Var}(\bar{x})}{\chi}$$

!!! danger "The testable hypothesis, in one sentence"
    **One and the same number $\hat{T}$ governs both a group's spontaneous variability and its
    response to a push** — the same across group sizes, intervention intensities, and groups of
    equal exposure diversity.

The refutable content is not the *value* of $\hat{T}$: the field $h$ is defined only up to a
scale, so $\hat{T}$ is too. The refutable content is its **invariance**.

### The three invariances, and what kills them

| Predicted invariance | Statistic | Refutation |
|---|---|---|
| $\hat{T}$ does not depend on $N$ | regression of $\log \hat{T}$ on $\log N$ | significantly non-zero slope |
| $\hat{T}$ does not depend on intensity $h$ | $\hat{T}$ estimated at $h$ and $2h$ | discrepancy beyond a factor of 2 |
| $\hat{T}$ increases with measured exposure diversity | regression of $\hat{T}$ on the index | zero or negative slope |

**If the first or the second fails, the system is not at equilibrium and the free energy has no
referent.** All the vocabulary of landscapes, wells and barriers becomes decorative, and the
first half of this repository must be withdrawn.

**If the third fails**, "social temperature" is not what the repository says it is — it may
exist, but exposure is not its measure.

## 3. What this settles about size

The question "the larger the system, the more ordered the opinions?" dissolves here, and it is a
good example of what the protocol gains over intuition. Two distinct quantities, two distinct
predictions:

| Quantity | What statistical mechanics predicts |
|---|---|
| fluctuation of the group **mean**, $\mathrm{Var}(\bar{x})$ | shrinks as $1/N$ — the group becomes **rigid** |
| dispersion of **individual** opinions, $\sigma_{\text{ind}}$ | **no prediction** — it may stay constant |

A large population is therefore not "more ordered": it can be exactly as divided, but its
division stops moving. What grows with size is **the stability of disagreement**, not agreement.
And this is testable: $\alpha$ in $\mathrm{Var}(\bar{x}) \propto N^{-\alpha}$ equals $1$ in mean
field. A significantly smaller value would say individuals do not fluctuate independently — which
is likely on a platform where everyone sees the same content, and would be a result in itself.

## 4. Three corollaries, if the decisive test passes

They hold only in this order: each assumes the previous one held.

**Barrier crossing (Kramers).** The individual switching rate between two poles follows
$\ln r = a - \Delta E / T$, with $\Delta E$ read off the observed distribution
($\Delta E = -\log p(x)$ at the saddle). *Refutation:* no linear relation between $\ln r$ and
$1/T$, or a slope of the wrong sign.

**Hysteresis with temperature-dependent loop area.** Apply $h$, then reverse it: the loop area is
strictly positive below $T_c$ and zero above. *Refutation:* no loop, or an area independent of
exposure diversity. This is the most specific prediction of the set — few non-physical opinion
models predict a **closed loop of decreasing area**.

**Critical slowing down.** The return time to equilibrium after a shock diverges as exposure
diversity approaches $T_c$ from above. The early-warning-signal literature (ecology, climate)
supplies the estimator and the protocol. *Refutation:* constant relaxation time.

## 5. What running it requires

Four things, none of them in any public log — including the four this repository examined, which
measure **no opinion at all**:

1. a **panel** with repeated measurement of individual attitude on a continuous scale;
2. **groups of varied size** drawn from the same population;
3. a **randomised, calibrated exposure intervention**, applied and then reversed;
4. **measured exposure diversity** per participant — that is, the index, which requires the
   verifiable served rank → [Article 40 request](article-40.en.md).

Points 1 to 3 belong to an experimental protocol that platform–researcher collaborations have
already run for other quantities. Point 4 is what this repository can specify and cannot obtain.

## 6. What this repository would lose

It must be said before, not after.

| If the decisive test fails | Consequence |
|---|---|
| free energy, landscape, wells, barriers | **withdrawn** — vocabulary without referent |
| social hysteresis, counter-field, annealing | **withdrawn** — the mechanics grounding them does not exist |
| social temperature | **withdrawn** as a quantity, kept as an explicit metaphor |
| the three log checks, measured severity, the index bounds, the access request | **untouched** — they never depended on it |

That partition is what counts: the metrological half of the repository is **independent** of the
answer. This protocol does not decide whether the exposed-diversity measurement is valid; it
decides whether the theory that made it worth looking for deserved to exist.

---

*[Critical audit](limites.en.md) · [Fokker-Planck](theorie/fokker-planck.md) ·
[Index](ide.en.md) · [Article 40 request](article-40.en.md)*
