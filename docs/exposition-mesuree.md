# L'exposition enfin mesurée, et non plus estimée

!!! success "L'impasse du test de forme est levée"
    Sur la mesure d'**examen** plutôt que sur le clic, cascade et budget de clics se séparent
    parfaitement : $z = -158$ à $-412$ sous cascade, $z = -1{,}03$ sous budget **quel que soit le
    budget**. Ce que les clics confondaient, l'affichage le tranche.

!!! failure "Sur Baidu-ULTR, la cascade est réfutée"
    L'examen sous un clic est **plus** fréquent, pas moins — 0,221 contre 0,136 au neuvième rang,
    $z = +8{,}4$ à $+10{,}9$ selon le seuil. Une cascade le rendrait nul.

!!! danger "Et le chiffre publié par ce dépôt est révisé"
    $\eta_{\text{examen}} = 0{,}882 \pm 0{,}046$ sur **143 documents**, contre
    $\eta_{\text{clic}} = 1{,}085 \pm 0{,}093$ sur 55. L'estimation par les clics **surestime la
    décroissance de 23 %**, parce qu'un clic mélange l'examen et l'attrait.

!!! warning "La loi de puissance est le pire des trois ajustements"
    Sur la courbe **mesurée** : $R^2 = 0{,}72$ et 42 % d'écart maximal, contre $0{,}96$ pour une
    décroissance géométrique et $0{,}99$ pour un modèle à **pli d'écran**. Au deuxième rang, elle
    prédit 0,47 quand la mesure donne 0,88.

---

## Ce que ces colonnes contiennent

Le [test de forme](test-de-forme.md) s'est arrêté sur une impasse — un budget de clics imite une
cascade — et une piste : Baidu-ULTR publie `displayed_time`, `serp_height` et
`slipoff_count_after_click`, que ce dépôt n'avait jamais lues.

`displayed_time` est peuplée et parlante : 1,6 % de valeurs nulles au premier rang, 92 % au
douzième. C'est une mesure directe de ce qui a été **montré**, là où tout le reste du dépôt
n'observait que ce qui avait été **cliqué**.

![L'exposition mesurée](figures/fig23_exposition_mesuree.png)

/// caption
La discrimination cascade / budget sur l'examen ; l'examen après un clic sur Baidu-ULTR ;
l'exposition mesurée contre l'exposition estimée ; et les trois formes ajustées sur la courbe
mesurée. Figure régénérée par [le notebook 23](notebooks/23_exposition_mesuree.ipynb).
///

## 1. Le contrôle, d'abord

La règle du dépôt : appliquer tout protocole à des données dont on connaît la réponse avant de le
porter sur des données réelles.

| Journal simulé | $z$ sur le **clic** | $z$ sur l'**examen** |
|---|---|---|
| cascade, $\gamma = 0{,}95$ | −206,7 | **−412,2** |
| cascade, $\gamma = 0{,}85$ | −151,5 | −295,4 |
| cascade, $\gamma = 0{,}60$ | −84,2 | −157,8 |
| position, budget = 1 | −121,8 | **−1,03** |
| position, budget = 2 | −18,6 | −1,03 |
| position, budget illimité | 0,00 | −1,03 |

Sur les **clics**, cascade et budget sont confondus : deux rejets massifs qu'aucun seuil ne
sépare. Sur l'**examen**, la séparation est totale. La limite d'identification du chapitre
précédent tombe dès qu'on dispose d'une mesure de ce qui a été montré.

## 2. Sur Baidu-ULTR

| Seuil d'impressions | $z$ sur l'examen | $p$ | Cellules |
|---|---|---|---|
| 2 | +10,87 | $1{,}7 \times 10^{-27}$ | 1 736 |
| 5 | +9,08 | $1{,}1 \times 10^{-19}$ | 527 |
| 10 | +8,86 | $7{,}8 \times 10^{-19}$ | 269 |
| 20 | +8,38 | $5{,}2 \times 10^{-17}$ | 165 |

La mesure d'examen est aussi **bien mieux dotée** que celle des clics : 1 736 cellules contre 780,
parce qu'un document est bien plus souvent affiché que cliqué.

| Rang | Examen après un clic | Sans clic | Écart |
|---|---|---|---|
| 2 | 0,855 | 0,877 | −0,022 |
| 4 | 0,479 | 0,412 | +0,067 |
| 6 | 0,307 | 0,221 | +0,086 |
| 9 | 0,221 | 0,136 | +0,085 |

**Sous cascade, l'examen après un clic devrait être nul.** Il est plus élevé, et l'écart s'installe
dès le troisième rang. C'est le **confondant d'hétérogénéité** mesuré directement : un lecteur qui
clique est un lecteur engagé, qui défile plus loin.

!!! note "Ce que `displayed_time` mesure, et ce qu'il ne mesure pas"
    Un temps d'affichage positif atteste que le document a été **montré**, non qu'il ait été
    **regardé** — c'est un substitut, meilleur que le clic mais imparfait. Il se peut aussi qu'il
    soit enregistré au retour d'un clic : un lecteur qui clique, revient, puis poursuit. Cette
    lecture reste incompatible avec une cascade stricte, qui suppose la session terminée.

## 3. Mesurer plutôt qu'estimer

| Méthode | $\hat\eta$ | Documents |
|---|---|---|
| effets fixes sur le **clic** | 1,085 ± 0,093 | 55 |
| effets fixes sur l'**examen** | **0,882 ± 0,046** | **143** |

| Rang | Examen mesuré | $R^{-1{,}085}$ estimé | Écart |
|---|---|---|---|
| 2 | 0,884 | 0,471 | −47 % |
| 4 | 0,447 | 0,222 | −50 % |
| 9 | 0,178 | 0,092 | −48 % |

**Pourquoi les deux diffèrent.** Un clic est le produit de l'examen **et** de l'attrait. Comme
l'attrait décroît lui aussi avec le rang — une plateforme place ses meilleurs documents en tête —
la sévérité ajustée sur les clics **absorbe les deux**.

C'est le même confondant que le [rang servi](rang-servi.md) avait identifié entre l'ajustement
agrégé (1,49) et les effets fixes (1,10). Les effets fixes en retirent une part, pas la totalité :
un même document ne conserve pas le même attrait à tous les rangs, ce que la littérature appelle
le **biais de confiance**. La mesure d'examen, elle, ne dépend pas de l'attrait.

## 4. La forme, enfin testable

| Ajustement sur la courbe **mesurée** | $R^2$ | Écart max |
|---|---|---|
| loi de puissance ($\eta = 0{,}88$) | **0,7215** | **42 %** |
| géométrique ($\gamma = 0{,}79$) | 0,9621 | 24 % |
| pli d'écran (pli au rang 2, queue $\eta = 1{,}07$) | 0,9879 | 13 % |

La courbe mesurée ne décroît pas régulièrement : elle tient jusqu'au deuxième rang, chute
brutalement du troisième au cinquième, puis s'aplatit. C'est la signature d'un **seuil d'écran** —
ce qui est visible sans défiler contre ce qui exige de défiler — et non celle d'une loi lisse. La
colonne `serp_height` encode précisément la hauteur de page, donc le rang où ce seuil tombe.

!!! warning "Ce que cette section ne prétend pas"
    Trois formes ajustées sur neuf points, ce n'est pas une sélection de modèle : le pli d'écran a
    deux paramètres libres contre un pour les autres, et il gagne pour cette raison autant que par
    sa forme. Ce qui est solide est plus modeste et suffit : **la loi de puissance décrit mal la
    courbe mesurée**, et elle se trompe surtout là où la norme se joue — au deuxième rang.

## 5. Ce que cela change à la demande d'accès aux données

Les quatre tableaux de [l'article 40](article-40.md) portent tous sur les clics. Il suffirait
d'**une colonne de plus** — le nombre d'impressions effectivement **affichées**, par cellule
(contenu, rang) — pour que l'exposition cesse d'être estimée.

Cette colonne retirerait d'un coup :

* le besoin d'**estimer** $\eta$, donc l'hypothèse de forme qui l'accompagne ;
* l'**ambiguïté** entre cascade et budget de clics ;
* et le **confondant d'attrait** qui gonfle l'estimation par les clics de 23 %.

Une colonne, contre trois problèmes ouverts depuis six chapitres. Et elle est **moins sensible**
que les clics : savoir qu'un contenu a été affiché en dit moins sur un lecteur que savoir qu'il
l'a choisi.

## Reproductibilité

Le journal brut n'est pas versionné. Le condensé porte désormais les comptes d'examen par cellule
— impressions, impressions affichées, et les mêmes scindées selon qu'un clic a eu lieu plus haut.
Le résultat s'y recalcule **à l'identique**, écart nul aux quatre seuils, ce qu'un test vérifie.

## Réserves

`displayed_time` mesure un **affichage**, pas un regard. La mesure surestime donc l'exposition,
dans une proportion que ce dépôt ne peut pas chiffrer.

La tranche employée reste une tranche : 524 164 documents sur les 1,2 milliard de sessions de
Baidu-ULTR, et une page de résultats de recherche n'est pas un fil d'actualité. Le 0,88 vaut pour
cette surface.

`slipoff_count_after_click` et `media_type` n'ont pas été exploitées : la première compte les
documents sortis de l'écran après un clic, ce qui affinerait la mesure ; la seconde distingue les
formats, dont la littérature indique qu'ils modifient l'attention à rang égal.

---

*Implémentation : `ide.exposure.examination_counts`, `ide.logs.upstream_dependence_test` ·
Notebook : [23 — L'exposition mesurée](notebooks/23_exposition_mesuree.ipynb) ·
[le test de forme](test-de-forme.md) · [journaux qui enregistrent le rang](rang-servi.md) ·
[demande au titre de l'article 40](article-40.md)*
