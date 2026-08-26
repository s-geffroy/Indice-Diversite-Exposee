# Critical audit and limitations

This is the central document of the repository.

The underlying work was built as a discussion thread, in a single day, by accumulating
analogies. That method produces sound intuitions alongside shortcuts that do not hold.
Publishing the thread as-is would expose the whole to being dismissed over a detail,
when the starting intuition deserves better.

Twenty-three points are documented. Each follows the same structure: what the thread claimed, why it is a
problem, and the formulation adopted. Every correction is **traceable** — implemented in
`src/`, verified in `tests/`, illustrated in a notebook.

The final section, [what the model cannot do](#what-the-model-cannot-do), corrects
nothing: it lists the limitations that remain, including those bearing on regulatory use
of the index.

---

## A. Nomenclature

### 1. The index and the algorithm are two distinct objects

**The thread.** The executive summary reads: "we recommend technical regulation imposing
an **Entropic Dissipation Index** (ADE)". The acronym and the name refer to two
different things, and the rest of the thread uses both interchangeably.

**The problem.** This is not a typo. An index is a **metric** — something a regulator
measures and sets a threshold on. An algorithm is a **mechanism** — something a platform
implements. Conflating them makes the regulatory proposal unintelligible: is a
measurement being mandated, or an implementation? The difference is considerable, legally
and technically.

**Adopted.**

| Acronym | Object | Nature | Used by |
|---|---|---|---|
| **IDE / EDI** | Exposed Diversity Index | auditable metric in $[0, 1]$ | the regulator |
| **ADE / EDA** | Exposed Diversity Algorithm | recommender filter | the platform |

The index is measurable without code access: observing the content served is enough. The
algorithm is one way among others of keeping it above a threshold. The memorandum
mandates the former and **does not prescribe** the latter — mandating an implementation
would be both unenforceable and counterproductive.

!!! success "And the name itself was corrected, after the fact"
    Both objects were originally called the *Entropic Dissipation* Index and Algorithm, after
    the quantum decoherence analogy. Section B of this audit dismantles that analogy transfer by
    transfer, and the conclusion is that none of its specifically quantum borrowings survived:
    what holds is classical statistical mechanics.

    Keeping that name would have kept a refuted claim in the instrument's title. The acronym
    **EDI / IDE** is kept — it names the Python package — but it now reads **Exposed Diversity
    Index**, which is exactly what the retained measure computes: the spread of served attention
    across the declared viewpoints. The repository and site address followed, at a price known in
    advance: GitHub does not redirect published pages, and old `Index-Dissipation-Entropique`
    links no longer work. The historical function is now called
    `label_diversity_index`, because it measures the diversity of **labels** and nothing more.

---

## B. Mathematical corrections

### 2. The sign of the regulation coefficient

**The thread.** The score is first written
$S(i,c) = \mathrm{Relevance}(i,c) - \mu \cdot \Delta H(i,c)$, then, a few lines later:
"we configure the algorithm with a positive sign ($+\mu \cdot \Delta H$) to reward
content that maximises entropy".

**The problem.** The two versions do the opposite of one another. With $\Delta H > 0$ for
content that diversifies a feed, the negative version **penalises** diversity: it would
close the very bubble it claims to open. A bad-faith platform could implement the first
version and cite the text.

**Adopted.** $S(i,c) = \mathrm{Relevance}(i,c) + \mu \cdot \Delta H(i,c)$ with
$\mu \ge 0$. The code **refuses** a negative $\mu$ with an explicit exception rather than
silently accepting it.

### 3. The two scales of $N$: the central tension of the work

**The thread.** "Increasing size $N$ acts as an entropy pump." And, pages later, the
Fokker-Planck diffusion term: $B(x) = k_B T (1-x^2) / N$.

**The problem.** These two statements contradict each other, and it is the first thing a
statistical physicist will flag. The $1/N$ factor means that **the larger the population,
the less noisy its macroscopic variable**: this is the law of large numbers. A large
population is not more disordered, it is more predictable.

**Adopted.** Both statements are true, but they are not about the same object.

* **Total configurational** entropy is extensive: it grows as $N$. There really are
  exponentially more ways for a million people to disagree than for ten.
* Fluctuations of the **mean** $x$ decay as $1/N$. The observable quantity — the
  adoption rate of an idea — becomes increasingly stable.

The defensible thesis is therefore not "a large population becomes noisy" but:

> **A large population becomes rigid.** Its size does not agitate it; it deprives it of
> stochastic plasticity. And it is precisely that rigidity which makes organic consensus
> unreachable and polarisation irreversible: a system without noise can no longer leave
> the potential well it has fallen into.

This reformulation is stronger than the original, not weaker: it explains
irreversibility, which the "entropy pump" version did not.

### 4. The drift $A(x) = Jx + H$ cannot produce any phase transition

**The thread.** The social potential is posited as $V(x) = -\frac{J}{2}x^2 - Hx$, giving
$A(x) = Jx + H$ and
$P_{\text{stat}}(x) \propto \exp\!\left(\frac{2N}{k_BT}\left(\frac{J}{2}x^2 + Hx\right)\right)$.

**The problem.** That exponential is **convex**: it is maximal at the extremes
$x = \pm 1$ at any temperature. The model therefore predicts a permanently polarised
society, including at infinite temperature — the opposite of the "scenario A" the thread
describes two paragraphs later. No phase transition exists in this formulation. Moreover
$A(x) = Jx + H$ is unbounded: nothing keeps opinion within $[-1, 1]$.

**Adopted.** The missing term is the **entropy of mixing** — the number of individual
configurations compatible with a mean opinion $x$. Adding it recovers exactly the
Helmholtz free energy the thread invoked without ever writing it:

$$f(x) = \underbrace{-\frac{J}{2}x^2 - Hx}_{E} \; + \; T \underbrace{\left[\frac{1+x}{2}\ln\frac{1+x}{2} + \frac{1-x}{2}\ln\frac{1-x}{2}\right]}_{-S}$$

$$A(x) = -f'(x) = Jx + H - T\,\mathrm{artanh}(x)$$

The entropic restoring term diverges at unanimity, which bounds the dynamics, and yields
a **genuine mean-field critical temperature** $T_c = J$. The thread's formulation is its
linearisation near $x = 0$: not wrong, but incomplete — and incomplete precisely where
the phenomenon it claimed to describe takes place.

### 5. The biased voter-model transition probabilities go negative

**The thread.** $P(x \to x + \tfrac{1}{N}) = x(1-x) + h(1-x)$ and
$P(x \to x - \tfrac{1}{N}) = x(1-x) - hx$.

**The problem.** The second reads $x(1 - x - h)$: it is **negative** as soon as
$h > 1-x$. That is not a probability.

**Adopted.** The two influence channels are **mixed** rather than added — with
probability $h$, the individual listens to the media source instead of a neighbour:

$$P(x \to x + \tfrac{1}{N}) = (1-h)\,x(1-x) + h\,(1-x) \qquad
  P(x \to x - \tfrac{1}{N}) = (1-h)\,x(1-x)$$

This stays non-negative over all $h \in [0,1]$, reduces exactly to the classical voter
model at $h = 0$, and preserves the asymmetric drift that made the original formulation
interesting.

### 6. The sign of the restoring term in the resonance equation

**The thread.** $\ddot{V} + (\lambda - \gamma\alpha)\dot{V} - \omega_0^2 V = \xi(t)$.

**The problem.** The negative sign makes the equilibrium point an **unstable saddle
regardless of the other parameters**. The system would diverge even at zero algorithmic
gain, and the criterion $\gamma\alpha > \lambda$ — the most interesting result in the
whole thread — would lose all content.

**Adopted.** $\ddot{V} + (\lambda - \gamma\alpha\,\sigma(V))\dot{V} + \omega_0^2 V = \xi(t)$.

### 7. An unbounded resonance describes nothing observable

**The thread.** "Visibility no longer oscillates, it explodes exponentially:
$V(t) \propto e^{(\gamma\alpha - \lambda)t}$."

**The problem.** Mathematically exact, physically empty: available attention is finite. A
model predicting infinite visibility allows neither comparing two configurations nor
calibrating a threshold.

**Adopted.** A saturation factor $\sigma(V) = 1/\big(1 + (V/V_{\text{sat}})^2\big)$
progressively switches off amplification as visibility approaches attention capacity. The
system no longer diverges: it settles into a **Van der Pol limit cycle**.

This is a gain in realism, not a convergence trick: what one observes of an established
piece of disinformation is not an explosion but a **recurring topic**.

---

## C. Conceptual requalifications

### 8. Decoherence does not increase the entropy of the global system

**The thread.** "Von Neumann entropy jumped from $0$ to a positive value."

**The problem.** The evolution of a **closed** quantum system is unitary, so its von
Neumann entropy is rigorously constant. What grows is the entropy of the **reduced
subsystem**, obtained by tracing over environmental degrees of freedom. Information is
not destroyed; it is delocalised into system-environment correlations. A physicist
dismisses the analogy in one sentence if this is not stated.

**Adopted.** The precise formulation, plus a related clarification that *strengthens* the
analogy: **a coherent superposition is a pure state with zero entropy**. It is therefore
not the multiplicity of possibilities that produces disorder, but the loss of coherence
between them.

The social counterpart is more accurate this way: a population where everyone keeps
several opinions open is not disordered. Disorder arises from contact with an environment
that fixes positions.

### 9. "Social tunnelling": requalified as a metaphor

**The thread.** Direct switching from one extreme to the other without passing through
moderation is attributed to a "social tunnel effect".

**The problem.** Tunnelling is strictly quantum, with no counterpart in a classical noisy
system. The correct mechanism has a name and a theory: **thermally activated barrier
crossing**, described by Kramers' formula, with rate $\propto e^{-\Delta V / k_B T}$.

**Adopted.** Kramers as the mechanism, tunnelling as an explicitly flagged image. The
difference is not cosmetic: Kramers' law is *testable* and yields a temperature
dependence that tunnelling does not. A seductive image is lost; a prediction is gained.

### 10. $1/k^N$ describes an initial state, not a dynamic

**The thread.** "The probability of spontaneous unanimity collapses as $1/k^N$."

**The problem.** That computation assumes $N$ individuals drawing opinions
**independently** from $k$ options — the probability of unanimity by chance at the initial
instant. But the whole point of the subject is that individuals **interact**, and that
interaction is what produces (or fails to produce) consensus. The figure is correct and
beside the point.

**Adopted.** The statement is kept as a description of the initial state, and the dynamic
question is treated where it has meaning: the voter model's **consensus time**, growing
as $N$ (globalised network) or $N^2$ (local neighbourhood).

### 11. $\tau_D \propto \tau_R / N$ is a heuristic, not a result

**The thread.** Decoherence time is given as inversely proportional to the number of
environmental particles.

**The problem.** Zurek's result involves the spatial separation of the superposition
components and the thermal de Broglie wavelength, not a literal $1/N$. Presented as a
law, the statement is false; presented as an order of magnitude, it is useful.

**Adopted.** Kept, explicitly labelled a **heuristic scaling law**, with a reference to
the exact calculation.

---

## D. Arguments to reformulate

### 12. Global connectivity accelerates consensus, it does not prevent it

**The thread.** "The social network moves from a classical network to an infinitely
coupled small-world network […] making any macroscopic consensus strictly impossible."

**The problem.** This is measurably false. Voter-model consensus time grows as $N^2$ on a
ring, $N \ln N$ in two dimensions, and only $N$ in mean field. A densely connected
network therefore converges **faster** than a geographic neighbourhood. The thread in
fact quotes these laws correctly one page earlier, before drawing the opposite
conclusion.

**Adopted.** Connectivity is not the cause of fragmentation. It amplifies and
accelerates — in whatever direction the field gives it. The real causes are:

1. the **directional bias** $h$ of the algorithmic micro-fields $H_i(t)$;
2. **homophily** — new links connecting already-similar individuals, which compartments
   the graph into internal subgraphs.

The consequence matters for the memorandum: **the useful lever acts on the field, not on
the number of links.** Throttling share reach remains defensible as an emergency measure,
but connectivity as such is not the target.

### 13. Two critical temperatures, two meanings

| Model | $T_c$ | Interaction assumption |
|---|---|---|
| 2D Ising (Onsager, exact) | $2/\ln(1+\sqrt{2}) \approx 2.269\,J$ | four geographic neighbours |
| Mean field (Curie-Weiss) | $J$ | everyone experiences the average opinion of all |

The gap is not an error: mean field overestimates cohesion, hence underestimates the
temperature needed to break it. The comparison has sociological meaning — a globalised
social network is **closer to mean field** than a real neighbourhood, which makes it more
fragile to polarisation, not less.

Onsager's value serves as the **validation test** for the code: it is the only point in
the repository where an exact theoretical prediction, independent of our sociological
assumptions, can confirm the implementation is correct.

---

## E. The software prototype

### 14. Five defects in the thread's code

The `pygame` prototype is preserved verbatim in
`legacy/simulation_thread_2026-08.py` and reimplemented properly in `ide.abm`.

1. **No social temperature.** The heaviest defect, and a silent one: without individual
   agitation, conformity is a purely contracting force. The population collapses onto a
   single point, the index falls to zero whatever the other settings, and the model can
   represent **neither** fluid debate **nor** the thermal-noise injection the paper
   proposes. The central parameter of the entire theory was absent from its only
   implementation.
2. **Contamination by teleportation.** `infecter()` wrote
   `self.opinion.x = 1.0 if self.opinion.x > 0 else -1.0`: the individual was instantly
   placed in a corner of the compass. All subsequent dynamics disappeared, and the
   "polarisation" measured became a mere infection count. Replaced by progressive
   radicalisation.
3. **Infallible fact-checking.** Any infected individual within reach of a fact-checker
   was cured with certainty — an assumption directly contradicted by the belief-hysteresis
   literature invoked elsewhere in the same thread. Efficacy is now probabilistic and
   parameterised.
4. **Absorbing boundaries.** Clamping opinions accumulated agitated individuals on the
   compass edges, where they stayed trapped. The measured index fell at high temperature
   for a purely numerical reason. Boundaries now reflect.
5. **Lost indentation.** In the printed thread, the body of `main()` and the
   `if __name__ == "__main__"` guard lost their indentation: the script does not run as
   printed.

---

## F. A correction that came from measurement

These points were not found by re-reading the thread but by **confronting the data**. They are
appended after the fact, which is how an audit should live. The second corrects not the original
thread but an instrument this repository had itself built.

### 15. The $\gamma\alpha > \lambda$ criterion is not a test, it is a definition

**The thread, and the memorandum that followed from it.** "Prohibit algorithmic
configurations in which a piece of content's amplification rate exceeds its natural damping
rate: $\gamma\alpha > \lambda$."

**The problem, revealed by [calibration](calibration.en.md).** The ratio
$\gamma\alpha/\lambda$ exceeds 1 in all 19 measured attention episodes, under all four
estimators tested. This is not an alarming property of the ecosystem: it is a **tautology of
the estimation procedure**. An observable attention episode necessarily went through a growth
phase, so $r_{\text{up}} > 0$, so $\gamma\alpha > \lambda$.

In other words, the recommendation asked a regulator to check a condition that holds of any
content which broke through. It was **inapplicable**, and nothing in the theoretical
reasoning flagged it.

**Adopted.** A **ceiling on the ratio**, $\gamma\alpha/\lambda \leq \rho_{\max}$. The
regulatory quantity is the margin above the threshold, not the crossing of it. The
measurement supplies a descriptive reference — median 2.5 to 4.2 depending on estimator —
from which a normative $\rho_{\max}$ can be argued.

**What this episode teaches about method.** An error of this kind is invisible to re-reading:
it only becomes apparent when you try to measure. It is the most concrete argument for
empirical calibration — not to confirm the model, but to discover where its recommendations
mean nothing.

### 16. Abundant rank variation is not exploration

**What this repository had built.** Estimating the severity $\eta$ of position bias
([adversarial rank](rang-adverse.en.md)) comes with an identifiability check: it refuses to
answer when no item was served at more than one rank. That check was presented as the guard to
pass before estimating.

**The problem, revealed by measuring [MIND](mind.en.md).** The check counts rank variation
without saying where it comes from. In MIND the recorded order is **shuffled**: variation is
maximal — a median item appears at sixteen distinct positions — and entirely artificial. The
estimator therefore accepts the dataset, declares itself identifiable, and returns a severity
that is merely an increasing function of a nuisance parameter, from $-0.13$ to $+0.25$ depending
on the impression threshold, always with a standard error below 0.007.

**Adopted.** A **within-feed exchangeability test** that precedes estimation: given the feed, are
clicks distributed independently of the recorded position? It is exact — expectation and variance
are known under the null — and it comes with its power calibration, without which a test that
rejects nothing says nothing.

**What this episode teaches about method.** A necessary check invites one to believe it
sufficient. This one was written to catch the visible case — a deterministic platform, producing
no variation at all — and it let through the invisible one, variation both abundant and false. A
check is worth only what it is worth against the case it was not designed to see.


### 17. A digest that assumed instead of verifying

**What this repository had built.** The impression logs measured here weigh 135 MB to 2.2 GB and
cannot be versioned: the repository carries only a **digest**, which a test checks returns the
same figures as the raw log. For MIND, that digest summarised a feed's structure by its
**length**, assuming a feed of length $L$ occupies exactly ranks 1 to $L$.

**The problem, revealed by [Baidu-ULTR](rang-servi.en.md).** The assumption is true of MIND and
false of a search results page, which **skips ranks** — twenty distinct positions for sessions of
at most nineteen documents. The digest then reconstructed ranks that had never been served.

**What makes this defect instructive is that it was painless.** It produced neither error nor
absurd value: $z = -200$ instead of $-206$, a severity of 1.32 instead of 1.49. Figures of the
right order, the right sign, with the right conclusion. Without the systematic comparison against
the raw log, there was nothing to see.

**Adopted.** The digest now **verifies** the structure instead of assuming it, and keeps served
ranks one by one when the assumption fails. A test locks both cases.

**What this episode teaches about method.** A storage optimisation is an assumption about the
data and must be treated as one. What caught it was not a re-reading: it was the rule, laid down
at the previous stage, that a digest must be compared against the raw log at every build.


### 18. Comparing two measures at the same nominal floor

**What this repository published.** [Adversarial rank](rang-adverse.en.md) compared four
diversity measures **at the same 0.70 floor** and concluded that "target proximity" resisted
burial best. The conclusion was carried into the memorandum and the landing page.

**The problem.** The four measures do not live on the same scale. A 0.70 floor on target
proximity does not demand the diversity a 0.70 floor on entropy demands: at that level the former
exposes only 0.43 of entropy, the latter 0.70. Comparing their costs at equal floor compares a
demanding standard with a lax one.

**Adopted.** The comparison is made at **equal actually exposed diversity**. It yields identical
costs, within 0.6 % of the exact bound: the choice of measure barely matters; it is the **level**
and **rank-awareness** that make the standard.

**What this episode teaches about method.** The repository already had the right method and had
not applied it to its own measures: the [baselines](lignes-de-base.en.md) comparison fixes the
floor precisely to make competitors comparable. A method acquired in one chapter does not
transport itself into the others.

### 19. A conventional attention discount passed off as universal

**What this repository published.** "A platform certified at 0.70 exposes only 0.36", with no
mention of the discount used — $1/R$, i.e. an attention severity of 1.

**The problem.** That same repository measured severity to be a property of the **surface**: 1.10
on a results page, 0.04 to 0.11 on a three-thumbnail banner. Recomputed at severity 0.1, the feed
"certified at 0.70" exposes **0.747**: burial disappears. At severity 2 it exposes 0.157 and the
loophole costs only 2.7 %.

**Adopted.** The discount must be **measured on the surface** and published with the result. The
price of the rank-aware standard is stable — 20.8 to 24.1 % — which is the only thing the
convention allowed one to say safely.

**What this episode teaches about method.** An evaluation convention borrowed from another field
— here the reciprocal-rank discount — enters a result as an assumption, even when never stated.
The repository had measured the quantity that replaces it **before** publishing the result that
depended on it.


### 20. An assumed examination shape, never tested

**What this repository publishes.** A position-bias severity, $\hat\eta = 1.10 \pm 0.09$ on
Baidu-ULTR, estimated under the model $P(\text{click} \mid i, R) = g(i)\,R^{-\eta}$.

**The problem.** The repository built a test saying whether a log's order carries information —
the [exchangeability test](mind.en.md) — and never built one saying **in what form**. Yet under a
**cascade** model, where the reader stops on finding what they wanted, attention decay is
**geometric** rather than polynomial. The fitted law then overstates real exposure by a factor of
**40 to 4,110** at rank twelve — and the fit looks excellent, with a standard error of 0.04.

**What is confirmed along the way.** The exchangeability test itself **holds**: it rejects under
cascade between $z = -208$ and $z = -241$, more strongly than on real data. Precisely because it
assumes nothing — it tests only independence.

**Adopted.** Severity must be published **with its assumed shape**, and that shape remains to be
tested. It is the open lead of the [blind spots page](angles-morts.en.md).

**What this episode teaches about method.** An instrument that assumes nothing survives a change
of model; an instrument that assumes a shape survives only as long as that shape holds. The
repository had both and had tested only the first.


### 21. Restricting to multi-click feeds, and manufacturing one's own answer

**What I was about to publish.** The [form test](test-de-forme.en.md) cannot separate a cascade
from a simple **click budget** — a reader who stops clicking once served. The natural idea was to
restrict the log to **multi-click** sessions, where a budget of one is excluded by construction.
Applied to Baidu-ULTR, the restriction gives $z = -8.2$ ($p = 2 \times 10^{-16}$): a clear
cascade signature on real data.

**The problem.** A feed's click count is a **collider** of its individual clicks. Conditioning on
it induces negative dependence between them — Berkson's paradox — and therefore manufactures
exactly the signature the test seeks. On a log simulated under a **pure** position model, with
neither cascade nor budget, the restriction moves the deviation from $+0.74$ to $\mathbf{-45.7}$.

**What the restriction measured** was therefore not a property of the log but the selection I had
just performed.

**Adopted.** The restriction is proscribed, and the warning sits in the function's documentation —
where someone will have the idea of doing it again.

**What this episode teaches about method.** This is the third time a seemingly reasonable protocol
manufactures its own result, and the third time a check on **simulated data** catches it before
publication. The rule deserves writing down: *any protocol applied to real data must first be
applied to data whose answer is known.*


### 22. Estimating an exposure that could be measured

**What this repository did for six chapters.** Estimate exposure severity **through clicks**,
under the model $P(\text{click} \mid i, R) = g(i)\,R^{-\eta}$, and publish
$\hat\eta = 1.10 \pm 0.09$ on Baidu-ULTR.

**The problem.** Baidu-ULTR publishes a `displayed_time` column the repository had never read. It
measures directly what was **displayed**, hence exposure itself. Measured that way, severity is
$0.882 \pm 0.046$ over **143** documents, against 55 for the click-based estimate: the estimate
**overstates decay by 23 %**.

The gap is not imprecision but an **identified confounder**: a click is the product of examination
and attractiveness, and since attractiveness also declines with rank, the severity fitted on clicks
absorbs both.

**What the measurement settled besides.** The [form test](test-de-forme.en.md)'s impasse — cascade
indistinguishable from a click budget — falls immediately: on examination, discrimination is total
($z = -158$ to $-412$ against $-1.03$), and **cascade is refuted** on Baidu-ULTR. The power law
turns out to be the **worst** of three fits on the measured curve: $R^2 = 0.72$ against $0.96$ and
$0.99$.

**Adopted.** Exposure is **measured** when the data exists, and the [access
request](article-40.en.md) now asks for a `displays` column — which removes at a stroke the need to
estimate $\eta$, the shape assumption, and the attractiveness confounder.

**What this episode teaches about method.** The repository built three successive checks, a
fixed-effects estimator, a power calibration and an identification limit — all to approximate a
quantity that was **in a column of the file**. Before refining an estimate, read the data schema.


### 23. A mechanical explanation put forward without testing it

**What I wrote.** The examination curve measured on Baidu-ULTR does not follow a power law: it
holds through rank two, drops, then flattens. I saw in it "the signature of a **screen
threshold**", and added that the `serp_height` column "encodes exactly the page height, hence the
rank at which that threshold falls".

**The problem.** That was a mechanical hypothesis, plausible, and **untested** — when the very
column invoked allowed it to be tested. On verification, **rank** explains better than cumulative
height above (McFadden $R^2$ $0.082$ against $0.057$), and pixels add only $0.0007$ once rank is
known. At equal rank, the pixel effect survives only at the first two ranks then dies out — the
opposite of what a screen threshold would predict.

**What remains true.** The **finding** holds: the measured curve is not a power law, and a
two-regime model fits it better. Only the explanation falls.

**What measurement suggests instead.** The decay would come from **content** rather than place: a
rich format above removes 8.4 points of examination from what follows, at equal rank and
comparable height ([format and return](format-et-retour.en.md)). That is a satisfaction effect,
not a geometric one.

**What this episode teaches about method.** A mechanical explanation takes one sentence to state
and an hour to test; the gap between the two is exactly where a false claim settles in. The
repository's rule — publish nothing unmeasured — applies to explanations too, not only to figures.

### 24. An effect measured without holding the item fixed

**What I wrote.** A rich format served higher up removes 8.4 points of examination from what
follows, at equal rank **and** comparable page height — 21 strata, all of the same sign. From it
I concluded that the attention discount $w_R$ "is not a property of rank, nor even of the
surface: it is a property of the **page served**", and that "no law $e(R)$ can represent it".

**The problem.** The strata held rank and pixels fixed, but **not the item**. An answer box does
not appear at random: it answers a factual question, which does not invite the same reading as an
exploratory search. The comparison therefore ran across two populations of queries, and the gap
could come from the format or from what the format appears on.

**What the matched measurement returns.** With the item held fixed — same document, same rank,
served once with a rich format above and once without — the risk ratio goes from $0.82$ to
$0.940$ (95 % CI $[0.916, 0.964]$). A second matching, by **query**, independent of the first,
returns $0.942$. **Two thirds of the published effect were composition.**

**What makes the episode sharp.** A simulation where the format has *no* effect, but where
enriched pages land on less-consulted items, returns $0.785$ when stratified on rank — roughly
the figure this repository had published. The protocol, applied to data whose answer is known,
manufactures the result it was supposed to measure.

**What remains true.** The residual effect is **established** by the most populated matching, and
its bearing on the index can be quantified: $0.0025$, against $0.0350$ for the $1/R$ convention
the original conclusion was meant to disqualify. **Fourteen times less.** The rank law therefore
holds, and the `format` column of the [access request](article-40.en.md) goes from necessary to
useful.

**What this episode teaches about method.** This is the **fourth** time a reasonable protocol has
manufactured its own result, and the first time it happened in a chapter that already applied the
simulated-control rule — but to a different question. The control had been placed on geometry,
not on composition. A control protects only against what it controls.

### 25. An absence stated as a fact, without having looked

**What I wrote.** Six chapters repeat the same sentence: "no public dataset carries both the
served rank and an interpretable viewpoint label". It justifies the
[access request](article-40.en.md), concludes [MIND](mind.en.md) and
[served rank](rang-servi.en.md), and stands as a permanent caveat on the [index](ide.en.md).

**The problem.** Three datasets had been examined — MIND, Baidu-ULTR, the Open Bandit Dataset —
and the sentence was written as though it ranged over **all** of them. It is a claim of absence,
and a claim of absence cannot be established by measurement: it is established by a search, and
no search had been made. The fourth dataset looked at carries both columns.

**What the fourth dataset gives.** EB-NeRD (*Ekstra Bladet*, RecSys Challenge 2024) gives the
served list and a declared section for every article. The repository's first check then says its
**recorded order does not contain the rank**: $z = +1.05$, $p = 0.29$ over 232,887 feeds, and the
log would have detected a severity of $0.0066$ — one hundred and thirty-four times smaller than
the one measured on Baidu-ULTR. This is not a power failure.

**What the correction buys.** The practical conclusion survives — the exposed index is not
measurable on public data — but its reason changes, and the new reason is more useful: a platform
can deliver an order column that is not the rank, without lying and with nothing signalling it.
The Article 40 request now asks for a **verifiable** rank, and the exchangeability test becomes
an **admissibility clause** rather than a methodological preliminary. In passing, the rank-blind
index finally gets a real figure: $0.47$ per user-day, $4.6$ effective sections out of $26$.

**What this episode teaches about method.** The repository has a rule — publish nothing you have
not measured — and it does not cover this case: an absence cannot be measured. Its twin was
missing: **a claim of absence must publish the extent of the search behind it.** "No public
dataset" should have read "none of the three datasets examined", and the gap between those two
phrasings is exactly what let the error live for six chapters.

---

## What the model cannot do

These are not pending corrections. They are the boundaries of the work, and they should
be stated by its author rather than by its reviewers.

### An analogy is not an explanation

Nothing in this repository demonstrates that human opinion *obeys* statistical
mechanics. The work establishes that a formalism borrowed from physics **reproduces**
certain observed behaviours — abrupt transition, persistence after retraction, selective
amplification. It is a structural hypothesis, fruitful because it yields measurable
quantities. It is not a law of social nature.

Exactly one of its parameters is now calibrated on real data: the ratio
$\gamma\alpha/\lambda$ ([calibration](calibration.en.md)). And that calibration, far from
reinforcing the model, showed that one of its regulatory recommendations was meaningless
(point 15) and that one of its mechanisms is not data-supported. **$J$, $T$, $\gamma$ and
$\alpha$ taken separately still have no estimation procedure**: the formalism is coherent,
its empirical grounding has barely begun. This remains the work's principal weakness. See the
[roadmap](feuille-de-route.en.md).

!!! tip "The hypothesis is now stated in a form that can fail"
    This caveat stood untouched from day one, and it was an admission: the hypothesis had never
    been stated so that it could be lost. It is now — a **fluctuation–response** constraint,
    three invariances, and the list, written in advance, of what the repository would have to
    withdraw if the test failed.
    → [the underlying hypothesis, refutable](hypothese-testable.en.md)


### The starting analogy is refuted — and that is a result

This deserves stating more plainly than "an analogy is not an explanation". The claims
**proper to** the quantum analogy were checked one by one, and none held:

| What the analogy claimed | Verdict |
|---|---|
| the larger the system, the more disordered | **false, and backwards** — not "more ordered" but **more rigid**: fluctuations of the macroscopic variable shrink as $1/N$, while the dispersion of individual opinions is left unsaid (point 3) |
| decoherence increases entropy | **false** — global evolution stays unitary; it is the reduced subsystem whose entropy grows (point 8) |
| $\tau_D \propto \tau_R/N$ | heuristic, not Zurek's result (point 11) |
| social tunnelling | **metaphor** — the correct analogue is activated barrier crossing (point 9) |
| $1/k^N$ measures the improbability of consensus | describes an **initial state**, not a dynamics (point 10) |

What survives — free-energy landscape, phase transition, hysteresis, Kramers' law — belongs to
**classical statistical mechanics**, in the Ising and sociophysics lineage. Nothing specifically
quantum came through.

The analogy therefore worked as **scaffolding**: it suggested measurable quantities that outlive
it — an exposed diversity index, an exposure severity, an amplification threshold. That is a
real role, and it is not the same as being true. The instrument's name was corrected accordingly
(point 1).

### Individuals are not spins

* **Intentionality.** A person can adopt a contrarian, ironic or strategic stance. A spin
  has no intentions, and a spin model cannot represent someone feigning agreement.
* **Multidimensionality.** The agent model uses two continuous axes rather than a binary
  spin, which mitigates the problem without solving it.
* **Dynamic networks.** People cut ties, switch platforms, reorganise. Topology here is
  fixed, except through the bubble threshold.
* **The environment is not passive.** A thermal bath pursues no objective. A recommender
  algorithm does — it optimises a cost function, which makes it a strategic actor rather
  than an environment. This is where the physical analogy is weakest, and it is also what
  makes the algorithm conceivable: a cost function can be changed, a physical law cannot.

### Limitations specific to the index as a regulatory instrument

These reservations matter at least as much as the mathematical corrections, because they
bear on what the memorandum asks of a legislator.

* **Discretisation into viewpoints is a political choice.** Whoever defines the
  modalities defines the index. Partitioning opinion space into 4, 40 or 400 categories
  changes the measured value, and that partition is not a neutral technical act.
* **The index is gameable.** A platform required to keep the index above a threshold can
  do so by serving formally divergent but substantively empty content — label diversity
  without argument diversity. Any mandated metric becomes a target; this one is no
  exception, and the memorandum should be read as a proposal to harden, not a
  ready-to-use mechanism.
* **A floor on the index is a constraint on what people see.** It is defensible — but it
  is a constraint, and presenting it as a mere technical measure would be dishonest. The
  thread writes that "regulation ceases to be arbitrary censorship and becomes an
  engineering of stability". The phrase is elegant and should be treated with suspicion:
  an engineering of stability *is* an intervention in public debate. It must be justified
  as such, with corresponding democratic safeguards, not naturalised by thermodynamic
  vocabulary.
* **Privacy.** Measuring the index of individual feeds requires observing what is served
  to individuals. A credible audit protocol must be aggregative and differentially
  private — this repository now proposes one, and publishes its price: noise is nearly free on
  the regulated quantity, ruinous on the severity it depends on, and the real cost is the
  **contribution bound**, which overstates non-compliance by 0.6 to 2.5 points.
  → [what privacy costs](vie-privee.en.md)

### What the simulations do not show

The notebooks explore parameter regimes chosen for legibility. No systematic sensitivity
study has been carried out, system sizes are modest (24×24 lattices, populations of a few
hundred), and no result is compared against real data. The conclusions are
**qualitative**: they concern the existence of regimes and the direction of dependencies,
never transposable numerical values.


### What twenty-five corrections teach, taken together

The corrections above were recorded one by one, in the order they occurred. Taken together, they
trace three regularities worth more than their sum.

**The errors that survive longest are those producing plausible figures.** None ever produced an
absurd value. The digest that assumed feed structure returned $z = -200$ instead of $-206$; the
restriction to multi-click feeds returned $-8.2$ instead of nothing; fitting a power law to a
cascade returned $\hat\eta = 0.5$ with a standard error of $0.04$. A figure of the right order,
the right sign, with the right conclusion — exactly what no re-reading catches.

**What caught them was never re-reading, it was confrontation.** With data whose answer is known,
with a ground truth, with another estimation method, or with the field's literature. Five of the
twenty-five corrections come from the initial reading of the thread; the other twenty come from
having measured — or, for the last one, from having looked.

**And half bear on the repository's own proposals, not on its starting point.** An instrument
built to check other people's claims must be turned against one's own, and here it is turned that
way more often than it was against the original thread. That is the only defence against the bias
of testing rigorously what one believes false and superficially what one believes true.

**What these three regularities do not prove.** They were briefly promoted to the repository's
conclusion, under the heading "the method is the real result". That was an overclaim, and it is
withdrawn, for three reasons.

* The rules drawn from them — measure rather than estimate, test a protocol on data whose answer
  is known, test an explanation like a figure — are **banal**. Nobody disputes them, they are not
  being stated here for the first time, and no reviewer will receive them as a result.
* The demonstration is **circular**. The argument was "the method is worth something because it
  caught twenty-five errors"; but the same work produced those errors. A method assessed on its
  own faults is compared against a baseline it manufactured. With no error, there is nothing to
  catch and the claimed value drops to zero.
* Nothing has been **validated from the outside**. The 623 tests check that the code does what is
  claimed, not that what is claimed is true, and no reviewer has been through it
  ([call for review](relecture.md)).

What carries over from a repository is its **objects**: an exact exchangeability test, a
six-column aggregate specification, a measured attention exponent, ten negative results. Each
applies to other people's data and answers on its own. A precept does not: it asks to be believed.
What remains of the three regularities is a quantified warning, and its place is here, in an
audit, not in a conclusion: a forewarned piece of work broke all three rules **while knowing
them**, and the cost of each breach is recorded above, episode by episode.
