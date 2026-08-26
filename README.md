# Indice de Diversité Exposée (IDE)

**Mesurer la diversité qu'un fil algorithmique expose réellement — et éprouver ce qu'on croit en savoir.**

[![Licence : MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Documentation : CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS)
[![Champ : mesure de l'exposition](https://img.shields.io/badge/champ-mesure%20de%20l'exposition-8a2be2.svg)](https://s-geffroy.github.io/Indice-Diversite-Exposee/)
[![Tests : 261](https://img.shields.io/badge/tests-261-brightgreen.svg)](tests/)

📖 **[Documentation complète](https://s-geffroy.github.io/Indice-Diversite-Exposee/)**
· [English](https://s-geffroy.github.io/Indice-Diversite-Exposee/en/)

---

## Résumé

Un **instrument**, et rien d'autre : une mesure de la diversité qu'un fil d'actualité expose
réellement à son lecteur, calculable sans accès au code de la plateforme — avec tout ce qu'il faut
pour l'établir, l'attaquer, et le mesurer sur des journaux réels.

### Le verdict

| Objet | État |
|---|---|
| l'indice tel qu'il était d'abord proposé | **intenable** : saturable à coût nul, puis contournable par l'enterrement |
| la forme retenue | **définie et attaquée** : entropie des contenus servis sur un catalogue déclaré, pondérée par l'attention de chaque rang |
| l'exposition, dont dépend cette pondération | **mesurée** : 0,88 ± 0,05 et non 1 par convention, sans cascade, transportable à 6 % près |
| l'indice **aveugle au rang**, sur des fils réels | **mesuré** : 0,50 par journée-utilisateur, 5,1 rubriques effectives sur 26 |
| l'indice **exposé**, sur ces mêmes fils | **encadré, non mesuré** : la colonne d'ordre du seul jeu qui l'offre ne contient pas le rang |
| le **catalogue** de points de vue | il décide du niveau — 0,50 sur 26 rubriques, 0,92 sur 3 — mais l'ordre entre lecteurs tient jusqu'à six |
| les instruments de mesure | **valides après correction** : trois restreints, trois conclusions retirées |

**L'indice tient comme mesure, pas comme norme.** Ce qu'il faut pour le calculer se mesure —
l'attention, sa forme, sa portabilité. Ce qu'il faudrait pour l'imposer — un niveau, un catalogue,
une grandeur agrégée — ne se déduit d'aucune mesure.

### Ce qui tient

- **Trois contrôles à passer sur un journal, dans cet ordre** : l'**échangeabilité** — l'ordre
  dit-il quelque chose ? — qui ne détecte rien dans MIND ($z = +0{,}12$) et rejette à $z = -206$
  sur Baidu-ULTR ; l'**identifiabilité**, nécessaire et non suffisante ; et la **forme** — l'examen
  dépend-il de ce qui a été cliqué au-dessus ?
- **Une exposition mesurée, et non plus supposée** : $\eta = 0{,}88 \pm 0{,}05$ sur 143 documents,
  par affichage plutôt que par clic. La **cascade est réfutée** par deux voies indépendantes, et la
  loi en $R^{-\eta}$ est le **pire** des trois ajustements sur la courbe mesurée.
- **Cette mesure est transportable d'une page à l'autre** : à contenu tenu fixe, la composition de
  la page ne déplace l'examen que de **6 %** et l'indice que de **0,0025** — quatorze fois moins
  que la convention $1/R$.
- **Un encadrement exact quand l'ordre manque** : largeur médiane **0,104** sur 232 887 fils réels.
- **Un premier chiffre réel** : la diversité **servie** vaut 0,50 par journée-utilisateur, et le
  catalogue déplace ce niveau bien plus que le fil lui-même.

### Ce qui est tombé

**Sur le monde** : aucun jeu public ne permet la mesure annoncée — mais pas pour la raison publiée,
c'est la **colonne d'ordre qui ne contient pas l'ordre** ; l'examen n'est ni une cascade ni une loi
de puissance ; la sévérité ne se transporte pas d'une surface à l'autre ; aucun estimateur
contrefactuel ne remplace l'exploration.

**Sur les propositions du dépôt lui-même** : un plancher d'indice se sature à coût nul ; le premier
correctif prescrivait la polarisation ; « la proximité à la cible résiste le mieux » était un
artefact d'échelle ; l'explication du « pli d'écran » est fausse ; et l'effet de format publié
était pour les deux tiers une **composition**.

## À lire d'abord : ce que le travail ne prétend pas

L'**[audit critique](docs/limites.md)** recense **vingt-sept corrections** apportées au
raisonnement, dont cinq formules invalides et une moitié qui porte sur les propositions du dépôt
lui-même. Neuf résultats négatifs y sont publiés comme tels.

**Trois moitiés ont été retirées.** Le projet est parti d'une analogie entre décohérence quantique
et effondrement du consensus, en a tiré un formalisme emprunté à la physique statistique, un
algorithme de recommandation et un cadre de régulation. L'analogie a été réfutée transfert par
transfert ; la seule prédiction testable du formalisme a été mesurée quatre fois sans effet ;
l'appareil de régulation a été vidé de sa substance par ses propres mesures. L'audit en garde le
registre entier — c'est le registre de ce que ce travail a eu faux, et c'est la partie qu'on ne
supprime pas.

## Démarrer

Tout passe par Docker, rien n'est installé localement.

```bash
docker compose run --rm test          # 261 tests, dont les exemples de docstrings
docker compose run --rm lint          # ruff
docker compose run --rm notebooks     # exécute les notebooks, régénère les figures
docker compose up site                # http://localhost:8000
```

Les journaux bruts ne sont pas versionnés — licences propres, plusieurs gigaoctets — mais leurs
**condensés** le sont, et tout se recalcule à l'identique depuis eux :

```bash
docker compose run --rm lab python scripts/fetch_mind.py
docker compose run --rm lab python scripts/build_mind_digest.py
```

## Structure

```
src/ide/            l'indice, les journaux, l'exposition — onze modules purs
notebooks/          les douze chapitres exécutables ; les numéros ont des trous,
                    ce sont ceux des chapitres retirés
docs/               le site bilingue, audit compris
data/               les condensés versionnés ; les journaux bruts sont ignorés
paper/              les deux notes LaTeX et leurs figures
scripts/            récupération des journaux, condensés, rendu du site
```

## Ce qui est vérifié, et comment

- **261 tests** verrouillent chaque chiffre publié, y compris ceux qui ont dû être corrigés.
- **Le site est vérifié page par page** après construction : une construction qui réussit ne prouve
  rien tant qu'on n'a pas regardé ce qu'elle produit — le dépôt a publié ses notebooks en JSON brut
  pendant des mois sans qu'une seule alerte le signale.
- **Les notebooks sont rejoués** en intégration continue, depuis les seuls condensés versionnés.

## Relecture

Ce travail est **ouvert à la relecture critique** et n'a été relu par personne. Les retours sur la
forme retenue de l'indice, sur les instruments de mesure, et sur la discrétisation en points de vue
sont les plus utiles. → **[Appel à relecture](docs/relecture.md)**

## Licences

Code (`src/`, `tests/`, `notebooks/`, `legacy/`) sous [MIT](LICENSE) · contenus
rédactionnels (`docs/`, `paper/`) sous [CC BY 4.0](LICENSE-DOCS).
