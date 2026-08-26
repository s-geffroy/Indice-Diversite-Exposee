#!/usr/bin/env python3
"""Vérifie que le site construit contient bien ce qu'il prétend publier.

Ce contrôle existe pour une raison précise. Le site s'est construit pendant des mois en mode
strict, sans une alerte, alors que **chaque notebook était publié en JSON brut** : le greffon
qui devait les rendre voyait son travail défait par celui qui gère les deux langues, et rien
dans la chaîne ne comparait le résultat à l'intention.

Une construction qui réussit ne prouve donc rien sur ce qu'elle produit. Ce script regarde le
site fini.

Usage :

    docker compose run --rm site-build   # l'appelle automatiquement
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def check(site: Path, notebooks: Path) -> list[str]:
    """Rend la liste des manquements constatés sur le site construit."""
    failures: list[str] = []

    sources = sorted(notebooks.glob("*.ipynb"))
    if not sources:
        return [f"aucun notebook trouvé dans {notebooks}"]

    for notebook in sources:
        page = site / "notebooks" / notebook.stem / "index.html"
        if not page.exists():
            failures.append(f"{notebook.stem} : page absente du site")
            continue

        content = page.read_text(encoding="utf-8", errors="replace")
        if not content.lstrip().lower().startswith("<!doctype html"):
            failures.append(f"{notebook.stem} : publié tel quel, non rendu")
        elif '"cell_type"' in content[:2000]:
            failures.append(f"{notebook.stem} : le JSON du notebook affleure dans la page")

    # Aucune page du site ne doit commencer par le JSON d'un notebook, dans aucune langue.
    for page in site.rglob("index.html"):
        if page.read_text(encoding="utf-8", errors="replace").lstrip().startswith('{'):
            failures.append(f"{page.relative_to(site)} : JSON brut publié")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--notebooks", type=Path, default=Path("notebooks"))
    arguments = parser.parse_args()

    failures = check(arguments.site, arguments.notebooks)
    if failures:
        print("Le site construit ne publie pas ce qu'il annonce :", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    count = len(list(arguments.notebooks.glob("*.ipynb")))
    print(f"site vérifié : {count} notebooks rendus en HTML")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
