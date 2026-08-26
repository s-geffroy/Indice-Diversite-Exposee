# L'hypothèse de fond, sous une forme réfutable

!!! warning "Ce chapitre ne mesure rien"
    Tout le reste du dépôt publie des mesures. Celui-ci publie un **protocole** : la seule chose
    qui manquait à la question de fond était une forme qui permette de la perdre. Il est écrit
    pour être exécuté par d'autres, et pour dire à l'avance ce qui le réfuterait.

L'[audit](limites.md) se termine sur une réserve restée intacte depuis le premier jour :

> Rien ne démontre que les opinions humaines **obéissent** à une mécanique statistique.

Ce n'était pas une conclusion prudente, c'était un aveu : l'hypothèse n'avait jamais été posée
sous une forme qui puisse échouer. Voici cette forme.

## 1. Ce que l'hypothèse n'est pas

Elle n'est pas « les opinions ressemblent à des spins ». Une ressemblance ne se réfute pas.

Elle n'est pas non plus « un modèle d'Ising ajuste les données ». Un modèle à deux paramètres
ajuste à peu près n'importe quelle distribution bimodale, et un bon ajustement ne dit rien de la
mécanique sous-jacente — c'est l'erreur que ce dépôt a commise quatre fois sur d'autres sujets.

Ce qui distingue une mécanique statistique d'une métaphore thermodynamique est une **contrainte
de cohérence** entre deux grandeurs qu'on peut mesurer séparément : ce qu'un système fait
**tout seul**, et ce qu'il fait **quand on le pousse**.

## 2. L'énoncé décisif — fluctuation et réponse

Pour un système à l'équilibre décrit par une énergie libre et une température $T$, la variance
spontanée du paramètre d'ordre et la réponse à un champ extérieur ne sont pas indépendantes :

$$\chi = \frac{N \, \mathrm{Var}(\bar{x})}{T}, \qquad
\chi \equiv \frac{\partial \langle \bar{x} \rangle}{\partial h}$$

où $\bar{x}$ est l'opinion moyenne d'un groupe de $N$ personnes et $h$ un champ exogène — une
intervention d'exposition d'intensité connue.

Les deux membres se mesurent **séparément** : $\mathrm{Var}(\bar{x})$ sans rien faire, $\chi$ en
intervenant. Leur rapport définit une température estimée :

$$\hat{T} = \frac{N \, \mathrm{Var}(\bar{x})}{\chi}$$

!!! danger "L'hypothèse testable, en une phrase"
    **Un seul et même nombre $\hat{T}$ gouverne à la fois la variabilité spontanée d'un groupe et
    sa réponse à une poussée** — le même à travers les tailles de groupe, les intensités
    d'intervention et les groupes de même diversité d'exposition.

Le contenu réfutable n'est pas la *valeur* de $\hat{T}$ : le champ $h$ n'est défini qu'à une
échelle près, donc $\hat{T}$ aussi. Le contenu réfutable est son **invariance**.

### Les trois invariances, et ce qui les tue

| Invariance prédite | Statistique | Réfutation |
|---|---|---|
| $\hat{T}$ ne dépend pas de $N$ | régression de $\log \hat{T}$ sur $\log N$ | pente significativement non nulle |
| $\hat{T}$ ne dépend pas de l'intensité $h$ | $\hat{T}$ estimé à $h$ et $2h$ | écart supérieur à un facteur 2 |
| $\hat{T}$ croît avec la diversité d'exposition mesurée | régression de $\hat{T}$ sur l'IDE | pente nulle ou négative |

**Si la première ou la deuxième tombe, le système n'est pas à l'équilibre et l'énergie libre n'a
pas de référent.** Tout le vocabulaire de paysage, de puits et de barrière devient décoratif, et
la première moitié de ce dépôt doit être retirée.

**Si la troisième tombe**, la « température sociale » n'est pas ce que le dépôt en dit — elle
existe peut-être, mais l'exposition n'en est pas la mesure.

## 3. Ce que cela règle sur la taille

La question « plus le système est grand, plus les avis sont-ils ordonnés ? » se dissout ici, et
c'est un bon exemple de ce que le protocole gagne sur l'intuition. Deux grandeurs distinctes,
deux prédictions distinctes :

| Grandeur | Ce que la mécanique statistique prédit |
|---|---|
| fluctuation de la **moyenne** du groupe, $\mathrm{Var}(\bar{x})$ | décroît en $1/N$ — le groupe devient **rigide** |
| dispersion des opinions **individuelles**, $\sigma_{\text{ind}}$ | **aucune prédiction** — elle peut rester constante |

Une grande population n'est donc pas « plus ordonnée » : elle peut être exactement aussi divisée,
mais sa division cesse de bouger. C'est **la stabilité du désaccord** qui croît avec la taille,
pas l'accord. Et cela se teste : $\alpha$ dans $\mathrm{Var}(\bar{x}) \propto N^{-\alpha}$ vaut
$1$ en champ moyen. Une valeur significativement inférieure dirait que les individus ne
fluctuent pas indépendamment — ce qui est probable sur une plateforme où tout le monde voit le
même contenu, et serait un résultat en soi.

## 4. Trois corollaires, si le test décisif passe

Ils ne valent que dans cet ordre : chacun suppose que le précédent a tenu.

**Franchissement de barrière (Kramers).** Le taux de bascule individuel entre deux pôles suit
$\ln r = a - \Delta E / T$, avec $\Delta E$ lu sur la distribution observée
($\Delta E = -\log p(x)$ au col). *Réfutation :* pas de relation linéaire entre $\ln r$ et $1/T$,
ou pente de signe contraire.

**Hystérésis à aire dépendante de la température.** On applique $h$, on le renverse : l'aire de
la boucle est strictement positive sous $T_c$ et nulle au-dessus. *Réfutation :* pas de boucle,
ou aire indépendante de la diversité d'exposition. C'est la prédiction la plus spécifique du
lot — peu de modèles d'opinion non physiques prédisent une **boucle fermée d'aire décroissante**.

**Ralentissement critique.** Le temps de retour à l'équilibre après un choc diverge quand la
diversité d'exposition s'approche de $T_c$ par le haut. La littérature des signaux précoces
(écologie, climat) fournit l'estimateur et le protocole. *Réfutation :* temps de relaxation
constant.

## 5. Ce qu'il faut pour l'exécuter

Quatre choses, dont aucune n'est dans les journaux publics — y compris les quatre que ce dépôt a
examinés, qui ne mesurent **aucune opinion** :

1. un **panel** avec mesure répétée de l'attitude individuelle sur une échelle continue ;
2. des **groupes de tailles variées** tirés de la même population ;
3. une **intervention d'exposition randomisée et calibrée**, appliquée puis renversée ;
4. la **diversité d'exposition mesurée** par participant — c'est-à-dire l'IDE, qui exige le rang
   servi vérifiable → [demande au titre de l'article 40](article-40.md).

Les points 1 à 3 relèvent d'un protocole expérimental que des collaborations
plateforme–chercheurs ont déjà mené pour d'autres grandeurs. Le point 4 est ce que ce dépôt sait
spécifier et ne sait pas obtenir.

## 6. Ce que ce dépôt perdrait

Il faut le dire avant, pas après.

| Si le test décisif échoue | Conséquence |
|---|---|
| énergie libre, paysage, puits, barrière | **retirés** — vocabulaire sans référent |
| hystérésis sociale, contre-champ, recuit | **retirés** — la mécanique qui les fonde n'existe pas |
| température sociale | **retirée** comme grandeur, conservée comme métaphore explicite |
| les trois contrôles de journal, la sévérité mesurée, l'encadrement de l'indice, la demande d'accès | **intacts** — ils n'en ont jamais dépendu |

C'est la partition qui compte : la moitié métrologique du dépôt est **indépendante** de la
réponse. Ce protocole ne décide pas si la mesure de diversité exposée est valide ; il décide si
la théorie qui l'a fait chercher méritait d'exister.

---

*[Audit critique](limites.md) · [Fokker-Planck](theorie/fokker-planck.md) ·
[IDE](ide.md) · [demande au titre de l'article 40](article-40.md)*
