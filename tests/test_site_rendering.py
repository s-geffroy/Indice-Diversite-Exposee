"""Le rendu des notebooks pour le site, et le contrôle qui manquait.

Le site s'est construit en mode strict pendant des mois en publiant les notebooks en **JSON
brut** : le greffon qui devait les rendre voyait son travail défait par celui qui gère les deux
langues. Aucune alerte, aucun test, aucune trace. Ces tests couvrent le rendu qui remplace cette
interaction, et le contrôle qui regarde désormais le site fini.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load(name: str):
    """Charge un script du dépôt comme un module."""
    specification = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


render_notebooks = load("render_notebooks")
check_site = load("check_site")


class TestRecibleDesLiens:
    """Un notebook déplacé dans le site ne vise plus les mêmes chemins."""

    @staticmethod
    def retarget(text: str) -> str:
        return render_notebooks.DOCS_LINK.sub(render_notebooks._retarget, text)

    def test_un_lien_vers_une_page_remonte_d_un_dossier(self):
        attendu = "voir [l'audit](../limites.md)"
        assert self.retarget("voir [l'audit](../docs/limites.md)") == attendu
        assert self.retarget("voir [l'audit](limites.md)") == attendu

    def test_un_lien_d_un_notebook_a_l_autre_reste_dans_le_dossier(self):
        rendered = self.retarget("voir [le notebook 10](10_changement_de_regime.md)")
        assert rendered == "voir [le notebook 10](10_changement_de_regime.md)"

    def test_un_lien_deja_correct_n_est_pas_deplace_deux_fois(self):
        assert self.retarget("[x](../ide.md)") == "[x](../ide.md)"

    def test_le_lien_source_vers_le_notebook_devient_le_rendu(self):
        rendered = render_notebooks.SOURCE_LINK.sub(r"(\1.md)", "[a](09_calibration.ipynb)")
        assert rendered == "[a](09_calibration.md)"


class TestControleDuSite:
    """Une construction qui réussit ne prouve rien sur ce qu'elle produit."""

    @staticmethod
    def build(tmp_path: Path, page: str) -> tuple[Path, Path]:
        notebooks = tmp_path / "notebooks"
        notebooks.mkdir()
        (notebooks / "01_essai.ipynb").write_text(json.dumps({"cells": []}))
        site = tmp_path / "site"
        (site / "notebooks" / "01_essai").mkdir(parents=True)
        (site / "notebooks" / "01_essai" / "index.html").write_text(page)
        return site, notebooks

    def test_une_page_rendue_passe(self, tmp_path):
        site, notebooks = self.build(tmp_path, "<!doctype html>\n<html>ok</html>")
        assert check_site.check(site, notebooks) == []

    def test_le_json_brut_est_detecte(self, tmp_path):
        """C'est exactement la panne qui a vécu des mois sans être vue."""
        site, notebooks = self.build(tmp_path, '{\n "cells": [\n  {"cell_type": "markdown"}]}')
        failures = check_site.check(site, notebooks)

        assert failures
        assert any("non rendu" in failure for failure in failures)

    def test_une_page_absente_est_detectee(self, tmp_path):
        site, notebooks = self.build(tmp_path, "<!doctype html>")
        (site / "notebooks" / "01_essai" / "index.html").unlink()

        assert any("absente" in failure for failure in check_site.check(site, notebooks))

    def test_un_dossier_sans_notebook_est_refuse(self, tmp_path):
        (tmp_path / "vide").mkdir()
        assert check_site.check(tmp_path, tmp_path / "vide")
