# Appel à relecture

Ce travail est un **document de travail ouvert**. Il croise deux disciplines, et son
auteur n'est spécialiste ni de l'une ni de l'autre : la relecture critique n'est pas une
formalité, c'est ce qui décidera s'il vaut quelque chose.

## Les retours les plus utiles

Ce dépôt ne mesure plus qu'une chose : la diversité qu'un fil expose réellement. Les retours
utiles portent donc sur cette mesure, par ordre décroissant :

1. **La forme retenue de l'indice.** L'IDE mesure l'entropie des contenus servis, pondérée par
   l'attention de chaque rang, sur un catalogue déclaré. Est-elle la bonne ? Les trois choix qui
   la définissent répondent chacun à une attaque qui a réussi — en reste-t-il une qui ne l'a pas
   été ? → [IDE](ide.md) · [test adverse](gaming.md)
2. **Les instruments de mesure.** Le test d'échangeabilité, l'estimation de la sévérité, le test
   de forme et l'encadrement de l'indice sont ce qui survit à tout le reste. Une erreur
   méthodologique là serait la plus coûteuse. → [MIND](mind.md) · [rang servi](rang-servi.md)
3. **La discrétisation en points de vue.** Le catalogue décide du niveau — 0,50 sur vingt-six
   rubriques, 0,92 sur trois — et deux axes d'étiquetage du même corpus ne concordent qu'à
   $\rho = 0{,}16$. Ce n'est pas une question technique. → [le catalogue](catalogue.md)
4. **Un journal qui porte un rang vérifiable et une étiquette.** Quatre journaux publics ont été
   examinés, aucun ne permet la mesure de l'indice **exposé**. C'est le seul verrou que ce dépôt
   ne peut pas lever seul. → [feuille de route](feuille-de-route.md)

## Ce qui a déjà été corrigé

Merci de consulter l'[audit critique](limites.md) et les [errata](errata.md) avant de signaler une
erreur : **vingt-sept corrections** y sont documentées, dont cinq formules invalides, une moitié
qui porte sur les propositions du dépôt lui-même, et neuf résultats négatifs publiés comme tels.

Le dépôt a par ailleurs **retiré trois moitiés** : l'analogie avec la décohérence quantique, le
formalisme de physique statistique qu'elle avait fait emprunter, et l'appareil de régulation
(algorithme, plancher, demande d'accès). L'audit en garde le registre entier ; il n'est pas prévu
de les reconstituer.

## Comment contribuer

* **Ouvrir une [issue](https://github.com/s-geffroy/Indice-Diversite-Exposee/issues)** —
  y compris pour une objection de fond, qui n'a pas besoin d'être accompagnée d'un
  correctif.
* **Proposer une *pull request*** — les corrections de formalisme sont bienvenues ;
  merci d'y joindre le test qui échouait avant et passe après.
* **Écrire directement**, si l'objection est trop large pour une issue.

Tout retour intégré est crédité dans le [CHANGELOG](https://github.com/s-geffroy/Indice-Diversite-Exposee/blob/main/CHANGELOG.md).

## Communautés visées

Le travail se situe à l'intersection de deux champs :

| Champ | Ce qui s'y joue |
|---|---|
| **Recommandation et évaluation hors ligne** | validité du test d'échangeabilité, de l'estimation du biais de position, du test de forme et des estimateurs contrefactuels |
| **Mesure de la diversité informationnelle** | la forme retenue de l'indice, la discrétisation en points de vue, et ce qu'une entropie normalisée mesure vraiment |

---

## Modèle de courriel de sollicitation

Le texte ci-dessous est un modèle réutilisable. Les crochets sont à compléter ; aucune
coordonnée personnelle n'est incluse dans ce dépôt.

> **Objet** — Proposition de relecture : mesurer la diversité qu'un fil algorithmique expose
> réellement (métrologie de l'audit algorithmique)
>
> Madame, Monsieur,
>
> Je me permets de solliciter votre expertise pour la relecture d'un travail ouvert portant sur
> la **mesure de la diversité réellement exposée** par un fil de recommandation, et sur les
> conditions auxquelles cette mesure est possible sur données réelles.
>
> **Résumé.** Le travail définit un *Indice de Diversité Exposée* (IDE) — l'entropie des
> contenus servis sur un catalogue de points de vue déclaré, pondérée par l'attention de chaque
> rang — puis le soumet aux attaques qu'il doit supporter. Trois d'entre elles réussissent contre
> les formulations naïves et imposent chacune une correction. L'essentiel des résultats est
> **métrologique** : trois contrôles à passer sur un journal de recommandation avant toute
> mesure, la sévérité de l'attention **mesurée** plutôt que supposée — 0,88 et non 1 —, et la
> première mesure de l'indice sur des fils réels.
>
> **Ce que je sollicite en particulier.** Le dépôt publie **neuf résultats négatifs** et
> **vingt-sept corrections** de son propre raisonnement, dont cinq invalidaient une formule et
> dont la moitié portent sur ses propres propositions. Les avis les plus utiles porteraient sur
> la forme retenue de l'indice, sur la discrétisation en points de vue, ou sur les instruments de
> mesure eux-mêmes, où une erreur méthodologique serait la plus coûteuse. Une validation
> d'ensemble me serait bien moins utile.
>
> L'intégralité du travail est en libre accès : équations, code reproductible en conteneur,
> suite de tests, figures régénérables, et jeux de données dérivés.
>
> [lien vers le dépôt]
>
> Seriez-vous ouvert à y jeter un œil critique, ou auriez-vous un chercheur de votre
> équipe à me recommander pour cette relecture ?
>
> En vous remerciant par avance du temps accordé,
>
> [Prénom Nom] · [affiliation ou statut] · [contact]

### Conseil d'usage

Ce que le fil de travail d'origine notait à juste titre : il faut que le lecteur qui
clique sur le lien puisse comprendre l'essentiel **en moins de deux minutes**. La page
d'accueil du dépôt est écrite pour cela — un chercheur sollicité ne lira pas trois pages
d'équations avant de décider s'il répond.

Un conseil supplémentaire, issu de l'audit : mentionner explicitement les limites du
travail dans le courriel de sollicitation. Un relecteur qui découvre lui-même une
faiblesse non signalée devient méfiant sur tout le reste ; un relecteur à qui l'on
annonce la faiblesse la traite comme une question de recherche.
