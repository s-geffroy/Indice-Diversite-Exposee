#!/usr/bin/env python3
"""Récupère EB-NeRD, le premier journal public qui porte le fil servi **et** une étiquette.

EB-NeRD (Ekstra Bladet News Recommendation Dataset, RecSys Challenge 2024) est distribué
**pour usage de recherche uniquement**, sans exploitation commerciale ni redistribution.
L'archive n'est donc pas versionnée, et le dépôt ne porte que son condensé de comptes
agrégés, construit ensuite par ``scripts/build_ebnerd_digest.py``.

Usage :

    docker compose run --rm lab python scripts/fetch_ebnerd.py
    docker compose run --rm lab python scripts/build_ebnerd_digest.py
"""

from __future__ import annotations

import argparse
import sys
import urllib.request
import zipfile

from ide.ebnerd import EBNERD_DIRECTORY, EBNERD_SOURCE, SOURCES, source_path, verify_source


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="retélécharge une archive déjà là")
    arguments = parser.parse_args()

    archive = EBNERD_DIRECTORY / "ebnerd_small.zip"
    if arguments.force or not archive.exists():
        EBNERD_DIRECTORY.mkdir(parents=True, exist_ok=True)
        print(f"Téléchargement : {EBNERD_SOURCE}")
        urllib.request.urlretrieve(EBNERD_SOURCE, archive)  # noqa: S310 — URL fixe et publique

    with zipfile.ZipFile(archive) as bundle:
        bundle.extractall(EBNERD_DIRECTORY / "small")

    failures = 0
    for name in SOURCES:
        conforming, size, fingerprint = verify_source(name)
        print(f"{name} : {source_path(name)}")
        print(f"  taille   : {size:,} octets".replace(",", " "))
        print(f"  SHA-256  : {fingerprint}")
        print(f"  conforme : {'oui' if conforming else 'NON'}")
        failures += 0 if conforming else 1

    if failures:
        print("\nUne table au moins ne correspond pas à son empreinte attendue.", file=sys.stderr)
        return 1

    print("\nCondensé à construire : "
          "docker compose run --rm lab python scripts/build_ebnerd_digest.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
