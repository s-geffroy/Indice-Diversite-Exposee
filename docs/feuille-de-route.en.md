# Roadmap

This repository now measures one thing only: the diversity a feed actually exposes. What follows
is what is missing for that measurement to be complete, in the order in which it blocks.

## 1. A log carrying a verifiable rank **and** a label

This is the only real lock, and it is not methodological.

Four public logs have been examined. None allows the **exposed** index to be computed:

| Log | Served rank | Label | Verdict |
|---|---|---|---|
| MIND | no — the order says nothing ($z = +0.12$) | editorial categories | served set, not ordered feed |
| Baidu-ULTR | yes ($z = -206$) | none | exposure measurable there, the index not |
| Open Bandit Dataset | yes, with propensities | anonymised attributes | ground truth, not viewpoints |
| EB-NeRD | **the column exists and does not contain the rank** ($z = +1.05$) | declared sections | the blind index measurable, the exposed one bounded |

What would be needed: an impression log carrying, per row, the **served rank** — whose
informativeness can be tested — and a **viewpoint label** from a declared catalogue. Without it,
the exposed index will stay bounded and never measured.

## 2. External validation

Twenty-seven corrections, 256 tests, and **nobody outside has read this work**. The tests check
that the code does what is claimed, not that what is claimed is true. This is the one lock the
repository cannot open by itself, and it will not open by writing one more chapter.
→ [call for review](relecture.md)

## 3. Two caveats calling for a measurement, not an argument

**A section is not a viewpoint.** The two labelling axes of the only corpus measured agree at only
$\rho = 0.16$. Knowing what the index really measures would take a corpus **annotated in
viewpoints** — by humans, over an explicit catalogue — not by topical section.

**Attention severity does not transport from one platform to another.** It was measured on a
search engine; nothing guarantees its value elsewhere, and the page-effect chapter establishes
portability only from one *page* to another.

## 4. What was removed, and will not return

Three halves have left this repository: the **analogy** with quantum decoherence, refuted transfer
by transfer; the statistical-mechanics **formalism** it had prompted, whose only own prediction was
measured four times with no effect; and the **regulatory** apparatus — algorithm, floor, access
request — hollowed out by its own measurements.

The [audit](limites.en.md) keeps the entire record of their corrections. There is no plan to
reinstate them: this repository measures, it does not prescribe.

---

*[Critical audit](limites.en.md) · [Index](ide.en.md) · [call for review](relecture.md)*
