# Les deux dernières colonnes, et une hypothèse abandonnée

!!! success "La cascade réfutée une seconde fois, par un compteur"
    `slipoff_count_after_click` est non nul pour **43,7 %** des lignes cliquées et **0,5 %** des
    autres. Après un clic, le journal enregistre explicitement que des documents ont défilé : le
    lecteur est revenu. Sous cascade stricte, cette colonne serait toujours nulle.

!!! failure "Corrigé — les deux tiers de cet effet étaient une composition"
    Ce chapitre a mesuré qu'un format enrichi au-dessus retire **8,4 points** d'examen à ce qui
    suit, à rang **et** à hauteur de page comparables, et en a conclu que la remise d'attention
    $w_R$ était une propriété de la **page servie**. Le contrôle qui manquait était le
    **contenu** : à contenu tenu fixe, il ne reste que **6 %** au lieu de 18 %, et une simulation
    sans aucun effet reproduit presque exactement le chiffre publié ici.

    Ce qui suit est conservé tel qu'il a été publié. Sa correction est
    [au chapitre suivant](effet-de-page.md).

!!! failure "Et une hypothèse que j'avais avancée est fausse"
    Le [pli d'écran](exposition-mesuree.md) — « l'exposition serait affaire de pixels, non de
    rang » — ne tient pas. Le rang explique mieux ($R^2$ de McFadden **0,082**) que la hauteur
    cumulée (**0,057**), et les pixels n'ajoutent que **0,0007** une fois le rang connu.

---

## Ce qui restait à lire

L'[exposition mesurée](exposition-mesuree.md) s'est terminée sur deux colonnes laissées de côté.
Elles font ici trois choses : l'une confirme une hypothèse par une voie indépendante, l'autre en
établit une nouvelle, et une troisième — formulée avec assurance au chapitre précédent — ne
survit pas à sa vérification.

![Format et retour](figures/fig24_format_et_retour.png)

/// caption
Le retour après clic ; l'effet d'un format enrichi au-dessus ; la survie de cet effet une fois la
géométrie neutralisée ; et l'hypothèse du pli d'écran mise en échec. Figure régénérée par
[le notebook 24](notebooks/24_format_et_retour.md).
///

## 1. Le retour après clic, mesuré

Le chapitre précédent avait constaté que l'examen se poursuit sous un clic, et proposé une
explication : *« un lecteur qui clique, revient, puis poursuit sa lecture »*. C'était une
hypothèse avancée pour expliquer un signe inattendu.

`slipoff_count_after_click` la vérifie directement : elle compte les documents sortis de l'écran
**après** un clic, et ne peut être non nulle que si le lecteur est revenu.

| Rang du contenu cliqué | Part des clics suivis d'un défilement |
|---|---|
| 1 | 0,374 |
| 3 | 0,469 |
| 6 | **0,586** |
| 8 | 0,526 |

La part **croît avec la profondeur du clic**, ce qui se lit sans peine : un lecteur qui a dû
descendre pour trouver n'a pas fini de chercher.

**Deux voies indépendantes concordent.** L'[exposition mesurée](exposition-mesuree.md) a réfuté
la cascade par un test statistique sur l'examen ; cette colonne la réfute par un **fait
consigné**. C'est ce qu'on peut demander de mieux à une réfutation.

## 2. Le format modifie l'exposition

Un format enrichi — encadré de réponse, image, tableau — est plus haut : 273 pixels en médiane
contre 192 pour un résultat ordinaire. L'hypothèse naturelle est donc géométrique : un contenu
enrichi en tête repousserait les suivants vers le bas de l'écran.

Elle se teste en neutralisant la hauteur — à rang égal **et** à pixels cumulés comparables :

| Rang | Bande de pixels | Sans enrichi | Avec enrichi | Écart |
|---|---|---|---|---|
| 3 | tiers médian | 0,800 | 0,722 | −0,078 |
| 6 | tiers médian | 0,367 | 0,280 | −0,087 |
| 9 | tiers médian | 0,266 | 0,178 | −0,088 |

**Écart médian sur 21 strates : −0,084**, toutes de même signe. L'effet subsiste une fois la
géométrie neutralisée : ce n'est pas un effet de repoussement.

L'explication qui reste est celle de la **satisfaction** : un encadré de réponse répond à la
question, et le lecteur cesse de descendre. C'est la lecture que propose la littérature sur la
« page entière », et le chiffre lui donne raison ici.

!!! danger "Ce que cela retire à toute mesure fondée sur le rang seul"
    L'exposition d'un contenu au rang $R$ dépend du **format de ce qui est au-dessus**, et cette
    dépendance ne se réduit ni au rang ni à la place occupée. Aucune loi $e(R)$ — puissance,
    géométrique ou autre — ne peut la représenter, puisqu'elle ne prend pas la page en argument.

    Deux fils de composition identique, servis avec des formats différents, n'exposent pas la
    même chose.

!!! failure "Retiré — cette conclusion supposait un contrôle qui manquait"
    Les strates ci-dessus tiennent le rang et les pixels fixes, mais **pas le contenu**. Un
    encadré de réponse ne s'affiche pas au hasard : il répond à une question factuelle, qui
    n'appelle pas la même lecture. Une fois le même document comparé à lui-même au même rang,
    l'écart tombe à 6 % — et l'incidence sur l'indice à $0{,}0025$, quatorze fois moins que celle
    de la convention $1/R$ qu'il devait disqualifier. → [l'effet de page](effet-de-page.md)

## 3. Une hypothèse retirée

Le chapitre précédent avait constaté que la courbe d'examen mesurée n'est pas une loi de
puissance, et proposé un modèle à **pli d'écran**. J'avais écrit :

> C'est la signature d'un **seuil d'écran** […] La colonne `serp_height` encode précisément la
> hauteur de page, donc le rang où ce seuil tombe.

C'était une hypothèse mécanique, et `serp_height` permet de la tester.

| Modèle | $R^2$ de McFadden |
|---|---|
| log(rang) seul | **0,0820** |
| pixels cumulés seuls | 0,0567 |
| les deux | 0,0827 |

Le rang explique **mieux** que les pixels, et ceux-ci n'ajoutent que 0,0007. À rang égal, les
pixels ne comptent qu'aux deux premiers rangs (+0,196 et +0,138 d'amplitude) et l'effet s'éteint
ensuite — l'inverse de ce qu'un seuil d'écran prédirait.

!!! failure "Hypothèse retirée : « l'exposition est affaire de pixels, non de rang »"
    Le **constat** du chapitre précédent tient : la courbe mesurée n'est pas une loi de
    puissance, et un modèle à deux régimes l'ajuste mieux. C'est l'**explication mécanique** que
    j'en avais donnée qui tombe. La forme en deux temps existe ; elle ne vient pas de la
    géométrie de la page.

Ce que la mesure suggère à la place, sans l'établir : la décroissance vient du **contenu** plus
que de la place. Un format enrichi en tête satisfait le besoin — section 2 — et ce qui suit n'est
plus consulté quelle que soit sa position à l'écran.

## 4. Ce qui s'ajoute à la demande d'accès aux données

Le tableau 3 réclame déjà une colonne `affichages`. Il en faudrait une
quatrième : le **format** du contenu servi, catégorie déclarée par la plateforme.

Sans elle, deux fils de composition identique peuvent exposer des diversités différentes sans que
rien ne le signale — et un plancher devient dépendant d'une variable qu'on ne voit pas. C'est
aussi une variable **peu sensible** : le format d'un contenu ne dit rien de son lecteur.

!!! failure "Révisé — la colonne reste utile, elle n'est plus nécessaire"
    Une fois l'effet mesuré à contenu fixé, son incidence sur l'indice est de $0{,}0025$. La
    colonne `format` ne conditionne donc plus le calcul ; elle sert à **vérifier** ce chapitre
    sur une autre plateforme. → [l'effet de page](effet-de-page.md)

## Réserves

`slipoff_count_after_click` mesure un défilement **après** un clic, pas un examen : il atteste que
le lecteur est revenu, non qu'il ait regardé ce qui a défilé. La réfutation de la cascade stricte
tient ; l'ampleur du retour, non.

`media_type` compte 437 valeurs distinctes dont la signification n'est pas documentée. Le
regroupement en « ordinaire » (valeur 0, 68,8 % des lignes) contre « enrichi » est un choix de ce
dépôt, non une catégorisation de la plateforme, et un découpage plus fin donnerait peut-être un
autre résultat.

Enfin, ce chapitre lit le **journal brut** et non le condensé : croiser rang, pixels et format
n'a pas d'équivalent agrégé, et porter ces strates dans le condensé multiplierait les cellules.
C'est le seul chapitre du dépôt dans ce cas.

Il en découle qu'il est **écarté du balayage d'intégration continue**, qui régénère les
vingt-quatre autres. Le reproduire demande de récupérer d'abord le journal
(`scripts/fetch_exposure.py`), puis `docker compose run --rm notebooks-full`. C'est une entorse à
la règle du dépôt — tout doit se régénérer depuis ce qui est versionné — et elle est signalée ici
plutôt que laissée à découvrir.

---

*Notebook : [24 — Format et retour](notebooks/24_format_et_retour.md) ·
[exposition mesurée](exposition-mesuree.md) · [le test de forme](test-de-forme.md)*
