# Ce que la vie privée coûte à l'audit

!!! success "La grandeur réglementée est presque gratuite à protéger"
    La part de la population sous le plancher — ce que le protocole prescrit de publier — ne
    bouge pas d'un millième entre $\varepsilon = 10$ et $\varepsilon = 0{,}1$. Un histogramme de
    50 classes sur 58 549 journées-utilisateur est hors d'atteinte du bruit.

!!! danger "La grandeur dont elle dépend ne l'est pas du tout"
    À $\varepsilon = 1$ — la valeur de référence usuelle — la sévérité de l'attention passe de
    **0,88 à 0,50**, et son erreur type ne bouge pas. Le résultat est faux **avec assurance**, et
    dans le sens qui fait paraître l'enterrement moins grave qu'il n'est.

!!! warning "Et le vrai prix n'est pas le bruit"
    C'est le **plafonnement des contributions**, sans lequel aucune garantie *par personne* n'est
    possible. Il déplace la part sous le plancher de **+0,7 à +2,8 points**, toujours vers
    l'excès : les lecteurs assidus sont plus divers que les autres, et les écarter fait paraître
    la plateforme moins conforme qu'elle n'est.

---

## Une lacune que le dépôt s'était signalée

La [demande au titre de l'article 40](article-40.md) prouve qu'un régulateur n'a pas besoin du
journal : quatre tableaux agrégés suffisent, pour 95 fois moins de lignes. Elle ne dit rien de
leur **innocuité**, et l'[audit](limites.md) le reconnaissait sans y remédier :

> Un protocole d'audit crédible doit être agrégatif et **différentiellement privé** — ce dépôt ne
> le propose pas.

Un agrégat n'est pas anonyme. Le seuil de suppression des faibles effectifs employé jusqu'ici
n'offre **aucune garantie formelle** : il rend l'attaque plus laborieuse, pas impossible.

![Ce que la vie privée coûte](figures/fig27_vie_privee.png)

/// caption
La sévérité atténuée par le bruit puis surcorrigée par le seuil, la grandeur réglementée
insensible, le plafonnement comme vrai coût, et la raison de tout cela — la sparsité du tableau.
Figure régénérée par [le notebook 27](notebooks/27_vie_privee.md).
///

## 1. Deux coûts distincts

Le **bruit** protège contre l'inférence sur une ligne du journal. Son effet dépend de la
**densité** du tableau publié, non de l'importance de la quantité :

| Tableau | Cellules | Effectif médian | Résiste jusqu'à |
|---|---|---|---|
| marge de rang des affichages | 9 | 56 000 | $\varepsilon = 0{,}03$ |
| histogramme d'indice par journée-utilisateur | 50 | 1 100 | $\varepsilon = 0{,}1$ |
| **cellules (contenu, rang)** | **451 100** | **1** | **rien** |

99,7 % des cellules du tableau 3 portent moins de cinq impressions. C'est la seule chose qui
compte, et elle explique tout le reste.

Le **plafonnement des contributions** est ce qui rend possible une garantie *par personne* : on
ne retient au plus que $C$ observations par lecteur. C'est un choix de conception, pas un
artefact, et c'est lui qui déplace les chiffres.

## 2. La grandeur réglementée résiste

| Plafond | Journées gardées | Biais du plafond | $\varepsilon = 1$ | $\varepsilon = 0{,}1$ |
|---|---|---|---|---|
| 1 | 26 % | **+0,028** | 0,165 | 0,165 |
| 3 | 63 % | +0,015 | 0,152 | 0,153 |
| 5 | 86 % | +0,007 | 0,144 | 0,145 |
| 8 (aucun) | 100 % | 0,000 | 0,137 | 0,139 |

*Vraie part sous 0,40 : 0,137.*

Le bruit est invisible sur toute la plage. Le plafonnement, lui, ajoute jusqu'à 2,8 points à une
part de 13,7 % — un excès relatif de 21 %, **toujours dans le même sens**.

C'est un résultat inattendu, et il est du bon côté pour le régulateur : sous garantie par
utilisateur, on **surestime** la non-conformité. L'erreur qu'on commet en protégeant les lecteurs
n'innocente pas la plateforme.

## 3. La sévérité ne résiste pas

| $\varepsilon$ | $\eta$ bruité | Erreur type | $\eta$ après seuil de publication | Contenus retenus |
|---|---|---|---|---|
| 10 | 0,871 | 0,047 | 0,871 | 145 |
| 3 | 0,797 | 0,052 | **0,881** | 57 |
| **1** | **0,505** | 0,051 | 1,034 | 25 |
| 0,3 | 0,151 | 0,050 | 1,201 | 9 |

*Sans bruit : $\eta = 0{,}882 \pm 0{,}046$ sur 143 contenus.*

Le bruit sur des effectifs agit comme une **erreur de mesure** : il atténue l'estimation vers
zéro, et l'erreur type ne le dit pas. C'est le mode d'échec que ce dépôt a rencontré cinq fois —
un chiffre plausible, un intervalle serré, une conclusion fausse.

**Le seuil de publication corrige le niveau, puis le dépasse.** Ne garder que les cellules dont
l'effectif bruité dépasse $\tau$ échange un biais d'atténuation contre un biais de **sélection** :
survivent les cellules les plus exposées, donc les premiers rangs et les contenus populaires. À
$\varepsilon = 3$ l'échange est bon ; en dessous il tourne mal. Le remède ne supprime pas
l'erreur, il en change le signe.

## 4. Le nœud

La marge de rang survit à $\varepsilon = 0{,}03$, et sur ce journal elle tombe à **0,7 %** de la
valeur estimée à contenu fixé — 0,876 contre 0,882.

Mais on ne le sait que parce qu'on dispose du tableau à contenu fixé, celui qu'aucune garantie ne
protège.

!!! danger "Ce qui se publie sans risque est ce qu'on ne peut pas vérifier"
    Sur une plateforme où la composition varierait davantage avec le rang, la marge pourrait être
    fausse **sans que rien ne le montre**. La quantité vérifiable et la quantité publiable ne
    sont pas la même, et aucun budget de confidentialité ne les réconcilie.

## 5. Ce que cela change à la demande

**Un budget par quantité, publié avec elle.** Les budgets ne se composent pas gratuitement :
deux tableaux sous $\varepsilon$ chacun donnent une garantie à $2\varepsilon$. Une demande réelle
doit les additionner et le dire.

**Le tableau 3 ne doit pas être demandé tel quel.** Trois demandes le remplacent :

1. la **marge de rang** des affichages, publiable à $\varepsilon = 0{,}1$ sans dommage ;
2. l'**estimation à effets fixes de contenu calculée par la plateforme elle-même**, publiée
   comme un scalaire bruité — un nombre a une sensibilité bornée, un tableau creux non ;
3. l'**écart entre les deux**, seul contrôle disponible de la première par la seconde.

**Le plafond de contributions doit être publié avec le résultat**, comme l'est déjà le seuil de
suppression. Il n'est pas neutre, et son sens est connu.

## Réserves

Le mécanisme employé est le plus simple qui soit — bruit de Laplace sur des effectifs, seuil de
publication pour la garantie $(\varepsilon, \delta)$. Des mécanismes mieux adaptés aux tableaux
creux existent et feraient mieux : ce chapitre **borne le coût par le haut**, il ne prétend pas
l'atteindre.

La garantie *par utilisateur* n'est mesurée que sur EB-NeRD, seul journal du dépôt qui porte un
identifiant de lecteur. Sur Baidu-ULTR, seule une garantie **par impression** est possible — plus
faible, et c'est une propriété du jeu de données, non de la méthode.

Enfin, le biais de plafonnement est calculé **en espérance** depuis le croisement charge × indice
du condensé ; un tirage réel s'en écarte de quelques millièmes.

---

*Notebook : [27 — Ce que la vie privée coûte](notebooks/27_vie_privee.md) ·
[demande au titre de l'article 40](article-40.md) · [l'indice mesuré](indice-mesure.md) ·
[audit critique](limites.md)*
