"""EB-NeRD : le premier journal public qui porte le fil servi **et** une étiquette."""

from __future__ import annotations

import numpy as np
import pytest
from scipy import stats

from ide.ebnerd import (
    SOURCES,
    catalogue_size,
    load_digest,
    section_counts,
    signature_counts,
)
from ide.entropy import (
    attainable_index,
    coarsen_catalogue,
    exposed_index_bounds,
    substitutions_to_floor,
)
from ide.logs import detectable_severity, exchangeability_test


def normalised_entropy(signature, catalogue):
    """L'IDE aveugle au rang d'une signature de composition."""
    counts = np.asarray(signature, dtype=float)
    parts = counts[counts > 0]
    parts = parts / parts.sum()
    return float(-(parts * np.log2(parts)).sum() / np.log2(catalogue))


def weighted_quantile(values, weights, probability):
    order = np.argsort(values)
    return values[order][np.searchsorted(np.cumsum(weights[order]), probability)]


def test_les_empreintes_attendues_sont_bien_formees():
    for relative, size, fingerprint in SOURCES.values():
        assert relative.startswith("small/")
        assert size > 0
        assert len(fingerprint) == 64 and set(fingerprint) <= set("0123456789abcdef")


def test_l_ordre_enregistre_par_ebnerd_ne_dit_rien_de_la_position():
    """Le premier contrôle du dépôt, appliqué à un troisième journal.

    EB-NeRD porte enfin les deux colonnes qui manquaient partout ailleurs. Le test dit que la
    liste servie est un **ensemble**, non un fil ordonné : l'indice exposé n'y est donc pas
    mesurable, seulement encadrable.
    """
    verdict = exchangeability_test(load_digest().impressions("ebnerd"))

    assert verdict.deviation == pytest.approx(1.05, abs=0.05)
    assert verdict.p_value > 0.05
    assert verdict.feeds_used > 200_000


def test_ce_silence_n_est_pas_un_defaut_de_puissance():
    """Un test qui ne rejette pas ne dit rien tant qu'on ignore ce qu'il aurait su rejeter."""
    lengths = load_digest().splits["ebnerd"]["feed_lengths"]
    threshold = detectable_severity(lengths, probe=0.02, rng=np.random.default_rng(20260823))

    # deux ordres de grandeur sous la sévérité mesurée sur Baidu-ULTR
    assert threshold < 0.01
    assert 0.88 / threshold > 100


def test_la_diversite_exposee_est_mesuree_pour_la_premiere_fois_sur_un_fil_reel():
    """La forme aveugle au rang, sur 232 887 fils réels et 58 549 journées-utilisateur.

    Les chiffres par journée-utilisateur ont d'abord été publiés faux : l'agrégation
    additionnait des effectifs **triés**, ce qui confond deux rubriques au motif qu'elles
    occupent le même rang (audit, point 27). Ce test verrouille la version corrigée.
    """
    digest = load_digest()
    catalogue = catalogue_size(digest)
    assert catalogue == 26

    for window, expected, below_forty in (("feed", 0.417, 0.350), ("user_day", 0.498, 0.137)):
        signatures, occurrences = signature_counts(digest, window)
        values = np.array([normalised_entropy(row, catalogue) for row in signatures])
        weights = occurrences / occurrences.sum()

        assert weighted_quantile(values, weights, 0.5) == pytest.approx(expected, abs=0.005)
        assert weights[values < 0.40].sum() == pytest.approx(below_forty, abs=0.005)


def test_sans_le_rang_on_peut_condamner_mais_rarement_acquitter():
    """Le prix exact de la colonne manquante, mesuré sur des fils réels."""
    digest = load_digest()
    catalogue = catalogue_size(digest)
    signatures, occurrences = signature_counts(digest, "feed")
    short = signatures.sum(1) <= 10

    bounds = np.array([
        exposed_index_bounds(tuple(int(value) for value in row[row > 0]), catalogue, 0.88)
        for row in signatures[short]
    ])
    weights = occurrences[short] / occurrences[short].sum()
    low, high = bounds[:, 0], bounds[:, 1]

    assert weighted_quantile(high - low, weights, 0.5) == pytest.approx(0.104, abs=0.005)
    assert weights[high < 0.40].sum() == pytest.approx(0.324, abs=0.005)
    assert weights[low >= 0.40].sum() == pytest.approx(0.079, abs=0.005)
    # la majorité des fils reste indécidable : c'est ce que coûte l'absence du rang
    assert weights[(low < 0.40) & (high >= 0.40)].sum() > 0.55


def test_une_fenetre_inconnue_est_refusee():
    with pytest.raises(ValueError):
        signature_counts(load_digest(), "semaine")



def test_l_agregation_par_journee_ne_confond_pas_deux_rubriques():
    """Le contrôle qui manquait quand les chiffres par journée-utilisateur étaient faux.

    Additionner des effectifs triés revient à traiter « la rubrique la plus servie de lundi »
    et « la rubrique la plus servie de mardi » comme la même. Les compositions identifiées du
    condensé rendent le même indice que les signatures triées — ce qui n'était pas le cas
    avant la correction.
    """
    digest = load_digest()
    catalogue = catalogue_size(digest)

    signatures, occurrences = signature_counts(digest, "user_day")
    named, named_occurrences = section_counts(digest, "section")

    assert occurrences.sum() == named_occurrences.sum()

    from_sorted = np.array([normalised_entropy(row, catalogue) for row in signatures])
    from_named = np.array([normalised_entropy(row, catalogue) for row in named])
    median_sorted = weighted_quantile(from_sorted, occurrences / occurrences.sum(), 0.5)
    median_named = weighted_quantile(from_named, named_occurrences / named_occurrences.sum(), 0.5)

    assert median_sorted == pytest.approx(median_named, abs=0.002)


def test_les_deux_axes_d_etiquetage_ne_se_deduisent_pas_l_un_de_l_autre():
    """Une rubrique n'est pas un point de vue, et l'écart se chiffre."""
    digest = load_digest()
    sections, occurrences = section_counts(digest, "section")
    tones, tone_occurrences = section_counts(digest, "tone")

    assert np.array_equal(occurrences, tone_occurrences), "les deux axes doivent être appariés"
    assert tones.shape[1] == 3

    by_section = np.array([normalised_entropy(row, sections.shape[1]) for row in sections])
    by_tone = np.array([normalised_entropy(row, tones.shape[1]) for row in tones])
    concordance = stats.spearmanr(np.repeat(by_section, occurrences),
                                  np.repeat(by_tone, occurrences)).statistic

    assert 0.0 < concordance < 0.3


def test_le_catalogue_deplace_le_niveau_sans_deplacer_l_ordre():
    """Le niveau n'a pas de sens absolu ; l'ordre en a un, jusqu'à une demi-douzaine."""
    digest = load_digest()
    catalogue = catalogue_size(digest)
    sections, occurrences = section_counts(digest, "section")
    weights = occurrences / occurrences.sum()

    def index_of(matrix, size):
        return np.array([normalised_entropy(row, size) for row in matrix])

    reference = index_of(sections, catalogue)
    assert weighted_quantile(reference, weights, 0.5) == pytest.approx(0.498, abs=0.005)

    coarse = {keep: index_of(coarsen_catalogue(sections, keep), keep) for keep in (12, 6, 3)}

    # le niveau grimpe à mesure que le catalogue rétrécit
    medians = [weighted_quantile(coarse[keep], weights, 0.5) for keep in (12, 6, 3)]
    assert medians == sorted(medians)
    assert medians[-1] > 0.9

    # et le plancher perd son mordant : neuf fois moins de journées en dessous
    assert weights[coarse[3] < 0.40].sum() < weights[reference < 0.40].sum() / 5

    # l'ordre, lui, survit à douze modalités et meurt à trois
    def concordance(values):
        return stats.spearmanr(np.repeat(reference, occurrences),
                               np.repeat(values, occurrences)).statistic

    assert concordance(coarse[12]) > 0.99
    assert concordance(coarse[6]) > 0.85
    assert abs(concordance(coarse[3])) < 0.3


def test_le_plancher_propose_par_ce_depot_ne_contraint_presque_rien():
    """Le résultat publié, verrouillé sur le condensé versionné.

    Ramener toute la population au-dessus de 0,40 demande de remplacer un contenu servi sur
    177. Une norme peut être peu coûteuse sans être décorative ; celle-ci est les deux.
    """
    digest = load_digest()
    catalogue = catalogue_size(digest)
    sections, occurrences = section_counts(digest, "section")
    served = sections.sum(1)
    total = float((served * occurrences).sum())

    values = np.array([normalised_entropy(row, catalogue) for row in sections])
    below = np.flatnonzero(values < 0.40)
    costs = np.array([substitutions_to_floor(sections[row], catalogue, 0.40) for row in below],
                     dtype=object)

    assert all(cost is not None for cost in costs), "à 0,40, aucun fil n'est hors d'atteinte"
    numeric = np.array(list(costs), dtype=float)

    spend = float((numeric * occurrences[below]).sum() / total)
    assert spend == pytest.approx(0.0057, abs=0.0005)
    assert np.median(np.repeat(numeric, occurrences[below])) == 1.0


def test_au_dela_de_la_moitie_un_plancher_regule_le_volume():
    """Un lecteur léger ne peut pas être rendu conforme, quoi que fasse la plateforme."""
    digest = load_digest()
    catalogue = catalogue_size(digest)
    sections, occurrences = section_counts(digest, "section")
    weights = occurrences / occurrences.sum()

    ceiling = np.array([attainable_index(int(count), catalogue) for count in sections.sum(1)])

    assert weights[ceiling < 0.40].sum() == 0.0
    assert weights[ceiling < 0.60].sum() == pytest.approx(0.109, abs=0.01)
    assert weights[ceiling < 0.80].sum() == pytest.approx(0.229, abs=0.01)
