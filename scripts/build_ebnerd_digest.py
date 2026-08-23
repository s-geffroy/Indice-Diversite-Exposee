#!/usr/bin/env python3
"""Réduit EB-NeRD au condensé versionnable.

Le journal brut pèse 89 Mo et porte une licence de recherche non redistribuable : il n'est
pas versionné. Le condensé retient la structure d'ordre des fils — de quoi rejouer le test
d'échangeabilité — et les **signatures de composition** : les effectifs par rubrique, triés
et anonymes, seule chose dont l'indice dépende.

Usage :

    docker compose run --rm lab python scripts/fetch_ebnerd.py
    docker compose run --rm lab python scripts/build_ebnerd_digest.py
"""

from __future__ import annotations

import argparse

from ide.ebnerd import DIGEST_PATH, build_digest
from ide.logs import save_digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="écrase un condensé déjà présent")
    arguments = parser.parse_args()

    if DIGEST_PATH.exists() and not arguments.force:
        print(f"Condensé déjà présent : {DIGEST_PATH}")
        print("Utiliser --force pour le reconstruire.")
        return 0

    digest = build_digest()
    arrays = digest.splits["ebnerd"]
    print(f"source (SHA-256)        : {digest.sources['ebnerd']}")
    print(f"fils servis             : {arrays['feed_lengths'].size:,}".replace(",", " "))
    print(f"signatures distinctes   : {arrays['feed_signatures'].shape[0]:,}".replace(",", " "))
    print(f"journées-utilisateur    : {int(arrays['user_days']):,}".replace(",", " "))
    print(f"catalogue de rubriques  : {int(arrays['catalogue_size'])}")

    save_digest(digest, DIGEST_PATH)
    size = DIGEST_PATH.stat().st_size / 1e6
    print(f"\nÉcrit : {DIGEST_PATH} ({size:.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
