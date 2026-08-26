# Changelog

Toutes les évolutions notables de ce projet sont consignées dans ce fichier.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le
versionnement respecte [Semantic Versioning](https://semver.org/lang/fr/).

## [Non publié]

### Corrigé — relecture complète après la coupe

Une relecture systématique du dépôt restreint, après coup. Sept défauts, dont un de fond.

- **Le chiffre mesuré emploie la forme que le dépôt a lui-même disqualifiée.** Les 0,50 par
  journée-utilisateur sont calculés sur les **étiquettes**, sans regarder le rang — c'est-à-dire
  la forme que le test adverse sature à 1,000 et que le rang adverse contourne par l'enterrement.
  Ce n'est pas une négligence — sur un journal qui n'enregistre ni le rang ni le contenu, c'est
  la seule forme calculable — mais rien ne le disait. **0,50 se lit désormais comme une borne
  supérieure**, et la réserve figure sur les quatre pages qui citent le chiffre.
- **`substitutions_to_floor` est retirée** : elle ne servait qu'à tarifer une norme.
  `attainable_index` reste — le plafond de l'indice selon le volume servi est une propriété de la
  grandeur, pas de la régulation.
- **`data/pageviews/`** — 461 fichiers, 2,8 Mo de cache Wikipédia versionné pour un corpus
  supprimé — disparaît.
- Deux renvois morts dans les docstrings (`docs/memorandum.md`, `ide.privacy`), deux ancres
  d'audit inexistantes (`§2.1`, `§2.2`), un compte de tests périmé (623) et une dérive de
  vocabulaire (« index » pour « indice », cadrage normatif resté en français mais corrigé en
  anglais) : corrigés.
- **Le README documente enfin les trois chaînes de récupération** — MIND, Baidu-ULTR et Open
  Bandit, EB-NeRD. Les deux scripts EB-NeRD, qui produisent le condensé derrière la seule mesure
  réelle du dépôt, n'étaient cités nulle part.
- 256 tests.

### Nettoyé — les traces des moitiés retirées

Supprimer des fichiers ne suffit pas à changer un périmètre. Un décompte après coup a trouvé
**une soixantaine de mentions** des moitiés retirées dans les pages conservées.

- **16 mentions du « régulateur »**, 8 renvois à l'article 40, 6 à l'ADE, 4 au mémorandum et 4
  aux lignes de base, réécrits — dans les deux langues. Ce qui relevait d'un cadrage normatif
  (« ce qu'un régulateur doit exiger ») devient ce qu'il faut exiger d'un journal ; ce qui
  désignait un déposant devient le déclarant du catalogue.
- **Le test adverse est recadré.** Il attaquait une *norme* ; il attaque une **mesure**. Une
  grandeur qu'on sature à coût nul est mauvaise, qu'on l'impose ou non.
- **La bibliographie est ramenée à ce que le travail utilise** : quatre thèmes au lieu de sept,
  vingt références au lieu de trente-quatre. Décohérence quantique, physique statistique de
  l'opinion et droit européen disparaissent de `paper/refs.bib`, et les deux notes recompilent
  sans citation manquante.
- **`legacy/`** — le prototype `pygame` du modèle à agents — est supprimé.
- **`docs/errata.md`** reçoit le même avertissement que l'audit : il couvre plus que le dépôt, et
  c'est délibéré.

### Retiré — le dépôt ne mesure plus qu'une chose

Décision de périmètre : **un vrai Indice de Diversité Exposée, et pas plus.** Trois moitiés
quittent le dépôt.

- **L'appareil de régulation** — mémorandum, demande au titre de l'article 40, plancher, coût de
  la vie privée, tableaux agrégés. Ses propres mesures l'avaient vidé de sa substance : un niveau
  qui dépend du catalogue, qu'un contenu servi sur 177 suffit à satisfaire, et une grandeur
  agrégée qui invite à traiter la marge plutôt que les lecteurs les plus enfermés.
- **L'algorithme** — l'ADE et les lignes de base qui le jugeaient. Ce dépôt mesure, il ne
  prescrit pas, et une heuristique de 1998 faisait aussi bien.
- **La physique** — analogie avec la décohérence, Ising, Voter, Fokker-Planck, résonance, modèle
  à agents, calibration, corpus étendu, annotation en aveugle. L'analogie avait été réfutée
  transfert par transfert, et la seule prédiction propre du formalisme mesurée quatre fois sans
  effet.

Ce qui reste est l'indice, ce qui l'attaque et ce qui le mesure : sa définition et ses trois
choix, les trois contrôles de recevabilité d'un journal, l'exposition mesurée, la mesure sur des
fils réels, et le catalogue.

- **L'audit est conservé entier.** Les vingt-sept corrections restent, **y compris celles qui
  portent sur les moitiés retirées** — une erreur retirée du dépôt reste une erreur commise. Les
  renvois vers les pages disparues sont devenus du texte ; les chiffres et les verdicts sont
  inchangés. Un avertissement en tête de l'audit dit pourquoi il couvre plus que le dépôt.
- **Les numéros des notebooks ne sont pas renumérotés.** Les trous sont ceux des chapitres
  retirés, et l'audit continue de désigner ce dont il parle.
- Onze modules sur vingt-six, douze notebooks sur vingt-neuf, **261 tests**. Les deux notes
  LaTeX passent de 29 et 28 pages à **16 et 16**, sans référence morte ni boîte débordante.
- `README`, page d'accueil, `docs/ide.md`, feuille de route, appel à relecture et métadonnées de
  citation réécrits autour de l'indice seul. Version **0.2.0**.


### Ajouté — le prix d'un plancher, mesuré sur des fils réels

Le dépôt chiffrait le coût d'une norme de diversité entre 8,2 % et 18,9 % d'engagement — mais en
**supposant la pertinence connue**, sur des fils simulés. Les journées-utilisateur réelles
permettent de poser la question sans rien supposer : combien de contenus servis faudrait-il
**remplacer** ?

- **Le contrôle d'abord.** Le calcul est glouton ; confronté à l'énumération exhaustive de
  toutes les redistributions sur deux cents compositions courtes, il coïncide **200 fois sur
  200**. Le prix publié n'est donc pas une borne prudente.
- **Le plancher proposé par ce dépôt est décoratif.** Ramener toute la population au-dessus de
  0,40 demande de remplacer **un contenu servi sur 177** — 0,57 % du journal — et la
  journée-utilisateur médiane à traiter n'exige qu'**une seule** substitution.
- **Le prix est convexe** : 0,21 % à un plancher de 0,30 ; **2,27 %** à 0,50 ; **8,24 %** à
  0,60 ; **17,11 %** à 0,70. Le niveau retenu jusqu'ici est à l'extrémité indolore de la courbe.
- **La forme de la grandeur réglementée est en cause.** La part sous le seuil a été choisie
  contre le masquage par la moyenne ; mais une part est un seuil, et un seuil s'atteint **par la
  marge** — on corrige les lecteurs juste en dessous, les plus enfermés restent où ils sont.
- **Un plafond que rien ne lève.** Une entropie ne dépasse pas le logarithme du nombre de
  contenus *servis* : cinq contenus plafonnent à 0,49. À 0,60, **10,9 %** des journées sont hors
  d'atteinte ; à 0,80, **22,9 %**. Ce sont des lecteurs **légers**, pas enfermés, et la seule
  conformité possible serait de leur servir davantage — ce qu'une norme de diversité n'a aucune
  raison d'encourager.
- `ide.entropy.attainable_index` et `substitutions_to_floor`,
  [`docs/prix-du-plancher.md`](docs/prix-du-plancher.md) et
  [notebook 29](notebooks/29_prix_du_plancher.ipynb).
- 659 tests, deux notes recompilées (29 et 28 pages).

### Ajouté — qui choisit le catalogue choisit l'indice

Le dépôt répétait depuis le premier jour que « la discrétisation en points de vue est un choix
politique » sans jamais le chiffrer. C'est fait, sur 58 549 journées-utilisateur réelles.

- **Le niveau n'a aucun sens absolu.** Le même corpus vaut **0,498** sur vingt-six rubriques et
  **0,924** sur trois. À un plancher de 0,40, la part de la population sous le seuil passe de
  **13,7 % à 1,5 %** : le même plancher devient décoratif sans qu'une impression ait changé.
- **L'ordre, lui, tient — puis s'effondre.** Concordance de rang avec le catalogue complet :
  **1,000** à douze modalités, **0,911** à six, **−0,09** à trois. La raison est banale : les
  onze rubriques les plus servies couvrent **99,8 %** du corpus, et regrouper les quinze autres
  ne fusionne quoi que ce soit que pour une journée sur mille.
- **La taille ne spécifie pas le catalogue.** Vingt regroupements aléatoires en six classes
  rendent 0,682 ± 0,093 contre 0,860 par fréquence, et une concordance de 0,769 contre 0,911.
  C'est la **liste** qui doit figurer dans une norme, pas le nombre.
- **Et « la diversité exposée » n'existe pas au singulier.** Rubriques et tonalité ne concordent
  qu'à **ρ = +0,155** ; parmi le quart le plus divers en rubriques, 23,8 % sont aussi dans le
  quart le plus divers en tonalité, là où l'indépendance donnerait 25 %.
- `ide.entropy.coarsen_catalogue`, le second axe d'étiquetage dans le condensé EB-NeRD,
  [`docs/catalogue.md`](docs/catalogue.md) et [notebook 28](notebooks/28_catalogue.ipynb).

### Corrigé — les chiffres par journée-utilisateur du chapitre 26 étaient faux

Trouvés en écrivant le chapitre ci-dessus, qui avait besoin de l'identité des rubriques.

- **La cause.** Le condensé retenait les effectifs par rubrique **triés**, et l'agrégation d'un
  lecteur sur une journée additionnait ces vecteurs triés — ce qui revient à traiter « la rubrique
  la plus servie de ce fil-ci » et « celle de ce fil-là » comme la même.
- **Les chiffres corrigés.** 0,466 → **0,498** ; 4,56 → **5,07** rubriques effectives ; 18,8 % →
  **13,7 %** sous 0,40 ; et surtout 71,2 % → **50,7 %** sous 0,50. L'erreur **concentrait** la
  composition, donc sous-estimait la diversité : elle faisait paraître la plateforme moins
  conforme qu'elle n'est. Les chiffres par **fil servi** étaient justes.
- [`docs/limites.md`](docs/limites.md) reçoit sa **vingt-septième correction** : une optimisation
  de stockage est une hypothèse déguisée, et c'est la **deuxième fois** que ce dépôt s'y laisse
  prendre. Le condensé retient désormais les compositions **identifiées**, et un test vérifie que
  les deux tables rendent le même indice.
- Le chapitre sur la vie privée est mis à jour en conséquence ; ses conclusions ne bougent pas.
- 650 tests, deux notes recompilées (29 et 27 pages).

### Corrigé — le site publiait les notebooks en JSON brut

Signalé par un lecteur : ouvrir n'importe quel notebook du site rendait
`{ "cells": [ …` sur plusieurs milliers de lignes. **Aucun notebook n'a jamais été rendu.**

- **La cause.** `mkdocs-jupyter` enveloppe les `.ipynb` dans une classe qui les rend comme des
  pages ; `mkdocs-static-i18n` reconstruit ensuite la collection de fichiers et **perd
  l'enveloppe**. MkDocs recopie alors le notebook tel quel. Toutes les combinaisons de versions
  essayées échouent de la même façon : le rendu n'a jamais fonctionné.
- **Ce qui rend la panne remarquable :** la construction réussissait **en mode strict**, sans une
  alerte, et l'intégration continue était verte à chaque fois. Le mode strict vérifie les liens
  et les fichiers manquants — **pas le contenu des pages**.
- **Le correctif.** [`scripts/render_notebooks.py`](scripts/render_notebooks.py) rend les
  notebooks en Markdown avec `nbconvert` **avant** MkDocs : plus aucune interaction entre
  greffons à espérer. Les liens internes sont recalculés pour l'arborescence du site, et chaque
  page renvoie vers sa source exécutable.
- **Le garde-fou.** [`scripts/check_site.py`](scripts/check_site.py), appelé à chaque
  construction locale et en intégration continue, **ouvre les pages produites** et refuse un site
  où un notebook n'est pas du HTML. Quatre tests couvrent le rendu et le contrôle.
- **Les versions de l'image du site sont figées**, non plus bornées : une plage ouverte est ce
  qui a permis à la panne de rester invisible.
- [`docs/limites.md`](docs/limites.md) reçoit sa **vingt-sixième correction**, dont la leçon est
  la même que les vingt-cinq précédentes, appliquée cette fois à l'outillage du dépôt :
  *une vérification qui réussit ne prouve rien tant qu'on n'a pas regardé ce qu'elle vérifie.*
- 646 tests, site vérifié page par page.

### Ajouté — ce que la vie privée coûte à l'audit

La demande au titre de l'article 40 prouvait que quatre tableaux agrégés **suffisent**. Elle ne
disait rien de leur **innocuité** — et l'audit le reconnaissait sans y remédier : « un protocole
d'audit crédible doit être agrégatif et différentiellement privé, ce dépôt ne le propose pas ».
Il le propose maintenant, et en publie le prix.

- **La grandeur réglementée est presque gratuite à protéger.** La part de la population sous le
  plancher ne bouge pas d'un millième entre $\varepsilon = 10$ et $\varepsilon = 0{,}1$ : un
  histogramme de 50 classes sur 58 549 journées-utilisateur est hors d'atteinte du bruit.
- **La grandeur dont elle dépend ne l'est pas du tout.** À $\varepsilon = 1$ — valeur de
  référence usuelle — la sévérité passe de **0,88 à 0,50**, et son erreur type ne bouge pas. Le
  bruit sur des effectifs agit comme une erreur de mesure : il **atténue** sans que rien ne le
  signale, et dans le sens qui fait paraître l'enterrement moins grave.
- **Le vrai prix n'est pas le bruit, c'est le plafonnement des contributions**, sans lequel
  aucune garantie *par personne* n'existe. Il ajoute **+0,6 à +2,5 points** à une part de 18,8 %,
  toujours vers l'excès : les lecteurs assidus sont plus divers, et les écarter fait paraître la
  plateforme moins conforme qu'elle n'est. L'erreur commise en protégeant les lecteurs
  **n'innocente pas** la plateforme.
- **Le nœud, qui ne se dénoue pas.** La marge de rang survit à $\varepsilon = 0{,}03$ et tombe à
  0,7 % de la valeur à contenu fixé — mais on ne le sait que grâce au tableau que nulle garantie
  ne protège. *La quantité qui se publie sans risque est celle qu'on ne peut pas vérifier.*
- **La demande change.** Le tableau 3 ne doit plus être demandé tel quel : la marge de rang
  ($\varepsilon = 0{,}1$), l'estimation à effets fixes **calculée par la plateforme** et publiée
  comme scalaire bruité, et l'écart entre les deux. Le plafond de contributions se publie avec le
  résultat, comme le seuil de suppression.
- Nouveau module `ide.privacy` (mécanisme de Laplace, seuil de publication $(\varepsilon,
  \delta)$, plafonnement des contributions), croisement charge × indice ajouté au condensé
  EB-NeRD, [`docs/vie-privee.md`](docs/vie-privee.md) et
  [notebook 27](notebooks/27_vie_privee.ipynb), reproductible depuis les condensés versionnés.
- 638 tests, deux notes recompilées (28 et 27 pages, zéro boîte débordante).

### Ajouté — l'hypothèse de fond, enfin sous une forme qui peut échouer

L'audit se terminait depuis le premier jour sur la même réserve : *rien ne démontre que les
opinions humaines obéissent à une mécanique statistique*. Ce n'était pas de la prudence, c'était
un aveu — l'hypothèse n'avait jamais été énoncée de façon à pouvoir être perdue.

- **L'énoncé décisif est une contrainte de fluctuation-réponse.** Ce qui distingue une mécanique
  statistique d'une métaphore thermodynamique n'est pas un bon ajustement — un modèle à deux
  paramètres ajuste n'importe quelle bimodale — mais le fait qu'**un seul et même nombre**
  gouverne ce qu'un groupe fait tout seul et ce qu'il fait quand on le pousse :
  $\hat{T} = N \, \mathrm{Var}(\bar{x}) / \chi$.
- **Le contenu réfutable est l'invariance, non la valeur** : le champ n'étant défini qu'à une
  échelle près, seule compte la constance de $\hat{T}$ à travers les tailles de groupe, les
  intensités d'intervention et les groupes de même diversité d'exposition. Trois régressions,
  trois seuils de réfutation écrits à l'avance.
- **La liste des retraits est publiée avant le test**, pas après : énergie libre, paysage,
  hystérésis, recuit et température sociale tombent si le test échoue — et les trois contrôles de
  journal, la sévérité mesurée, l'encadrement de l'indice et la demande d'accès **n'en dépendent
  pas**. C'est la partition qui compte.
- **Une ligne du verdict de l'audit est corrigée.** « Plus le système est grand, plus il se
  désordonne : faux, et à l'envers » invitait à lire « donc plus ordonné ». Ce n'est pas ce que
  le modèle dit : la fluctuation de la **moyenne** décroît en $1/N$, la dispersion des opinions
  **individuelles** ne fait l'objet d'aucune prédiction. Ce qui croît avec la taille est la
  **stabilité du désaccord**, pas l'accord.
- [`docs/hypothese-testable.md`](docs/hypothese-testable.md), sa jumelle anglaise, et les renvois
  depuis l'audit et la page d'accueil. **Ce chapitre ne mesure rien** — c'est le premier du dépôt
  dans ce cas, et il le dit en tête.

### Ajouté — l'indice, mesuré pour la première fois sur un fil réel

Six chapitres répétaient qu'« aucun jeu de données public ne porte à la fois le rang servi et une
étiquette de point de vue interprétable ». C'était une **affirmation d'absence** fondée sur trois
jeux examinés, écrite comme si elle portait sur tous. Le quatrième jeu regardé porte les deux
colonnes.

- **EB-NeRD** (*Ekstra Bladet*, RecSys Challenge 2024) donne la liste servie **et** une rubrique
  déclarée par article. Le premier contrôle du dépôt dit alors que son **ordre enregistré ne
  contient pas le rang** : $z = +1{,}05$, $p = 0{,}29$ sur 232 887 fils — et ce n'est pas un
  défaut de puissance, le journal aurait détecté une sévérité de $0{,}0066$, **134 fois plus
  faible** que celle mesurée sur Baidu-ULTR.
- **Le chiffre qui manquait depuis le premier jour.** L'indice aveugle au rang vaut **0,47** par
  journée-utilisateur — la fenêtre que le protocole du dépôt prescrit — soit **4,6 rubriques
  également servies sur 26**, avec 18,8 % des journées sous 0,40 et 71,2 % sous 0,50. Le dépôt
  n'avait jamais publié ce nombre autrement qu'en simulation.
- **L'indice exposé, faute d'ordre, est encadré exactement.** `ide.entropy.exposed_index_bounds`
  énumère toutes les mises en ordre distinctes : largeur médiane **0,104**. À un plancher de
  0,40, **32,4 %** des fils y contreviennent quelle que soit leur mise en ordre — constat
  opposable sans la colonne manquante — 7,9 % sont sûrement conformes, et **59,7 % restent
  indécidables**. *Sans le rang, on peut condamner ; on n'acquitte presque jamais.*
- **La demande au titre de l'article 40 change d'objet.** Elle réclamait « le rang servi » ; elle
  réclame désormais le rang **vérifiable**, parce qu'une plateforme peut livrer une colonne
  d'ordre qui n'est pas le rang sans mentir et sans que rien ne le signale. Le test
  d'échangeabilité devient une **clause de recevabilité**.
- Nouveau module `ide.ebnerd` (empreintes SHA-256, lecture, condensé de **signatures de
  composition** — effectifs par rubrique, triés et anonymes), `ide.entropy.exposed_index_bounds`,
  deux scripts, [`docs/indice-mesure.md`](docs/indice-mesure.md) et
  [notebook 26](notebooks/26_indice_mesure.ipynb), **reproductible depuis le condensé versionné**.
  Le journal brut, sous licence de recherche non redistribuable, ne l'est pas.
- [`docs/limites.md`](docs/limites.md) reçoit sa **vingt-cinquième correction**, dont la leçon est
  neuve : la règle du dépôt — ne rien publier qu'on n'ait mesuré — ne couvre pas les absences.
  Sa jumelle manquait : **une affirmation d'absence doit publier l'étendue de la recherche qui la
  fonde.**
- 623 tests, deux notes recompilées (27 et 26 pages, zéro boîte débordante).

### Ajouté — l'effet de page, une fois la composition retirée

L'entrée précédente retirait la méthode du rang de résultat sans rien mettre à la place. Ce
chapitre met autre chose : une **mesure**, et elle corrige le dépôt d'un facteur trois.

- **Le chapitre 24 avait conclu trop vite.** Il mesurait qu'un format enrichi servi plus haut
  retire 8,4 points d'examen à ce qui suit, à rang **et** à hauteur de page comparables, et en
  tirait qu'« aucune loi $e(R)$ ne peut représenter cela ». Il tenait le rang et les pixels fixes,
  mais **pas le contenu** — or un encadré de réponse ne s'affiche pas au hasard.
- **À contenu tenu fixe, il reste 6 % au lieu de 18 %.** Rapport de risques de Mantel-Haenszel
  $0{,}940$, IC95 $[0{,}916 ; 0{,}964]$, sur 1 106 strates et 31 045 impressions. Un **second
  appariement, par requête**, indépendant du premier, rend $0{,}942$ — deux plans qui ne partagent
  aucune strate, à deux millièmes près.
- **Une simulation sans aucun effet reproduit le chiffre publié.** Dans un monde où le format ne
  fait rien mais où les pages enrichies tombent sur des contenus moins consultés, la
  stratification par le rang rend $0{,}785$ ; l'appariement rend $1{,}005$, et retrouve $0{,}896$
  quand un effet de $0{,}90$ est simulé.
- **La conclusion positive :** ignorer la composition de la page déplace l'indice de $0{,}0025$,
  là où la convention $1/R$ le déplace de $0{,}0350$ — **quatorze fois plus**. La remise
  d'attention redevient **transportable**, ce qui était l'enjeu réel : si elle dépendait de la
  page, aucun plancher réglementaire ne pouvait s'écrire sans décrire chaque page servie.
- Nouveau chapitre [`docs/effet-de-page.md`](docs/effet-de-page.md) et
  [notebook 25](notebooks/25_effet_de_page.ipynb), **reproductibles depuis le condensé versionné**
  — contrairement au chapitre 24, qui exigeait le journal brut.
- `ide.logs` gagne `stratified_risk_ratio` (Mantel-Haenszel, variance de Greenland-Robins) et
  `count_above` ; `ide.exposure` gagne `PageComposition`, `page_effect_counts` et
  `page_examination_curve`. Le condensé porte les comptes appariés des deux stratifications.
- [`docs/limites.md`](docs/limites.md) reçoit sa **vingt-quatrième correction** ; la demande au
  titre de l'article 40 ramène la colonne `format` de nécessaire à **utile** ; la conclusion
  générale devient : *ce qui tient est une grandeur — l'exposition, qu'on peut mesurer au lieu de
  la supposer : 0,88 et non 1, sans cascade, et à 6 % près indépendante de la page servie.*
- 610 tests, deux notes recompilées (26 et 25 pages, zéro boîte débordante).

### Retiré — « la méthode est le vrai résultat »

L'entrée précédente donnait pour conclusion au dépôt trois règles de méthode. C'était un excès,
signalé en relecture, et il est retiré. Trois raisons, désormais consignées dans
[`docs/limites.md`](docs/limites.md) :

- les règles — mesurer plutôt qu'estimer, éprouver un protocole sur des données dont on connaît la
  réponse, tester une explication comme un chiffre — sont **banales** : personne ne les conteste,
  et aucun relecteur ne les recevra comme un résultat ;
- la démonstration est **circulaire** : une méthode dont la valeur se prouve par les vingt-trois
  erreurs qu'elle a rattrapées se compare à une référence que le même travail a fabriquée ;
- rien n'a été **validé de l'extérieur** : les 599 tests vérifient que le code fait ce qui est
  annoncé, non que ce qui est annoncé soit vrai.

Ce qui se transmet d'un dépôt, ce sont ses **objets** — un test exact, une spécification agrégée,
un exposant mesuré, dix résultats négatifs : chacun s'applique à d'autres données et répond seul,
là où un précepte demande qu'on y adhère. La section de méthode disparaît de l'accueil et du
README ; la phrase de conclusion devient *« les instruments tiennent, mais seulement après
correction — et ce qui se transmet d'un dépôt, ce sont ses objets, pas la discipline qui les a
produits »* ; « ce qui n'est pas tranché » gagne l'entrée qui manquait — **rien n'a été validé de
l'extérieur**, et c'est le seul verrou que ce dépôt ne peut pas lever seul.

### Modifié — la conclusion générale, remise à l'état des mesures

La page d'accueil avait de nouveau grossi par accrétion : six paragraphes commençant par « Et… »,
un par chapitre, et un tableau de verdict qui datait d'avant la contre-expertise. Réécriture.

- **Le verdict** est refait : huit lignes, dont trois nouvelles — la forme retenue dont la
  pondération dépend de la **page servie**, les instruments **valides après correction**, et
  l'exposition **mesurable et mesurée**.
- **Une section neuve — « la méthode, qui est le vrai résultat »** : mesurer plutôt qu'estimer ;
  appliquer tout protocole d'abord à des données dont on connaît la réponse ; tester une
  explication comme un chiffre. Trois règles acquises chacune en violant la précédente.
- **La phrase de conclusion est corrigée.** « La théorie n'a pas tenu, la métrologie oui »
  devient : *la métrologie tient, mais seulement parce qu'elle a été corrigée à chaque étape — et
  ce qui survit le mieux n'est aucun instrument en particulier, c'est la méthode.*
- **« Ce qui est tombé » est scindé** en résultats négatifs *sur le monde* (cinq) et *sur les
  propositions du dépôt lui-même* (cinq). La seconde moitié n'existait pas.
- **La figure d'ouverture** passe de l'enterrement à l'exposition mesurée : le premier résultat a
  été restreint depuis, le second illustre la thèse du dépôt.
- [`docs/limites.md`](docs/limites.md) reçoit une **synthèse des vingt-trois corrections** :
  les erreurs qui survivent le plus longtemps sont celles qui produisent des chiffres
  vraisemblables ; ce qui les attrape n'est jamais la relecture mais la confrontation ; et la
  moitié portent sur les propositions du dépôt, non sur son point de départ.
- Les **résumés des deux notes LaTeX** intègrent la mesure directe de l'exposition, la réfutation
  de la cascade et l'effet du format — la conclusion principale de leur partie I étant désormais
  négative pour la méthode qui venait d'y être construite.
- [`docs/feuille-de-route.md`](docs/feuille-de-route.md) — la demande a gagné deux colonnes, et
  chacune parce qu'une mesure a montré ce qu'on perdait sans elle.

### Ajouté — le format, le retour, et une explication retirée

Les deux dernières colonnes inexploitées de Baidu-ULTR. Détail :
[`docs/format-et-retour.md`](docs/format-et-retour.md) et le
[notebook 24](notebooks/24_format_et_retour.ipynb).

### Résultats — la cascade réfutée deux fois, et le format qui manquait

- **`slipoff_count_after_click` réfute la cascade par un fait consigné** : la colonne est non
  nulle pour **43,7 %** des lignes cliquées et 0,5 % des autres. Après un clic, le journal
  enregistre que des documents ont défilé, donc que le lecteur est revenu — sous cascade stricte,
  elle serait toujours nulle. La part croît avec la profondeur du clic, de 0,37 au premier rang à
  0,59 au sixième. C'est une **voie indépendante** du test statistique du chapitre précédent.
- **`media_type` établit que le format modifie l'exposition** : un format enrichi au-dessus retire
  **8,4 points** d'examen à ce qui suit, médiane sur 21 strates toutes de même signe, à rang **et**
  à hauteur cumulée comparables. L'effet **ne passe donc pas par la géométrie** — un contenu
  enrichi est pourtant plus haut, 273 pixels contre 192 — et l'explication qui reste est celle de
  la **satisfaction**.
- **Conséquence sur la norme** : la remise d'attention $w_R$ n'est pas une propriété du rang, ni
  même de la surface, mais de la **page servie**. Deux fils de composition identique, servis avec
  des formats différents, n'exposent pas la même chose. Aucune loi $e(R)$ ne peut le représenter.

### Corrigé — une explication mécanique avancée sans la tester

- Le chapitre précédent attribuait la forme en deux temps de la courbe d'examen à un **pli
  d'écran**, et invoquait `serp_height`. Cette colonne permettait précisément de tester
  l'hypothèse, et elle la **réfute** : le rang explique mieux l'examen ($R^2$ de McFadden 0,082)
  que la hauteur cumulée au-dessus (0,057), et les pixels n'ajoutent que 0,0007 une fois le rang
  connu. À rang égal, l'effet des pixels ne subsiste qu'aux deux premiers rangs puis s'éteint —
  l'inverse de ce qu'un seuil d'écran prédirait.
- **Le constat tient, l'explication tombe** : la courbe mesurée n'est toujours pas une loi de
  puissance. Vingt-troisième entrée de l'[audit](docs/limites.md), avec sa leçon : *une
  explication mécanique se formule en une phrase et se teste en une heure ; l'écart entre les deux
  est exactement l'endroit où une affirmation fausse s'installe.*

### Modifié — une sixième colonne à la demande d'accès

- [`docs/article-40.md`](docs/article-40.md) — le tableau 3 réclame désormais aussi une colonne
  **`format`**. Sans elle, deux fils de composition identique peuvent exposer des diversités
  différentes sans que rien ne le signale. C'est la moins sensible des colonnes demandées : le
  format d'un contenu ne dit rien de son lecteur.
- [`docs/memorandum.md`](docs/memorandum.md) — la remise d'attention est une propriété de la page
  servie, non de la surface.
- [`docs/exposition-mesuree.md`](docs/exposition-mesuree.md) porte l'avertissement sur le pli
  d'écran, à l'endroit où l'hypothèse avait été avancée.
- Les deux notes LaTeX reçoivent la sous-section correspondante (25 et 24 pages).

### Ajouté — l'exposition mesurée, et non plus estimée

La piste ouverte par le test de forme : lire les colonnes d'**examen** de Baidu-ULTR, jamais
ouvertes par ce dépôt. Détail : [`docs/exposition-mesuree.md`](docs/exposition-mesuree.md) et le
[notebook 23](notebooks/23_exposition_mesuree.ipynb).

- **`ide.exposure.load_baidu_part(with_examination=True)`** lit `displayed_time` et rend le masque
  d'affichage ; **`ide.exposure.examination_counts`** l'expose depuis le condensé, qui porte
  désormais les comptes d'examen par cellule.
- **`ide.logs.upstream_dependence_test(outcome=…)`** — le test de forme accepte une grandeur
  autre que le clic. C'est l'unique modification nécessaire pour lever son impasse.
- **`notebooks/23_exposition_mesuree.ipynb`**, `paper/figures/fig23_exposition_mesuree.png` et 4
  tests supplémentaires (599 au total).

### Résultats — la cascade réfutée, le chiffre publié révisé

- **L'impasse du test de forme tombe.** Sur les clics, cascade et budget sont confondus ; sur
  l'examen, la discrimination est totale : $z = -158$ à $-412$ sous cascade contre $-1{,}03$ sous
  budget, **quel que soit le budget**.
- **Sur Baidu-ULTR, la cascade est réfutée** : l'examen sous un clic y est **plus** fréquent, pas
  moins — 0,221 contre 0,136 au neuvième rang, $z = +8{,}4$ à $+10{,}9$. C'est le confondant
  d'hétérogénéité, mesuré directement.
- **La sévérité publiée est révisée** : $\eta = 0{,}882 \pm 0{,}046$ sur **143** documents, contre
  $1{,}085 \pm 0{,}093$ sur 55 estimé par les clics. L'estimation **surestime la décroissance de
  23 %**, parce qu'un clic est le produit de l'examen **et** de l'attrait, et que l'attrait décroît
  lui aussi avec le rang.
- **La loi de puissance est le pire des trois ajustements** sur la courbe mesurée : $R^2 = 0{,}72$
  et 42 % d'écart maximal, contre 0,96 pour une décroissance géométrique et 0,99 pour un modèle à
  **pli d'écran**. Au deuxième rang, elle prédit 0,47 quand la mesure donne 0,88.

### Modifié — une cinquième colonne à la demande d'accès

- [`docs/article-40.md`](docs/article-40.md) — le tableau 3 réclame désormais une colonne
  **`affichages`**. Elle retire d'un coup le besoin d'estimer $\eta$, l'hypothèse de forme, et le
  confondant d'attrait — et elle est **moins sensible** que les clics : savoir qu'un contenu a été
  affiché en dit moins sur un lecteur que savoir qu'il l'a choisi.
- [`docs/rang-servi.md`](docs/rang-servi.md) et [`docs/test-de-forme.md`](docs/test-de-forme.md)
  portent la révision et la levée de l'impasse.
- Vingt-deuxième entrée de l'[audit](docs/limites.md) : *estimer une exposition qu'on pouvait
  mesurer*. Le dépôt avait construit trois contrôles, une estimation par effets fixes, un
  étalonnage de puissance et une limite d'identification — pour approcher une grandeur qui était
  dans une colonne du fichier.
- Les deux notes LaTeX reçoivent la sous-section correspondante (24 pages chacune).

### Ajouté — le test de forme, troisième contrôle de la série

La piste ouverte par les angles morts : tester la **forme** de l'examen, pas seulement son
existence. Détail : [`docs/test-de-forme.md`](docs/test-de-forme.md) et le
[notebook 22](notebooks/22_test_de_forme.ipynb).

- **`ide.logs.upstream_dependence_test`** — statistique de Mantel-Haenszel stratifiée par cellule
  (contenu, rang), qui teste si le clic dépend de ce qui s'est passé **au-dessus** dans le même
  fil. Sous modèle de position il n'en dépend pas ; sous cascade, un clic au-dessus supprime les
  clics en dessous. Les moments sont exacts sous l'hypothèse nulle.
- **`ide.logs.upstream_dependence_from_counts`** et **quatre comptes par cellule dans les deux
  condensés** — impressions, impressions précédées d'un clic, clics, clics précédés. Le test se
  recalcule ainsi **à l'identique** sans le journal brut, ce qu'un test vérifie, et il devient
  calculable depuis des agrégats au même titre que les trois autres mesures du dépôt.
- **`notebooks/22_test_de_forme.ipynb`**, `paper/figures/fig22_test_de_forme.png` et 8 tests
  supplémentaires (595 au total).

### Résultats — il fonctionne, et ne tranche pas

- **Les deux contrôles passent.** Aucun rejet sous modèle de position ($|z| < 1$ pour
  $\eta \in \{0 ; 0{,}5 ; 1 ; 2\}$), rejet massif sous cascade ($z = -97$ à $-307$). Le test
  sépare parfaitement les deux modèles **quand ils sont purs**.
- **Mais un budget de clics imite une cascade.** Un lecteur qui cesse de cliquer une fois servi —
  tout en continuant de parcourir le fil — produit $z = -144$ sous modèle de position **pur**,
  contre $-179$ sous cascade véritable. **Rien dans les clics ne les sépare**, et la différence
  est pourtant décisive : sous budget, le contenu placé sous un clic est examiné ; sous cascade,
  il ne l'est pas.
- **Sur Baidu-ULTR, aucune signature de cascade** : $z = +5{,}6$ au seuil le plus permissif,
  $+0{,}5$ à $+0{,}6$ aux plus stricts — le signe est celui du confondant d'hétérogénéité, pas
  celui de la cascade. Trois lectures restent ouvertes, dont la couverture trop mince : 108
  cellules au seuil le plus strict.
- **Ce non-rejet ne valide pas la loi de puissance** : les angles morts ont montré qu'elle se
  trompe d'un facteur 4 110 au douzième rang *si* l'examen est une cascade.

### Corrigé — un collider, rattrapé avant publication

- Restreindre le journal aux **sessions à plusieurs clics** semblait la façon évidente de séparer
  budget et cascade. Appliquée à Baidu-ULTR, la restriction donne $z = -8{,}2$
  ($p = 2 \times 10^{-16}$) : une signature nette, que j'allais publier.
- Le nombre de clics d'un fil est un **collider** de ses clics individuels : conditionner dessus
  induit une dépendance négative entre eux — paradoxe de Berkson — et fabrique donc la signature
  recherchée. Sur un journal simulé sous modèle de position **pur**, la restriction fait passer
  $z$ de $+0{,}74$ à $\mathbf{-45{,}7}$.
- La restriction est proscrite, la mise en garde figure dans la documentation de la fonction, et
  un test fige le faux rejet. Vingt-et-unième entrée de l'[audit](docs/limites.md).
- **Un signal manqué, noté après coup** : la restriction exige le journal **complet** — elle ne se
  calcule pas depuis des comptes agrégés. Un protocole qui a besoin de revenir aux lignes
  individuelles opère une sélection, et une sélection se paie.
- **Troisième occurrence** d'un protocole qui fabrique son propre résultat, et troisième fois
  qu'un contrôle sur données simulées le rattrape. La règle est désormais écrite : *tout protocole
  appliqué à des données réelles doit d'abord être appliqué à des données dont on connaît la
  réponse.*

### Modifié

- [`docs/angles-morts.md`](docs/angles-morts.md) — la piste ouverte est réglée, sans trancher.
- Les deux notes LaTeX reçoivent la sous-section *un troisième contrôle : la forme de l'examen*
  et sont recompilées (23 pages chacune).

### Ajouté — les deux angles morts de la contre-expertise, éprouvés

La contre-expertise s'était terminée en énonçant ce qu'elle n'avait pas fait. Ce sont les deux
hypothèses les plus profondes du dépôt — l'une sur la **forme de l'attention**, l'autre sur ce
que la plateforme **sait de son lecteur**. Détail :
[`docs/angles-morts.md`](docs/angles-morts.md) et le
[notebook 21](notebooks/21_angles_morts.ipynb).

- **`ide.logs.simulate_cascade`** — journal simulé sous un modèle de clic **à cascade**
  (Craswell *et al.*, 2008), où l'examen dépend de ce qui précède. Il rend en option le
  **masque d'examen réel**, vérité terrain que les données réelles ne donnent jamais.
- **`notebooks/21_angles_morts.ipynb`**, `paper/figures/fig21_angles_morts.png` et 5 tests
  supplémentaires (587 au total). Une référence nouvelle au fichier BibTeX.

### Résultats — le test tient, la loi de puissance non

- **Le test d'échangeabilité rejette sous cascade** entre $z = -208$ et $z = -241$ selon la
  probabilité de poursuite — **plus fortement que sur Baidu-ULTR** ($-206$), alors même que la
  cascade réduit le nombre de fils exploitables. Il ne suppose rien de la forme de l'attention,
  et son verdict négatif sur MIND garde donc son sens sous n'importe quel modèle.
- **La loi de puissance $R^{-\eta}$, elle, s'effondre.** Sous cascade la décroissance est
  **géométrique** : au douzième rang, la loi ajustée surestime l'exposition réelle d'un facteur
  **40** ($\gamma = 0{,}95$), **129** ($\gamma = 0{,}85$) et **4 110** ($\gamma = 0{,}60$). Et
  l'ajustement paraît excellent — $\hat\eta \approx 0{,}5$, erreur type $0{,}04$.
- **Sous pertinence estimée, l'avantage des méthodes réglées s'efface.** Leur ordre tient à tous
  les niveaux de bruit, mais l'écart au tirage au sort passe de **16,4 points** à bruit nul à
  **5,8 points** pour une corrélation de rang de 0,50, et **s'inverse** en deçà de 0,36. Le
  hasard est le seul réordonnanceur qui n'utilise pas la pertinence : son manque à gagner est
  invariant, celui de tous les autres croît.

### Corrigé — une forme d'examen supposée, jamais testée

- Le dépôt publie $\hat\eta = 1{,}10 \pm 0{,}09$ sur Baidu-ULTR sous un modèle de position. Ce
  chiffre n'a de sens **que si** l'examen y suit une loi de puissance — et Baidu-ULTR est une
  page de résultats de recherche, terrain d'élection du modèle à cascade. La sévérité doit être
  publiée **avec la forme supposée**, et cette forme reste à tester. Vingtième entrée de
  l'[audit critique](docs/limites.md).
- Les chiffres des [lignes de base](docs/lignes-de-base.md) — 0,0 à 1,0 % de manque à gagner —
  valent pour une **pertinence connue** ; sous un bruit $\sigma = 0{,}2$, le même filtre en
  laisse **5,0 %**.

### Modifié

- [`docs/rang-servi.md`](docs/rang-servi.md), [`docs/lignes-de-base.md`](docs/lignes-de-base.md)
  et [`docs/contre-expertise.md`](docs/contre-expertise.md) portent les restrictions
  correspondantes ; les deux notes LaTeX reçoivent la sous-section *les deux hypothèses les plus
  profondes, éprouvées* et sont recompilées (22 pages chacune).

### Ajouté — contre-expertise des instruments, et bibliographie publiée

Les chapitres précédents attaquaient l'index, la norme, les jeux de données et l'algorithme.
Aucun n'avait attaqué **les instruments de mesure eux-mêmes**, ni confronté les choix du dépôt à
la littérature du domaine. Détail : [`docs/contre-expertise.md`](docs/contre-expertise.md) et le
[notebook 20](notebooks/20_contre_expertise.ipynb).

- **`ide.radio.rank_weights`** accepte désormais une **sévérité mesurée** en plus des remises
  nommées : $w_R = R^{-\eta}$. Les remises nommées sont des conventions d'évaluation, et le
  dépôt a lui-même montré que la sévérité est une propriété de la surface.
- **`ide.entropy.effective_viewpoints`** — conversion de l'indice en **nombre effectif de points
  de vue** (Jost, 2006), la seule forme sous laquelle un seuil se lit sans formation.
- **`docs/bibliographie.md`** et sa version anglaise — **toutes les références du travail**, avec
  ce que chacune sert ici, **dérivées** de `paper/refs.bib` par
  `scripts/build_bibliography.py`. Un test échoue si les deux divergent.
- **`notebooks/20_contre_expertise.ipynb`**, `paper/figures/fig20_contre_expertise.png` et 10
  tests supplémentaires (582 au total). Neuf références nouvelles au fichier BibTeX.

### Corrigé — une conclusion retirée, une restreinte, une incertitude élargie

- **Retirée : « la proximité à la cible résiste le mieux à l'enterrement ».** Les quatre mesures
  étaient comparées **au même plancher nominal**, alors qu'elles ne vivent pas sur la même
  échelle. À diversité **réellement exposée** égale, les deux mesures retenues coûtent la même
  chose, à moins de 0,6 % de la borne exacte. Ce qui fait la norme est le **niveau** et la
  **conscience du rang**. Dix-huitième entrée de l'[audit](docs/limites.md).
- **Restreinte : « certifiée à 0,70, elle expose 0,36 ».** Le chiffre suppose une remise en
  $1/R$. À la sévérité **mesurée** d'un bandeau de trois vignettes ($\eta \approx 0{,}1$), le
  même fil expose **0,747** — l'enterrement disparaît ; à $\eta = 2$ il n'expose que **0,157** et
  l'échappatoire ne coûte plus que 2,7 %. Seul le prix de la norme consciente du rang est stable,
  20,8 à 24,1 %. Dix-neuvième entrée de l'audit.
- **Élargie : l'incertitude sur $\hat\eta$.** Sous le modèle de clic **affine** documenté par
  Vardasbi *et al.* (2020) — clics de confiance sur des contenus non pertinents en tête —
  l'estimateur dérive de **+12,8 %** sans que son erreur type de 0,013 ne le signale. Bien moins
  grave que poser $\eta$ au jugé (+179 %), mais l'intervalle publié est trop étroit.
- **Confirmée : l'exploration ne se remplace pas.** L'estimateur doublement robuste fait *moins
  bien* que l'IPS simple sur données réelles (−4,9 % contre +2,5 %), et la taille d'échantillon
  effective ne bouge pas : elle ne dépend que des poids d'importance.

### Modifié — ce que la littérature ajoute

- **Hager *et al.* (SIGIR 2024)** sur Baidu-ULTR, le jeu même où ce dépôt mesure
  $\hat\eta = 1{,}10$ : les corrections de biais de position améliorent la prédiction des clics
  **sans** améliorer la qualité du classement jugée par des experts. La présence du biais est
  corroborée ; l'étape suivante ne suit pas mécaniquement.
- **van Drunen & Vrijenhoek (2025)** établissent **avant ce dépôt** que les jeux publics sont le
  goulot d'étranglement et que le droit européen est la voie d'accès. Nous corroborons, nous ne
  découvrons pas.
- **Vrijenhoek *et al.* (2022)** : l'indice n'occupe qu'une des cinq dimensions de la diversité
  normative, et aucune mesure automatique ne distingue la pluralité de la fausse balance.
- [`docs/ide.md`](docs/ide.md), [`docs/memorandum.md`](docs/memorandum.md) et
  [`docs/rang-adverse.md`](docs/rang-adverse.md) portent les avertissements correspondants ; les
  deux notes LaTeX reçoivent la sous-section *ce que la contre-expertise a retiré ou restreint*
  et sont recompilées (22 et 21 pages).

### Ajouté — le filtre jugé contre des lignes de base et contre la frontière exacte

La dette la plus ancienne du programme d'évaluation : le filtre n'avait jamais été comparé qu'au
classement par pertinence, dont il se distingue par construction. Détail :
[`docs/lignes-de-base.md`](docs/lignes-de-base.md) et le
[notebook 19](notebooks/19_lignes_de_base.ipynb).

- **`ide.baselines`** — cinq réordonnanceurs à paramètre balayable (tour de rôle, MMR, Boltzmann,
  filtre entropique, tirage au sort), la mesure conjointe (diversité exposée, engagement) sous la
  **même** remise de rang, et la **frontière de Pareto exacte** par énumération des 151 200
  arrangements ordonnés. Au-delà d'une limite déclarée, le module refuse plutôt que de basculer
  en silence sur une frontière approchée.
- **`notebooks/19_lignes_de_base.ipynb`**, `paper/figures/fig19_lignes_de_base.png` et 16 tests
  supplémentaires (572 au total).

### Résultats — le filtre tient la frontière, et n'est pas premier

- **Le filtre du dépôt se tient sur la frontière exacte** : manque à gagner médian de **0,0 à
  1,0 %** d'engagement selon le plancher, sur 150 viviers tirés au sort. Ce n'était pas acquis —
  le tirage au sort atteint les mêmes diversités en laissant **9 à 19 %** sur la table.
- **Mais MMR, publié en 1998, tient la frontière aussi** — 0,0 à 0,2 % — et devance le filtre en
  duel direct au plancher 0,80 (35 victoires contre 18). **La nouveauté de ce dépôt n'est pas
  dans son algorithme.**
- **Le filtre ne se détache qu'à l'exigence haute** : au plancher 0,90, MMR ne trouve aucun
  réglage conforme dans **47 %** des viviers — son paramètre sature — contre **12 %** pour le
  filtre, qui l'emporte alors 72 fois contre 14. Il optimise la grandeur contrainte ; MMR
  optimise un substitut.
- **Le prix de la norme dépend du lecteur**, et personne ne l'avait isolé : un plancher de 0,90
  coûte **3,8 %** d'engagement quand la pertinence est indépendante du point de vue et **17,1 %**
  quand elle en découle entièrement. **La norme coûte le plus cher là où elle sert le plus.**
- Cette dépendance **réconcilie** deux chiffres du dépôt qui semblaient se contredire : les
  10 à 21 % du [rang adverse](docs/rang-adverse.md) correspondaient à un alignement de 1.

### Modifié

- [`docs/ade.md`](docs/ade.md) — encadré : le filtre n'apporte rien qu'une heuristique de 1998
  n'apporte déjà, sauf aux planchers élevés.
- [`docs/memorandum.md`](docs/memorandum.md) — deux objections anticipées et ce que la mesure en
  dit : refondre les moteurs n'est pas nécessaire, et le coût dépend du lecteur.
- [`docs/feuille-de-route.md`](docs/feuille-de-route.md) — la dette des lignes de base est
  réglée.

### Modifié — le dépôt et l'adresse du site renommés

- `Index-Dissipation-Entropique` devient **`Indice-Diversite-Exposee`**. Le site publié passe
  de `s-geffroy.github.io/Index-Dissipation-Entropique/` à
  **`s-geffroy.github.io/Indice-Diversite-Exposee/`**.
- **Ce qui suit le renommage** : GitHub redirige les opérations `git` — `clone`, `fetch`,
  `push` — de l'ancien nom vers le nouveau, ainsi que les URL du dépôt lui-même.
- **Ce qui casse** : les adresses des pages publiées ne sont **pas** redirigées. Tout lien vers
  `s-geffroy.github.io/Index-Dissipation-Entropique/…` renvoie désormais une erreur 404. C'était
  connu avant de renommer, et accepté : un nom qui annonce une analogie réfutée coûtait plus
  cher que des liens à refaire.
- Les 35 occurrences de l'ancien nom sont mises à jour dans le README, la documentation
  bilingue, `mkdocs.yml`, `CITATION.cff`, les deux notes LaTeX — recompilées — et les
  *user-agents* des trois clients d'API du dépôt.

### Modifié — la note de synthèse réécrite en partant de la mesure

La note LaTeX suivait l'ordre historique : l'analogie quantique, le formalisme, puis les
instruments en fin de parcours — et les six chantiers de mesure y avaient été ajoutés en
appendice. Elle est réécrite dans l'ordre inverse.

- **Partie I — La mesure** (nouvelle, huit sections) : le problème métrologique et ses trois
  pièges ; la définition de l'indice, avec le tableau des trois choix et l'attaque qui a imposé
  chacun ; l'épreuve adverse par énumération exhaustive ; l'estimation de l'exposition et le
  test d'échangeabilité, avec l'espérance et la variance exactes sous l'hypothèse nulle ;
  l'évaluation contrefactuelle et sa confrontation à une vérité terrain ; les trois journaux
  publics ; la demande au titre de l'article 40 ; le filtre, avec son état.
- **Partie II — Le modèle d'arrière-plan** : le formalisme thermodynamique et la calibration,
  précédés d'un avertissement — aucun résultat de la partie I n'en dépend — et suivis du
  **verdict sur l'analogie**, avec le tableau des cinq transferts et leur réfutation.
- **Partie III — Réserves** : limites réorganisées en quatre familles (indice et norme, mesures
  d'exposition, modèle, annotation), dont plusieurs entrées nouvelles : la forme retenue jamais
  mesurée sur un fil réel, la borne de l'énumération exhaustive, la politique cible unique de la
  confrontation, et la non-indépendance des codeurs.
- **Neuf références ajoutées** — Rao (1982), Ohsaka & Togashi (2023), Joachims *et al.* (2017),
  Agarwal *et al.* (2019), Swaminathan & Joachims (2015), Saito *et al.* (2020), Wu *et al.*
  (2020), Zou *et al.* (2022), et le règlement délégué (UE) 2025/2050.
- Les deux notes compilent sans référence ni citation indéfinie et sans boîte débordante :
  **20 pages** en français, **19** en anglais.

### Modifié — revue complète des pages à l'état des derniers résultats

Les pages avaient grossi par accrétion : chaque chantier ajoutait un paragraphe « Et… » à la
suite du précédent, si bien que la page d'accueil racontait la chronologie du projet plutôt que
son état. Revue de fond, page par page.

- **Sous-titre** — « De la décohérence quantique à la polarisation algorithmique » devient
  **« Mesurer la diversité qu'un fil algorithmique expose réellement — et éprouver ce qu'on
  croit en savoir »**, dans le README, la page d'accueil, `mkdocs.yml`, `CITATION.cff` et
  `pyproject.toml`. Le titre des deux notes LaTeX suit.
- **Page d'accueil et README réécrits** autour de quatre sections : le **verdict** en un
  tableau, **ce qui tient** (quatre instruments de mesure), **ce qui est tombé** (six résultats
  négatifs), **ce qui n'est pas tranché**. L'origine du projet passe en fin de page, où elle a
  désormais sa place.
- **[`docs/ide.md`](docs/ide.md)** — la définition présente maintenant la **forme retenue** en
  premier : entropie des contenus servis, projetés sur le catalogue déclaré, pondérés par
  l'attention de chaque rang — chacun de ces trois choix étant la conséquence d'une attaque qui
  a réussi. La forme d'origine, sur les étiquettes, est reléguée à une section qui dit ce
  qu'elle mesure et pourquoi elle ne peut pas servir de norme.
- **[`docs/ade.md`](docs/ade.md)** — encadré d'état : proposé, jamais évalué sur données
  réelles, et non évaluable en l'état. La limite « le coût en engagement n'est pas évalué » est
  corrigée : il l'est en simulation, entre 10,6 % et 20,9 %.
- **[`docs/theorie/entropie.md`](docs/theorie/entropie.md)** — le parallèle von Neumann /
  Shannon est explicitement présenté comme un **échafaudage qui n'a pas tenu**, et le renvoi vers
  l'index pointe la distribution effectivement retenue.
- **[`docs/limites.md`](docs/limites.md)** — nouvelle section : *l'analogie de départ est
  réfutée, et c'est un résultat*, avec le tableau des cinq transferts et leur verdict.
- **[`docs/memorandum.md`](docs/memorandum.md)** — la recommandation 1 s'ouvre sur **ce qui est
  recommandé aujourd'hui**, prix chiffré et grandeurs de contrôle comprises ; l'historique des
  trois corrections reste dessous, dans l'ordre où elles sont survenues.
- **[`docs/relecture.md`](docs/relecture.md)** — les retours demandés ont changé d'ordre : la
  forme de l'indice et les instruments de mesure passent devant la calibration. Le modèle de
  courriel est réécrit et annonce les six résultats négatifs.
- **[`docs/feuille-de-route.md`](docs/feuille-de-route.md)** — « si une seule chose devait être
  faite » n'est plus l'annotation humaine mais le **dépôt de la demande d'accès aux données par
  un organisme de recherche** : c'est le seul verrou que ce dépôt ne peut pas lever seul, et il
  commande les trois mesures qui manquent.
- **`paper/*.tex`** — nouvelle section *Ce que les mesures postérieures ont établi* : les six
  résultats qui invalident une partie du corps de la note, résumés avec leurs chiffres. Les deux
  PDF sont recompilés.

### Modifié — l'index porte enfin le nom de ce qu'il mesure

- **IDE** ne se lit plus « Index de Dissipation Entropique » mais **« Indice de Diversité
  Exposée »** ; **ADE**, « Algorithme de Diversité Exposée ». En anglais, *Exposed Diversity
  Index* (EDI) et *Exposed Diversity Algorithm* (EDA).
- **Le motif.** L'analogie avec la décohérence quantique, qui donnait son nom à l'index, a été
  démontée transfert par transfert par l'[audit critique](docs/limites.md) : entropie extensive
  confondue avec le bruit de la variable macroscopique, entropie globale invariante sous
  décohérence, $\tau_D \propto \tau_R/N$ heuristique, effet tunnel requalifié en métaphore,
  $1/k^N$ décrivant un état initial. Rien de spécifiquement quantique n'a survécu ; ce qui tient
  relève de la mécanique statistique classique. Garder ce nom, c'était garder une revendication
  réfutée dans l'intitulé de l'instrument.
- **Le nom retenu dit la mesure.** « Exposée » n'est pas décoratif : c'est la correction qu'ont
  imposée le [test adverse](docs/gaming.md) et le [rang adverse](docs/rang-adverse.md) — la
  norme porte sur l'attention **réellement servie**, contenus et rang compris, non sur les
  étiquettes annoncées.
- **`entropic_dissipation_index` devient `label_diversity_index`** : la fonction calcule la
  diversité des **étiquettes**, aveugle aux contenus et au rang, et son nom le dit maintenant.
  Son module porte l'avertissement correspondant.
- **Inchangés à cette étape** : le sigle IDE/ADE, le paquet Python `ide`, le dépôt GitHub et
  l'adresse du site — le dépôt et l'URL ont été renommés ensuite, voir l'entrée ci-dessus. Les
  citations du fil d'origine dans l'[audit](docs/limites.md) et les [errata](docs/errata.md)
  conservent le nom historique : ce sont des pièces, pas du texte courant.

### Ajouté — la demande d'accès aux données, écrite comme une spécification

Seule voie restante après le constat qu'aucun jeu public ne porte à la fois le rang servi et une
étiquette de point de vue. Détail : [`docs/article-40.md`](docs/article-40.md) et le
[notebook 18](notebooks/18_demande_article_40.ipynb).

- **`ide.aggregates`** — les **quatre tableaux agrégés** dont les mesures de ce dépôt ont
  réellement besoin : profils de fils, clics par rang, cellules (contenu, rang) avec propension,
  exposition par point de vue déclaré. Le module sait les construire depuis un journal, les
  consommer, et mesurer ce que leur seuil de confidentialité coûte aux estimations.
- **`docs/article-40.md`** — la demande elle-même, rédigée article par article du règlement
  délégué (UE) 2025/2050 : objet, données, nécessité et proportionnalité, risques, publication,
  calendrier et voies de recours.
- **`notebooks/18_demande_article_40.ipynb`**, `paper/figures/fig18_demande_article_40.png` et
  11 tests supplémentaires (556 au total).

### Résultats — les quatre tableaux suffisent, et c'est vérifié

- **Le test d'échangeabilité se recalcule à $3 \times 10^{-12}$ près** depuis les seuls tableaux
  1 et 2, sur MIND comme sur Baidu-ULTR — donc le contrôle qui décide si un journal est
  corrigible n'exige **aucune donnée individuelle**.
- **La sévérité $\eta$ se recalcule exactement** — écart nul — depuis le seul tableau 3.
- **Les deux mesures de diversité** — composée et exposée — se recalculent depuis le seul
  tableau 4, qui suffit donc à constater l'**enterrement** : à composition identique, un fil
  conforme au plancher aveugle n'expose que 0,160 d'attention aux points de vue minoritaires,
  contre 0,337 pour le même fil entrelacé et 0,375 en composition.
- **Ce qui est demandé pèse 95 fois moins de lignes** que le journal brut sur Baidu-ULTR (5 543
  contre 524 164) et 101 fois moins sur MIND (57 906 contre 5 843 444).
- **Le seuil de confidentialité n'est pas neutre** : passer de 5 à 20 impressions par cellule
  déplace la sévérité estimée de 1,10 à 1,40, soit +27 %, parce que les cellules rares sont
  celles des rangs profonds. Il doit être publié avec le résultat.
- **Deux clés d'agrégation plus simples ont été écartées parce qu'elles étaient fausses** :
  indexer les fils par leur longueur plutôt que par leur profil de rangs, et omettre le nombre de
  clics du fil — qui empêche d'écarter les fils entièrement cliqués et décale l'écart réduit de
  $-205{,}7$ à $-203{,}9$. Les deux erreurs produisaient des chiffres du bon ordre de grandeur.

### Modifié

- [`docs/feuille-de-route.md`](docs/feuille-de-route.md) §3.1 — la troisième voie est désormais
  outillée, avec sa réserve : l'art. 40(8)(a) exige une affiliation à un organisme de recherche,
  que ce dépôt n'a pas. Le document est un modèle prêt à déposer.
- [`docs/memorandum.md`](docs/memorandum.md) — nouvelle disposition : **normaliser la forme de
  la demande d'accès**, et y fixer le seuil de suppression des faibles effectifs.

### Ajouté — deux journaux publics qui enregistrent le rang servi

Suite directe de l'exigence sur laquelle s'était terminée la mesure sur MIND. Détail :
[`docs/rang-servi.md`](docs/rang-servi.md) et le
[notebook 17](notebooks/17_rang_servi.ipynb).

- **`ide.logs`** — la représentation commune d'un journal d'impressions et les mesures qui s'y
  appliquent, extraites de `ide.mind` : trois jeux de données les partagent désormais. Le
  condensé versionnable y vit aussi, et **vérifie** la structure des fils au lieu de la supposer.
- **`ide.exposure`** — lecture de **Baidu-ULTR** (rang d'affichage, session, clic) et de
  l'**Open Bandit Dataset** (position, propension vraie, seau à politique aléatoire), et
  confrontation d'une estimation contrefactuelle à une vérité terrain mesurée.
- **`scripts/fetch_exposure.py`**, **`scripts/build_exposure_digest.py`** et
  **`data/exposure_digest.npz`** — 0,7 Mo versionnés pour 3,1 Go de journaux bruts, sous deux
  licences distinctes, avec vérification de taille et d'empreinte à la récupération.
- **`notebooks/17_rang_servi.ipynb`**, `paper/figures/fig17_rang_servi.png` et 14 tests
  supplémentaires (545 au total). `pyarrow` rejoint les dépendances de laboratoire.

### Résultats — la sévérité se mesure, et elle dépend de la surface

- **Le contrôle positif passe.** Sur Baidu-ULTR, le test d'échangeabilité rejette à
  $z = -205{,}7$ ($p < 10^{-12}$) et **du bon côté** : les clics se concentrent en haut. Un test
  qui ne rejetterait jamais rien ne dirait rien de MIND.
- **$\hat\eta = 1{,}10 \pm 0{,}09$** par effets fixes de document, contre 1,49 par ajustement
  agrégé : l'écart est le confondant de qualité, la plateforme plaçant les meilleurs documents
  en tête. La couverture reste mince — 55 documents portent l'estimation, sur 444 709.
- **Dix fois plus faible sur une autre surface.** Sur l'Open Bandit Dataset, à allocation
  **aléatoire** donc à effet causal, un bandeau de trois vignettes horizontales décroît en
  $R^{-0{,}04}$ (campagne « all ») à $R^{-0{,}11}$ (campagne « men »). $\eta$ est une propriété
  de la surface, pas une constante, et le transporter coûte l'ordre de grandeur que le rang
  adverse avait chiffré.
- **Première confrontation à une vérité terrain.** La valeur d'une politique jamais déployée,
  estimée sur les seules données d'une autre politique : IPS à **+2,5 %** de la valeur mesurée
  directement, contre **+31,6 %** pour l'estimation naïve, **−7,0 %** pour SNIPS et **−12,7 %**
  pour un plafond à 10.
- **Et le diagnostic qui l'accompagne** : taille d'échantillon **effective** de **1 513** pour
  4 077 727 impressions, soit 0,04 %. L'estimation est sans biais et repose sur l'équivalent de
  mille cinq cents observations.
- **Troisième résultat négatif de la série** : aucun jeu public ne porte à la fois le rang servi
  et une étiquette de point de vue interprétable. L'évaluation de l'ADE annoncée par la feuille
  de route ne peut pas être faite sur données publiques en l'état.

### Corrigé — un condensé qui supposait au lieu de vérifier

- Le condensé résumait la structure d'un fil à sa **longueur**, en supposant qu'un fil de
  longueur $L$ occupe les rangs 1 à $L$. Vrai de MIND, **faux** d'une page de résultats qui saute
  des rangs. Le défaut était indolore — $z = -200$ au lieu de $-206$ — ce qui est la façon dont
  ce genre d'erreur survit. Dix-septième entrée de l'[audit critique](docs/limites.md).

### Modifié

- [`docs/feuille-de-route.md`](docs/feuille-de-route.md) §3.1 — le critère de choix d'un jeu de
  données est réglé, la piste ne l'est pas : trois mesures restent faisables, la quatrième passe
  par une demande au titre de l'article 40 du DSA.
- [`docs/memorandum.md`](docs/memorandum.md) — l'exigence de publication du rang servi a
  désormais un **précédent industriel** ; nouvelle disposition exigeant une **fraction
  d'exploration aléatoire**, sans laquelle la taille d'échantillon effective d'un audit tombe à
  0,04 % ; cette taille devient une grandeur de contrôle à publier.
- [`docs/mind.md`](docs/mind.md) — piste ouverte 1 réglée.

### Ajouté — l'exploration réellement enregistrée dans MIND

Le préalable inscrit à la feuille de route §3.1 : mesurer l'exploration d'un jeu de données
public **avant** d'y évaluer quoi que ce soit. Détail : [`docs/mind.md`](docs/mind.md) et le
[notebook 16](notebooks/16_exploration_mind.ipynb).

- **`ide.mind`** — lecture des journaux d'impressions de MIND, **test d'échangeabilité
  intra-fil** (exact, avec étalonnage de puissance par simulation à structure de fils
  identique), taux de clic par rang à longueur de fil contrôlée, et couverture de rang.
- **`scripts/fetch_mind.py`** — récupération des journaux, avec vérification du nombre de fils
  et de l'empreinte SHA-256 : la source officielle répond désormais *409 Public access is not
  permitted*, le jeu vient d'un miroir, et un miroir se vérifie.
- **`scripts/build_mind_digest.py`** et **`data/mind_digest.npz`** — condensé de 1,5 Mo, seul
  dérivé de MIND que ce dépôt puisse porter (licence de recherche Microsoft, 135 Mo bruts). Un
  test vérifie qu'il rend **exactement** les chiffres du journal brut.
- **`notebooks/16_exploration_mind.ipynb`**, `paper/figures/fig16_exploration_mind.png` et 19
  tests supplémentaires (531 au total).

### Résultats — l'ordre enregistré dans MIND n'en est pas un

- **Indiscernable d'un mélange** : $z = +0{,}12$ ($p = 0{,}91$) sur 156 965 fils, répliqué à
  $z = +0{,}28$ ($p = 0{,}78$) sur le second découpage. Le test détecterait $\eta = 0{,}02$ à
  douze écarts-types ; la sévérité minimale détectable vaut $\eta \approx 0{,}004$.
- **La courbe de biais de position qu'on y trace est un artefact de composition.** Le taux de
  clic décroît de 0,108 à 0,038 sur vingt rangs, soit $\hat\eta = 0{,}39$ — mais à longueur de
  fil fixée la pente est nulle et **change de signe** d'une longueur à l'autre. Les positions
  élevées n'existent que dans les fils longs, où le taux de clic par contenu est plus faible.
- **Cinq sévérités incompatibles tirées du même jeu**, de $-0{,}13$ à $+0{,}25$ selon un simple
  seuil d'impressions, toutes d'erreur type inférieure à 0,007.
- **Le mélange ne débiaise pas les clics, il détruit la variable qui les corrigerait.** Sur un
  journal simulé de sévérité vraie 1,00 : $\hat\eta = 1{,}003$ avec l'ordre conservé,
  $-0{,}003$ après mélange — à clics identiques. L'évaluation qui s'ensuit estime le coût d'un
  réordonnancement à **0,00 %** contre 6,61 % de valeur vraie : sous $\eta = 0$, deux politiques
  qui ne diffèrent que par l'ordre reçoivent la même valeur, donc l'évaluation est vide par
  construction.

### Corrigé — le contrôle d'identifiabilité était nécessaire et non suffisant

- Le drapeau d'identifiabilité de `estimate_position_bias`, présenté au chantier précédent comme
  la garde à passer avant d'estimer $\eta$, **compte la variation de rang sans dire d'où elle
  vient**. Une variation artificielle le satisfait mieux que n'importe quelle exploration réelle.
  Le test d'échangeabilité est le contrôle manquant, et il doit précéder l'estimation.
  Seizième entrée de l'[audit critique](docs/limites.md).

### Modifié

- [`docs/feuille-de-route.md`](docs/feuille-de-route.md) §3.1 — la quatrième condition n'est pas
  remplie par MIND : l'estimation contrefactuelle du coût d'engagement y est impossible, les
  autres étapes restent faisables à condition de dire que le coût publié est un coût en
  pertinence **déclarée**, et le choix du jeu de données devient le premier travail.
- [`docs/memorandum.md`](docs/memorandum.md) — nouvelle section **« ce qu'un journal doit
  contenir pour être auditable »** : publication du rang servi ou de la propension d'exposition,
  et test d'échangeabilité en contrôle d'acceptation des journaux transmis au titre de
  l'article 40 du DSA.
- [`docs/rang-adverse.md`](docs/rang-adverse.md) — avertissement sur le contrôle
  d'identifiabilité, et piste ouverte 3 réglée.

### Ajouté — le test adverse sur fils ordonnés, et la sévérité du biais estimée

Règle les deux dettes explicites laissées par le chantier précédent. Détail :
[`docs/rang-adverse.md`](docs/rang-adverse.md) et le
[notebook 15](notebooks/15_rang_adverse_et_severite.ipynb).

- **`ide.ranking`** — le test adverse repris sur des fils **ordonnés** et non sur des
  compositions. L'optimisation est **exhaustive** : les 65 536 fils possibles sont énumérés,
  l'optimum est donc exact et non le résultat d'une heuristique. Au-delà d'une limite déclarée,
  le module refuse plutôt que de basculer en silence sur une approximation.
- **`ide.offpolicy.estimate_position_bias`** — estimation de $\eta$ par régression à effets
  fixes de contenu sur $\log \mathrm{CTR} = \log g(i) - \eta \log R$, avec erreur type et
  **drapeau d'identifiabilité**.
- **`notebooks/15_rang_adverse_et_severite.ipynb`** et 24 tests supplémentaires.

### Résultats — les quatre mesures se laissent contourner par l'ordre

- **Une plateforme certifiée à 0,70 n'expose que 0,36.** Sous plancher aveugle au rang,
  l'entropie de Rao certifie 0,750 pour une diversité exposée de **0,355** ; l'entropie de
  position, 0,774 pour **0,443**. Le fil optimal a toujours la même forme — six contenus du
  point de vue préféré, puis les divergents relégués aux dernières positions.
- **Un plancher conscient du rang ferme l'échappatoire, et double le coût** : de 8,2 % à
  18,9 % pour l'entropie de Rao, de 10,7 % à 20,9 % pour l'entropie de position.
- **L'écart croît avec l'exigence** : 0,262 à plancher 0,40, 0,395 à plancher 0,70 pour Rao.
  Plus la norme aveugle demande de diversité, plus il devient rentable de l'enterrer.
- **La proximité à la cible résiste le mieux** — écart nul à plancher 0,40, 0,122 à 0,70 —
  troisième point sur lequel elle se détache des trois autres mesures.
- **Cet écart-là est seuillable**, contrairement à l'excès de signature : il compare **la même
  mesure à elle-même**, une fois à l'aveugle du rang et une fois en le prenant en compte.

### Résultats — la sévérité du biais de position s'estime, et il fallait l'estimer

- **$\hat\eta = 1{,}013 \pm 0{,}019$** sur 40 000 impressions ; la sévérité vraie est
  retrouvée de 0,4 à 1,6.
- **À politique déterministe, $\eta$ n'est pas identifiable.** Aucun contenu ne change de
  rang, il n'y a donc aucune variation à exploiter, et l'estimateur **refuse de renvoyer un
  chiffre**. À exploration faible il en renvoie un, mais l'erreur type dit qu'il ne vaut rien.
- **Poser $\eta$ de travers coûte jusqu'à 179 % d'erreur** — soit l'ordre de grandeur du biais
  de 201 % que la correction contrefactuelle prétendait éliminer. Avec $\eta$ estimé, le coût
  tient entre 6,6 % et 6,9 % contre 6,6 % de valeur vraie.
- **Conséquences** : la recommandation 1 du mémorandum reçoit le **prix** de la mesure
  consciente du rang et une **grandeur de contrôle** associée ; la feuille de route §3.1 ajoute
  une quatrième exigence — estimer $\eta$, et vérifier d'abord l'exploration du jeu de données.
- **Réserve maintenue :** la forme $e(R) = R^{-\eta}$ reste posée, seule sa sévérité est
  estimée. Et l'énumération exhaustive borne les fils étudiés à huit positions sur quatre
  points de vue — rien n'assure que le comportement se transporte à plus grande échelle.

### Ajouté — rang et contrefactuel, deux corrections avant l'évaluation sur données réelles

Détail : [`docs/evaluation.md`](docs/evaluation.md) et le
[notebook 14](notebooks/14_rang_et_contrefactuel.ipynb).

- **`ide.radio`** — divergences conscientes du rang, d'après RADio (Vrijenhoek *et al.*,
  RecSys 2022) : remise de rang réciproque ou logarithmique, divergence de Jensen-Shannon en
  base 2 donc **exactement** bornée par 1, et les cinq références du cadre — calibration,
  fragmentation, activation, représentation, voix alternatives.
- **`ide.offpolicy`** — estimateurs contrefactuels : IPS, SNIPS, IPS plafonné, doublement
  robuste, taille d'échantillon effective, et l'estimateur de *replay* implémenté **pour être
  comparé, non pour être employé**. Un défaut de recouvrement y lève une erreur au lieu de
  produire un chiffre.
- **`notebooks/14_rang_et_contrefactuel.ipynb`** et 68 tests supplémentaires.

### Résultats — un quatrième adversaire, et une évaluation qui ne mesurait rien

- **L'enterrement fonctionne.** À composition **rigoureusement identique**, déplacer les
  contenus divergents vers le bas du fil rapporte **10 % d'engagement** et fait passer la
  divergence de 0,525 à 0,630. L'entropie de position — le plancher retenu la veille — vaut
  0,774 dans les deux cas : elle ne voit que la composition, jamais l'ordre.
- **La remise de rang ferme l'échappatoire.** À composition fixe, faire glisser le bloc
  divergent du haut vers le bas laisse la mesure sans remise **parfaitement plate**, tandis que
  les mesures escomptées montent de 0,29 à 0,68.
- **L'évaluation naïve d'un réordonnancement est fausse de 201 % en médiane**, jusqu'à 851 %
  sur soixante jeux de contenus. Elle surestime le coût dans 56 cas sur 60 — ce qui inviterait
  à la tenir pour prudente — mais le sous-estime dans les 4 autres, à configuration pourtant
  identique. **Un chiffre naïf n'est donc même pas une borne supérieure.**
- **IPS et SNIPS retrouvent la valeur vraie à moins d'un point** (6,6 % contre 6,6 %, là où le
  replay annonce 5,0 %).
- **Trois grandeurs doivent accompagner tout résultat contrefactuel** : le modèle de propension
  employé, la taille d'échantillon effective — qui tombe de 60 000 à 10 026 quand le
  réordonnancement devient agressif — et le plafond, dont le seul choix déplace l'estimation de
  −6,5 % à −0,0 %.
- **Conséquences** : la recommandation 1 du mémorandum exige désormais une mesure **consciente
  du rang** ; la feuille de route §3.1 conditionne l'évaluation de l'ADE à trois exigences sans
  lesquelles « la frontière de Pareto annoncée mesurerait surtout le biais de position de la
  plateforme qui a produit les données ».
- **Réserve maintenue :** le modèle de biais de position est une hypothèse, non une mesure. Le
  problème se déplace d'un cran, de « les clics sont des étiquettes » vers « l'exposition se
  modélise par le rang ». Le second énoncé est bien meilleur, et il reste un énoncé.

### Corrigé — le remplaçant proposé pour l'IDE prescrivait la polarisation

Correction du correctif publié la veille. Détail : [`docs/gaming.md`](docs/gaming.md), section
« Le correctif », et le [notebook 13](notebooks/13_test_adverse_index.ipynb).

- **Le défaut.** L'entropie quadratique de Rao est la *distance intra-liste*, dont Ohsaka et
  Togashi (SIGIR 2023) ont montré qu'elle admet des optima dégénérés. Sur un axe d'opinion le
  dégénéré est le **fil bimodal** : elle attribue **1,000** à un fil servant les deux bords et
  rien entre eux, contre **0,750** à un fil étalé.
- **Ce n'est pas une faille exploitable, c'est la réponse optimale.** Sous plancher de Rao à
  0,80, la plateforme sert **4 points de vue sur 8** et laisse un vide de **0,71** — les sept
  dixièmes de l'axe. Le plancher réglementaire produit lui-même l'exposition bimodale que le
  projet cherche à mesurer.
- **La faute est de méthode** : le remplaçant avait été éprouvé contre l'attaque qu'il devait
  fermer, et contre aucune autre. L'erreur a été trouvée en lisant la littérature du domaine
  sur la mesure employée, non en relisant le code.

### Ajouté — trois mesures candidates, éprouvées contre trois adversaires

- **`position_entropy`** — l'IDE calculé sur les **contenus** servis, projetés sur les bacs du
  catalogue de référence, et non sur les étiquettes déclarées. Garde l'interprétation de
  l'index d'origine, résiste aux trois adversaires, et coûte **moins cher** que Rao (18,1 %
  contre 32,8 % à plancher 0,80).
- **`gaussian_ild`** — la proposition d'Ohsaka et Togashi. Métrique là où l'entropie est
  nominale, mais elle plafonne à 0,715 sur l'uniforme : sa borne dépend de $k$ et de la largeur
  de bande, donc un seuil chiffré n'y serait pas lisible. Bon diagnostic, mauvaise norme.
- **`target_divergence`** — proximité à une distribution d'exposition **déclarée** par le
  régulateur. Seule à rendre explicite la forme visée, là où les autres la supposent : l'entropie
  suppose l'uniforme, l'entropie de Rao suppose l'écartement.
- **`centre_share` et `largest_gap`** — diagnostics de forme. Ce sont eux qui ont rendu le
  défaut visible, alors qu'aucune grandeur contrainte ne s'en émouvait.
- **`optimal_feed_under`** — optimiseur générique : toutes les mesures passent désormais par le
  même solveur, une comparaison entre normes ne valant que si l'optimisation est identique de
  part et d'autre.
- **`Feed`** porte le catalogue de référence complet et non son seul écart maximal, ce qui lui
  donne aussi la grille de bacs.
- 25 tests supplémentaires, dont le défaut de Rao énoncé comme test — il est reproductible,
  donc il est réel.

### Résultats — ce que le correctif retient

| Rôle | Mesure |
|---|---|
| plancher | entropie de position |
| publié à côté | plus grand vide, l'entropie étant nominale |
| successeur à instruire | proximité à une cible déclarée |

- **Recommandation 1 du mémorandum révisée une seconde fois.** Le plancher ne porte ni sur
  l'IDE des étiquettes, ni sur l'entropie de Rao des contenus, mais sur l'**entropie de
  position**, publiée avec le plus grand vide.
- **Pages corrigées en place** : `gaming`, `memorandum`, `feuille-de-route` (§2.1 et §2.2),
  `index` et README, qui présentaient tous l'entropie de Rao comme le remplacement retenu.

### Ajouté — test adverse de l'index, et réplication de l'annotation

Deux vérifications indépendantes, l'une sur le livrable réglementaire, l'autre sur la méthode
d'annotation. Détail : [`docs/gaming.md`](docs/gaming.md) et
[`docs/annotation.md`](docs/annotation.md).

- **`ide.gaming`** — test de saturabilité de l'index sous contrainte. Une plateforme maximise
  l'engagement sous plancher d'IDE ou d'entropie de Rao, avec une latitude paramétrée de
  découplage entre étiquette et contenu. La solution sous contrainte d'entropie est **exacte**
  (distribution de Boltzmann : le plancher agit comme une température), ce qui importe pour un
  résultat négatif.
- **`ide.annotation`** — $\kappa$ de Cohen, $\kappa$ de Fleiss, registre consensuel, et
  chargement des recodages indépendants.
- **`data/annotations_replication.json`** — deux recodages complets du corpus, sous la grille
  identique, à partir du même matériau présenté dans un ordre différent et sans l'étiquette de
  catégorie.
- **`notebooks/13_test_adverse_index.ipynb`**, section 8 à 10 du notebook 12, et 48 tests
  supplémentaires.

### Résultats — l'index n'est pas une norme tenable en l'état

- **Un plancher d'IDE se sature à coût nul.** Une plateforme capable de dissocier l'étiquette
  du contenu obtient un **IDE de 1,000 — la note maximale — pour une diversité de contenu
  strictement nulle**, sans céder un point d'engagement. Sur un catalogue honnête, le même
  plancher à 0,80 coûte 18 % d'engagement : la contrainte mord, et c'est bien la manipulation
  qui l'annule.
- **La dégradation devance largement le découplage.** À mi-découplage, la contrainte n'a plus
  que **36 %** de sa force ; à 80 %, il en reste 7 %.
- **L'entropie quadratique de Rao résiste, et inverse l'incitation.** Au-delà d'un découplage
  de moitié le plancher devient **inatteignable** ; en deçà, il coûte *plus* cher à mesure que
  la plateforme vide ses étiquettes — 16 % à découplage nul, 40 % à mi-découplage.
- **Une signature de manipulation**, définie comme excès sur la contrefactuelle honnête et non
  comme écart brut : nulle par construction pour une plateforme honnête, croissante avec le
  découplage. L'écart brut, lui, vaut déjà 0,36 sur un fil honnête et ne se prête donc à aucun
  seuil.
- **Recommandation 1 du mémorandum révisée** : le plancher ne porte plus sur l'IDE des
  étiquettes mais sur l'entropie de Rao des contenus, le régulateur fixant l'étendue du
  catalogue de référence.
- **Défaut corrigé en cours de route.** Une première version normalisait l'entropie de Rao par
  l'étalement effectivement servi. La mesure devenait invariante d'échelle et un fil réduit à
  un point y marquait $Q \approx 1$ sur du bruit d'arrondi — la conclusion publiée aurait été
  l'inverse de la vérité. Un test verrouille désormais le point.

### Résultats — la grille d'annotation est reproductible

- **$\kappa$ de Fleiss = 0,921** sur trois codages du même corpus ; accords deux à deux de
  0,903, 0,917 et 0,944 ; unanimité sur **92,3 %** des sujets.
- **Le désaccord tombe au bon endroit.** Sur 34 sujets non unanimes, **33** portent sur
  l'appartenance à un registre et **1** seul inverse `accusation` et `discovery` :
  l'imprécision résiduelle fait varier les effectifs de la comparaison, pas son sens.
- **Le résultat est inchangé sous le codage consensuel** : taux de basculement 4,3 % contre
  5,4 % ($p = 0{,}77$), persistance ×3,06 contre ×2,90 ($p = 0{,}84$).
- **Réserve maintenue :** les trois codeurs sont des instances du même modèle de langue.
  L'accord mesure la reproductibilité de la **grille**, non l'accord entre juges humains
  indépendants, et il le surestime nécessairement. La feuille de route en fait sa priorité n° 1.

### Résultats — l'annotation en aveugle tranche : l'écart n'existe pas

Détail : [`docs/annotation.md`](docs/annotation.md) et le
[notebook 12](notebooks/12_annotation_en_aveugle.ipynb).

- **Le bruit d'étiquetage est massif et mesuré.** 175 sujets sur 440 — **40 %** — ne relèvent
  d'aucun des deux registres, et l'accord entre catégorie et annotation n'atteint que
  **59,5 %**. Le bruit est asymétrique (31,8 % côté accusation, 47,7 % côté découverte) mais
  le registre franchement inversé est quasi nul : 3 sujets. C'est le profil d'un bruit qui
  dilue sans biaiser, tel que le corpus étendu l'avait supposé.
- **L'écart de taux de basculement disparaît.** 8,6 % contre 2,7 % (rapport de cotes 3,37,
  $p = 0{,}012$) devient **4,8 % contre 5,1 %** (rapport de cotes **0,93**, $p = 1{,}00$). Les
  sujets écartés basculent à 6,9 %, soit **plus souvent que les deux registres** : ce sont eux
  qui portaient l'écart. Quatre des cinq plus fortes élévations du corpus sont codées « ni
  l'un ni l'autre ».
- **Le déséquilibre d'audience était lui-même un effet de l'étiquetage.** Le trafic médian
  passe de 39 contre 11 vues/jour à 36 contre 26,5.
- **La persistance reste nulle, avec la puissance de conclure.** ×3,04 contre ×2,90
  ($p = 0{,}90$), robuste au retrait des sujets contaminés, des annotations incertaines et des
  sujets à faible trafic. À $n = 7$ contre 7, un écart aussi séparé que celui qu'annonçait le
  corpus pilote aurait été détecté ($p = 0{,}04$ avec quatre rangs de chevauchement).
- **Un défaut de plan d'expérience est révélé.** Correctement étiquetés, les deux registres ne
  portent presque pas sur les mêmes types de sujets — 58 événements et 63 concepts côté
  accusation, 58 objets et 39 personnes côté découverte. Les concepts ne basculent jamais
  (0/63 et 0/15). Une comparaison bâtie sur des catégories thématiques compare donc aussi des
  natures d'objets.
- **Bilan :** quatre mesures, aucun effet du registre émotionnel. La dernière hypothèse de
  sauvetage — la dilution par l'étiquetage — est éliminée. Le mécanisme de la charge
  émotionnelle $\alpha$ reste sans appui empirique.
- **Pages corrigées en place** : `corpus-etendu`, `regimes`, `memorandum` (dont la ligne
  « persistance » du tableau des points non mesurés, restée en ×9,2 contre ×2,9), `index`,
  README et feuille de route, dont la priorité n° 1 devient le double codage.

### Ajouté — pré-enregistrement de l'annotation en aveugle

Fixe la grille d'annotation manuelle du registre **avant** toute annotation, pour trancher
entre absence d'effet et effet dilué par le bruit d'étiquetage. Protocole :
[`docs/annotation.md`](docs/annotation.md).

- **`ide.annotation`** — grille à trois registres (`accusation`, `discovery`, `neither`),
  cinq règles de départage arrêtées d'avance, type de sujet et confiance en dimensions
  accessoires ; chargement d'annotations refusé si la version de grille diffère.
- **`scripts/fetch_extracts.py`** — fige le chapeau des 440 articles dans
  `data/extracts.json`, seule entrée de l'annotateur, dont l'empreinte SHA-256 est inscrite
  dans le fichier d'annotations.
- **Contamination déclarée** — les six sujets cités avec leur élévation dans la page du
  corpus étendu sont listés dans `ide.annotation.CONTAMINATED`, annotés comme les autres, et
  l'analyse est reprise sans eux.
- **`data/extracts.json` et `data/annotations.json`** — les chapeaux figés des 440 articles et
  leur codage manuel, avec l'empreinte SHA-256 des premiers inscrite dans le second.
- **`notebooks/12_annotation_en_aveugle.ipynb`** et 22 tests supplémentaires.

### Ajouté — corpus étendu et réplication

Met à l'épreuve, sur 440 sujets, le seul écart entre registres émotionnels que le projet
avait mesuré. Détail : [`docs/corpus-etendu.md`](docs/corpus-etendu.md).

- **`ide.catalogue`** — construction d'un corpus depuis dix-sept catégories de Wikipédia
  déclarées à l'avance, avec classes disjointes, filtre de substance et échantillonnage
  déterministe par empreinte de titre. Remplace le choix des *sujets* par celui des
  *catégories* : à trois cents titres, une sélection manuelle ne se relit plus.
- **`scripts/build_catalogue.py`** et le manifeste versionné `data/catalogue.json`.
- **Cache compressé** — `ide.pageviews` écrit désormais des fichiers `.json.gz`, ce qui
  ramène 440 séries quotidiennes sur onze ans de dix mégaoctets à trois.
- **`notebooks/11_corpus_etendu.ipynb`** et 40 tests supplémentaires.

### Résultats — le résultat du corpus pilote est infirmé

- **L'écart de persistance ne se réplique pas.** ×9,2 contre ×2,9 ($p = 0{,}08$) sur
  quatorze sujets choisis à la main devient **×3,04 contre ×2,90** ($p = 0{,}53$) sur 440
  sujets dérivés de catégories. Le corpus pilote contenait les théories du complot les plus
  connues — c'est précisément ce qu'une sélection manuelle produit.
- **L'écart de taux de basculement est un effet d'audience.** Les sujets d'accusation
  basculent trois fois plus souvent (8,6 % contre 2,7 %, $p = 0{,}014$), mais ils sont aussi
  trois fois et demie plus consultés ($p = 5\times10^{-14}$). À trafic comparable, le rapport
  de cotes tombe de 3,4 à 1,38 ($p = 0{,}63$) ; sur 173 paires appariées, McNemar donne
  $p = 0{,}18$.
- **Le nouveau protocole a son propre défaut.** L'appartenance à une catégorie est un
  indicateur bruité du registre — « Lil Tay » est dans une catégorie de canulars, mais son
  audience est celle d'une célébrité. Un bruit d'étiquetage attire tout écart vers zéro : le
  résultat nul est compatible avec l'absence d'effet **comme** avec un effet dilué.
- **Bilan :** aucune différence entre registres émotionnels ne résiste à sa vérification, ni
  par le taux d'amplification, ni par la persistance. Le mécanisme de la charge émotionnelle
  reste sans appui empirique.

### Modifié

- **Contrôle d'observabilité ajouté à `ide.regime`.** Le temps d'oubli doit tenir dans la
  fenêtre ajustée. Sans lui, deux transitions presque en marche d'escalier du corpus étendu
  produisaient des rapports de 697 et 5431 — soit des mémoires collectives de plusieurs
  années — avec une dispersion résiduelle excellente.
- **Affirmations corrigées** dans `docs/regimes.md`, le mémorandum et les pages d'accueil :
  l'écart de persistance y était présenté comme le premier écart mesuré du projet. Les
  sections concernées sont conservées, avec l'avertissement qui les infirme.

### Ajouté — détection de changement de régime

Traite l'angle mort de la calibration par pic : les désinformations qui ne flambent pas mais
s'installent. Détail et réserves : [`docs/regimes.md`](docs/regimes.md).

- **`ide.regime`** — segmentation binaire sur les logarithmes pour détecter les ruptures de
  niveau, localisation séparée du décollage de la transition, déduplication des escaliers de
  ruptures, correction de la périodicité hebdomadaire, et identification de
  $\gamma\alpha$, $\lambda$, $W_{\text{sat}}$ par ajustement de trajectoire.
- **`notebooks/10_changement_de_regime.ipynb`** et 58 tests supplémentaires (324 au total).

### Résultats — deux réussites à ne pas confondre

- **La détection fonctionne, et couvre l'angle mort.** 14 changements de régime sur le
  corpus, aux bonnes dates sans qu'aucune date ne lui soit fournie : affaire Benalla le
  20 juillet 2018, révélations Pegasus en juillet 2021, annonce de LIGO en février 2016,
  bascule QAnon en mars 2020. Et surtout dans les sujets que la méthode par pic manquait —
  QAnon, désinformation Covid-19, hésitation vaccinale.
- **L'identification échoue sur données réelles.** Zéro des 14 livre des paramètres
  exploitables : la dispersion résiduelle médiane est de 0,63, alors que l'incertitude
  relative sur le rapport atteint déjà 77 % à 0,15. La récupération est pourtant exacte sur
  trajectoire de synthèse, y compris pour $\rho = 40$ — c'est une inadéquation entre un
  modèle à trois paramètres et le bruit réel, non un défaut d'implémentation.
- **Une limite théorique domine les deux.** Sous saturation logistique, l'équation se réduit
  à une logistique à deux paramètres de forme : $\gamma\alpha/\lambda$ y est **structurellement
  non identifiable**, et deux triplets de rapports 5,0 et 1,7 produisent la même courbe.
  L'identifiabilité du rapport n'est donc pas une propriété des données mais une hypothèse
  sur la forme de la saturation.
- **Premier écart mesuré entre registres émotionnels.** L'élévation durable du palier vaut
  ×9,2 pour les contenus d'accusation contre ×2,9 pour les annonces de découverte
  ($p = 0{,}08$, n = 14). Ce n'est pas le taux d'amplification qui sépare les registres,
  c'est la durée pendant laquelle l'attention reste captée.

### Modifié

- **Recommandation 2 du mémorandum, à nouveau amendée.** Le plafond sur
  $\gamma\alpha/\lambda$ supposait le rapport mesurable ; il ne l'est ni sur les régimes
  installés, ni indépendamment d'une hypothèse de forme. Un indicateur de remplacement est
  proposé — date du basculement et élévation du palier — qui se mesure, distingue les
  registres, et porte sur ce qu'un régulateur cherche réellement à constater.
- **Table de correction de biais supprimée.** Une première version du module publiait une
  sous-estimation de 20 % à 10 % de bruit. Cette table était fausse : elle venait d'un
  prototype dont l'initialisation, un lissage aux bords corrompus, dégradait l'ajustement
  bien plus que le bruit. Corriger l'initialisation a supprimé le biais qu'il fallait
  soi-disant corriger. Elle est remplacée par une table de **précision**, mesurée sur la
  chaîne complète et non sur un ajustement isolé.

### Ajouté — calibration empirique de γα/λ

Première mesure d'un paramètre du modèle sur des données réelles. Détail et réserves :
[`docs/calibration.md`](docs/calibration.md).

- **`ide.calibration`** — identification de $\gamma\alpha$ et $\lambda$ par réduction de
  l'équation de résonance au premier ordre, avec deux estimateurs : fenêtres adaptatives, et
  fenêtres à horizon fixe. Détection d'épisodes par proéminence sur niveau de fond glissant,
  avec compte rendu des rejets par motif.
- **`ide.pageviews`** — accès à l'API de consultations de Wikimedia et cache sur disque.
  Filtre d'agent `user` par défaut, pour exclure les robots.
- **`ide.corpus`** — corpus pré-enregistré de 24 sujets, réparti en deux registres
  émotionnels. Figé dans le code afin qu'aucun sujet ne puisse être écarté au vu de son
  résultat.
- **`scripts/fetch_pageviews.py`** — seul point d'accès réseau du dépôt, exécuté une fois.
- **`data/pageviews/`** — les 24 séries, versionnées : l'analyse est reproductible hors
  ligne et un test vérifie que le corpus reste intégralement disponible.
- **`notebooks/09_calibration_visibilite.ipynb`** et 63 tests supplémentaires (266 au total).

### Résultats

- $\gamma\alpha/\lambda$ vaut **1,5 à 12** sur 19 épisodes, de médiane **2,5 à 4,2** selon
  l'estimateur. L'amplification est deux à quatre fois plus rapide que l'oubli.
- **Le critère de signe est vide** — nouveau point 15 de l'audit. Le rapport dépasse 1 dans
  tous les épisodes, par construction de la procédure d'estimation : un épisode observable a
  nécessairement connu une phase de croissance.
- **La prédiction sur la charge émotionnelle n'est pas étayée** : aucun écart détectable
  entre registres ($p \geq 0{,}13$), et l'estimation ponctuelle va dans le sens contraire.

### Modifié

- **Recommandation 2 du mémorandum réécrite** — d'une interdiction des configurations où
  $\gamma\alpha > \lambda$, inapplicable puisque toujours vraie, vers un **plafond sur le
  rapport** $\gamma\alpha/\lambda \leq \rho_{\max}$.
- `docs/limites.md` : ajout du point 15 et révision de la section sur la calibration, qui
  n'est plus absente mais seulement entamée.
- `ide.calibration.fit_exponential_rate` exige des valeurs strictement positives au lieu de
  les rabattre sur un plancher — un rabattement aplatissait silencieusement les
  décroissances et produisait un taux nul.

### À faire

Priorisé dans [`docs/feuille-de-route.md`](docs/feuille-de-route.md). En tête désormais :

- **détecter des changements de régime, et non des pics** — la calibration actuelle ne voit
  pas les désinformations qui s'installent, soit précisément les cas archétypaux ;
- résolution infra-quotidienne, et décroissance non exponentielle ;
- test adverse de manipulabilité de l'IDE, entièrement simulable ;
- évaluation hors ligne de l'ADE sur un jeu de données de recommandation réel.

## [0.1.0] — 2026-08-17

Première mise en forme du travail : passage d'un fil de discussion à un dépôt
scientifique reproductible, bilingue et publié.

### Ajouté

- **Noyau scientifique** `src/ide/` — modules purs, sans entrée-sortie, à graine
  explicite : entropies de Shannon et de von Neumann, calcul de l'IDE, modèle d'Ising 2D
  par Metropolis en damier avec champ externe et cycle d'hystérésis, Voter Model avec
  dérive de désinformation, énergie libre de champ moyen et solveur de Fokker-Planck en
  volumes finis, cinétique de résonance saturée, score de recommandation de l'ADE avec
  recuit, et modèle à agents « compas politique ».
- **Module de tracé** `ide.plotting` — style et palette communs à toutes les figures,
  isolé du noyau parce que `matplotlib` est une dépendance facultative.
- **Suite de 203 tests** — température critique d'Onsager retrouvée à ±0,25 sur un réseau
  24×24, conservation de la masse de probabilité à 10⁻¹⁵, bimodalité sous $T_c$ et
  unimodalité au-dessus, exposants des lois d'échelle du temps de consensus, aire du
  cycle d'hystérésis strictement positive sous $T_c$ et nulle au-dessus, équivalence de
  l'ADE avec un filtre d'engagement à $\mu = 0$, reproductibilité à la graine du modèle à
  agents. Les exemples des docstrings sont exécutés avec la suite.
- **Notebooks** `01` à `08` — un par bloc théorique, exécutables en conteneur, produisant
  l'intégralité des figures de la note.
- **Documentation bilingue** publiée sur GitHub Pages — théorie, index IDE, algorithme
  ADE, mémorandum de régulation ARCOM/DSA. Les pages de théorie sont en français, avec
  repli automatique depuis l'anglais ; la note scientifique anglaise couvre la science.
- **Note scientifique** `paper/` en LaTeX, versions française (9 pages) et anglaise
  (8 pages), compilées en conteneur texlive avec bibliographie BibTeX.
- **Audit critique** [`docs/limites.md`](docs/limites.md) — quatorze corrections
  documentées et traçables, plus les limites qui subsistent, y compris celles qui portent
  sur l'usage réglementaire de l'index : manipulabilité, arbitraire de la discrétisation
  en points de vue, vie privée, et le fait qu'un plancher d'IDE est une intervention sur
  le débat public et non une simple mesure technique.
- **Feuille de route** [`docs/feuille-de-route.md`](docs/feuille-de-route.md) — une piste
  concrète par limite, classée par rapport valeur/effort.
- **Errata** [`docs/errata.md`](docs/errata.md) — table de correspondance ligne à ligne
  avec le fil de travail d'origine.
- **Environnement conteneurisé** — services `lab`, `test`, `lint`, `notebooks`, `site`,
  `site-build` et `latex` ; aucune dépendance installée sur la machine hôte.
- **Intégration continue** — tests, lint, exécution des notebooks et build du site à
  chaque push ; déploiement automatique de la documentation.

### Modifié par rapport au fil de travail d'origine (14 août 2026)

Les cinq premières entrées corrigent des **formules invalides**.

- **Signe du coefficient de régulation** — le score de l'ADE est fixé à
  `S = Pertinence + μ·ΔH` avec `μ ≥ 0`. Le fil hésitait entre `-μ·ΔH` et `+μ·ΔH` ; la
  version négative refermait la bulle qu'elle prétendait ouvrir. Le code refuse désormais
  un `μ` négatif par une exception explicite.
- **Dérive de l'équation de Fokker-Planck** — `A(x) = Jx + H` est remplacée par
  `A(x) = Jx + H - T·artanh(x)`. Sans le terme entropique de mélange, la distribution
  stationnaire est convexe : le modèle ne pouvait produire **aucune transition de phase**,
  et la dynamique n'était pas bornée. La correction fait apparaître l'énergie libre
  `F = E - TS` que le fil invoquait sans l'écrire, et une température critique de champ
  moyen `T_c = J`.
- **Probabilités de transition du Voter Model biaisé** — la forme du fil,
  `P(x → x-1/N) = x(1-x) - hx`, devient négative dès que `h > 1-x`. Les deux canaux
  d'influence sont désormais mélangés plutôt qu'additionnés.
- **Signe du rappel dans l'équation de résonance** — `-ω₀²V` est corrigé en `+ω₀²V`. Le
  signe d'origine rendait le système instable même à gain algorithmique nul, ce qui privait
  de tout contenu le critère `γα > λ`.
- **Cinétique de résonance bornée** — ajout d'un facteur de saturation traduisant la
  finitude de l'attention. La version d'origine divergeait exponentiellement sans limite,
  ce qui rendait impossible toute comparaison entre configurations.
- **Effet de la taille du système reformulé** — l'entropie de configuration totale croît
  avec `N`, mais le bruit de la variable macroscopique décroît en `1/N`. La thèse retenue
  est qu'une grande population devient **rigide**, non bruyante — ce qui explique
  l'irréversibilité de la polarisation, contrairement à la métaphore de la « pompe à
  entropie ».
- **Argument sur la connectivité corrigé** — le temps de consensus croît en `N` en champ
  moyen contre `N²` sur un anneau : un réseau globalisé converge **plus vite**. Ce ne sont
  donc pas les liens qui fragmentent, mais le biais directionnel et l'homophilie.
- **Statut des analogies requalifié** — l'entropie qui croît sous décohérence est celle du
  sous-système réduit, non du système fermé ; l'effet tunnel social devient une métaphore,
  le mécanisme correct étant le franchissement de barrière par activation thermique
  (Kramers) ; `1/k^N` décrit un état initial et non une dynamique ; `τ_D ∝ τ_R/N` est
  étiqueté loi d'échelle heuristique.
- **Nomenclature dissociée** — l'**IDE** désigne l'*index* métrologique, l'**ADE**
  l'*algorithme* de filtrage. Le fil employait les deux sigles indifféremment, ce qui
  rendait la proposition réglementaire ambiguë : impose-t-on une mesure ou une
  implémentation ?
- **Conclusion du mémorandum nuancée** — la formule « la régulation devient une ingénierie
  de la stabilité » est conservée, accompagnée de la réserve qu'une ingénierie de la
  stabilité *est* une intervention sur le débat public.

### Ajouté au modèle à agents

- **Température sociale** — le paramètre central de toute la théorie était absent de sa
  seule implémentation. Sans agitation individuelle, le conformisme fait converger la
  population vers un point unique : l'IDE tombe à zéro quels que soient les autres
  réglages, et le modèle ne pouvait représenter ni le débat fluide ni l'effet du bruit
  thermique qu'il recommandait d'injecter.
- **Radicalisation progressive** à la contamination, en remplacement de la téléportation
  dans un coin du compas, qui supprimait toute dynamique ultérieure.
- **Vérification probabiliste** — l'efficacité des fact-checkers est paramétrable, là où le
  prototype soignait avec certitude tout individu à portée.
- **Bords réfléchissants** — la troncature des opinions accumulait les individus agités sur
  les bords, ce qui faisait chuter l'IDE à haute température pour une raison purement
  numérique.

### Archivé

- [`legacy/simulation_thread_2026-08.py`](legacy/) — la simulation `pygame` du fil
  d'origine, conservée **sans correction**, y compris son indentation perdue à
  l'impression. Ses cinq défauts et ses trois bons choix sont documentés dans
  [`legacy/README.md`](legacy/README.md).

### Note sur la source

Le fil de travail source est une impression Gmail rasterisée, sans couche de texte. Il n'a
pas été commité : il contient des adresses électroniques personnelles et
professionnelles. Son contenu a été réécrit, non copié.

[Non publié]: https://github.com/s-geffroy/Indice-Diversite-Exposee/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/s-geffroy/Indice-Diversite-Exposee/releases/tag/v0.1.0
