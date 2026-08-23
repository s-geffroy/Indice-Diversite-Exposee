# Indice de Diversité Exposée

**Mesurer la diversité qu'un fil algorithmique expose réellement — et éprouver ce qu'on croit en savoir.**

---

## Ce que ce dépôt contient

Un **instrument** — une mesure de la diversité qu'un fil d'actualité expose réellement à son
lecteur, calculable sans accès au code de la plateforme — et la **méthode adverse** qui l'a mis à
l'épreuve : chaque proposition y est attaquée, et ce qui tombe est publié comme tel, y compris
quand ce qui tombe vient du dépôt lui-même.

Il en reste vingt-quatre notebooks exécutables, 599 tests, **vingt-trois corrections consignées**,
et un état des lieux qui ne ressemble ni à ce que le projet annonçait, ni à ce qu'il croyait avoir
établi six chapitres plus tôt.

![L'exposition mesurée directement, contre l'exposition estimée à travers les
clics](figures/fig23_exposition_mesuree.png)

/// caption
Le résultat qui résume la méthode : pendant six chapitres, ce dépôt a **estimé** l'exposition à
travers les clics ; une colonne du fichier permettait de la **mesurer**. L'estimation surestimait
la décroissance de 23 %. Figure régénérée par
[le notebook 23](notebooks/23_exposition_mesuree.ipynb).
///

## Le verdict, en une page

| Objet | État |
|---|---|
| L'analogie décohérence quantique ↔ effondrement du consensus | **réfutée**, transfert par transfert → [audit](limites.md) |
| Le formalisme classique qu'elle a fait emprunter | **cohérent**, un seul paramètre calibré, et sa seule prédiction propre — l'effet de la charge émotionnelle — **testée quatre fois sans effet** |
| L'écart de persistance entre registres émotionnels | **n'existe pas** — artefact de sélection → [corpus étendu](corpus-etendu.md) |
| L'indice tel qu'il était proposé au régulateur | **intenable** : saturable à coût nul, puis contournable par l'enterrement → [test adverse](gaming.md) · [rang adverse](rang-adverse.md) |
| La forme retenue de l'indice | **définie et chiffrée**, jamais mesurée sur un fil réel — et sa pondération de rang dépend de la **page servie**, non du rang seul → [format et retour](format-et-retour.md) |
| L'algorithme (ADE) | **sur la frontière exacte, et superflu** : une heuristique de 1998 fait aussi bien, et l'écart s'efface encore à pertinence bruitée → [lignes de base](lignes-de-base.md) · [angles morts](angles-morts.md) |
| Les instruments de mesure | **valides après correction** — trois d'entre eux ont dû être restreints, et deux conclusions retirées → [contre-expertise](contre-expertise.md) |
| L'exposition, grandeur centrale de tout l'édifice | **mesurable**, et mesurée : $0{,}88 \pm 0{,}05$ — non $1{,}09$ comme estimé → [exposition mesurée](exposition-mesuree.md) |

**En une phrase : la théorie n'a pas tenu ; la métrologie tient, mais seulement parce qu'elle a
été corrigée à chaque étape — et ce qui survit le mieux n'est aucun instrument en particulier,
c'est la méthode.**

## La méthode, qui est le vrai résultat

Trois règles, chacune acquise en violant la précédente :

1. **Mesurer plutôt qu'estimer.** Le dépôt a construit trois contrôles, un estimateur à effets
   fixes, un étalonnage de puissance et une limite d'identification — pour approcher une grandeur
   qui était dans une colonne du fichier. → [exposition mesurée](exposition-mesuree.md)
2. **Tout protocole s'applique d'abord à des données dont on connaît la réponse.** Trois fois un
   protocole apparemment raisonnable a fabriqué son propre résultat ; trois fois un contrôle sur
   données simulées l'a rattrapé avant publication. → [test de forme](test-de-forme.md)
3. **Une explication se teste comme un chiffre.** Une hypothèse mécanique se formule en une phrase
   et se vérifie en une heure ; l'écart entre les deux est l'endroit exact où une affirmation
   fausse s'installe. → [format et retour](format-et-retour.md)

## Ce qui tient

**Trois contrôles à passer sur un journal, dans cet ordre.** L'**échangeabilité** — l'ordre
enregistré dit-il quelque chose ? — ne détecte rien dans MIND ($z = +0{,}12$) et rejette à
$z = -206$ sur Baidu-ULTR ; l'**identifiabilité** — y a-t-il de quoi estimer ? — nécessaire et non
suffisante ; la **forme** — l'examen dépend-il de ce qui a été cliqué au-dessus ?
→ [MIND](mind.md) · [rang servi](rang-servi.md) · [test de forme](test-de-forme.md)

**Une exposition mesurée, et non plus supposée.** $\eta = 0{,}88 \pm 0{,}05$ sur 143 documents,
par affichage plutôt que par clic. La **cascade est réfutée** sur Baidu-ULTR, par deux voies
indépendantes. Et la loi en $R^{-\eta}$ qu'emploie tout le dépôt est le **pire** des trois
ajustements sur la courbe mesurée. → [exposition mesurée](exposition-mesuree.md)

**Des estimateurs contrefactuels confrontés à une vérité terrain.** +2,5 % d'écart contre +32 %
pour l'estimation naïve — avec le diagnostic qui interdit d'en tirer gloire, une taille
d'échantillon effective de 1 513 pour 4 millions d'impressions. Aucun estimateur ne remplace
l'exploration : le doublement robuste fait moins bien. → [rang servi](rang-servi.md)

**Une frontière exacte contre laquelle juger un réordonnanceur.** Le filtre du dépôt s'y tient —
0,0 à 1,0 % d'engagement laissé sur la table — mais MMR aussi, et le prix de la norme dépend du
lecteur : 3,8 % quand ses intérêts traversent les points de vue, 17,1 % quand sa préférence *est*
un point de vue. → [lignes de base](lignes-de-base.md)

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
* **aucun jeu public ne permet l'évaluation annoncée** — MIND a les catégories sans le rang,
  Baidu-ULTR le rang sans étiquette → [MIND](mind.md) · [rang servi](rang-servi.md) ;
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
  → [format et retour](format-et-retour.md).

## Ce qui n'est pas tranché

* **L'indice n'a jamais été mesuré sur un fil réel.** La lacune est de **donnée**, non de méthode,
  et [la demande](article-40.md) dit exactement ce qu'il faudrait.
* **La pondération de rang dépend de la page servie**, pas seulement de la surface : un format
  enrichi au-dessus retire 8,4 points d'examen à ce qui suit. Aucune loi $e(R)$ ne représente
  cela, et le dépôt n'en propose pas de remplaçante.
* **Le niveau du plancher est une décision politique**, comme le catalogue de points de vue. La
  mesure décrit, elle ne prescrit pas.
* **Les trois codeurs de l'annotation sont des instances du même modèle de langue.**
* **Rien ne démontre que les opinions humaines *obéissent* à une mécanique statistique.**

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
[le notebook 04](notebooks/04_fokker_planck_paysage.ipynb).
///

## Explorer

Les vingt-quatre notebooks sont exécutables et produisent l'intégralité des figures de la
note. Chacun se lit indépendamment.

| Notebook | Ce qu'il montre |
|---|---|
| [01 — Entropie et pureté](notebooks/01_entropie_et_purete.ipynb) | une superposition cohérente a une entropie nulle ; l'IDE et sa normalisation |
| [02 — Ising](notebooks/02_ising_temperature_sociale.ipynb) | la température critique d'Onsager, retrouvée numériquement |
| [03 — Voter Model](notebooks/03_voter_consensus_et_taille.ipynb) | les lois d'échelle du consensus, et pourquoi la connectivité n'est pas la coupable |
| [04 — Fokker-Planck](notebooks/04_fokker_planck_paysage.ipynb) | les trois régimes de l'opinion publique dans un même paysage d'énergie libre |
| [05 — Hystérésis](notebooks/05_hysteresis_et_contre_champ.ipynb) | la mémoire d'une fausse croyance, et les deux façons de l'effacer |
| [06 — Résonance](notebooks/06_resonance_larsen.ipynb) | le seuil $\gamma\alpha > \lambda$ et le cycle limite de l'attention |
| [07 — ADE](notebooks/07_ade_filtre_entropique.ipynb) | un fil gelé qui se réouvre sous l'effet du recuit |
| [08 — Modèle à agents](notebooks/08_abm_compas_politique.ipynb) | la bulle de filtres vue depuis l'individu |
| [09 — Calibration](notebooks/09_calibration_visibilite.ipynb) | $\gamma\alpha/\lambda$ mesuré sur 19 épisodes d'attention publics |
| [10 — Changement de régime](notebooks/10_changement_de_regime.ipynb) | 14 basculements datés, et pourquoi le rapport n'y est pas identifiable |
| [11 — Corpus étendu](notebooks/11_corpus_etendu.ipynb) | 440 sujets dérivés de catégories : l'écart de persistance ne se réplique pas |
| [12 — Annotation en aveugle](notebooks/12_annotation_en_aveugle.ipynb) | 40 % de bruit d'étiquetage mesuré, et le double recodage à $\kappa = 0{,}92$ |
| [13 — Test adverse](notebooks/13_test_adverse_index.ipynb) | un plancher d'IDE saturé à coût nul, et le correctif qui prescrivait la polarisation |
| [14 — Rang et contrefactuel](notebooks/14_rang_et_contrefactuel.ipynb) | l'enterrement de la diversité, et l'évaluation hors ligne fausse de 201 % |
| [15 — Rang adverse](notebooks/15_rang_adverse_et_severite.ipynb) | les quatre mesures contournées par l'ordre, et la sévérité du biais estimée |
| [16 — Exploration de MIND](notebooks/16_exploration_mind.ipynb) | un ordre indiscernable d'un mélange, et cinq sévérités tirées du même jeu |
| [17 — Rang servi](notebooks/17_rang_servi.ipynb) | deux journaux qui enregistrent le rang, et un estimateur jugé contre la vérité |
| [18 — Demande article 40](notebooks/18_demande_article_40.ipynb) | quatre tableaux agrégés qui suffisent, et la preuve qu'ils suffisent |
| [19 — Lignes de base](notebooks/19_lignes_de_base.ipynb) | le filtre jugé contre quatre concurrents et contre la frontière exacte |
| [20 — Contre-expertise](notebooks/20_contre_expertise.ipynb) | cinq contre-épreuves, dont une qui retire une conclusion publiée |
| [21 — Angles morts](notebooks/21_angles_morts.ipynb) | le test tient sous cascade, la loi de puissance non |
| [22 — Test de forme](notebooks/22_test_de_forme.ipynb) | le troisième contrôle, et le collider qu'il a failli publier |
| [23 — Exposition mesurée](notebooks/23_exposition_mesuree.ipynb) | une colonne jamais lue, et six chapitres d'estimation rendus inutiles |
| [24 — Format et retour](notebooks/24_format_et_retour.ipynb) | la cascade réfutée deux fois, et une de mes explications retirée |

## Reproduire

Tout s'exécute en conteneur. Aucune dépendance n'est installée sur la machine hôte.

```bash
git clone git@github.com:s-geffroy/Indice-Diversite-Exposee.git
cd Indice-Diversite-Exposee

docker compose run --rm test          # 599 tests
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
