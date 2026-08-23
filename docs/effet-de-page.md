# L'effet de page, une fois la composition retirée

!!! danger "Une conclusion de ce dépôt, corrigée d'un facteur trois"
    Le [chapitre précédent](format-et-retour.md) mesurait qu'un format enrichi servi plus haut
    retire **18 %** d'examen à ce qui suit. À **contenu tenu fixe**, il en reste **6 %**
    (RR = 0,940, IC95 [0,916 ; 0,964]). Les deux tiers de l'effet publié étaient une
    **composition** : quelles requêtes déclenchent un encadré de réponse, non ce que l'encadré
    fait au lecteur.

!!! success "Deux appariements indépendants concordent"
    Même document au même rang : **0,940**. Même requête au même rang : **0,942** — sur sept fois
    moins d'impressions, et sans établir seul. Deux plans qui ne partagent aucune strate rendent
    le même chiffre à deux millièmes près.

!!! tip "Et la loi de rang, que ce chapitre devait enterrer, tient"
    Ignorer la composition de la page déplace l'indice de **0,0025** ; employer la convention
    $1/R$ au lieu de la courbe mesurée le déplace de **0,0350**. **Quatorze fois plus.** Ce qui
    menace la mesure n'est pas la page, c'est de ne pas avoir mesuré.

---

## Ce que le chapitre précédent avait conclu

Il avait comparé les pages enrichies aux autres, à rang **et** à hauteur de page comparables, et
lu un écart de huit points d'examen sur une base de 0,45. Il en avait tiré une affirmation large :

> L'exposition d'un contenu au rang $R$ dépend du format de ce qui est au-dessus […] Aucune loi
> $e(R)$ — puissance, géométrique ou autre — ne peut la représenter, puisqu'elle ne prend pas la
> page en argument.

Cette affirmation reposait sur un contrôle qui manquait : **le contenu**. Un encadré de réponse
ne s'affiche pas au hasard. Il répond à une question factuelle, qui n'appelle pas la même lecture
qu'une recherche exploratoire. L'écart mesuré pouvait donc venir du format, ou de *ce sur quoi*
le format apparaît.

![L'effet de page](figures/fig25_effet_de_page.png)

/// caption
La description, l'effet une fois le contenu tenu fixe, son absence de tendance avec la
profondeur, et ce que coûte réellement d'ignorer la page. Figure régénérée par
[le notebook 25](notebooks/25_effet_de_page.ipynb).
///

## 1. Le contrôle qui décide de la suite

Règle du dépôt, acquise trois fois à ses dépens : appliquer d'abord le protocole à des données
dont on connaît la réponse.

On simule un monde où le format n'a **aucun** effet sur l'examen, mais où les pages enrichies
tombent sur des contenus systématiquement moins consultés — le confondant soupçonné, et rien
d'autre.

| Effet simulé | Lu en stratifiant par le rang | Lu à contenu fixé |
|---|---|---|
| **1,00** — aucun effet | **0,785** | 1,005 (IC95 [0,993 ; 1,016]) |
| **0,90** — effet connu | 0,701 | **0,896** (IC95 [0,886 ; 0,907]) |

L'appariement passe les deux épreuves. La stratification par le rang seul échoue à la première :
elle lit un effet franc dans un monde qui n'en porte aucun — et le chiffre qu'elle fabrique,
**0,785**, est à peu près celui que ce dépôt avait publié.

## 2. La mesure

| Lecture | RR | IC95 | Impressions |
|---|---|---|---|
| contraste brut | 0,613 | — | 452 689 |
| stratifié par rang | 0,817 | [0,812 ; 0,823] | 452 689 |
| **même document, même rang** | **0,940** | [0,916 ; 0,964] | 31 045 |
| même requête, même rang | 0,942 | [0,869 ; 1,022] | 4 261 |

Rang par rang, aucune tendance : l'effet ne se creuse pas avec la profondeur, et les intervalles
se recouvrent tous. L'hypothèse la plus simple qui reste est celle d'un **facteur constant**.

## 3. Ce que coûte, en pratique, d'ignorer la page

L'affirmation « aucune loi $e(R)$ ne peut représenter cela » se teste en la chiffrant. Sur quatre
mille fils simulés de neuf rangs et quatre points de vue :

| Ce qu'on ignore | Écart d'indice médian | 99ᵉ centile |
|---|---|---|
| la composition de la page | **0,0025** | 0,0066 |
| la mesure, remplacée par la convention $1/R$ | **0,0350** | 0,0735 |

Un facteur constant est une **homothétie**, à laquelle un indice normalisé est insensible ; seul
le rang 1, qui ne porte jamais rien au-dessus de lui, empêche l'effet de disparaître tout à fait.
C'est pourquoi six points de risque relatif ne font que deux millièmes d'indice.

Sur la sévérité, même ordre : $\eta = 0{,}876$ en ignorant la page, $0{,}854$ sur la page
contrefactuelle nue. **Deux centièmes.**

## 4. Ce que cela change

**L'ordre des priorités s'inverse.** Ce qu'un régulateur doit exiger d'abord n'est pas le format
servi, mais la **mesure de l'exposition elle-même** — la colonne `affichages`. La colonne
`format` de la [demande d'accès](article-40.md) reste utile, parce qu'elle permet de vérifier ce
chapitre ailleurs, mais elle **cesse d'être nécessaire** au calcul de l'indice.

**Et la remise d'attention redevient transportable.** C'était l'enjeu réel : si $w_R$ dépendait
de la page, aucun plancher réglementaire ne pouvait s'écrire sans décrire chaque page servie.
Il en dépend, de 6 %, et l'indice n'en bouge que de 0,0025.

## Réserves

L'appariement à contenu fixé ne retient que **1 106 strates sur 404 478** : ce sont les documents
servis au même rang dans des pages de compositions différentes, et rien ne garantit qu'ils
ressemblent aux autres. Le chiffre vaut pour eux.

L'appariement par requête est indépendant et concorde, mais il est sept fois moins peuplé : il
**n'établit rien seul**, son intervalle contenant 1.

Le regroupement de `media_type` en « ordinaire » contre « enrichi » reste un choix de ce dépôt,
et non une catégorisation de la plateforme.

Enfin, ce chapitre ne dit pas que la page est sans effet — l'intervalle de l'appariement le plus
peuplé exclut 1. Il dit que l'effet est **trois fois plus petit** que publié, et que son
incidence sur la grandeur réglementée est négligeable devant celle de la convention qu'il
remplace.

---

*Notebook : [25 — L'effet de page](notebooks/25_effet_de_page.ipynb) ·
[format et retour](format-et-retour.md) · [exposition mesurée](exposition-mesuree.md) ·
[demande au titre de l'article 40](article-40.md)*
