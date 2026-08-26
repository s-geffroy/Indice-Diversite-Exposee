# Bibliographie

Toutes les références sur lesquelles ce travail s'appuie, avec **ce que chacune y sert**. Une
référence sans usage identifiable n'appartient pas à une bibliographie mais à une liste de
lectures.

Cette page est **dérivée** de `paper/refs.bib`, le fichier que compilent les deux notes : les
deux ne peuvent pas diverger, et un test le vérifie. Elle se régénère par
`docker compose run --rm lab python scripts/build_bibliography.py`.


## Entropie et information

- **Shannon, Claude E.** (1948). *A Mathematical Theory of Communication*, Bell System Technical Journal, vol. 27(3), p. 379–423.  
  Définit l'entropie dont l'indice est la version normalisée.
- **von Neumann, John** (1932). *Mathematische Grundlagen der Quantenmechanik*.  
  Entropie du sous-système réduit, sur laquelle reposait l'analogie.
- **Jost, Lou** (2006). *Entropy and diversity*, Oikos, vol. 113(2), p. 363–375.  
  Justifie de publier l'indice en **nombre effectif de points de vue** plutôt qu'en entropie normalisée.


## Recommandation, diversité et normativité

- **Pariser, Eli** (2011). *The Filter Bubble: What the Internet Is Hiding from You*.  
  Formulation populaire de la bulle de filtres.
- **Carbonell, Jaime ; Goldstein, Jade** (1998). *The Use of MMR*, Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, p. 335–336. [→](https://doi.org/10.1145/290941.291025)  
  MMR : la ligne de base qui tient la frontière aussi bien que le filtre proposé ici.
- **Rao, C. Radhakrishna** (1982). *Diversity and dissimilarity coefficients: A unified approach*, Theoretical Population Biology, vol. 21(1), p. 24–43.  
  Entropie quadratique, premier remplaçant envisagé — et écarté.
- **Ohsaka, Naoto ; Togashi, Riku** (2023). *A Critical Reexamination of Intra-List Distance and Dispersion*, Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, p. 1619–1628. [→](https://arxiv.org/abs/2305.13801)  
  Établit les optima dégénérés de l'*intra-list distance*, retrouvés ici par optimisation sous contrainte.
- **Steck, Harald** (2018). *Calibrated Recommendations*, Proceedings of the 12th ACM Conference on Recommender Systems, p. 154–162. [→](https://doi.org/10.1145/3240323.3240372)  
  Recommandations calibrées : la cible comme distribution déclarée.
- **Vrijenhoek, Sanne ; Bénédict, Gabriel ; Gutierrez Granada, Mateo ; Odijk, Daan ; de Rijke, Maarten** (2022). *RADio – Rank-Aware Divergence Metrics to Measure Normative Diversity in News Recommendations*, Proceedings of the 16th ACM Conference on Recommender Systems, p. 208–219. [→](https://arxiv.org/abs/2209.13520)  
  RADio : divergences conscientes du rang et diversité normative, dont l'indice n'occupe qu'une dimension.
- **Deffuant, Guillaume ; Neau, David ; Amblard, Frederic ; Weisbuch, G\'erard** (2000). *Mixing beliefs among interacting agents*, Advances in Complex Systems, vol. 3(01n04), p. 87–98.  
  Rappelle que les opinions sont multidimensionnelles, ce qu'un catalogue de points de vue discrétise nécessairement.


## Biais de position et évaluation contrefactuelle

- **Joachims, Thorsten ; Swaminathan, Adith ; Schnabel, Tobias** (2017). *Unbiased Learning-to-Rank with Biased Feedback*, Proceedings of the Tenth ACM International Conference on Web Search and Data Mining, p. 781–789. [→](https://doi.org/10.1145/3018661.3018699)  
  Modèle de biais de position $e(R) = R^{-\eta}$ et correction par propension inverse.
- **Craswell, Nick ; Zoeter, Onno ; Taylor, Michael ; Ramsey, Bill** (2008). *An Experimental Comparison of Click Position-Bias Models*, Proceedings of the 2008 International Conference on Web Search and Data Mining, p. 87–94. [→](https://doi.org/10.1145/1341531.1341545)  
  Modèle à **cascade** : la contre-épreuve qui montre que le test d'échangeabilité tient et que la loi de puissance ne tient pas.
- **Agarwal, Aman ; Zaitsev, Ivan ; Wang, Xuanhui ; Li, Cheng ; Najork, Marc ; Joachims, Thorsten** (2019). *Estimating Position Bias without Intrusive Interventions*, Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining, p. 474–482.  
  Récolte d'interventions : estimer la sévérité sans expérience.
- **Swaminathan, Adith ; Joachims, Thorsten** (2015). *The Self-Normalized Estimator for Counterfactual Learning*, Advances in Neural Information Processing Systems 28, p. 3231–3239. [→](https://papers.nips.cc/paper/2015/hash/39027dfad5138c9ca0c474d71db915c3-Abstract.html)  
  Estimateur auto-normalisé, employé dans les comparaisons.
- **Vardasbi, Ali ; Oosterhuis, Harrie ; de Rijke, Maarten** (2020). *When Inverse Propensity Scoring does not Work: Affine Corrections for Unbiased Learning to Rank*, Proceedings of the 29th ACM International Conference on Information and Knowledge Management, p. 1475–1484. [→](https://arxiv.org/abs/2008.10242)  
  Biais de confiance et modèle affine : démontre que l'IPS ne peut pas le corriger, et fournit la contre-épreuve du notebook 20.
- **Hager, Philipp ; Deffayet, Romain ; Renders, Jean-Michel ; Zoeter, Onno ; de Rijke, Maarten** (2024). *Unbiased Learning to Rank Meets Reality: Lessons from Baidu's Large-Scale Search Dataset*, Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval. [→](https://arxiv.org/abs/2404.02543)  
  Sur le jeu même où ce dépôt mesure $\hat\eta = 1{,}10$ : corriger le biais de position n'améliore pas le classement.


## Jeux de données publics

- **Wu, Fangzhao ; Qiao, Ying ; Chen, Jiun-Hung ; Wu, Chuhan ; Qi, Tao ; Lian, Jianxun ; Liu, Danyang ; Xie, Xing ; Gao, Jianfeng ; Wu, Winnie ; Zhou, Ming** (2020). *MIND: A Large-scale Dataset for News Recommendation*, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, p. 3597–3606. [→](https://aclanthology.org/2020.acl-main.331/)  
  MIND, dont ce dépôt établit que l'ordre enregistré est mélangé.
- **Zou, Lixin ; Mao, Haitao ; Chu, Xiaokai ; Tang, Jiliang ; Ye, Wenwen ; Wang, Shuaiqiang ; Yin, Dawei** (2022). *A Large Scale Search Dataset for Unbiased Learning to Rank*, arXiv preprint arXiv:2207.03051. [→](https://arxiv.org/abs/2207.03051)  
  Baidu-ULTR, le contrôle positif du test d'échangeabilité.
- **Saito, Yuta ; Aihara, Shunsuke ; Matsutani, Megumi ; Narita, Yusuke** (2020). *Open Bandit Dataset and Pipeline: Towards Realistic and Reproducible Off-Policy Evaluation*, arXiv preprint arXiv:2008.07146. [→](https://arxiv.org/abs/2008.07146)  
  Open Bandit Dataset : propensions vraies et seau aléatoire, seule confrontation à une vérité terrain.
- **van Drunen, Max ; Vrijenhoek, Sanne** (2025). *How public datasets constrain the development of diversity-aware news recommender systems, and what law could do about it*, arXiv preprint arXiv:2510.05952. [→](https://arxiv.org/abs/2510.05952)  
  Établit avant nous que les jeux publics sont le goulot d'étranglement, et le droit européen la voie d'accès.


---

*Source : `paper/refs.bib` · les deux notes de synthèse citent ces mêmes entrées ·
[audit critique](limites.md) · [appel à relecture](relecture.md)*
