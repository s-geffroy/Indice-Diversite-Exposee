"""Ce que la confidentialité différentielle coûte à un audit de diversité exposée.

La [demande au titre de l'article 40](../../docs/article-40.md) prouve que quatre tableaux
agrégés suffisent à recalculer toutes les mesures de ce dépôt. Elle ne dit rien de leur
**innocuité** : un agrégat n'est pas anonyme, et le seuil de suppression des faibles effectifs
qu'elle emploie n'offre aucune garantie formelle.

Ce module fournit ce qui manquait — la publication sous confidentialité différentielle — et
permet de mesurer, quantité par quantité, à quel budget :math:`\\varepsilon` chaque conclusion
du dépôt survit.

**Deux coûts distincts, et ce n'est pas celui qu'on croit qui domine.**

* Le **bruit** protège contre l'inférence sur une ligne du journal. Son effet dépend de la
  *densité* du tableau publié : sur neuf cellules de rang portant des millions d'impressions, il
  est invisible ; sur 451 100 cellules dont 99,7 % en portent moins de cinq, il détruit tout.
* Le **plafonnement des contributions** est ce qui rend la garantie *par utilisateur* possible,
  et c'est lui qui déplace les chiffres : il retire des journées aux lecteurs les plus assidus,
  qui ne sont pas les moins divers.

.. warning::
    Un budget :math:`\\varepsilon` ne se compose pas gratuitement : publier deux tableaux sous
    :math:`\\varepsilon` chacun donne une garantie à :math:`2\\varepsilon`. Les budgets annoncés
    ici valent **par quantité publiée**, et une demande réelle doit les additionner.
"""

from __future__ import annotations

import math

import numpy as np

__all__ = [
    "clipped_histogram",
    "laplace_counts",
    "publication_threshold",
]


def laplace_counts(
    counts: np.ndarray,
    epsilon: float,
    sensitivity: float = 1.0,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """Publie des effectifs sous :math:`\\varepsilon`-confidentialité différentielle.

    Le mécanisme de Laplace ajoute à chaque cellule un bruit d'échelle
    :math:`\\Delta / \\varepsilon`, où :math:`\\Delta` est la **sensibilité** :math:`L_1` du
    tableau — de combien la présence d'une seule personne peut le déplacer.

    Args:
        counts: les effectifs à publier.
        epsilon: le budget de confidentialité. Plus il est petit, plus la garantie est forte.
        sensitivity: sensibilité :math:`L_1`. Vaut 1 si une personne ne peut toucher qu'une
            cellule d'une unité, et le **plafond de contributions** si elle peut en toucher
            plusieurs.
        rng: générateur, pour la reproductibilité.

    Returns:
        Les effectifs bruités, ramenés à zéro lorsqu'ils deviennent négatifs. Ce repliement est
        un post-traitement : il ne consomme pas de budget, mais il **biaise vers le haut** les
        cellules vides, et c'est l'une des raisons pour lesquelles un tableau creux résiste mal.

    Raises:
        ValueError: si le budget ou la sensibilité ne sont pas strictement positifs.

    Examples:
        >>> import numpy as np
        >>> counts = np.array([10_000.0, 20_000.0])
        >>> noisy = laplace_counts(counts, epsilon=1.0, rng=np.random.default_rng(0))
        >>> bool(np.all(np.abs(noisy - counts) < 100.0))  # invisible à cette échelle
        True
    """
    if epsilon <= 0.0:
        raise ValueError("le budget de confidentialité doit être strictement positif")
    if sensitivity <= 0.0:
        raise ValueError("la sensibilité doit être strictement positive")

    generator = np.random.default_rng() if rng is None else rng
    counts = np.asarray(counts, dtype=float)
    return np.clip(counts + generator.laplace(0.0, sensitivity / epsilon, counts.shape), 0.0, None)


def publication_threshold(epsilon: float, delta: float, sensitivity: float = 1.0) -> float:
    """Seuil au-dessus duquel une cellule bruitée peut être publiée.

    Publier la **liste** des cellules non vides trahit leur existence, ce que le bruit seul ne
    protège pas. Le remède standard est de ne publier que les cellules dont l'effectif bruité
    dépasse un seuil, ce qui donne une garantie :math:`(\\varepsilon, \\delta)`.

    Le seuil vaut :math:`1 + \\frac{\\Delta}{\\varepsilon}\\ln(1/\\delta)`, et c'est lui — bien
    plus que le bruit — qui décide de ce qui reste lisible dans un tableau creux.

    Examples:
        >>> round(publication_threshold(epsilon=1.0, delta=1e-6, sensitivity=2.0), 1)
        28.6
    """
    if not 0.0 < delta < 1.0:
        raise ValueError("delta doit appartenir à (0, 1)")
    if epsilon <= 0.0 or sensitivity <= 0.0:
        raise ValueError("budget et sensibilité doivent être strictement positifs")

    return 1.0 + sensitivity / epsilon * math.log(1.0 / delta)


def clipped_histogram(load_by_value: np.ndarray, cap: int) -> np.ndarray:
    """Applique un plafond de contributions, et rend l'histogramme qui en résulte.

    Une garantie *par utilisateur* exige de borner ce qu'une personne peut apporter au tableau.
    On ne garde donc au plus que ``cap`` observations par personne, tirées au hasard parmi les
    siennes — ce qui, en espérance, multiplie la ligne d'une personne en portant :math:`\\ell`
    par :math:`\\min(1, \\text{cap}/\\ell)`.

    C'est un **choix de conception, pas un artefact** : il rend la garantie possible et il
    déplace le résultat, puisque les personnes les plus assidues ne ressemblent pas aux autres.

    Args:
        load_by_value: tableau ``(charge, valeur)`` — nombre d'observations de valeur donnée
            provenant de personnes en portant exactement ``charge``. La ligne d'indice zéro est
            ignorée.
        cap: plafond de contributions par personne.

    Returns:
        L'histogramme des valeurs après plafonnement, en espérance.

    Raises:
        ValueError: si le plafond n'est pas strictement positif.

    Examples:
        Deux personnes, l'une avec une observation, l'autre avec quatre : plafonner à deux
        divise par deux l'apport de la seconde.

        >>> import numpy as np
        >>> table = np.zeros((5, 2))
        >>> table[1, 0] = 1.0    # une personne d'une observation, de valeur 0
        >>> table[4, 1] = 4.0    # une personne de quatre observations, de valeur 1
        >>> clipped_histogram(table, cap=2)
        array([1., 2.])
    """
    if cap <= 0:
        raise ValueError("le plafond de contributions doit être strictement positif")

    table = np.asarray(load_by_value, dtype=float)
    loads = np.arange(table.shape[0], dtype=float)
    keep = np.divide(np.minimum(loads, cap), loads, out=np.zeros_like(loads), where=loads > 0)
    return (table * keep[:, None]).sum(axis=0)
