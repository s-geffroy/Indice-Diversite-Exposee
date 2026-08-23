"""La représentation commune d'un journal, et ce que son condensé garantit."""

from __future__ import annotations

import numpy as np
import pytest

from ide.logs import (
    Digest,
    Impressions,
    click_rate_by_rank,
    digest_split,
    exchangeability_test,
    load_digest,
    save_digest,
    simulate_cascade,
    simulate_feeds,
)


def feed_impressions(ranks_per_feed, clicks_per_feed, items_per_feed):
    lengths = np.asarray([len(ranks) for ranks in ranks_per_feed], dtype=np.int64)
    return Impressions(
        items=np.concatenate(items_per_feed).astype(np.int64),
        ranks=np.concatenate(ranks_per_feed).astype(np.int64),
        clicks=np.concatenate(clicks_per_feed).astype(float),
        feeds=np.repeat(np.arange(lengths.size), lengths),
        feed_lengths=lengths,
    )


def round_trip(impressions, tmp_path):
    digest = Digest(sources={"x": "sha"}, minimum_impressions=1,
                    splits={"x": digest_split(impressions, minimum_impressions=1)})
    return load_digest(save_digest(digest, tmp_path / "d.npz")).impressions("x")


def test_un_journal_canonique_se_resume_a_ses_longueurs(tmp_path):
    impressions = feed_impressions(
        [np.arange(1, 4), np.arange(1, 3)],
        [[0, 1, 0], [1, 0]],
        [[10, 11, 12], [11, 13]],
    )

    arrays = digest_split(impressions, minimum_impressions=1)
    assert "clicked_ranks" in arrays and "served_ranks" not in arrays

    rebuilt = round_trip(impressions, tmp_path)
    assert list(rebuilt.ranks) == list(impressions.ranks)
    assert list(rebuilt.clicks) == list(impressions.clicks)


def test_un_journal_dont_les_rangs_sautent_conserve_ses_rangs(tmp_path):
    """Le défaut que Baidu-ULTR a révélé : une page de résultats peut sauter des rangs.

    Supposer qu'un fil de longueur $L$ occupe les rangs 1 à $L$ produisait alors un condensé
    faux — et faux d'une façon indolore, puisqu'il rendait des chiffres du bon ordre de
    grandeur.
    """
    impressions = feed_impressions(
        [np.asarray([1, 2, 5]), np.asarray([3, 7])],
        [[1, 0, 0], [0, 1]],
        [[10, 11, 12], [11, 13]],
    )

    arrays = digest_split(impressions, minimum_impressions=1)
    assert "served_ranks" in arrays and "clicked_ranks" not in arrays

    rebuilt = round_trip(impressions, tmp_path)
    assert list(rebuilt.ranks) == [1, 2, 5, 3, 7]
    assert list(rebuilt.clicks) == [1, 0, 0, 0, 1]
    assert exchangeability_test(rebuilt).deviation == pytest.approx(
        exchangeability_test(impressions).deviation, nan_ok=True
    )


def test_un_condense_indique_comment_le_reconstruire(tmp_path):
    with pytest.raises(FileNotFoundError, match="reconstruire-moi"):
        load_digest(tmp_path / "absent.npz", rebuild_with="reconstruire-moi")


def test_un_condense_sans_structure_de_fils_le_dit(tmp_path):
    digest = Digest(sources={"x": "sha"}, minimum_impressions=1,
                    splits={"x": {"cell_items": np.asarray([1])}})

    with pytest.raises(ValueError, match="structure des fils"):
        digest.impressions("x")


def test_le_test_rejette_aussi_sous_un_modele_a_cascade():
    """Le contrôle qui rend interprétable le verdict négatif sur MIND.

    Le test ne suppose rien de la forme de l'attention : il ne teste que l'indépendance entre
    position et clic. Il doit donc rejeter sous cascade — où l'examen dépend de ce qui précède —
    aussi bien que sous un modèle de position. Sinon, « le test ne détecte rien » ne
    distinguerait pas un journal mélangé d'un journal dont la dépendance a une autre forme.
    """
    feeds = simulate_cascade([12] * 6000, continuation=0.85, rng=np.random.default_rng(3))

    verdict = exchangeability_test(feeds)

    assert verdict.deviation < -20.0, "un biais de cascade doit être détecté"
    assert not verdict.exchangeable


def test_la_cascade_decroit_plus_vite_qu_une_loi_de_puissance():
    """La raison pour laquelle ajuster R^-eta sur une cascade produit un chiffre faux.

    Une décroissance géométrique ne s'approche pas par une décroissance polynomiale : les deux
    coïncident en tête et divergent en queue, d'autant plus que le fil est long.
    """
    cascade = simulate_cascade([12] * 8000, continuation=0.8, rng=np.random.default_rng(5))
    power = simulate_feeds([12] * 8000, severity=1.0, rng=np.random.default_rng(5))

    cascade_rates = click_rate_by_rank(cascade, 12)
    power_rates = click_rate_by_rank(power, 12)

    assert cascade_rates[0] > power_rates[0]
    assert cascade_rates[-1] < power_rates[-1]


def test_le_masque_d_examen_est_coherent_avec_les_clics():
    """La vérité terrain que la simulation rend, et que les données réelles ne donnent jamais."""
    feeds, examined = simulate_cascade([10] * 400, continuation=0.7,
                                       rng=np.random.default_rng(9), return_examination=True)

    # tout contenu cliqué a été examiné ; aucun contenu n'est examiné après un clic dans son fil
    assert np.all(examined[feeds.clicks > 0] == 1.0)
    per_feed = examined.reshape(-1, 10)
    clicks_per_feed = feeds.clicks.reshape(-1, 10)
    for row, clicks in zip(per_feed, clicks_per_feed, strict=True):
        stop = int(np.argmax(clicks)) if clicks.any() else None
        if stop is not None:
            assert row[stop + 1:].sum() == 0.0
        # l'examen est un préfixe : jamais de trou
        assert np.all(np.diff(row) <= 0)


def test_une_probabilite_de_poursuite_hors_bornes_est_refusee():
    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        simulate_cascade([5] * 10, continuation=1.5)

