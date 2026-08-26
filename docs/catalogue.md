# Qui choisit le catalogue choisit l'indice

!!! danger "Le niveau de l'indice n'a aucun sens absolu"
    Le **même corpus** vaut **0,50** sur vingt-six rubriques et **0,92** sur trois. À un plancher
    de 0,40, la part de la population sous le seuil passe de **13,7 % à 1,5 %** : le même
    plancher devient décoratif sans qu'une seule impression ait changé.

!!! success "L'ordre, lui, résiste — jusqu'à un point"
    Passer de vingt-six rubriques à douze ne change **rien** au classement des lecteurs
    ($\rho = 1{,}000$). À six, il tient encore ($0{,}911$). À trois, il est **détruit**
    ($-0{,}09$) : l'indice cesse alors de classer, pas seulement de mesurer.

!!! warning "Et « la diversité exposée » n'existe pas au singulier"
    Rubriques et **tonalité** — les deux axes d'étiquetage du corpus — ne concordent qu'à
    $\rho = +0{,}16$. Parmi le quart le plus divers en rubriques, 23,8 % sont aussi dans le quart
    le plus divers en tonalité, là où l'indépendance donnerait 25 %.

---

## Une réserve jamais chiffrée

Depuis le premier jour, l'[indice](ide.md) porte la même réserve :

> La discrétisation en points de vue est un **choix politique**. Qui définit les modalités
> définit l'indice. Découper l'espace des opinions en 4, 40 ou 400 catégories change la valeur
> mesurée, et ce découpage n'est pas un acte technique neutre.

C'est vrai, et cela ne dit rien : *de combien* ? Assez pour rendre un plancher arbitraire, ou
assez peu pour qu'on s'en accommode ? [Le chapitre 26](indice-mesure.md) fournit
enfin de quoi trancher — 58 549 journées-utilisateur réelles, composition connue rubrique par
rubrique.

![Le catalogue](figures/fig28_catalogue.png)

/// caption
Le même corpus sous quatre catalogues, l'effondrement du plancher avec la taille du catalogue,
la concordance de rang qui tient puis se défait, et l'indépendance des deux axes d'étiquetage.
Figure régénérée par [le notebook 28](notebooks/28_catalogue.md).
///

## 1. Trois grandeurs que la réserve confondait

| Catalogue | $k$ | Indice médian | Points de vue effectifs | Sous 0,40 | Sous 0,50 | $\rho$ de rang |
|---|---|---|---|---|---|---|
| rubriques complètes | 26 | 0,498 | 5,07 | 13,7 % | 50,7 % | — |
| 11 rubriques + reste | 12 | 0,654 | 5,07 | 4,7 % | 10,9 % | **+1,000** |
| 5 rubriques + reste | 6 | 0,860 | 4,67 | 2,1 % | 3,0 % | +0,911 |
| 2 rubriques + reste | 3 | 0,924 | 2,76 | 1,5 % | 3,1 % | **−0,093** |
| tonalité | 3 | 0,881 | 2,63 | 1,3 % | 4,0 % | +0,155 |

Le **niveau** bouge de moitié. La **part sous le plancher** est divisée par neuf. L'**ordre**,
lui, ne bouge pas du tout — jusqu'à ce qu'il s'effondre.

## 2. Pourquoi l'ordre tient si bien, puis plus du tout

La raison est banale et décide de tout : **les rubriques rares ne servent presque rien.**

| Rubriques les plus servies | Part du corpus |
|---|---|
| les 2 premières | 52,1 % |
| les 5 premières | 88,6 % |
| les 11 premières | **99,8 %** |

Regrouper les quinze rubriques restantes ne fusionne quoi que ce soit que pour **une journée sur
mille** : le classement ne peut donc pas bouger. Descendre à six force la fusion sur **64,5 %**
des journées ; à trois, sur **94,8 %**. C'est là que l'ordre se défait.

## 3. La taille d'un catalogue ne le spécifie pas

Si seule la taille comptait, n'importe quel découpage en six classes vaudrait le découpage par
fréquence. Vingt tirages aléatoires disent le contraire :

| Regroupement en 6 classes | Indice médian | $\rho$ de rang |
|---|---|---|
| par fréquence | **0,860** | **0,911** |
| aléatoire | 0,682 ± 0,093 | 0,769 ± 0,098 |

Deux catalogues de même taille rendent des indices distants de deux dixièmes et des classements
distants de quatorze points de concordance. **C'est la liste qui doit figurer dans la norme, pas
le nombre.**

## 4. Une rubrique n'est pas un point de vue — et cela se mesure

Le chapitre précédent posait cette réserve sans la chiffrer. Les deux axes d'étiquetage du corpus
permettent de le faire : la **rubrique** thématique et la **tonalité** déclarée.

$\rho = +0{,}155$. Un lecteur peut recevoir toutes les rubriques du journal sur un ton
uniformément négatif, ou une seule rubrique dans les trois tonalités. **La diversité exposée est
une grandeur par axe déclaré**, non une grandeur.

## 5. Ce que cela change à la demande d'accès

**Un plancher se publie avec son catalogue, ou ne se publie pas.** Un texte réglementaire qui
fixerait un seuil sans annexer la liste exacte des modalités laisserait à la plateforme le soin
de choisir sa propre note.

**Le catalogue doit compter au moins une demi-douzaine de modalités effectivement servies.** En
dessous, l'indice ne classe plus : la concordance avec un catalogue fin tombe à zéro, et deux
plateformes deviennent incomparables même relativement.

**Et il faut dire sur quel axe on mesure.** Thématique, tonalité, orientation
politique : ces axes ne se déduisent pas l'un de l'autre, et ce choix pèse au moins autant que le
seuil chiffré.
## Réserves

Les catalogues grossiers sont obtenus ici par **regroupement** d'un catalogue existant, ce qui
n'est pas la même chose qu'un catalogue conçu comme tel — un découpage pensé en six points de vue
serait probablement mieux équilibré que les cinq rubriques les plus servies plus un reste.

Le corpus est celui d'un **seul journal danois**. Rien ne garantit que la queue de distribution
des rubriques ait partout la même forme, or c'est elle qui explique la stabilité observée
jusqu'à douze modalités.

Enfin la tonalité est une étiquette produite par un **modèle**, non par une rédaction : sa
concordance faible avec les rubriques pourrait tenir en partie à son bruit propre.

---

*Notebook : [28 — Le catalogue](notebooks/28_catalogue.md) ·
[l'indice mesuré](indice-mesure.md) · [IDE](ide.md)*
