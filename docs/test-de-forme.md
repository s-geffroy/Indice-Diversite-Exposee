# Le test de forme, et ce qu'il ne peut pas séparer

!!! success "Le troisième contrôle existe et fonctionne"
    Il ne rejette jamais sous un modèle de position ($|z| < 1$ à toutes les sévérités) et rejette
    massivement sous cascade ($z = -97$ à $-307$). Il répond à la question que les deux autres
    contrôles laissaient ouverte : **sous quelle forme** l'ordre agit-il ?

!!! danger "Mais un budget de clics imite une cascade"
    Un lecteur qui cesse de cliquer une fois servi — tout en continuant de parcourir le fil —
    produit la même signature : $z = -144$ sous modèle de position **pur**, contre $-179$ sous
    cascade véritable. Les deux ne sont **pas séparables dans des données de clic seules**.

!!! info "Sur Baidu-ULTR : aucune signature de cascade"
    L'écart réduit est **positif** à tous les seuils — $+5{,}6$ au plus permissif, $+0{,}5$ à
    $+0{,}6$ aux plus stricts — alors qu'une cascade le rendrait négatif. Le signe est celui du
    confondant d'hétérogénéité, pas celui de la cascade.

!!! failure "Et une erreur de protocole, rattrapée avant publication"
    Restreindre le journal aux sessions à plusieurs clics semblait la façon évidente de séparer
    budget et cascade. Appliquée à Baidu-ULTR, la restriction donne $z = -8{,}2$
    ($p = 2 \times 10^{-16}$) — une signature nette, que j'allais publier. Sur un modèle de
    position **pur**, la même restriction fait passer $z$ de $+0{,}7$ à $\mathbf{-45{,}7}$.
    C'est un *collider*.

---

## La construction

Les deux formes d'examen ne se distinguent pas par leur **allure** : une décroissance géométrique
et une décroissance polynomiale s'ajustent aussi bien l'une que l'autre sur les premiers rangs.
C'est ce qui rendait le problème apparemment insoluble.

Elles se distinguent par une **indépendance conditionnelle** :

* sous un modèle de **position**, l'examen du rang $R$ ne dépend que de $R$. À contenu et rang
  fixés, le clic est donc indépendant de ce qui s'est passé au-dessus ;
* sous un modèle **à cascade**, un clic au-dessus **supprime** l'examen en dessous.

Pour chaque cellule $s = (\text{contenu}, \text{rang})$, les $n_s$ impressions se répartissent en
$n_{1s}$ précédées d'un clic dans le même fil et $n_{0s}$ qui ne le sont pas, pour $k_s$ clics au
total. Sous l'hypothèse d'indépendance, ces clics se répartissent comme un tirage sans remise, de
moments connus exactement :

$$\mathbb{E}[a_s] = \frac{k_s n_{1s}}{n_s}, \qquad
\mathbb{V}[a_s] = \frac{k_s (n_s - k_s)\, n_{1s} n_{0s}}{n_s^2 (n_s - 1)}$$

C'est la statistique de Mantel-Haenszel, stratifiée par cellule. Le conditionnement à la cellule
élimine la qualité du contenu — sans lui, les fils qui contiennent un clic en haut sont aussi ceux
dont les contenus sont meilleurs, et la comparaison ne mesurerait que cela.

![Le test de forme](figures/fig22_test_de_forme.png)

/// caption
Les deux contrôles sur modèles purs ; le budget de clics qui imite la cascade ; l'application à
Baidu-ULTR ; et la restriction qui fabrique la signature qu'elle cherche. Figure régénérée par
[le notebook 22](notebooks/22_test_de_forme.ipynb).
///

## Les deux contrôles

| Modèle | $z$ | Cellules | Verdict |
|---|---|---|---|
| position, $\eta = 0{,}0$ | −0,33 | 2 197 | compatible position |
| position, $\eta = 1{,}0$ | +0,08 | 1 882 | compatible position |
| position, $\eta = 2{,}0$ | +0,92 | 952 | compatible position |
| cascade, $\gamma = 1{,}00$ | **−307,4** | 2 032 | rejette |
| cascade, $\gamma = 0{,}85$ | −178,7 | 1 660 | rejette |
| cascade, $\gamma = 0{,}60$ | −96,7 | 1 010 | rejette |

Le test sépare donc parfaitement les deux modèles **quand ils sont purs**. C'est la condition
minimale, et elle est remplie.

## Ce qu'il ne peut pas séparer

Un lecteur qui ne cherche qu'une chose cesse de cliquer une fois servi, **tout en continuant de
parcourir le fil**. Son examen est celui d'un modèle de position ; seule la production de clics
s'arrête. C'est un comportement parfaitement ordinaire.

| Budget de clics (modèle de **position**) | $z$ | Clics par fil |
|---|---|---|
| illimité | +0,74 | 0,990 |
| 3 | −2,15 | 0,979 |
| 2 | −21,1 | 0,917 |
| **1** | **−144,2** | 0,661 |
| *cascade $\gamma = 0{,}85$, pour mémoire* | *−178,7* | *0,750* |

**Rien dans les clics ne les distingue** — et c'est attendu : dans les deux cas, le journal montre
exactement la même chose, à savoir qu'après un clic il n'y a plus rien.

La différence est pourtant considérable pour ce qui nous occupe :

| | Après un clic, le contenu en dessous… | Conséquence pour un réordonnancement |
|---|---|---|
| **cascade** | n'est pas examiné | le remonter change tout |
| **budget de clics** | est examiné mais ne sera pas cliqué | le remonter ne change rien au clic |

La question à laquelle ce test devait répondre — *quelle exposition attribuer aux rangs
profonds ?* — reste donc ouverte, et elle ne peut pas être tranchée par des clics.

## Sur données réelles

Baidu-ULTR est le seul journal du dépôt qui enregistre à la fois l'ordre servi et l'identité des
documents : 64 200 sessions, 0,688 clic par session, 53,4 % sans aucun clic.

| Seuil d'impressions | $z$ | $p$ | Cellules |
|---|---|---|---|
| 2 | **+5,65** | $1{,}6 \times 10^{-8}$ | 780 |
| 5 | +1,20 | 0,229 | 261 |
| 10 | +0,54 | 0,593 | 151 |
| 20 | +0,61 | 0,543 | 108 |

**Aucune signature de cascade.** Le signe compte autant que l'ampleur, et il est ici celui du
confondant annoncé : un lecteur plus enclin à cliquer clique davantage partout, donc plus haut
*et* plus bas.

Trois lectures restent possibles, et le dépôt ne peut pas trancher entre elles : l'examen y est
proche d'un modèle de position ; ou bien une cascade existe mais le confondant la masque — le test
est conservateur, il l'a toujours dit ; ou bien la couverture est trop mince, 108 cellules au seuil
le plus strict, parce qu'une même URL réapparaît rarement dans un journal de recherche.

!!! warning "Ce que ce non-rejet ne fait pas"
    Il **ne valide pas** la loi de puissance. Les [angles morts](angles-morts.md) ont montré
    qu'elle se trompe d'un facteur 4 110 au douzième rang **si** l'examen est une cascade. Ne pas
    détecter de cascade avec 108 cellules n'établit pas son absence.

## L'erreur, et le contrôle qui l'a rattrapée

53 % des sessions de Baidu-ULTR n'ont aucun clic. L'idée vient naturellement de restreindre le
test aux sessions à **plusieurs clics** — là où un budget de un est exclu par construction, donc
là où cascade et budget devraient enfin se séparer. Appliquée à Baidu-ULTR, la restriction donne
$z = -8{,}2$ : une signature de cascade nette, sur données réelles.

Le même protocole, appliqué à des journaux dont on connaît la vérité :

| Modèle | $z$ (journal entier) | $z$ (restreint) |
|---|---|---|
| **position, budget illimité** | **+0,74** | **−45,7** |
| position, budget = 2 | −21,1 | −52,5 |
| cascade, $\gamma = 0{,}85$ | −178,7 | *aucune cellule* |

Sur un journal simulé sous modèle de position **pur, sans cascade et sans budget**, la restriction
fabrique un écart réduit de −45,7. La raison porte un nom : le nombre de clics d'un fil est un
**collider** de ses clics individuels, et conditionner dessus induit une dépendance négative entre
eux — c'est le paradoxe de Berkson.

Le $-8{,}2$ obtenu sur Baidu-ULTR ne mesure donc pas une cascade : il mesure la sélection que je
venais d'opérer. La mise en garde est désormais dans la documentation de la fonction, à l'endroit
où quelqu'un aura l'idée de le refaire.

C'est la troisième fois dans ce dépôt qu'un protocole apparemment raisonnable fabrique son propre
résultat, et la troisième fois qu'un contrôle sur données simulées le rattrape avant publication.
La règle qui s'en dégage vaut d'être écrite : **tout protocole appliqué à des données réelles doit
d'abord être appliqué à des données dont on connaît la réponse.**

## Les trois contrôles, désormais

| Contrôle | Question | MIND | Baidu-ULTR |
|---|---|---|---|
| **échangeabilité** | l'ordre dit-il quelque chose ? | non ($z = +0{,}12$) | oui ($z = -206$) |
| **identifiabilité** | y a-t-il de quoi estimer $\eta$ ? | oui, artificiellement | oui, 55 documents |
| **forme** | l'examen dépend-il de l'amont ? | inapplicable | non détecté ($z = +0{,}5$) |

Le troisième existe, fonctionne, et ne tranche pas ce qu'on voulait trancher.

## Piste ouverte

Baidu-ULTR publie `displayed_time`, `serp_height` et `slipoff_count_after_click` — des mesures de
l'**examen** et non du clic. Ce dépôt n'a jamais lu ces colonnes. Elles trancheraient précisément
ce que les clics ne peuvent pas : un contenu situé sous un clic a-t-il été affiché assez longtemps
pour être vu ?

C'est la suite directe, elle ne demande aucune donnée nouvelle, et c'est la seule voie connue pour
séparer les deux modèles.

---

*Implémentation : `ide.logs.upstream_dependence_test` · Notebook :
[22 — Le test de forme](notebooks/22_test_de_forme.ipynb) ·
[les deux angles morts](angles-morts.md) · [exploration de MIND](mind.md) ·
[journaux qui enregistrent le rang](rang-servi.md)*
