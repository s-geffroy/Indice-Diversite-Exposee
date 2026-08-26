# Site de documentation bilingue publié sur GitHub Pages.
# Base Debian plutôt que l'image alpine officielle de mkdocs-material : mkdocs-jupyter
# tire nbconvert et ses dépendances, qui disposent de wheels prêtes à l'emploi ici.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Versions **figées**, et non bornées. Une plage ouverte a déjà coûté cher : le rendu des
# notebooks reposait sur une interaction entre deux greffons que rien ne garantissait, et le
# site publiait du JSON brut sans qu'aucune alerte ne le signale. Les notebooks sont désormais
# rendus par `scripts/render_notebooks.py` avant MkDocs, d'où `nbconvert` en dépendance directe.
RUN pip install --no-cache-dir \
        "mkdocs==1.6.1" \
        "mkdocs-material==9.7.7" \
        "mkdocs-static-i18n==1.3.1" \
        "nbconvert==7.17.1" \
        "pymdown-extensions==10.16.1"

WORKDIR /docs
EXPOSE 8000
