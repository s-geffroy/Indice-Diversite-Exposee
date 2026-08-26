# IDE — Indice de Diversité Exposée

!!! success "Renommé — le nom dit ce qui est mesuré"
    L'indice s'est d'abord appelé « **Index de Dissipation Entropique** », d'après une analogie
    avec la décohérence quantique. L'[audit](limites.md) a démonté cette analogie transfert par
    transfert : rien de spécifiquement quantique n'y a survécu. Un nom qui renvoie à une analogie
    fausse annonce autre chose que ce que l'instrument mesure.

    Le sigle reste **IDE**. Il se lit **Indice de Diversité Exposée** — la répartition de
    l'attention **réellement servie** entre les points de vue d'un catalogue déclaré.

## Définition

L'IDE est l'entropie de Shannon de la distribution des **points de vue exposés**, normalisée par
son maximum théorique :

$$\mathrm{IDE} = \frac{H(q)}{\log_2 k}, \qquad
q_i = \frac{\sum_R w_R \, \mathbb{1}[\text{le contenu servi au rang } R \text{ tombe dans le bac } i]}
{\sum_R w_R}$$

Trois choix la distinguent de l'entropie qu'on écrirait spontanément, et chacun est la
**conséquence d'une attaque qui a réussi** :

| Choix | Pourquoi | Ce qui arrive sans lui |
|---|---|---|
| $q$ porte sur les **contenus servis**, projetés sur les bacs du catalogue de référence — non sur les étiquettes qui les annoncent | une étiquette se choisit, un contenu se constate | l'indice atteint **1,000 pour une diversité de contenu nulle**, à coût d'engagement nul → [test adverse](gaming.md) |
| chaque rang est pondéré par l'**attention** qu'il reçoit, $w_R$ | un lecteur consulte le premier élément bien plus souvent que le dernier | la mesure se laisse satisfaire en **enterrant** les contenus divergents : mesurée à 0,70 sans regarder le rang, une plateforme n'expose que **0,36** → [rang adverse](rang-adverse.md) |
| le dénominateur $\log_2 k$ est fixé par un **catalogue déclaré**, non par ce que la plateforme sert | comparer deux fils exige la même unité | un fil parfaitement fermé ne présente qu'une modalité : le dénominateur dégénère et l'indice flatte |

| Valeur | Interprétation |
|---|---|
| $\mathrm{IDE} = 1$ | l'attention servie se répartit également entre les $k$ points de vue du catalogue |
| $\mathrm{IDE} \to 0$ | l'attention servie va à un seul point de vue |

!!! tip "Se lire en **nombre effectif de points de vue**"
    Une entropie normalisée n'est pas linéaire en ce qu'on entend par « deux fois plus divers ».
    Sa conversion $k^{\mathrm{IDE}}$ l'est : c'est le nombre de points de vue **également servis**
    qui produirait la même entropie (Jost, 2006). Sur les fils réels mesurés, $0{,}50$ sur
    vingt-six rubriques vaut **5,1 rubriques effectives**. Le premier chiffre ne se comprend pas
    sans formation, le second si. → `ide.entropy.effective_viewpoints`

## La remise d'attention se mesure

Employer $1/R$ revient à poser $\eta = 1$ par convention. Ce dépôt l'a mesurée :

| Ce qu'on croyait | Ce qui est mesuré |
|---|---|
| $\eta = 1$, par convention | $\eta = 0{,}88 \pm 0{,}05$ sur 143 documents, **par affichage** et non par clic |
| l'examen suit une cascade | **réfuté** deux fois sur Baidu-ULTR, par un test et par un compteur |
| la loi en $R^{-\eta}$ ajuste la courbe | c'est le **pire** des trois ajustements essayés |
| la remise dépend de la page servie | elle en dépend de **6 %**, ce qui déplace l'indice de $0{,}0025$ |

→ [exposition mesurée](exposition-mesuree.md) · [l'effet de page](effet-de-page.md)

La sévérité reste en revanche une propriété de la **surface** : environ 1,1 sur une page de
résultats, 0,04 à 0,11 sur un bandeau de trois vignettes. Elle ne se transporte pas d'une
plateforme à l'autre, et doit donc être mesurée là où l'indice est calculé.
→ [contre-expertise](contre-expertise.md)

## Ce qu'il faut pour le calculer

1. **Un journal qui passe les trois contrôles** — l'ordre enregistré porte-t-il une information de
   position ? y a-t-il de quoi estimer la sévérité ? l'examen dépend-il de ce qui a été cliqué
   au-dessus ? → [MIND](mind.md) · [rang servi](rang-servi.md) · [test de forme](test-de-forme.md)
2. **Un rang vérifiable**, et non déclaré. Un journal public au moins fournit une colonne d'ordre
   qui n'est pas le rang servi, sans mentir et sans que rien ne le signale : le test
   d'échangeabilité est ce qui le détecte. → [l'indice mesuré](indice-mesure.md)
3. **Un catalogue de points de vue déclaré**, publié en entier — c'est lui qui fixe le
   dénominateur, et il déplace le niveau bien plus que le fil lui-même.
   → [le catalogue](catalogue.md)

## Ce qui a été mesuré, et ce qui ne l'a pas été

!!! success "La forme aveugle au rang est mesurée sur des fils réels"
    $0{,}50$ par journée-utilisateur sur 232 887 fils du quotidien *Ekstra Bladet*, soit **5,1
    rubriques effectives sur 26**. C'est le premier chiffre du dépôt qui ne vient pas d'une
    simulation — et c'est celui de la forme **que le test adverse disqualifie**, faute de mieux
    sur un journal qui n'enregistre ni le rang ni le contenu. Il se lit comme une **borne
    supérieure**. → [l'indice mesuré](indice-mesure.md)

!!! warning "La forme exposée n'est qu'**encadrée**"
    Aucun journal public ne porte à la fois un rang vérifiable et une étiquette interprétable. La
    composition étant connue et l'ordre non, l'indice exposé n'est pas déterminé mais
    **contraint** : largeur médiane $0{,}104$. On peut donc parfois trancher sans le rang — jamais
    mesurer.

## La forme d'origine, et ce qu'elle mesurait

Le fil de travail définissait l'indice sur les **étiquettes** d'un fil, sans regarder le rang :

$$H_{\text{norm}} = \frac{H(X)}{\log_2 k}$$

C'est ce que calcule `ide.entropy.label_diversity_index`, dont le nom dit désormais la portée.
Cette forme reste utile là où le rang n'existe pas — c'est elle qu'on mesure sur un journal qui
n'enregistre que l'ensemble servi — mais **elle ne mesure pas l'exposition** : c'est elle que le
test adverse met en défaut.

## Pourquoi la normalisation est le point essentiel

L'entropie brute se mesure en bits, et sa valeur dépend du nombre de modalités disponibles. Deux
fils aux catalogues différents produiraient des chiffres incomparables. La normalisation par
$\log_2 k$ rend l'indice **sans dimension et borné** — c'est ce qui permet de comparer.

L'implémentation rend la dépendance explicite :

```python
from ide.entropy import label_diversity_index

feed = ["complot"] * 10 + ["factuel"] * 10

label_diversity_index(feed)                    # 1.0  — deux modalités observées
label_diversity_index(feed, catalogue_size=4)  # 0.5  — quatre points de vue disponibles
```

## Limites

Ces réserves comptent autant que la définition, et l'[audit critique](limites.md) les développe.

* **Le catalogue décide du niveau, et c'est mesuré.** Le même corpus vaut $0{,}50$ sur vingt-six
  rubriques et $0{,}92$ sur trois. L'**ordre** entre lecteurs, lui, tient jusqu'à six modalités
  puis s'effondre. Un niveau d'indice sans son catalogue ne veut rien dire.
  → [le catalogue](catalogue.md)
* **Une rubrique n'est pas un point de vue.** Les deux axes d'étiquetage du seul corpus mesuré —
  thématique et tonalité — ne concordent qu'à $\rho = 0{,}16$. La diversité exposée est une
  grandeur **par axe déclaré**.
* **L'indice reste manipulable, et cela a été mesuré.** La forme d'origine cède totalement : 1,000
  pour une diversité de contenu nulle, sans céder un point d'engagement. La forme retenue ferme
  cette voie et l'enterrement avec, mais une plateforme peut encore servir des contenus
  formellement divergents et substantiellement vides — de la diversité de bac sans diversité
  d'argument. Aucune mesure automatique ne distingue les deux. → [test adverse](gaming.md)
* **Le plafond dépend du volume servi.** Une entropie ne dépasse pas le logarithme du nombre de
  contenus servis : un lecteur qui en reçoit cinq plafonne à $0{,}49$ sur un catalogue de
  vingt-six. L'indice mesure donc mal les lectures courtes, et c'est une propriété de la grandeur,
  pas de sa mesure.
* **Mesurer l'indice de fils individuels suppose d'observer ce qui est servi à des personnes.**
  Une mesure agrégée sur une population le suppose beaucoup moins ; le dépôt ne fournit pas de
  protocole de confidentialité, et n'en propose plus.

---

*Implémentation : `ide.entropy` · `ide.radio.rank_weights`*
