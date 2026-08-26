"""Ce que la confidentialité différentielle coûte à un audit, mesuré quantité par quantité."""

from __future__ import annotations

import numpy as np
import pytest

from ide.ebnerd import load_digest as load_ebnerd_digest
from ide.ebnerd import load_index_table
from ide.exposure import examination_counts
from ide.exposure import load_digest as load_exposure_digest
from ide.offpolicy import estimate_position_bias
from ide.privacy import clipped_histogram, laplace_counts, publication_threshold


class TestMecanisme:
    """Le mécanisme de Laplace et ses deux garde-fous."""

    def test_le_bruit_est_a_l_echelle_annoncee(self):
        generator = np.random.default_rng(0)
        counts = np.full(200_000, 10_000.0)
        noisy = laplace_counts(counts, epsilon=1.0, sensitivity=2.0, rng=generator)

        # écart type d'une loi de Laplace d'échelle b : b√2
        assert np.std(noisy - counts) == pytest.approx(2.0 * np.sqrt(2.0), rel=0.05)

    def test_un_budget_plus_petit_bruite_davantage(self):
        generator = np.random.default_rng(1)
        counts = np.full(50_000, 1_000.0)
        large = np.std(laplace_counts(counts, epsilon=10.0, rng=generator) - counts)
        strict = np.std(laplace_counts(counts, epsilon=0.1, rng=generator) - counts)

        assert strict > 50 * large

    def test_les_effectifs_negatifs_sont_repliés_a_zero(self):
        noisy = laplace_counts(np.zeros(1_000), epsilon=0.1, rng=np.random.default_rng(2))
        assert np.all(noisy >= 0.0)
        # ce repliement est un post-traitement, et il biaise les cellules vides vers le haut
        assert noisy.mean() > 0.0

    def test_le_seuil_de_publication_suit_sa_formule(self):
        assert publication_threshold(1.0, 1e-6, 2.0) == pytest.approx(1.0 + 2.0 * np.log(1e6))
        assert publication_threshold(3.0, 1e-6) < publication_threshold(1.0, 1e-6)

    def test_les_budgets_absurdes_sont_refuses(self):
        for epsilon, sensitivity in ((0.0, 1.0), (-1.0, 1.0), (1.0, 0.0)):
            with pytest.raises(ValueError):
                laplace_counts(np.ones(3), epsilon, sensitivity)
        with pytest.raises(ValueError):
            publication_threshold(1.0, delta=1.5)


class TestPlafonnement:
    """Le plafond de contributions, sans lequel aucune garantie par personne n'est possible."""

    def test_le_plafond_reduit_l_apport_des_plus_assidus(self):
        table = np.zeros((5, 2))
        table[1, 0] = 1.0
        table[4, 1] = 4.0

        assert np.array_equal(clipped_histogram(table, cap=2), np.array([1.0, 2.0]))
        assert np.array_equal(clipped_histogram(table, cap=4), np.array([1.0, 4.0]))

    def test_un_plafond_au_moins_egal_a_la_charge_maximale_ne_retire_rien(self):
        generator = np.random.default_rng(3)
        table = generator.integers(0, 50, size=(6, 4)).astype(float)

        # la ligne de charge nulle est ignorée par construction : elle ne porte personne
        assert np.allclose(clipped_histogram(table, cap=5), table[1:].sum(axis=0))

    def test_un_plafond_nul_est_refuse(self):
        with pytest.raises(ValueError):
            clipped_histogram(np.ones((3, 2)), cap=0)


def severity_from_cells(items, ranks, exposures, seen, keep):
    """La sévérité à effets fixes de contenu, telle que le chapitre la calcule."""
    total = np.round(np.maximum(exposures[keep], 1.0)).astype(int)
    hits = np.round(np.clip(np.minimum(seen[keep], exposures[keep]), 0.0, None)).astype(int)
    flags = np.concatenate([np.concatenate([np.ones(hit), np.zeros(count - hit)])
                            for count, hit in zip(total, hits, strict=True)])
    return estimate_position_bias(np.repeat(items[keep], total), np.repeat(ranks[keep], total),
                                  flags, minimum_impressions=5)


def examination_cells(depth=9):
    counts = examination_counts(load_exposure_digest())
    shallow = counts["ranks"] <= depth
    return (counts["items"][shallow], counts["ranks"][shallow],
            counts["exposures"][shallow].astype(float), counts["seen"][shallow].astype(float))


def test_le_tableau_des_cellules_est_trop_creux_pour_etre_publie():
    """99,7 % des cellules portent moins de cinq impressions — c'est ce qui décide de tout."""
    _, _, exposures, _ = examination_cells()

    assert exposures.size > 400_000
    assert (exposures < 5).mean() > 0.99


def test_a_budget_un_la_severite_est_divisee_par_deux_sans_que_rien_ne_le_signale():
    """Le mode d'échec que ce dépôt a rencontré cinq fois : un chiffre plausible et faux.

    Le bruit sur des effectifs agit comme une erreur de mesure : il **atténue** l'estimation
    vers zéro. L'erreur type, elle, ne bouge pas — le résultat est donc faux avec assurance,
    et dans le sens qui fait paraître l'enterrement moins grave qu'il n'est.
    """
    items, ranks, exposures, seen = examination_cells()
    generator = np.random.default_rng(20260826)
    everything = np.ones(items.size, dtype=bool)

    truth = severity_from_cells(items, ranks, exposures, seen, everything)
    assert truth.severity == pytest.approx(0.882, abs=0.01)

    noisy = severity_from_cells(
        items, ranks,
        laplace_counts(exposures, 1.0, sensitivity=2.0, rng=generator),
        laplace_counts(seen, 1.0, sensitivity=2.0, rng=generator),
        everything,
    )
    assert noisy.severity < 0.65
    assert noisy.standard_error == pytest.approx(truth.standard_error, abs=0.02)


def test_la_marge_de_rang_survit_a_tout_et_ne_se_verifie_pas():
    """Neuf cellules portant un demi-million d'impressions sont hors d'atteinte du bruit."""
    _, ranks, exposures, seen = examination_cells()
    margin_exposures = np.bincount(ranks, weights=exposures)[1:10]
    margin_seen = np.bincount(ranks, weights=seen)[1:10]
    generator = np.random.default_rng(20260826)

    def slope(exposed, observed):
        return -np.polyfit(np.log(np.arange(1, 10)), np.log(observed / exposed), 1)[0]

    assert slope(margin_exposures, margin_seen) == pytest.approx(0.876, abs=0.005)
    noisy = slope(laplace_counts(margin_exposures, 0.1, sensitivity=2.0, rng=generator),
                  laplace_counts(margin_seen, 0.1, sensitivity=2.0, rng=generator))
    assert noisy == pytest.approx(0.876, abs=0.01)


def test_la_grandeur_reglementee_ne_craint_pas_le_bruit_mais_craint_le_plafond():
    """Le prix de la vie privée n'est pas le bruit : c'est la borne de contribution.

    Et il est **directionnel** : les lecteurs assidus sont plus divers, les écarter fait
    paraître la plateforme moins conforme qu'elle n'est.
    """
    table, edges = load_index_table(load_ebnerd_digest())
    centres = (edges[:-1] + edges[1:]) / 2
    generator = np.random.default_rng(20260826)

    def below(histogram):
        return float(histogram[centres < 0.40].sum() / histogram.sum())

    truth = below(clipped_histogram(table, cap=table.shape[0]))
    assert truth == pytest.approx(0.188, abs=0.005)

    # le bruit, même à ε = 0,1, ne déplace la part que de quelques millièmes
    unbounded = clipped_histogram(table, cap=table.shape[0])
    draws = [below(laplace_counts(unbounded, 0.1, sensitivity=table.shape[0], rng=generator))
             for _ in range(50)]
    assert np.mean(draws) == pytest.approx(truth, abs=0.005)

    # le plafonnement, lui, biaise — et toujours vers l'excès de sévérité
    biases = [below(clipped_histogram(table, cap)) - truth for cap in (1, 2, 3, 5)]
    assert all(bias > 0.0 for bias in biases)
    assert biases == sorted(biases, reverse=True)
    assert biases[0] == pytest.approx(0.025, abs=0.005)
