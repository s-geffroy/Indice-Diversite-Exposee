# L'indice, mesuré sur un fil réel

!!! success "Le chiffre qui manquait depuis le premier jour"
    Sur **232 887 fils réels** du quotidien danois *Ekstra Bladet*, la diversité servie vaut
    **0,47** par journée-utilisateur — soit **4,6 rubriques également servies sur 26**. Le dépôt
    n'avait jamais publié ce nombre autrement qu'en simulation.

!!! danger "Mais la colonne de rang ne contient pas le rang"
    EB-NeRD porte enfin les deux colonnes qui manquaient partout : la liste servie **et** une
    étiquette. Le premier contrôle du dépôt dit pourtant que l'ordre enregistré ne porte
    **aucune** information de position — $z = +1{,}05$, $p = 0{,}29$ — et ce n'est pas un défaut
    de puissance : ce journal aurait détecté une sévérité **134 fois plus faible** que celle
    mesurée sur Baidu-ULTR.

!!! tip "Ce qui reste possible sans le rang : condamner, rarement acquitter"
    La composition étant connue, l'indice exposé est **encadré** : largeur médiane **0,104**. À
    un plancher de 0,40, **32,4 %** des fils y contreviennent quelle que soit leur mise en ordre
    — constat opposable sans la colonne manquante — mais **59,7 %** restent indécidables. C'est
    le prix exact de ce que la plateforme possède et ne publie pas.

---

## Une lacune mal énoncée

Six chapitres de ce dépôt reposaient sur une phrase :

> Aucun jeu de données public ne porte à la fois le rang servi et une étiquette de point de vue
> interprétable. → [MIND](mind.md) · [rang servi](rang-servi.md)

Elle est **fausse**. EB-NeRD — le journal d'*Ekstra Bladet* publié pour le RecSys Challenge 2024
— donne `article_ids_inview`, la liste servie, et rattache chaque article à une rubrique
déclarée, `category_str`. Les deux colonnes sont là.

Ce qui manque est ailleurs, et c'est plus intéressant : **la colonne d'ordre ne contient pas
l'ordre**.

![L'indice mesuré](figures/fig26_indice_mesure.png)

/// caption
La diversité servie mesurée sur des fils réels, ce que l'ordre inconnu laisse indéterminé, les
trois verdicts possibles sans la colonne de rang, et leur dépendance à la sévérité supposée.
Figure régénérée par [le notebook 26](notebooks/26_indice_mesure.md).
///

## 1. Le premier contrôle retire l'ordre

| Journal | Échangeabilité | Lecture |
|---|---|---|
| Baidu-ULTR | $z = -206$ | l'ordre enregistré **est** le rang servi |
| MIND | $z = +0{,}12$ | l'ordre ne dit rien |
| **EB-NeRD** | $z = +1{,}05$ ($p = 0{,}29$) | **l'ordre ne dit rien** |

Un test qui ne rejette pas ne dit rien tant qu'on ignore ce qu'il aurait su rejeter. Le journal
aurait détecté une sévérité de **0,0066**, quand Baidu-ULTR en mesure **0,88** : le silence n'est
pas un manque de puissance, c'est une réponse.

`article_ids_inview` est un **ensemble servi**. L'indice exposé — celui que ce dépôt propose au
régulateur — n'y est donc pas mesurable. L'indice **aveugle au rang** l'est, et il ne l'avait
jamais été sur données réelles.

## 2. La diversité servie, enfin chiffrée

| Fenêtre | Médiane | Quartiles | Points de vue effectifs | Sous 0,40 | Sous 0,50 |
|---|---|---|---|---|---|
| fil servi | 0,417 | [0,372 ; 0,489] | 3,89 sur 26 | 35,0 % | 78,8 % |
| **journée-utilisateur** | **0,466** | [0,411 ; 0,507] | **4,56 sur 26** | **18,8 %** | **71,2 %** |

La seconde ligne est celle qui compte : c'est la fenêtre que le [protocole](ide.md) prescrit, et
la grandeur réglementaire y est la **part de la population sous le plancher**, non la moyenne.

Ce chiffre ne dit pas si c'est peu ou beaucoup — le niveau d'un plancher est une décision
politique, et le dépôt ne la tranche pas. Il donne l'**ordre de grandeur** qui manquait à toute
discussion : un lecteur reçoit en une journée l'équivalent de quatre à cinq rubriques également
servies, sur vingt-six disponibles.

## 3. Ce que l'ordre inconnu laisse indéterminé

L'ordre manque, la composition est connue : l'indice exposé n'est pas déterminé, il est
**contraint**. `ide.entropy.exposed_index_bounds` énumère toutes les mises en ordre distinctes et
rend l'encadrement **exact** — non une heuristique.

| Plancher | Sûrement sous | Sûrement au-dessus | Indécidable |
|---|---|---|---|
| 0,30 | 8,2 % | 50,6 % | 41,3 % |
| **0,40** | **32,4 %** | 7,9 % | **59,7 %** |
| 0,50 | 91,5 % | 0,7 % | 7,7 % |

**Sans le rang, on peut condamner ; on n'acquitte presque jamais.** Un tiers des fils
contreviennent à un plancher de 0,40 quelle que soit leur mise en ordre : c'est un constat
opposable, obtenu sans la colonne manquante. Mais six fils sur dix restent indécidables, et c'est
ce que coûte son absence.

**Sensibilité.** La largeur de l'encadrement croît avec la sévérité supposée — 0,062 à
$\eta = 0{,}5$, 0,104 à 0,88, 0,127 à 1,1. La part indécidable, elle, culmine vers 0,9 puis
redescend : à sévérité plus forte, l'intervalle entier glisse sous le plancher et le fil redevient
décidable — **par condamnation**.

## 4. Ce que cela change pour la demande d'accès

La [demande au titre de l'article 40](article-40.md) réclamait « le rang servi ». Ce chapitre
montre que ce n'est pas assez : une plateforme peut fournir une colonne d'ordre qui n'est pas le
rang, sans mentir et sans qu'on le voie. Il faut donc réclamer le rang **vérifiable**, et le test
d'échangeabilité est ce qui le vérifie — sur les données livrées, avant toute autre mesure.

C'est aussi ce qui rend le premier contrôle du dépôt plus qu'un préalable méthodologique : c'est
une **clause de recevabilité**.

## Réserves

`category_str` est une **rubrique** — « nyheder », « sport », « krimi » — non un point de vue au
sens de l'indice. La mesure porte sur la diversité **thématique** exposée. C'est le substitut déjà
employé sur MIND, et il doit être lu comme tel : deux articles de la même rubrique peuvent
défendre des thèses opposées, et deux rubriques différentes peuvent dire la même chose.

La sévérité $\eta = 0{,}88$ est **transportée** de Baidu-ULTR, un moteur de recherche.
[Le chapitre 25](effet-de-page.md) a établi qu'elle se transporte d'une page à l'autre — pas
d'une plateforme à l'autre. D'où le test de sensibilité, qui ne renverse pas la conclusion.

Le catalogue de 26 rubriques est celui du corpus, non un catalogue de référence imposé par un
régulateur. Changer $k$ change le niveau de l'indice, jamais son classement.

L'encadrement exact ne couvre que les fils de **dix contenus ou moins**, soit 64 % du journal :
au-delà, l'énumération cesse d'être praticable.

Enfin, EB-NeRD est distribué **pour usage de recherche uniquement**. Le journal brut n'est pas
versionné ; seul l'est le condensé de signatures de composition — des effectifs par rubrique,
triés et anonymes — dont quatre tests vérifient qu'il rend les mêmes chiffres.

---

*Notebook : [26 — L'indice mesuré](notebooks/26_indice_mesure.md) ·
[MIND](mind.md) · [rang servi](rang-servi.md) · [l'effet de page](effet-de-page.md) ·
[demande au titre de l'article 40](article-40.md)*
