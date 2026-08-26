# Bibliography

Every reference this work rests on, together with **what each is used for here**. A reference
with no identifiable use belongs to a reading list, not to a bibliography.

This page is **derived** from `paper/refs.bib`, the file both notes compile: the two cannot
diverge, and a test checks it. Regenerate with
`docker compose run --rm lab python scripts/build_bibliography.py`.


## Entropy and information

- **Shannon, Claude E.** (1948). *A Mathematical Theory of Communication*, Bell System Technical Journal, vol. 27(3), p. 379–423.  
  Defines the entropy of which the index is the normalised version.
- **von Neumann, John** (1932). *Mathematische Grundlagen der Quantenmechanik*.  
  Reduced-subsystem entropy, on which the analogy rested.
- **Jost, Lou** (2006). *Entropy and diversity*, Oikos, vol. 113(2), p. 363–375.  
  Justifies publishing the index as an **effective number of viewpoints** rather than a normalised entropy.


## Recommendation, diversity and normativity

- **Pariser, Eli** (2011). *The Filter Bubble: What the Internet Is Hiding from You*.  
  Popular formulation of the filter bubble.
- **Carbonell, Jaime ; Goldstein, Jade** (1998). *The Use of MMR*, Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, p. 335–336. [→](https://doi.org/10.1145/290941.291025)  
  MMR: the baseline that holds the frontier as well as the filter proposed here.
- **Rao, C. Radhakrishna** (1982). *Diversity and dissimilarity coefficients: A unified approach*, Theoretical Population Biology, vol. 21(1), p. 24–43.  
  Quadratic entropy, the first replacement considered — and discarded.
- **Ohsaka, Naoto ; Togashi, Riku** (2023). *A Critical Reexamination of Intra-List Distance and Dispersion*, Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, p. 1619–1628. [→](https://arxiv.org/abs/2305.13801)  
  Establishes the degenerate optima of intra-list distance, recovered here by constrained optimisation.
- **Steck, Harald** (2018). *Calibrated Recommendations*, Proceedings of the 12th ACM Conference on Recommender Systems, p. 154–162. [→](https://doi.org/10.1145/3240323.3240372)  
  Calibrated recommendations: the target as a declared distribution.
- **Vrijenhoek, Sanne ; Bénédict, Gabriel ; Gutierrez Granada, Mateo ; Odijk, Daan ; de Rijke, Maarten** (2022). *RADio – Rank-Aware Divergence Metrics to Measure Normative Diversity in News Recommendations*, Proceedings of the 16th ACM Conference on Recommender Systems, p. 208–219. [→](https://arxiv.org/abs/2209.13520)  
  RADio: rank-aware divergences and normative diversity, of which the index occupies only one dimension.
- **Deffuant, Guillaume ; Neau, David ; Amblard, Frederic ; Weisbuch, G\'erard** (2000). *Mixing beliefs among interacting agents*, Advances in Complex Systems, vol. 3(01n04), p. 87–98.  
  A reminder that opinions are multidimensional, which a viewpoint catalogue necessarily discretises.


## Position bias and counterfactual evaluation

- **Joachims, Thorsten ; Swaminathan, Adith ; Schnabel, Tobias** (2017). *Unbiased Learning-to-Rank with Biased Feedback*, Proceedings of the Tenth ACM International Conference on Web Search and Data Mining, p. 781–789. [→](https://doi.org/10.1145/3018661.3018699)  
  Position-bias model $e(R) = R^{-\eta}$ and inverse-propensity correction.
- **Craswell, Nick ; Zoeter, Onno ; Taylor, Michael ; Ramsey, Bill** (2008). *An Experimental Comparison of Click Position-Bias Models*, Proceedings of the 2008 International Conference on Web Search and Data Mining, p. 87–94. [→](https://doi.org/10.1145/1341531.1341545)  
  The **cascade** model: the counter-test showing the exchangeability test holds and the power law does not.
- **Agarwal, Aman ; Zaitsev, Ivan ; Wang, Xuanhui ; Li, Cheng ; Najork, Marc ; Joachims, Thorsten** (2019). *Estimating Position Bias without Intrusive Interventions*, Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining, p. 474–482.  
  Intervention harvesting: estimating severity without an experiment.
- **Swaminathan, Adith ; Joachims, Thorsten** (2015). *The Self-Normalized Estimator for Counterfactual Learning*, Advances in Neural Information Processing Systems 28, p. 3231–3239. [→](https://papers.nips.cc/paper/2015/hash/39027dfad5138c9ca0c474d71db915c3-Abstract.html)  
  The self-normalised estimator, used in the comparisons.
- **Vardasbi, Ali ; Oosterhuis, Harrie ; de Rijke, Maarten** (2020). *When Inverse Propensity Scoring does not Work: Affine Corrections for Unbiased Learning to Rank*, Proceedings of the 29th ACM International Conference on Information and Knowledge Management, p. 1475–1484. [→](https://arxiv.org/abs/2008.10242)  
  Trust bias and the affine model: proves IPS cannot correct it, and provides notebook 20's counter-test.
- **Hager, Philipp ; Deffayet, Romain ; Renders, Jean-Michel ; Zoeter, Onno ; de Rijke, Maarten** (2024). *Unbiased Learning to Rank Meets Reality: Lessons from Baidu's Large-Scale Search Dataset*, Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval. [→](https://arxiv.org/abs/2404.02543)  
  On the very dataset where this repository measures $\hat\eta = 1.10$: correcting position bias does not improve ranking.


## Public datasets

- **Wu, Fangzhao ; Qiao, Ying ; Chen, Jiun-Hung ; Wu, Chuhan ; Qi, Tao ; Lian, Jianxun ; Liu, Danyang ; Xie, Xing ; Gao, Jianfeng ; Wu, Winnie ; Zhou, Ming** (2020). *MIND: A Large-scale Dataset for News Recommendation*, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, p. 3597–3606. [→](https://aclanthology.org/2020.acl-main.331/)  
  MIND, whose recorded order this repository shows to be shuffled.
- **Zou, Lixin ; Mao, Haitao ; Chu, Xiaokai ; Tang, Jiliang ; Ye, Wenwen ; Wang, Shuaiqiang ; Yin, Dawei** (2022). *A Large Scale Search Dataset for Unbiased Learning to Rank*, arXiv preprint arXiv:2207.03051. [→](https://arxiv.org/abs/2207.03051)  
  Baidu-ULTR, the exchangeability test's positive control.
- **Saito, Yuta ; Aihara, Shunsuke ; Matsutani, Megumi ; Narita, Yusuke** (2020). *Open Bandit Dataset and Pipeline: Towards Realistic and Reproducible Off-Policy Evaluation*, arXiv preprint arXiv:2008.07146. [→](https://arxiv.org/abs/2008.07146)  
  Open Bandit Dataset: true propensities and a random bucket, the only confrontation with a ground truth.
- **van Drunen, Max ; Vrijenhoek, Sanne** (2025). *How public datasets constrain the development of diversity-aware news recommender systems, and what law could do about it*, arXiv preprint arXiv:2510.05952. [→](https://arxiv.org/abs/2510.05952)  
  Establishes before us that public datasets are the bottleneck, and European law the route to access.


---

*Source: `paper/refs.bib` · both synthesis notes cite these same entries ·
[critical audit](limites.en.md) · [call for review](relecture.md)*
