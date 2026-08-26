#!/usr/bin/env python3
"""Convertit les notebooks en Markdown pour le site, sans dépendre d'un greffon.

Le site employait ``mkdocs-jupyter``. Ce greffon enveloppe les fichiers ``.ipynb`` dans une
classe qui les rend comme des pages ; ``mkdocs-static-i18n`` reconstruit ensuite la collection
de fichiers et **perd cette enveloppe**. Le notebook était alors recopié tel quel : le lecteur
recevait le JSON brut. Aucune version de l'un ou l'autre greffon ne corrige cette interaction,
et rien dans la construction ne le signalait — le site se construisait en mode strict sans une
seule alerte.

Le rendu est donc fait ici, avant MkDocs, par ``nbconvert``. Le dépôt le contrôle, un test le
vérifie, et il n'y a plus d'interaction entre greffons à espérer.

Usage :

    docker compose run --rm site-build   # l'appelle automatiquement
    python scripts/render_notebooks.py --source notebooks --destination docs/notebooks
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

SOURCE_LINK = re.compile(r"\(([^)]*?)\.ipynb\)")
DOCS_LINK = re.compile(r"\((\.\./)?(?:docs/)?([^)/]+\.md)\)")
NOTEBOOK_NAME = re.compile(r"^\d+_")


def _retarget(match: re.Match[str]) -> str:
    """Réécrit un lien du notebook vers l'arborescence du site.

    Un notebook vit dans ``notebooks/`` et vise les pages par ``../docs/page.md`` ; une fois
    rendu, il vit dans ``docs/notebooks/`` et doit viser ``../page.md``. Les liens d'un
    notebook à l'autre, eux, restent relatifs au même dossier.
    """
    target = match.group(2)
    if NOTEBOOK_NAME.match(target):
        return f"({target})"
    return f"(../{target})"


def render(source: Path, destination: Path) -> int:
    """Rend chaque notebook en Markdown, images comprises, et rend leur nombre."""
    from nbconvert import MarkdownExporter  # dépendance du site, pas du noyau
    from traitlets.config import Config

    settings = Config()
    settings.MarkdownExporter.exclude_input_prompt = True
    settings.MarkdownExporter.exclude_output_prompt = True
    exporter = MarkdownExporter(config=settings)

    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    notebooks = sorted(source.glob("*.ipynb"))
    for notebook in notebooks:
        body, resources = exporter.from_filename(str(notebook))

        # Les liens d'un notebook à l'autre visent le .ipynb ; après rendu, c'est le .md
        # qui existe comme page, et un lien mort ferait échouer la construction stricte.
        body = SOURCE_LINK.sub(r"(\1.md)", body)
        body = DOCS_LINK.sub(_retarget, body)
        body += (
            f"\n\n---\n\n*Source exécutable : "
            f"[`{notebook.name}`](https://github.com/s-geffroy/Indice-Diversite-Exposee/"
            f"blob/main/notebooks/{notebook.name})*\n"
        )
        (destination / f"{notebook.stem}.md").write_text(body, encoding="utf-8")

        for name, payload in resources.get("outputs", {}).items():
            (destination / name).write_bytes(payload)

    return len(notebooks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("notebooks"))
    parser.add_argument("--destination", type=Path, default=Path("docs/notebooks"))
    arguments = parser.parse_args()

    count = render(arguments.source, arguments.destination)
    print(f"{count} notebooks rendus dans {arguments.destination}")
    return 0 if count else 1


if __name__ == "__main__":
    raise SystemExit(main())
