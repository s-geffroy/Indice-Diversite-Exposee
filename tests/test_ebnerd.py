"""EB-NeRD : le premier journal public qui porte le fil servi **et** une étiquette."""

from __future__ import annotations

import numpy as np
import pytest

from ide.ebnerd import SOURCES, catalogue_size, load_digest, signature_counts
from ide.entropy import exposed_index_bounds
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
    """La forme aveugle au rang, sur 232 887 fils réels et 58 549 journées-utilisateur."""
    digest = load_digest()
    catalogue = catalogue_size(digest)
    assert catalogue == 26

    for window, expected, below_forty in (("feed", 0.417, 0.350), ("user_day", 0.466, 0.188)):
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
