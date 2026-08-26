"""EB-NeRD — le premier journal public qui porte à la fois le fil servi et une étiquette.

Six chapitres de ce dépôt reposent sur une lacune énoncée comme définitive : *aucun jeu de
données public ne porte à la fois le rang servi et une étiquette de point de vue
interprétable*. MIND a les catégories sans l'ordre, Baidu-ULTR l'ordre sans les catégories.

EB-NeRD (Ekstra Bladet News Recommendation Dataset, RecSys Challenge 2024) porte les deux
colonnes : ``article_ids_inview`` donne la **liste servie**, et chaque article déclare une
``category_str``. C'est donc le premier candidat sérieux à la mesure que le dépôt annonce
depuis le début.

.. warning::
    Le premier contrôle du dépôt — l'échangeabilité intra-fil — dit que l'**ordre** de
    ``article_ids_inview`` ne porte aucune information de position ($z = +1{,}05$,
    $p = 0{,}29$ sur 232 887 fils). La liste est un **ensemble servi**, pas un fil ordonné.
    L'indice aveugle au rang y est donc mesurable ; l'indice exposé, non — seulement
    encadrable, par :func:`ide.entropy.exposed_index_bounds`.

.. note::
    ``category_str`` est une **rubrique** (« nyheder », « sport », « krimi »), non un point de
    vue au sens de l'indice. La mesure porte sur la diversité **thématique** exposée, qui en
    est un substitut — le même que celui employé sur MIND, et il doit être lu comme tel.

Licence : EB-NeRD est distribué pour usage de recherche uniquement, sans exploitation
commerciale ni redistribution. Les fichiers bruts ne sont donc **pas versionnés** ; seul le
condensé de comptes agrégés l'est, à l'identique des deux autres journaux.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ide.logs import Digest, Impressions, digest_split
from ide.logs import load_digest as _load_digest

__all__ = [
    "DIGEST_PATH",
    "EBNERD_DIRECTORY",
    "EBNERD_SOURCE",
    "SOURCES",
    "FeedComposition",
    "build_digest",
    "catalogue_size",
    "load_digest",
    "load_ebnerd",
    "load_index_table",
    "section_counts",
    "signature_counts",
    "verify_source",
]

EBNERD_DIRECTORY = Path(__file__).resolve().parents[2] / "data" / "ebnerd"
DIGEST_PATH = Path(__file__).resolve().parents[2] / "data" / "ebnerd_digest.npz"

#: L'archive publique, telle que la distribue Ekstra Bladet.
EBNERD_SOURCE = "https://ebnerd-dataset.s3.eu-west-1.amazonaws.com/ebnerd_small.zip"

#: Chemin relatif, taille et empreinte SHA-256 des deux tables lues.
SOURCES: dict[str, tuple[str, int, str]] = {
    "articles": (
        "small/articles.parquet",
        25_803_208,
        "b1cea52ee4c152086ff6b70962fe543a43de50c684c1ec0735a4f061bded43d2",
    ),
    "behaviors": (
        "small/train/behaviors.parquet",
        10_322_189,
        "eeedd1b5cb42e952b7688f3199c5eb97da5596e6245a52714083eea3cb8e3736",
    ),
}


@dataclass(frozen=True)
class FeedComposition:
    """Ce qu'un fil servi contenait, et à qui.

    Attributes:
        signatures: effectifs par rubrique d'un fil, **triés par ordre décroissant** et
            complétés de zéros. À fil donné, l'ordre ne change pas l'indice.
        sections: les mêmes effectifs, **à leur place dans le catalogue**. L'identité est
            nécessaire dès qu'on agrège plusieurs fils — deux fils triés ne s'additionnent pas —
            et dès qu'on veut regrouper des rubriques.
        tones: effectifs par **tonalité** déclarée — négative, neutre, positive. C'est un
            second axe d'étiquetage, plus proche d'un point de vue qu'une rubrique, et il
            permet de mesurer ce que le choix de l'axe change.
        users: identifiant d'utilisateur, réindexé.
        days: jour de service, en jours depuis la première impression du journal.
    """

    signatures: np.ndarray
    sections: np.ndarray
    tones: np.ndarray
    users: np.ndarray
    days: np.ndarray


def verify_source(name: str, directory: Path | None = None) -> tuple[bool, int, str]:
    """Vérifie taille et empreinte d'une table récupérée.

    Returns:
        Conformité, taille lue, empreinte SHA-256.
    """
    if name not in SOURCES:
        raise ValueError(f"table inconnue : {name!r}")
    relative, expected_size, expected_digest = SOURCES[name]
    base = EBNERD_DIRECTORY if directory is None else directory
    path = base / relative
    if not path.exists():
        raise FileNotFoundError(
            f"{path} absent. Récupérer le journal : "
            "docker compose run --rm lab python scripts/fetch_ebnerd.py"
        )

    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 22), b""):
            digest.update(chunk)

    return (path.stat().st_size == expected_size and digest.hexdigest() == expected_digest,
            path.stat().st_size, digest.hexdigest())


def source_path(name: str, directory: Path | None = None) -> Path:
    """Chemin d'une table du journal."""
    if name not in SOURCES:
        raise ValueError(f"table inconnue : {name!r}")
    base = EBNERD_DIRECTORY if directory is None else directory
    return base / SOURCES[name][0]


def load_ebnerd(directory: Path | None = None) -> tuple[Impressions, FeedComposition, int]:
    """Lit le journal et rend le fil servi, sa composition thématique, et le catalogue.

    Le journal est mis à plat comme les autres : une ligne par contenu servi, le « rang »
    étant la place dans ``article_ids_inview``. Le premier contrôle décide ensuite si cette
    place veut dire quelque chose — sur ce journal, elle ne veut rien dire.

    Returns:
        Le journal, la composition des fils, et la taille du catalogue de rubriques.
    """
    import pyarrow.parquet as parquet  # dépendance de laboratoire, pas du noyau

    articles = parquet.read_table(source_path("articles", directory),
                                  columns=["article_id", "category_str", "sentiment_label"])
    section_of = dict(zip(articles["article_id"].to_pylist(),
                          articles["category_str"].to_pylist(), strict=True))
    tone_of = dict(zip(articles["article_id"].to_pylist(),
                       articles["sentiment_label"].to_pylist(), strict=True))
    tones_order = {"Negative": 0, "Neutral": 1, "Positive": 2}
    catalogue = sorted(set(section_of.values()))
    section_index = {label: position for position, label in enumerate(catalogue)}

    behaviours = parquet.read_table(
        source_path("behaviors", directory),
        columns=["article_ids_inview", "article_ids_clicked", "user_id", "impression_time"],
    )
    served = behaviours["article_ids_inview"].to_pylist()
    chosen = behaviours["article_ids_clicked"].to_pylist()

    lengths = np.array([len(feed) for feed in served], dtype=np.int64)
    feeds = np.repeat(np.arange(lengths.size, dtype=np.int64), lengths)
    ranks = np.concatenate([np.arange(1, length + 1) for length in lengths]).astype(np.int64)
    items = np.concatenate([np.asarray(feed, dtype=np.int64) for feed in served])
    clicks = np.concatenate([
        np.isin(np.asarray(feed, dtype=np.int64), np.asarray(hits, dtype=np.int64))
        for feed, hits in zip(served, chosen, strict=True)
    ]).astype(float)

    journal = Impressions(
        items=np.unique(items, return_inverse=True)[1].astype(np.int64),
        ranks=ranks,
        clicks=clicks,
        feeds=feeds,
        feed_lengths=lengths,
    )

    width = len(catalogue)
    signatures = np.zeros((lengths.size, width), dtype=np.int32)
    sections = np.zeros((lengths.size, width), dtype=np.int32)
    tones = np.zeros((lengths.size, len(tones_order)), dtype=np.int32)
    for row, feed in enumerate(served):
        tally = Counter(section_index[section_of[article]] for article in feed)
        for position, count in tally.items():
            sections[row, position] = count
        for label, count in Counter(tone_of[article] for article in feed).items():
            tones[row, tones_order[label]] = count
        ordered = sorted(tally.values(), reverse=True)
        signatures[row, :len(ordered)] = ordered

    users = np.unique(np.asarray(behaviours["user_id"]), return_inverse=True)[1]
    stamps = np.asarray(behaviours["impression_time"]).astype("datetime64[D]")
    days = (stamps - stamps.min()).astype(np.int64)

    return (journal,
            FeedComposition(signatures, sections, tones, users.astype(np.int64), days),
            width)


def _composition_cells(composition: FeedComposition) -> dict[str, np.ndarray]:
    """Réduit les compositions à leurs **signatures distinctes**, avec leur fréquence.

    L'indice ne dépend que de la répartition des effectifs entre rubriques : deux fils de même
    signature ont le même indice aveugle et le même encadrement exposé. Le condensé ne retient
    donc que les signatures distinctes, ce qui le rend à la fois compact et suffisant.
    """
    signatures = composition.signatures
    unique, occurrences = np.unique(signatures, axis=0, return_counts=True)
    return {
        "feed_signatures": unique.astype(np.int32),
        "feed_occurrences": occurrences.astype(np.int64),
    }


INDEX_BINS = 50


def _blind_index(signatures: np.ndarray, catalogue: int) -> np.ndarray:
    """IDE aveugle au rang de chaque signature de composition."""
    counts = signatures.astype(float)
    totals = counts.sum(axis=1, keepdims=True)
    shares = np.divide(counts, totals, out=np.zeros_like(counts), where=totals > 0)
    logs = np.log2(shares, out=np.zeros_like(shares), where=shares > 0)
    return -(shares * logs).sum(axis=1) / np.log2(catalogue)


def _user_day_cells(composition: FeedComposition, catalogue: int) -> dict[str, np.ndarray]:
    """Agrège les fils d'un même utilisateur sur une même journée.

    C'est la fenêtre que le protocole du dépôt prescrit — vingt-quatre heures glissantes — et
    la grandeur réglementaire est la part de la population sous le plancher, non la moyenne.
    """
    keys, index = np.unique(np.stack([composition.users, composition.days], axis=1), axis=0,
                            return_inverse=True)

    # L'agrégation se fait **à leur place dans le catalogue**, jamais sur les signatures
    # triées : additionner deux vecteurs triés revient à confondre des rubriques différentes
    # au motif qu'elles occupent le même rang, ce qui n'a aucun sens.
    identified = np.zeros((len(keys), composition.sections.shape[1]), dtype=np.int64)
    np.add.at(identified, index, composition.sections)
    voiced = np.zeros((len(keys), composition.tones.shape[1]), dtype=np.int64)
    np.add.at(voiced, index, composition.tones)
    totals = -np.sort(-identified, axis=1)
    unique, occurrences = np.unique(totals, axis=0, return_counts=True)
    # Les compositions **identifiées**, de quoi refaire l'indice sur un autre catalogue.
    # Rubriques et tonalités sont dédupliquées **ensemble** : comparer les deux axes exige
    # que chaque ligne reste la même journée-utilisateur des deux côtés.
    joint = np.concatenate([identified, voiced], axis=1)
    named, named_counts = np.unique(joint, axis=0, return_counts=True)
    width = identified.shape[1]

    # Croisement charge x indice, seul tableau qui permette de chiffrer le prix d'une garantie
    # **par utilisateur** : le plafonnement des contributions retire des journées aux lecteurs
    # les plus assidus, et ceux-là ne ressemblent pas aux autres.
    load = np.bincount(keys[:, 0])[keys[:, 0]]
    values = _blind_index(identified, catalogue)
    edges = np.linspace(0.0, 1.0, INDEX_BINS + 1)
    bins = np.clip(np.digitize(values, edges) - 1, 0, INDEX_BINS - 1)
    crossing = np.zeros((int(load.max()) + 1, INDEX_BINS), dtype=np.int64)
    np.add.at(crossing, (load, bins), 1)

    return {
        "user_day_signatures": unique.astype(np.int32),
        "user_day_occurrences": occurrences.astype(np.int64),
        "user_day_sections": named[:, :width].astype(np.int32),
        "user_day_tones": named[:, width:].astype(np.int32),
        "user_day_section_occurrences": named_counts.astype(np.int64),
        "user_day_load_index": crossing,
        "index_bin_edges": edges,
        "user_days": np.asarray(len(keys), dtype=np.int64),
        "users": np.asarray(len(np.unique(composition.users)), dtype=np.int64),
    }


def build_digest(directory: Path | None = None) -> Digest:
    """Construit le condensé du journal depuis les fichiers bruts."""
    fingerprints = {}
    for name in SOURCES:
        _, _, fingerprint = verify_source(name, directory=directory)
        fingerprints[name] = fingerprint

    journal, composition, catalogue = load_ebnerd(directory=directory)
    tables = {"ebnerd": digest_split(journal)}
    tables["ebnerd"].update(_composition_cells(composition))
    tables["ebnerd"].update(_user_day_cells(composition, catalogue))
    tables["ebnerd"]["catalogue_size"] = np.asarray(catalogue, dtype=np.int64)

    return Digest(sources={"ebnerd": "+".join(sorted(fingerprints.values()))},
                  minimum_impressions=2, splits=tables)


def load_digest(path: Path | None = None) -> Digest:
    """Relit le condensé versionné du journal."""
    return _load_digest(
        DIGEST_PATH if path is None else path,
        rebuild_with="docker compose run --rm lab python scripts/build_ebnerd_digest.py",
    )


def section_counts(digest: Digest, axis: str = "section") -> tuple[np.ndarray, np.ndarray]:
    """Les compositions **identifiées** par journée-utilisateur, et leur fréquence.

    Une ligne par composition distincte, une colonne par modalité du catalogue. C'est ce
    qu'il faut pour refaire l'indice sur un **autre** catalogue — regrouper des rubriques
    exige de savoir lesquelles.

    Args:
        digest: le condensé versionné.
        axis: ``"section"`` pour les rubriques déclarées, ``"tone"`` pour la tonalité. Les
            deux tables partagent l'ordre de leurs lignes : une même journée-utilisateur
            occupe la même ligne des deux côtés, ce qui rend les deux axes comparables.
    """
    if axis not in ("section", "tone"):
        raise ValueError(f"axe d'étiquetage inconnu : {axis!r}")

    arrays = digest.splits["ebnerd"]
    if "user_day_sections" not in arrays:
        raise ValueError("le condensé ne retient pas les compositions identifiées")
    name = "user_day_sections" if axis == "section" else "user_day_tones"
    return arrays[name], arrays["user_day_section_occurrences"]


def load_index_table(digest: Digest) -> tuple[np.ndarray, np.ndarray]:
    """Le croisement charge x indice, et les bornes des classes.

    Une ligne par nombre de journées portées par un même lecteur, une colonne par classe
    d'indice. C'est ce qu'il faut pour chiffrer le prix d'une garantie de confidentialité
    **par utilisateur**.
    """
    arrays = digest.splits["ebnerd"]
    if "user_day_load_index" not in arrays:
        raise ValueError("le condensé ne retient pas le croisement charge x indice")
    return arrays["user_day_load_index"], arrays["index_bin_edges"]


def catalogue_size(digest: Digest) -> int:
    """Nombre de rubriques du catalogue déclaré."""
    return int(digest.splits["ebnerd"]["catalogue_size"])


def signature_counts(digest: Digest, window: str = "feed") -> tuple[np.ndarray, np.ndarray]:
    """Les signatures distinctes et leur fréquence.

    Args:
        digest: le condensé versionné.
        window: ``"feed"`` pour un fil servi, ``"user_day"`` pour tout ce qu'un utilisateur a
            reçu dans une journée — la fenêtre que le protocole prescrit.

    Returns:
        Les signatures, une ligne par composition distincte, et le nombre de fils qu'elle
        représente.
    """
    if window not in ("feed", "user_day"):
        raise ValueError(f"fenêtre inconnue : {window!r}")

    arrays = digest.splits["ebnerd"]
    prefix = "feed_" if window == "feed" else "user_day_"
    return (arrays[prefix + "signatures"],
            arrays[prefix + "occurrences"])
