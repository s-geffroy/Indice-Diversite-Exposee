"""Les deux journaux qui enregistrent le rang servi, et ce qu'ils permettent de vérifier."""

from __future__ import annotations

import numpy as np
import pytest

from ide.entropy import label_diversity_index
from ide.exposure import (
    SOURCES,
    Digest,
    bucket_from_digest,
    examination_counts,
    load_digest,
    obd_cells,
    obd_click_rates,
    off_policy_check,
    page_effect_counts,
    page_examination_curve,
    source_path,
    verify_source,
)
from ide.logs import exchangeability_test, naive_severity_fit, stratified_risk_ratio
from ide.offpolicy import estimate_position_bias


def synthetic_bucket(rows, catalogue=4, severity=0.0, seed=0):
    """Un seau de service à propensions **connues**, pour éprouver la confrontation."""
    generator = np.random.default_rng(seed)
    quality = generator.uniform(0.05, 0.4, catalogue)
    positions = generator.integers(1, 4, rows)
    weights = generator.dirichlet(np.full(catalogue, 0.6))
    items = generator.choice(catalogue, size=rows, p=weights)
    probability = quality[items] * positions.astype(float) ** (-severity)
    return {
        "items": items.astype(np.int64),
        "positions": positions.astype(np.int64),
        "clicks": (generator.random(rows) < probability).astype(float),
        "propensities": weights[items],
        "item_count": np.asarray(catalogue),
    }


def test_un_journal_inconnu_est_refuse():
    with pytest.raises(ValueError, match="journal inconnu"):
        source_path("gallica")
    with pytest.raises(ValueError, match="journal inconnu"):
        verify_source("gallica")


def test_un_journal_absent_indique_comment_le_recuperer(tmp_path):
    with pytest.raises(FileNotFoundError, match="fetch_exposure"):
        verify_source("baidu", directory=tmp_path)


def test_les_empreintes_attendues_sont_bien_formees():
    for name, (relative, size, digest) in SOURCES.items():
        assert relative.count("/") == 1, name
        assert size > 100_000_000, name
        assert len(digest) == 64, name


def test_le_taux_de_clic_par_position_porte_son_erreur_type():
    bucket = synthetic_bucket(6000, severity=0.0, seed=3)

    rates = obd_click_rates(bucket)

    assert set(rates) == {1, 2, 3}
    for exposures, successes, rate, error in rates.values():
        assert successes <= exposures
        assert rate == pytest.approx(successes / exposures)
        assert error == pytest.approx(np.sqrt(rate * (1 - rate) / exposures))


def test_les_cellules_redeployees_rendent_le_seau_d_origine():
    bucket = synthetic_bucket(20_000, severity=0.3, seed=7)
    digest = Digest(sources={"b": "sha"}, minimum_impressions=1, splits={"b": obd_cells(bucket)})

    rebuilt = bucket_from_digest(digest, "b")

    assert rebuilt["clicks"].size == bucket["clicks"].size
    assert rebuilt["clicks"].sum() == bucket["clicks"].sum()
    assert obd_click_rates(rebuilt) == obd_click_rates(bucket)
    assert estimate_position_bias(
        rebuilt["items"], rebuilt["positions"], rebuilt["clicks"]
    ).severity == pytest.approx(
        estimate_position_bias(bucket["items"], bucket["positions"], bucket["clicks"]).severity
    )


def test_la_confrontation_retrouve_la_valeur_de_la_politique_cible():
    """Le cas d'école : la cible est uniforme, le journal ne l'est pas, et l'IPS le corrige."""
    logged = synthetic_bucket(400_000, severity=0.0, seed=11)
    generator = np.random.default_rng(12)
    catalogue = int(logged["item_count"])
    items = generator.integers(0, catalogue, 200_000)
    quality = np.array([logged["clicks"][logged["items"] == item].mean()
                        for item in range(catalogue)])
    target = {
        "items": items,
        "positions": generator.integers(1, 4, items.size),
        "clicks": (generator.random(items.size) < quality[items]).astype(float),
        "propensities": np.full(items.size, 1.0 / catalogue),
        "item_count": np.asarray(catalogue),
    }

    check = off_policy_check(target, logged)

    assert abs(check.relative_error(check.importance_sampling)) < 0.05
    assert abs(check.relative_error(check.naive)) > abs(
        check.relative_error(check.importance_sampling)
    )
    assert 0.0 < check.effective_share <= 1.0
    assert set(check.clipped) == {10.0, 100.0, 1000.0}


def test_baidu_enregistre_bien_le_rang_servi():
    """Le contrôle positif que MIND avait échoué, sur le condensé versionné.

    L'écart réduit doit être **négatif** : un biais de position concentre les clics en haut.
    Un test qui rejetterait du mauvais côté signalerait une erreur de signe, pas une découverte.
    """
    impressions = load_digest().impressions("baidu")

    verdict = exchangeability_test(impressions)

    assert verdict.deviation < -100.0
    assert verdict.p_value < 1e-12
    assert not verdict.exchangeable


def test_la_severite_de_baidu_se_situe_autour_de_un():
    digest = load_digest()
    items, ranks, clicks = digest.rows("baidu")

    fixed_effects = estimate_position_bias(items, ranks, clicks, minimum_impressions=5)
    aggregate = naive_severity_fit(digest.impressions("baidu"), maximum_rank=10)

    assert fixed_effects.severity == pytest.approx(1.10, abs=0.05)
    assert fixed_effects.standard_error < 0.1
    # L'ajustement agrégé surestime : la plateforme place les meilleurs documents en tête, et
    # cette qualité-là entre dans la pente tant qu'on ne l'élimine pas par effets fixes.
    assert aggregate > fixed_effects.severity + 0.3


def test_le_bandeau_de_l_open_bandit_dataset_a_un_biais_bien_plus_faible():
    """Trois vignettes horizontales, allocation aléatoire : l'effet de position y est ténu.

    C'est la mesure qui interdit de traiter $\\eta$ comme une constante : la même grandeur vaut
    1,1 sur une page de résultats verticale et un dixième de cela sur un bandeau de trois.
    """
    rates = obd_click_rates(bucket_from_digest(load_digest(), "obd_random_all"))

    first, last = rates[1], rates[3]
    assert first[2] > last[2]
    # L'écart entre la première et la dernière vignette ne dépasse pas deux erreurs types
    # cumulées : mesurable en tendance, pas concluant vignette à vignette.
    assert first[2] - last[2] < 2 * (first[3] + last[3])


def test_l_estimation_contrefactuelle_est_confrontee_a_une_mesure_directe():
    """Le seul endroit du dépôt où l'estimateur est jugé contre la valeur qu'il estime."""
    digest = load_digest()

    check = off_policy_check(
        bucket_from_digest(digest, "obd_random_men"),
        bucket_from_digest(digest, "obd_bts_men"),
    )

    assert check.truth == pytest.approx(0.00512, abs=0.0001)
    assert abs(check.relative_error(check.importance_sampling)) < 0.05
    assert check.relative_error(check.naive) > 0.25
    # Et le diagnostic qui interdit de crier victoire : l'estimation sans biais repose sur
    # l'équivalent de mille cinq cents observations, pour quatre millions d'impressions.
    assert check.effective_size < 3_000
    assert check.effective_share < 0.001


def test_la_mesure_d_examen_est_absente_d_un_condense_qui_ne_la_porte_pas():
    digest = Digest(sources={"x": "sha"}, minimum_impressions=1,
                    splits={"x": {"cell_items": np.asarray([1])}})

    with pytest.raises(ValueError, match="mesure d'examen"):
        examination_counts(digest, "x")


def test_l_examen_separe_ce_que_le_clic_confond():
    """Le résultat qui lève l'impasse du test de forme, figé en simulation.

    Sous cascade, l'examen s'arrête après un clic ; sous budget de clics, il continue. Le clic,
    lui, montre la même chose dans les deux cas — c'est pourquoi il ne peut pas trancher.
    """
    from ide.logs import Impressions as Journal
    from ide.logs import simulate_cascade, upstream_dependence_test

    slots, feeds, catalogue = 10, 12_000, 150
    generator = np.random.default_rng(3)

    cascade, cascade_seen = simulate_cascade([slots] * feeds, continuation=0.85,
                                            catalogue=catalogue,
                                            rng=np.random.default_rng(3),
                                            return_examination=True)

    # budget de clics : l'examen suit R^-1 et ne dépend pas de l'amont
    quality = 0.25 * generator.lognormal(0.0, 0.8, size=catalogue)
    items = generator.integers(0, catalogue, size=feeds * slots).reshape(feeds, slots)
    ranks = np.tile(np.arange(1, slots + 1), (feeds, 1))
    seen = generator.random((feeds, slots)) < ranks.astype(float) ** (-1.0)
    drawn = seen & (generator.random((feeds, slots)) < np.clip(quality[items], 0.0, 1.0))
    kept = drawn & (np.cumsum(drawn, axis=1) <= 1)
    budgeted = Journal(items=items.ravel().astype(np.int64),
                       ranks=ranks.ravel().astype(np.int64),
                       clicks=kept.ravel().astype(float),
                       feeds=np.repeat(np.arange(feeds), slots).astype(np.int64),
                       feed_lengths=np.full(feeds, slots, dtype=np.int64))

    # sur les CLICS, les deux rejettent : indiscernables
    assert upstream_dependence_test(cascade).deviation < -10.0
    assert upstream_dependence_test(budgeted).deviation < -10.0

    # sur l'EXAMEN, seule la cascade rejette : la séparation est nette
    assert upstream_dependence_test(cascade, outcome=cascade_seen).deviation < -50.0
    assert abs(upstream_dependence_test(budgeted,
                                        outcome=seen.ravel().astype(float)).deviation) < 3.0


def test_l_exposition_mesuree_sur_baidu_est_moins_severe_que_celle_estimee():
    """Le résultat publié, verrouillé sur le condensé versionné.

    Un clic est le produit de l'examen et de l'attrait. Comme l'attrait décroît lui aussi avec
    le rang, la sévérité ajustée sur les clics absorbe les deux et surestime la décroissance.
    """
    counts = examination_counts(load_digest())
    shallow = counts["ranks"] <= 9

    items = np.repeat(counts["items"][shallow], counts["exposures"][shallow])
    ranks = np.repeat(counts["ranks"][shallow], counts["exposures"][shallow])
    seen = np.concatenate([
        np.concatenate([np.ones(total), np.zeros(exposures - total)])
        for exposures, total in zip(counts["exposures"][shallow], counts["seen"][shallow],
                                    strict=True)
    ])

    examination = estimate_position_bias(items, ranks, seen, minimum_impressions=5)

    assert examination.severity == pytest.approx(0.882, abs=0.01)
    assert examination.standard_error < 0.06
    # et la mesure repose sur bien plus de documents que l'estimation par les clics
    assert examination.items_with_variation > 2 * 55


def test_sur_baidu_l_examen_ne_s_arrete_pas_apres_un_clic():
    """La cascade réfutée sur données réelles : l'écart est positif, pas négatif."""
    from ide.logs import upstream_dependence_from_counts

    counts = examination_counts(load_digest())

    for minimum in (5, 10, 20):
        verdict = upstream_dependence_from_counts(
            counts["exposures"], counts["upstream_preceded"], counts["seen"],
            counts["upstream_seen"], minimum_impressions=minimum)
        assert verdict.deviation > 5.0, "une cascade rendrait cet écart négatif"
        assert not verdict.position_like



def rapport_de_page(digest, stratification, rangs=(2, 9)):
    """Le rapport de risques apparié, tel que le chapitre le publie."""
    counts = page_effect_counts(digest, stratification)
    kept = (counts["ranks"] >= rangs[0]) & (counts["ranks"] <= rangs[1])
    return stratified_risk_ratio(
        counts["untreated"][kept], counts["treated"][kept],
        counts["untreated_seen"][kept], counts["treated_seen"][kept],
    )


def test_les_deux_tiers_de_l_effet_de_format_etaient_de_la_composition():
    """Le résultat publié, verrouillé sur le condensé versionné.

    Le chapitre précédent comparait les pages enrichies aux autres à rang et à hauteur
    comparables, et lisait un écart de dix-huit points relatifs. À contenu fixé, il en reste
    six : le reste tenait à *quelles* requêtes déclenchent un encadré de réponse, non à ce que
    l'encadré fait au lecteur.
    """
    digest = load_digest()
    curve = page_examination_curve(digest)
    exposures = curve["exposures"].reshape(-1, 5).astype(float)
    seen = curve["seen"].reshape(-1, 5).astype(float)
    ranks = np.arange(1, exposures.shape[0] + 1)
    kept = (ranks >= 2) & (ranks <= 9)

    par_rang = stratified_risk_ratio(
        exposures[kept, 0], exposures[kept, 1:].sum(1),
        seen[kept, 0], seen[kept, 1:].sum(1),
    )
    assert par_rang.ratio == pytest.approx(0.817, abs=0.01)

    apparie = rapport_de_page(digest, "document")
    assert apparie.ratio == pytest.approx(0.940, abs=0.01)
    # l'effet résiduel reste établi ; il est seulement trois fois plus petit
    assert apparie.established
    assert apparie.ratio > par_rang.ratio


def test_les_deux_appariements_independants_concordent():
    """Même contenu / même rang, et même requête / même rang : deux plans, un seul chiffre."""
    digest = load_digest()
    par_contenu = rapport_de_page(digest, "document")
    par_requete = rapport_de_page(digest, "query")

    assert par_requete.ratio == pytest.approx(par_contenu.ratio, abs=0.02)
    # l'appariement par requête est bien moins peuplé : il concorde sans rien établir seul
    assert par_requete.impressions < par_contenu.impressions / 5
    assert not par_requete.established


def test_ignorer_la_page_coute_bien_moins_que_la_convention_en_un_sur_R():
    """Ce qui décide de la remise d'attention est la mesure, non la composition de la page."""
    digest = load_digest()
    curve = page_examination_curve(digest)
    exposures = curve["exposures"].reshape(-1, 5).astype(float)
    seen = curve["seen"].reshape(-1, 5).astype(float)
    depth = 9

    marginale = (seen.sum(1) / exposures.sum(1))[:depth]
    part = (exposures[:, 1:].sum(1) / exposures.sum(1))[:depth]
    ratio = rapport_de_page(digest, "document").ratio
    # Le rang 1 ne porte jamais de format enrichi au-dessus de lui : sans cette exemption
    # l'effet serait une homothétie, à laquelle un indice normalisé est insensible.
    enrichie = marginale / (1 - part + part * ratio)
    enrichie[1:] *= ratio
    convention = np.arange(1, depth + 1, dtype=float) ** -1.0

    generator = np.random.default_rng(20260823)
    ecart_page, ecart_convention = [], []
    for _ in range(500):
        labels = generator.integers(0, 4, size=depth)
        reference = exposed_index(marginale, labels)
        ecart_page.append(abs(reference - exposed_index(enrichie, labels)))
        ecart_convention.append(abs(reference - exposed_index(convention, labels)))

    assert 0.0 < np.median(ecart_page) < 0.005
    assert np.median(ecart_convention) > 10 * np.median(ecart_page)


def exposed_index(weights, labels, catalogue=4):
    """L'IDE d'un fil, sous une remise d'attention donnée."""
    served = np.array([weights[labels == viewpoint].sum() for viewpoint in range(catalogue)])
    return label_diversity_index(
        np.repeat(np.arange(catalogue), np.round(served / served.sum() * 10_000).astype(int)),
        catalogue_size=catalogue,
    )
