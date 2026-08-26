"""Indice de Diversité Exposée — mesurer la diversité qu'un fil expose réellement.

Ce paquet ne contient qu'une chose : l'**IDE**, l'entropie des contenus servis sur un catalogue
de points de vue déclaré, **pondérée par l'attention que reçoit chaque rang** — et tout ce qu'il
faut pour l'établir, l'attaquer et le mesurer sur des journaux réels.

Trois familles de modules, et rien d'autre :

* **l'indice** — :mod:`ide.entropy` en porte la définition, ses bornes lorsque l'ordre servi est
  inconnu, et le regroupement de catalogue ; :mod:`ide.radio` la remise d'attention ;
  :mod:`ide.gaming` et :mod:`ide.ranking` les attaques auxquelles il a dû survivre ;
* **les journaux** — :mod:`ide.logs` fournit la représentation commune, les trois contrôles de
  recevabilité (échangeabilité, identifiabilité, forme) et le condensé versionnable ;
  :mod:`ide.mind`, :mod:`ide.exposure` et :mod:`ide.ebnerd` lisent les quatre journaux publics
  examinés ;
* **l'exposition** — :mod:`ide.offpolicy` estime la sévérité de l'attention et confronte les
  estimateurs contrefactuels à une vérité terrain.

Les modules réexportés ici sont purs — aucune entrée-sortie — et prennent une graine explicite
lorsqu'ils sont stochastiques. Les modules qui touchent au disque ou au réseau
(:mod:`ide.mind`, :mod:`ide.exposure`, :mod:`ide.ebnerd`) et :mod:`ide.plotting`, qui dépend de
``matplotlib``, ne le sont pas : les importer ici mêlerait les entrées-sorties au noyau.

.. note::
    Le dépôt a longtemps porté deux autres moitiés : une **théorie** empruntée à la physique
    statistique, dont l'audit a réfuté toutes les affirmations propres, et un appareil de
    **régulation** — algorithme, plancher, demande d'accès — que ses propres mesures ont vidé de
    sa substance. Les deux ont été retirées. Ce qui reste est ce qui a survécu à ses contrôles.
    L'[audit](../../docs/limites.md) en garde le registre entier.
"""

from ide.entropy import (
    attainable_index,
    coarsen_catalogue,
    effective_viewpoints,
    exposed_index_bounds,
    label_diversity_index,
    shannon_entropy,
    shannon_entropy_from_counts,
    substitutions_to_floor,
    von_neumann_entropy,
)
from ide.logs import (
    Coverage,
    Digest,
    ExchangeabilityTest,
    Impressions,
    StratifiedRatio,
    UpstreamDependenceTest,
    count_above,
    detectable_severity,
    exchangeability_test,
    rank_coverage,
    stratified_risk_ratio,
    upstream_dependence_test,
)
from ide.offpolicy import (
    PositionBiasEstimate,
    clipped_ips,
    doubly_robust,
    effective_sample_size,
    estimate_position_bias,
    ips,
    snips,
)
from ide.radio import rank_weights

__version__ = "0.2.0"

__all__ = [
    "Coverage",
    "Digest",
    "ExchangeabilityTest",
    "Impressions",
    "PositionBiasEstimate",
    "StratifiedRatio",
    "UpstreamDependenceTest",
    "attainable_index",
    "clipped_ips",
    "coarsen_catalogue",
    "count_above",
    "detectable_severity",
    "doubly_robust",
    "effective_sample_size",
    "effective_viewpoints",
    "estimate_position_bias",
    "exchangeability_test",
    "exposed_index_bounds",
    "ips",
    "label_diversity_index",
    "rank_coverage",
    "rank_weights",
    "shannon_entropy",
    "shannon_entropy_from_counts",
    "snips",
    "stratified_risk_ratio",
    "substitutions_to_floor",
    "upstream_dependence_test",
    "von_neumann_entropy",
    "__version__",
]
