# Les deux angles morts de la contre-expertise

!!! success "Le test d'échangeabilité tient sous cascade"
    Éprouvé contre un modèle de clic où l'examen dépend de ce qui précède, le test rejette entre
    $z = -208$ et $z = -241$ selon la probabilité de poursuite — **plus fortement que sur
    Baidu-ULTR** ($-206$), alors même que la cascade réduit le nombre de fils exploitables. Son
    verdict négatif sur MIND garde donc tout son sens.

!!! danger "Mais la loi de puissance $R^{-\eta}$ ne tient pas"
    Sous cascade, la décroissance de l'attention est **géométrique**, pas polynomiale. Au
    douzième rang, la loi ajustée surestime l'exposition réelle d'un facteur **40 à 4 110** — et
    l'estimateur renvoie $\hat\eta \approx 0{,}5$ avec une erreur type de $0{,}04$ : un chiffre
    parfaitement confiant qui ne décrit **aucune** exposition réelle.

!!! warning "Et sous pertinence estimée, l'avantage des méthodes réglées s'efface"
    Le classement des réordonnanceurs tient à tous les niveaux de bruit, mais l'écart au tirage
    au sort passe de **16,4 points** à bruit nul à **5,8 points** à $\sigma = 0{,}4$, et
    **s'inverse** à $\sigma = 0{,}6$. Le hasard est le seul qui n'utilise pas la pertinence :
    son manque à gagner est invariant.

---

## Pourquoi cette page

La [contre-expertise](contre-expertise.md) s'est terminée en énonçant ce qu'elle n'avait pas
fait. Ce sont les deux hypothèses les plus profondes du dépôt — l'une sur la **forme de
l'attention**, l'autre sur ce que la plateforme **sait de son lecteur** — et aucune n'avait été
éprouvée.

![Les deux angles morts](figures/fig21_angles_morts.png)

/// caption
Le test d'échangeabilité sous cascade ; l'exposition réelle contre la loi ajustée ; les deux
formes de décroissance du taux de clic ; et l'effondrement de l'avantage des méthodes réglées
quand la pertinence est estimée. Figure régénérée par
[le notebook 21](notebooks/21_angles_morts.ipynb).
///

## 1. Le test survit, la loi de puissance non

Le dépôt emploie partout un **modèle de position** : la probabilité d'examen vaut $R^{-\eta}$ et
ne dépend que du rang. Le modèle **à cascade** en pose un tout autre : le lecteur descend le fil,
s'arrête dès qu'il a trouvé son bonheur, poursuit sinon avec une probabilité $\gamma$. La
décroissance de l'attention n'y est plus une loi qu'on postule mais une **conséquence** du
parcours.

| Journal | $z$ | Verdict |
|---|---|---|
| MIND (ordre mélangé) | +0,12 | ne rejette pas |
| Baidu-ULTR (données réelles) | −205,7 | rejette |
| cascade, $\gamma = 1{,}00$ | **−240,8** | rejette |
| cascade, $\gamma = 0{,}85$ | −226,9 | rejette |
| cascade, $\gamma = 0{,}60$ | −207,9 | rejette |

**Le test ne suppose rien**, et c'est pourquoi il tient : il ne teste que l'indépendance entre
position et clic. S'il n'avait détecté qu'une forme particulière de dépendance, son silence sur
MIND n'aurait rien distingué — un journal mélangé d'un journal dont la dépendance a une autre
forme.

**L'estimateur, lui, suppose beaucoup.** La simulation rend ici la vérité terrain que les données
réelles ne donnent jamais : les positions réellement examinées.

| Rang | Examen réel ($\gamma = 0{,}85$) | $R^{-\hat\eta}$ ajusté | Erreur |
|---|---|---|---|
| 1 | 1,000 | 1,000 | 0 % |
| 2 | 0,573 | 0,710 | +24 % |
| 4 | 0,190 | 0,504 | +165 % |
| 8 | 0,020 | 0,358 | +1 715 % |
| 12 | 0,0023 | 0,293 | **+12 781 %** |

Une loi de puissance ne peut pas approcher une exponentielle sur douze rangs : elle colle en tête
et diverge en queue. Et l'ajustement paraît excellent — $\hat\eta = 2{,}19$ sur les dix premiers
rangs, erreur type $0{,}04$ par effets fixes — sur une forme qui n'est pas la bonne.

!!! danger "Ce que cela retire à la publication de $\hat\eta$"
    Le dépôt publie $\hat\eta = 1{,}10 \pm 0{,}09$ sur Baidu-ULTR. Ce chiffre n'a de sens **que
    si** l'examen y suit une loi de puissance. Rien ne le garantit : Baidu-ULTR est une page de
    résultats de recherche, terrain d'élection du modèle à cascade, et Hager *et al.* (2024)
    rapportent précisément qu'un modèle de position mal spécifié y expliquerait leur résultat
    négatif.

    La sévérité doit donc être publiée **avec la forme supposée**, et cette forme reste à tester.
    Le [test d'échangeabilité](mind.md) dit si l'ordre porte de l'information ; il ne dit pas
    **sous quelle forme**.

## 2. Ce qu'une pertinence estimée fait aux comparaisons

Les [lignes de base](lignes-de-base.md) comparent cinq réordonnanceurs contre la frontière
exacte, et supposent partout la pertinence **connue**. Aucune plateforme n'est dans ce cas.

Le protocole est modifié sur un point, et un seul : les méthodes **classent** sur la pertinence
perçue, et sont **jugées** sur la vraie.

| Bruit $\sigma$ | Corrélation de rang | Filtre | MMR | Tour de rôle | Boltzmann | Hasard |
|---|---|---|---|---|---|---|
| 0,00 | 1,000 | **0,0 %** | 0,0 % | 3,2 % | 2,2 % | 16,4 % |
| 0,10 | 0,899 | 1,3 % | 2,2 % | 4,7 % | 3,8 % | 16,4 % |
| 0,20 | 0,751 | 5,0 % | 6,0 % | 7,4 % | 7,7 % | 16,4 % |
| 0,40 | 0,500 | 10,6 % | 10,5 % | 13,6 % | 12,9 % | 16,4 % |
| 0,60 | 0,359 | **15,4 %** | 15,2 % | 16,6 % | 16,9 % | **16,4 %** |

**L'ordre des méthodes ne change pas** — le filtre et MMR devant, le hasard derrière. La
conclusion des lignes de base n'est pas invalidée.

**Mais l'avantage s'effondre.** La raison est mécanique : le tirage au sort est le seul
réordonnanceur qui **n'utilise pas** la pertinence, donc son manque à gagner est invariant au
bruit tandis que celui de toutes les autres méthodes croît. Passé $\sigma \approx 0{,}6$ — une
corrélation de rang de 0,36 — une règle gourmande sur une grandeur bruitée fait pire qu'une règle
qui l'ignore.

!!! warning "Ce que cela retire au chapitre des lignes de base"
    Ses chiffres — « 0,0 à 1,0 % de manque à gagner » — valent pour une **pertinence connue**.
    Sous un bruit $\sigma = 0{,}2$, le même filtre en laisse **5,0 %**. Sur une plateforme
    réelle, tout dépend de la qualité de son estimateur de pertinence, que ce dépôt n'a aucun
    moyen de mesurer.

    Cela ne change pas la conclusion de fond — **ce qui distingue ce dépôt n'est pas son
    algorithme** — mais cela ajoute une troisième raison de le penser : à pertinence réaliste,
    l'écart entre réordonnanceurs compte bien moins que la qualité du moteur de pertinence
    sous-jacent.

## 3. Ce que ces deux mesures changent

**Le test d'échangeabilité est confirmé**, et c'est le résultat le plus utile : il rejette sous
les deux modèles de clic, et plus fortement que sur données réelles. Un journal dont l'ordre ne
dit rien ne dit rien sous aucun modèle.

**L'estimateur de sévérité est restreint** : il n'estime une quantité interprétable que si
l'examen suit effectivement une loi de puissance — hypothèse que rien dans les données réelles ne
vérifie, et que la littérature met explicitement en doute pour les pages de résultats.

**Les lignes de base sont restreintes aussi** : leur classement tient, leur écart au hasard non.

## Piste ouverte

Tester la **forme** de l'examen, pas seulement son existence. Un journal qui enregistre le rang
permet en principe de distinguer une décroissance géométrique d'une décroissance polynomiale :
sous cascade, l'examen d'un rang dépend des **clics au-dessus**, ce qui laisse une signature
qu'un test conditionnel pourrait détecter. Ce serait le troisième contrôle de la série, après
l'échangeabilité et l'identifiabilité — et le dépôt ne l'a pas construit.

---

*Implémentation : `ide.logs.simulate_cascade` · Notebook :
[21 — Les deux angles morts](notebooks/21_angles_morts.ipynb) ·
[contre-expertise](contre-expertise.md) · [lignes de base](lignes-de-base.md) ·
[bibliographie](bibliographie.md)*
