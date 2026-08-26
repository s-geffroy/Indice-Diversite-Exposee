# Indice de Diversité Exposée

**Mesurer la diversité qu'un fil algorithmique expose réellement — et éprouver ce qu'on croit en savoir.**

---

## Ce que ce dépôt contient

Un **instrument** — une mesure de la diversité qu'un fil d'actualité expose réellement à son
lecteur, calculable sans accès au code de la plateforme — et la **méthode adverse** qui l'a mis à
l'épreuve : chaque proposition y est attaquée, et ce qui tombe est publié comme tel, y compris
quand ce qui tombe vient du dépôt lui-même.

Il en reste vingt-huit notebooks exécutables, 650 tests, **vingt-sept corrections consignées**,
et un état des lieux qui ne ressemble ni à ce que le projet annonçait, ni à ce qu'il croyait avoir
établi six chapitres plus tôt.

![L'exposition mesurée directement, contre l'exposition estimée à travers les
clics](figures/fig23_exposition_mesuree.png)

/// caption
Le résultat le plus net du dépôt : pendant six chapitres, ce dépôt a **estimé** l'exposition à
travers les clics ; une colonne du fichier permettait de la **mesurer**. L'estimation surestimait
la décroissance de 23 %. Figure régénérée par
[le notebook 23](notebooks/23_exposition_mesuree.md).
///

## Le verdict, en une page

| Objet | État |
|---|---|
| L'analogie décohérence quantique ↔ effondrement du consensus | **réfutée**, transfert par transfert → [audit](limites.md) |
| Le formalisme classique qu'elle a fait emprunter | **cohérent**, un seul paramètre calibré, et sa seule prédiction propre — l'effet de la charge émotionnelle — **testée quatre fois sans effet** |
| L'écart de persistance entre registres émotionnels | **n'existe pas** — artefact de sélection → [corpus étendu](corpus-etendu.md) |
| L'indice tel qu'il était proposé au régulateur | **intenable** : saturable à coût nul, puis contournable par l'enterrement → [test adverse](gaming.md) · [rang adverse](rang-adverse.md) |
| La forme retenue de l'indice | **définie et chiffrée**, et sa pondération de rang est **transportable** : la page servie ne la déplace que de 6 % → [l'effet de page](effet-de-page.md) |
| L'indice **aveugle au rang**, sur des fils réels | **mesuré pour la première fois** : 0,50 par journée-utilisateur, 5,1 rubriques effectives sur 26 → [l'indice mesuré](indice-mesure.md) |
| L'indice **exposé**, sur ces mêmes fils | **encadré, non mesuré** — la colonne d'ordre du seul jeu qui l'offre ne contient pas le rang ; 6 fils sur 10 restent indécidables → [l'indice mesuré](indice-mesure.md) |
| L'algorithme (ADE) | **sur la frontière exacte, et superflu** : une heuristique de 1998 fait aussi bien, et l'écart s'efface encore à pertinence bruitée → [lignes de base](lignes-de-base.md) · [angles morts](angles-morts.md) |
| Les instruments de mesure | **valides après correction** — trois d'entre eux ont dû être restreints, et trois conclusions retirées → [contre-expertise](contre-expertise.md) · [l'effet de page](effet-de-page.md) |
| L'exposition, grandeur centrale de tout l'édifice | **mesurable**, et mesurée : $0{,}88 \pm 0{,}05$ — non $1{,}09$ comme estimé → [exposition mesurée](exposition-mesuree.md) |
| Sa dépendance à la **page servie**, que ce dépôt disait rédhibitoire | **mesurée à contenu fixé, et trois fois plus petite que publiée** : 6 % d'examen, $0{,}0025$ d'indice → [l'effet de page](effet-de-page.md) |
| La **confidentialité** de la demande d'accès, jamais garantie formellement | **garantie et chiffrée** : le plancher survit à $\varepsilon = 0{,}1$, la sévérité est divisée par deux à $\varepsilon = 1$ → [ce que la vie privée coûte](vie-privee.md) |
| Le **catalogue de points de vue**, « choix politique » jamais chiffré | **mesuré** : le même corpus vaut 0,50 sur 26 rubriques et 0,92 sur 3 — mais l'ordre entre lecteurs tient jusqu'à six → [le catalogue](catalogue.md) |

**En une phrase : la théorie n'a pas tenu. Ce qui tient est une grandeur — l'exposition, celle
qui décide de tout le reste, et qu'on peut mesurer au lieu de la supposer : $0{,}88$ et non $1$,
sans cascade, et à 6 % près indépendante de la page servie. C'est assez pour écrire une norme ;
ce qui manque n'est plus une méthode mais un **rang vérifiable** — et le seul journal public qui
prétend le fournir ne le fournit pas.**

## Ce qui tient

Sept objets, et ils sont la seule chose que ce travail demande qu'on lui reprenne. Un test
statistique s'applique à d'autres données et répond seul ; il ne demande pas qu'on croie celui qui
l'a écrit. C'est le critère qui les distingue des préceptes de méthode que ce dépôt a un temps
promus au rang de résultat, à tort — cette page le disait, et l'[audit](limites.md) dit pourquoi
c'était un excès.

**Trois contrôles à passer sur un journal, dans cet ordre.** L'**échangeabilité** — l'ordre
enregistré dit-il quelque chose ? — ne détecte rien dans MIND ($z = +0{,}12$) et rejette à
$z = -206$ sur Baidu-ULTR ; l'**identifiabilité** — y a-t-il de quoi estimer ? — nécessaire et non
suffisante ; la **forme** — l'examen dépend-il de ce qui a été cliqué au-dessus ?
→ [MIND](mind.md) · [rang servi](rang-servi.md) · [test de forme](test-de-forme.md)

**Une exposition mesurée, et non plus supposée.** $\eta = 0{,}88 \pm 0{,}05$ sur 143 documents,
par affichage plutôt que par clic. La **cascade est réfutée** sur Baidu-ULTR, par deux voies
indépendantes. Et la loi en $R^{-\eta}$ qu'emploie tout le dépôt est le **pire** des trois
ajustements sur la courbe mesurée. → [exposition mesurée](exposition-mesuree.md)

**Et cette mesure est transportable d'une page à l'autre.** C'était la dernière objection, et
elle venait de ce dépôt : si la remise d'attention dépendait de la composition de la page, aucune
norme ne pouvait s'écrire sans décrire chaque page servie. À contenu tenu fixe, la dépendance
existe mais vaut **6 %**, et déplace l'indice de $0{,}0025$ — **quatorze fois moins** que la
convention $1/R$ qu'elle devait disqualifier. → [l'effet de page](effet-de-page.md)

**Des estimateurs contrefactuels confrontés à une vérité terrain.** +2,5 % d'écart contre +32 %
pour l'estimation naïve — avec le diagnostic qui interdit d'en tirer gloire, une taille
d'échantillon effective de 1 513 pour 4 millions d'impressions. Aucun estimateur ne remplace
l'exploration : le doublement robuste fait moins bien. → [rang servi](rang-servi.md)

**Une frontière exacte contre laquelle juger un réordonnanceur.** Le filtre du dépôt s'y tient —
0,0 à 1,0 % d'engagement laissé sur la table — mais MMR aussi, et le prix de la norme dépend du
lecteur : 3,8 % quand ses intérêts traversent les points de vue, 17,1 % quand sa préférence *est*
un point de vue. → [lignes de base](lignes-de-base.md)

**Et un premier chiffre réel, là où il n'y avait que des simulations.** Sur 232 887 fils
danois, la diversité **servie** vaut 0,50 par journée-utilisateur — 4,6 rubriques effectives sur
26. L'indice **exposé**, lui, n'est qu'encadré : la colonne d'ordre du seul jeu qui l'offre ne
contient pas le rang, et six fils sur dix restent indécidables à un plancher de 0,40.
→ [l'indice mesuré](indice-mesure.md)

**Et une demande d'accès qui se protège au lieu de se promettre.** La grandeur réglementée —
la part de la population sous le plancher — survit à $\varepsilon = 0{,}1$ sans bouger d'un
millième. Le vrai prix n'est pas le bruit mais le **plafonnement des contributions**, qui
surestime la non-conformité de 0,6 à 2,5 points. → [ce que la vie privée coûte](vie-privee.md)

**Une demande d'accès aux données qui se vérifie au lieu de se plaider.** Quatre tableaux
agrégés, sans donnée personnelle, prouvés suffisants — pour 95 fois moins de lignes que le
journal. Deux colonnes s'y sont ajoutées depuis, **`affichages`** et **`format`**, chacune parce
qu'une mesure a montré ce qu'on perdait sans elle.
→ [demande au titre de l'article 40](article-40.md)

## Ce qui est tombé

**Sur le monde**, cinq résultats négatifs :

* **le critère $\gamma\alpha > \lambda$ ne veut rien dire** — satisfait par construction pour
  tout contenu ayant percé → [calibration](calibration.md) ;
* **l'écart de persistance entre registres n'existe pas** — ×3,04 contre ×2,90 ($p = 0{,}53$) sur
  440 sujets → [corpus étendu](corpus-etendu.md) ;
* **il n'était pas dilué par l'étiquetage** — 40 % de bruit mesuré, l'écart disparaît quand même
  → [annotation en aveugle](annotation.md) ;
* **aucun jeu public ne permet l'évaluation annoncée** — mais pas pour la raison publiée :
  EB-NeRD porte les deux colonnes, et c'est sa **colonne d'ordre qui ne contient pas l'ordre**
  → [l'indice mesuré](indice-mesure.md) ;
* **l'examen n'est pas une cascade** sur Baidu-ULTR, et il ne suit pas une loi de puissance
  → [exposition mesurée](exposition-mesuree.md).

**Sur les propositions du dépôt lui-même**, cinq de plus :

* **un plancher d'indice se sature à coût nul** — 1,000 pour une diversité de contenu nulle ;
* **le premier correctif prescrivait la polarisation** — l'optimum de l'entropie de Rao est
  bimodal → [test adverse](gaming.md) ;
* **« la proximité à la cible résiste le mieux » était un artefact d'échelle** — à diversité
  exposée égale, le choix de la mesure ne compte presque pas ;
* **le filtre n'apporte rien qu'une heuristique de 1998 n'apporte déjà**, sauf aux planchers
  élevés → [lignes de base](lignes-de-base.md) ;
* **l'explication du « pli d'écran » est fausse** — le rang prédit mieux que les pixels
  → [format et retour](format-et-retour.md) ;
* **et l'effet de format publié était pour les deux tiers une composition** — 18 % à rang fixé,
  6 % à contenu fixé, et une simulation sans aucun effet reproduit le chiffre publié
  → [l'effet de page](effet-de-page.md).

## Ce qui n'est pas tranché

* **L'indice exposé n'a jamais été mesuré sur un fil réel** — seulement **encadré**, à 0,104
  près, sur 232 887 fils danois. La lacune est de **donnée**, non de méthode, et
  [la demande](article-40.md) dit exactement ce qu'il faudrait — un rang **vérifiable**.
* **Une rubrique n'est pas un point de vue.** Le seul chiffre réel dont le dépôt dispose porte
  sur la diversité **thématique** exposée. → [l'indice mesuré](indice-mesure.md)
* **Le niveau du plancher est une décision politique.** La mesure décrit, elle ne prescrit pas —
  et le **catalogue** pèse autant que le seuil : le même corpus passe de 0,50 à 0,92 selon le
  découpage. → [le catalogue](catalogue.md)
* **Les trois codeurs de l'annotation sont des instances du même modèle de langue.**
* **Rien n'a été validé de l'extérieur.** Les 650 tests vérifient que le code fait ce qui est
  annoncé, non que ce qui est annoncé soit vrai, et aucun relecteur n'est passé. C'est le seul
  verrou que ce dépôt ne peut pas lever seul. → [appel à relecture](relecture.md)
* **Rien ne démontre que les opinions humaines *obéissent* à une mécanique statistique** —
  mais l'hypothèse est désormais posée sous une forme qui peut échouer, avec la liste de ce
  qu'il faudrait retirer si elle échouait. → [l'hypothèse de fond](hypothese-testable.md)

## Les deux instruments

| | Objet | État |
|---|---|---|
| **[IDE](ide.md)** | *Indice de Diversité Exposée* — entropie des contenus servis sur le catalogue de référence déclaré, **pondérée par l'attention de chaque rang**, dans $[0, 1]$ | forme **définie**, jamais mesurée sur un fil réel ; sa pondération dépend de la page servie |
| **[ADE](ade.md)** | *Algorithme de Diversité Exposée* — filtre de recommandation qui optimise cet indice au lieu de l'engagement brut | **sur la frontière exacte, et superflu** : une heuristique de 1998 fait aussi bien |

Le [mémorandum de régulation](memorandum.md) traduit l'indice en recommandations pour l'ARCOM
et la Commission européenne, dans le cadre du *Digital Services Act* — avec, à chaque
recommandation, la mesure qui l'a corrigée.

## D'où cela vient

Le projet est parti d'une analogie : plus un système quantique est grand, plus vite il
décohère ; plus une population est grande, plus l'accord y est difficile. Cette analogie a
produit des quantités mesurables, et **aucune de ses affirmations propres n'a résisté à la
vérification**. C'est l'objet de l'[audit critique](limites.md), qui recense **dix-sept
corrections** — dont cinq invalidaient une formule, et deux ont été découvertes en tentant de
mesurer.

Ce qui subsiste du formalisme est classique : paysage d'énergie libre, transition de phase,
hystérésis, franchissement de barrière.

![Les trois régimes de l'opinion publique : paysage d'énergie libre, distributions
stationnaires, et scission d'une société initialement modérée](figures/fig04_paysage.png)

/// caption
Les trois régimes de l'opinion publique, obtenus en changeant deux paramètres du même paysage
d'énergie libre. Figure régénérée par
[le notebook 04](notebooks/04_fokker_planck_paysage.md).
///

## Explorer

Les vingt-huit notebooks sont exécutables et produisent l'intégralité des figures de la
note. Chacun se lit indépendamment.

| Notebook | Ce qu'il montre |
|---|---|
| [01 — Entropie et pureté](notebooks/01_entropie_et_purete.md) | une superposition cohérente a une entropie nulle ; l'IDE et sa normalisation |
| [02 — Ising](notebooks/02_ising_temperature_sociale.md) | la température critique d'Onsager, retrouvée numériquement |
| [03 — Voter Model](notebooks/03_voter_consensus_et_taille.md) | les lois d'échelle du consensus, et pourquoi la connectivité n'est pas la coupable |
| [04 — Fokker-Planck](notebooks/04_fokker_planck_paysage.md) | les trois régimes de l'opinion publique dans un même paysage d'énergie libre |
| [05 — Hystérésis](notebooks/05_hysteresis_et_contre_champ.md) | la mémoire d'une fausse croyance, et les deux façons de l'effacer |
| [06 — Résonance](notebooks/06_resonance_larsen.md) | le seuil $\gamma\alpha > \lambda$ et le cycle limite de l'attention |
| [07 — ADE](notebooks/07_ade_filtre_entropique.md) | un fil gelé qui se réouvre sous l'effet du recuit |
| [08 — Modèle à agents](notebooks/08_abm_compas_politique.md) | la bulle de filtres vue depuis l'individu |
| [09 — Calibration](notebooks/09_calibration_visibilite.md) | $\gamma\alpha/\lambda$ mesuré sur 19 épisodes d'attention publics |
| [10 — Changement de régime](notebooks/10_changement_de_regime.md) | 14 basculements datés, et pourquoi le rapport n'y est pas identifiable |
| [11 — Corpus étendu](notebooks/11_corpus_etendu.md) | 440 sujets dérivés de catégories : l'écart de persistance ne se réplique pas |
| [12 — Annotation en aveugle](notebooks/12_annotation_en_aveugle.md) | 40 % de bruit d'étiquetage mesuré, et le double recodage à $\kappa = 0{,}92$ |
| [13 — Test adverse](notebooks/13_test_adverse_index.md) | un plancher d'IDE saturé à coût nul, et le correctif qui prescrivait la polarisation |
| [14 — Rang et contrefactuel](notebooks/14_rang_et_contrefactuel.md) | l'enterrement de la diversité, et l'évaluation hors ligne fausse de 201 % |
| [15 — Rang adverse](notebooks/15_rang_adverse_et_severite.md) | les quatre mesures contournées par l'ordre, et la sévérité du biais estimée |
| [16 — Exploration de MIND](notebooks/16_exploration_mind.md) | un ordre indiscernable d'un mélange, et cinq sévérités tirées du même jeu |
| [17 — Rang servi](notebooks/17_rang_servi.md) | deux journaux qui enregistrent le rang, et un estimateur jugé contre la vérité |
| [18 — Demande article 40](notebooks/18_demande_article_40.md) | quatre tableaux agrégés qui suffisent, et la preuve qu'ils suffisent |
| [19 — Lignes de base](notebooks/19_lignes_de_base.md) | le filtre jugé contre quatre concurrents et contre la frontière exacte |
| [20 — Contre-expertise](notebooks/20_contre_expertise.md) | cinq contre-épreuves, dont une qui retire une conclusion publiée |
| [21 — Angles morts](notebooks/21_angles_morts.md) | le test tient sous cascade, la loi de puissance non |
| [22 — Test de forme](notebooks/22_test_de_forme.md) | le troisième contrôle, et le collider qu'il a failli publier |
| [23 — Exposition mesurée](notebooks/23_exposition_mesuree.md) | une colonne jamais lue, et six chapitres d'estimation rendus inutiles |
| [24 — Format et retour](notebooks/24_format_et_retour.md) | la cascade réfutée deux fois, et une de mes explications retirée |

## Reproduire

Tout s'exécute en conteneur. Aucune dépendance n'est installée sur la machine hôte.

```bash
git clone git@github.com:s-geffroy/Indice-Diversite-Exposee.git
cd Indice-Diversite-Exposee

docker compose run --rm test          # 650 tests
docker compose run --rm notebooks     # régénère les figures
docker compose up lab                 # JupyterLab sur :8888
docker compose up site                # cette documentation sur :8000
docker compose run --rm latex         # compile la note en PDF
```

## Relecture

Ce travail est **ouvert à la relecture critique**. Les retours sur le formalisme, sur
la viabilité de l'index ou sur les limites énumérées dans l'audit sont les plus
utiles. → [Appel à relecture](relecture.md)

---

*Code sous licence MIT · Contenus rédactionnels sous licence CC BY 4.0 ·
[Dépôt GitHub](https://github.com/s-geffroy/Indice-Diversite-Exposee)*
