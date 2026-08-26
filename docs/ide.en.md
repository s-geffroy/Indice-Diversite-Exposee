# EDI — Exposed Diversity Index

!!! success "Renamed — the name says what is measured"
    The index was first called the "**Entropic Dissipation Index**", after an analogy with quantum
    decoherence. The [audit](limites.en.md) dismantled that analogy transfer by transfer: nothing
    specifically quantum survived. A name pointing to a false analogy announces something other
    than what the instrument measures.

    The French acronym remains **IDE**; in English, **EDI** — *Exposed Diversity Index*: the
    distribution of the attention **actually served** across the viewpoints of a declared
    catalogue.

## Definition

The index is the Shannon entropy of the distribution of **exposed viewpoints**, normalised by its
theoretical maximum:

$$\mathrm{EDI} = \frac{H(q)}{\log_2 k}, \qquad
q_i = \frac{\sum_R w_R \, \mathbb{1}[\text{the item served at rank } R \text{ falls in bin } i]}
{\sum_R w_R}$$

Three choices distinguish it from the entropy one would write spontaneously, and each is the
**consequence of an attack that succeeded**:

| Choice | Why | What happens without it |
|---|---|---|
| $q$ bears on the **items served**, projected onto the reference catalogue's bins — not on the labels announcing them | a label is chosen, an item is observed | the index reaches **1.000 for zero content diversity**, at zero engagement cost → [adversarial test](gaming.en.md) |
| each rank is weighted by the **attention** it receives, $w_R$ | a reader consults the first item far more often than the last | the measure is satisfied by **burying** divergent items: measured at 0.70 without looking at rank, a platform exposes only **0.36** → [adversarial rank](rang-adverse.en.md) |
| the denominator $\log_2 k$ is fixed by a **declared catalogue**, not by what the platform serves | comparing two feeds requires the same unit | a perfectly closed feed shows one modality: the denominator degenerates and the index flatters |

| Value | Reading |
|---|---|
| $\mathrm{EDI} = 1$ | served attention is spread equally over the catalogue's $k$ viewpoints |
| $\mathrm{EDI} \to 0$ | served attention goes to a single viewpoint |

!!! tip "Read as an **effective number of viewpoints**"
    A normalised entropy is not linear in what "twice as diverse" means. Its conversion
    $k^{\mathrm{EDI}}$ is: the number of **equally served** viewpoints producing the same entropy
    (Jost, 2006). On the real feeds measured, $0.50$ over twenty-six sections is **5.1 effective
    sections**. The first figure means nothing without training; the second does.
    → `ide.entropy.effective_viewpoints`

## The attention discount is measured

Using $1/R$ amounts to setting $\eta = 1$ by convention. This repository measured it:

| What was believed | What is measured |
|---|---|
| $\eta = 1$, by convention | $\eta = 0.88 \pm 0.05$ over 143 documents, **by display** rather than by click |
| examination follows a cascade | **refuted** twice on Baidu-ULTR, by a test and by a counter |
| the $R^{-\eta}$ law fits the curve | it is the **worst** of the three fits tried |
| the discount depends on the page served | it does, by **6 %**, which moves the index by $0.0025$ |

→ [measured exposure](exposition-mesuree.en.md) · [the page effect](effet-de-page.en.md)

Severity remains a property of the **surface**, however: about 1.1 on a results page, 0.04 to 0.11
on a three-tile banner. It does not transport from one platform to another, and must therefore be
measured where the index is computed. → [counter-expertise](contre-expertise.en.md)

## What computing it requires

1. **A log that passes the three checks** — does the recorded order carry position information? is
   there enough to estimate severity? does examination depend on what was clicked above?
   → [MIND](mind.en.md) · [served rank](rang-servi.en.md) · [form test](test-de-forme.en.md)
2. **A verifiable rank**, not a declared one. At least one public log supplies an order column that
   is not the served rank, without lying and with nothing signalling it: the exchangeability test
   is what detects it. → [the index measured](indice-mesure.en.md)
3. **A declared viewpoint catalogue**, published in full — it fixes the denominator, and it moves
   the level far more than the feed itself does. → [the catalogue](catalogue.en.md)

## What has been measured, and what has not

!!! success "The rank-blind form is measured on real feeds"
    $0.50$ per user-day over 232,887 feeds of the Danish daily *Ekstra Bladet*, that is **5.1
    effective sections out of 26**. It is the repository's first figure that does not come from a
    simulation — and it is the figure of the form **the adversarial test disqualifies**, for want
    of better on a log recording neither rank nor content. It reads as an **upper bound**.
    → [the index measured](indice-mesure.en.md)

!!! warning "The exposed form is only **bounded**"
    No public log carries both a verifiable rank and an interpretable label. Composition being
    known and order not, the exposed index is not determined but **constrained**: median width
    $0.104$. One can therefore sometimes decide without the rank — never measure.

## The original form, and what it measured

The working thread defined the index over a feed's **labels**, without looking at rank:

$$H_{\text{norm}} = \frac{H(X)}{\log_2 k}$$

That is what `ide.entropy.label_diversity_index` computes, and its name now states its scope. The
form remains useful where rank does not exist — it is what one measures on a log recording only
the served set — but **it does not measure exposure**: it is the form the adversarial test defeats.

## Why normalisation is the essential point

Raw entropy is measured in bits, and its value depends on the number of available modalities. Two
feeds with different catalogues would produce incomparable figures. Normalising by $\log_2 k$ makes
the index **dimensionless and bounded** — which is what allows comparison.

The implementation makes the dependence explicit:

```python
from ide.entropy import label_diversity_index

feed = ["conspiracy"] * 10 + ["factual"] * 10

label_diversity_index(feed)                    # 1.0  — two observed modalities
label_diversity_index(feed, catalogue_size=4)  # 0.5  — four available viewpoints
```

## Limitations

These caveats matter as much as the definition, and the [critical audit](limites.en.md) develops
them.

* **The catalogue decides the level, and this is measured.** The same corpus scores $0.50$ over
  twenty-six sections and $0.92$ over three. The **ordering** between readers holds down to six
  modalities, then collapses. An index level without its catalogue means nothing.
  → [the catalogue](catalogue.en.md)
* **A section is not a viewpoint.** The two labelling axes of the only corpus measured — topical
  and tonal — agree only at $\rho = 0.16$. Exposed diversity is a quantity **per declared axis**.
* **The index remains gameable, and this has been measured.** The original form gives way
  entirely: 1.000 for zero content diversity, without conceding a point of engagement. The
  retained form closes that route and burial with it, but a platform can still serve formally
  divergent, substantially empty items — bin diversity without argument diversity. No automatic
  measure separates the two. → [adversarial test](gaming.en.md)
* **The ceiling depends on volume served.** An entropy cannot exceed the logarithm of the number
  of items served: a reader receiving five caps out at $0.49$ over a twenty-six-viewpoint
  catalogue. The index therefore measures short readings poorly, and that is a property of the
  quantity, not of its measurement.
* **Measuring the index of individual feeds means observing what is served to people.** A measure
  aggregated over a population assumes far less; the repository provides no privacy protocol, and
  no longer proposes one.

---

*Implementation: `ide.entropy` · `ide.radio.rank_weights`*
