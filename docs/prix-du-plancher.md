# Le prix d'un plancher, sur des fils réels

!!! danger "Le plancher que ce dépôt propose ne contraint presque rien"
    Ramener **toute** la population au-dessus de 0,40 demande de remplacer **un contenu servi sur
    177** — 0,57 % du journal. La journée-utilisateur médiane à traiter n'exige qu'**une seule
    substitution**. Ce que voient 99,4 % des contenus reste inchangé.

!!! warning "Et la forme de la grandeur réglementée invite à traiter la marge"
    Le protocole prescrit la **part de la population sous le seuil**, précisément pour qu'une
    moyenne satisfaisante ne masque pas une minorité enfermée. Mais une part est un seuil, et un
    seuil s'atteint **par la marge** : on corrige les lecteurs *juste en dessous*, et les plus
    enfermés restent où ils sont.

!!! failure "Au-dessus de 0,50, un plancher régule le volume, pas la diversité"
    À 0,60, **10,9 %** des journées-utilisateur sont hors d'atteinte quoi que fasse la
    plateforme ; à 0,80, **22,9 %**. Ce ne sont pas des lecteurs enfermés, ce sont des lecteurs
    **légers** : cinq contenus plafonnent à $\log_2 5 / \log_2 26 = 0{,}49$. La seule mise en
    conformité possible est de leur en **servir davantage**.

---

## Un prix qui ne suppose rien

Le dépôt chiffre le coût d'une norme de diversité depuis les [lignes de base](lignes-de-base.md)
— de 8,2 % à 18,9 % d'engagement. Ce chiffre a un défaut reconnu : il **suppose la pertinence
connue**, et porte sur des fils simulés.

Les 58 549 journées-utilisateur du [chapitre 26](indice-mesure.md) permettent de poser la
question sans rien supposer : **combien de contenus servis faudrait-il remplacer** pour qu'une
population réelle franchisse un plancher ? L'unité est la moins discutable qui soit.

![Le prix d'un plancher](figures/fig29_prix_du_plancher.png)

/// caption
Le prix d'un plancher niveau par niveau, la part de la population qu'aucune rédaction ne peut y
amener, le seuil de consommation qu'un plancher impose implicitement, et le nombre de
substitutions nécessaires à 0,40. Figure régénérée par
[le notebook 29](notebooks/29_prix_du_plancher.md).
///

## 1. Le contrôle qui décide de la suite

Le coût est calculé par un procédé **glouton** : chaque substitution retire un contenu à la
rubrique la plus servie et en ajoute un à la moins servie. Rien ne garantit *a priori* qu'il soit
optimal.

Règle du dépôt, appliquée : on énumère **toutes** les redistributions possibles sur deux cents
compositions assez courtes pour que ce soit faisable. **200 sur 200 identiques.** Le prix qui suit
n'est donc pas une borne prudente, c'est le prix.

## 2. Le prix, niveau par niveau

| Plancher | Sous le seuil | Population qu'on peut y amener | Contenus à changer |
|---|---|---|---|
| 0,30 | 4,6 % | 4,6 % | **0,21 %** |
| **0,40** | 13,7 % | 13,7 % | **0,57 %** |
| 0,50 | 50,7 % | 46,0 % | **2,27 %** |
| 0,60 | 96,2 % | 85,3 % | **8,24 %** |
| 0,70 | 100 % | 84,9 % | **17,11 %** |

Le prix est **convexe** : doubler le plancher de 0,30 à 0,60 multiplie le coût par quarante. Un
régulateur dispose donc d'une vraie marge de manœuvre — et le niveau retenu jusqu'ici par ce dépôt
est à l'extrémité indolore de la courbe.

Mais une colonne ne se lit pas comme les autres : **à partir de 0,50, la population qu'on peut
amener au-dessus du seuil est plus petite que celle qui est en dessous.**

## 3. Le plafond que rien ne peut lever

Une entropie ne dépasse pas le logarithme du nombre de contenus **servis**. Un lecteur qui en
reçoit cinq plafonne à 0,49, et aucune rédaction ne l'en fera sortir.

| Plancher | Journées hors d'atteinte | Contenus servis (médiane) |
|---|---|---|
| 0,40 | 0,0 % | — |
| 0,50 | 4,7 % | 5 |
| 0,60 | 10,9 % | 6 |
| 0,70 | 15,1 % | 6 |
| 0,80 | 22,9 % | 8 |

Ce plafond n'est pas une limite de mesure : c'est une limite de l'**objet régulé**. Un plancher
élevé compte comme non conformes des lecteurs dont le seul tort est de lire peu, et pousse la
plateforme à leur servir davantage — exactement ce qu'une norme de diversité n'a aucune raison
d'encourager.

## 4. Ce que cela change

**Le niveau retenu doit remonter, ou la norme est décorative.** À 0,40 sur vingt-six rubriques,
un contenu sur 177 suffit. Le [chapitre 28](catalogue.md) avait montré que le niveau n'a de sens
qu'avec son catalogue ; celui-ci montre qu'au niveau choisi, il ne mord pas.

**La grandeur réglementée doit être repensée.** La part sous le seuil a été choisie contre le
masquage par la moyenne ; elle invite au traitement de la marge. Une grandeur qui résisterait aux
deux reste à trouver — par exemple un plancher sur un **quantile bas** de la distribution, qui
oblige à corriger les plus enfermés plutôt que les plus proches du seuil.

**Et un plancher doit tenir compte du volume servi.** Deux issues, et il faut choisir : exempter
les sessions courtes, ou normaliser l'indice par le maximum **atteignable** plutôt que par
$\log_2 k$. La seconde change la définition de l'indice ; la première introduit un seuil de plus.

## Réserves

Le coût est mesuré en **contenus échangés**, non en engagement : EB-NeRD ne fournit aucun modèle
de pertinence, et une substitution peut être indolore comme elle peut coûter cher. Le chiffre de
0,57 % ne dit donc pas que la conformité est *facile*, seulement qu'elle est **peu étendue**.

Le calcul suppose que **n'importe quelle rubrique peut être servie à n'importe qui**, ce qui
surestime la facilité : un journal n'a pas toujours l'article qu'il faudrait, au moment où il le
faudrait.

Enfin tout ceci vaut pour le catalogue de vingt-six rubriques de ce corpus. À catalogue plus
grossier, le plancher mord encore moins.

---

*Notebook : [29 — Le prix d'un plancher](notebooks/29_prix_du_plancher.md) ·
[l'indice mesuré](indice-mesure.md) · [le catalogue](catalogue.md) ·
[lignes de base](lignes-de-base.md)*
