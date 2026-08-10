---
type: concept
title: "Keyword Cannibalization (Cannibalisation de Mots-Clés)"
slug: keyword-cannibalization
tags: [seo, on-page, content-strategy, keyword-research]
sources: ["[[jotaro-seo-keyword-cannibalization]]", "[[jotaro-seo-content-strategy]]", "[[content-pruning]]"]
source_count: 3
status: active
updated: 2026-07-25
note: "MAJ 2026-07-25 : PushRank content_creation peut être un faux positif si une collection Shopify canonique existe déjà."
---

# Keyword Cannibalization

**Definition:** Internal competition where multiple pages on the same site target the same keyword, sending Google contradictory signals about which page to rank, diluting authority, and causing both (or all) pages to rank worse than they would if unified.

## What we know
- **Mechanism**: two pages targeting keyword X → Google unsure which to show → splits attention → neither ranks in TOP 3, both stuck in mid-table → [[jotaro-seo-keyword-cannibalization]].
- **Core rule**: **1 keyword = 1 page**. The most important rule in [[keyword-research]] → [[jotaro-seo-content-strategy]].
- **Detection methods** (4):
  1. List all keywords → check which articles rank for each → identify overlaps → [[jotaro-seo-keyword-cannibalization]].
  2. Search the keyword on Google → see which site pages appear in results → [[jotaro-seo-keyword-cannibalization]].
  3. Compare ranking positions across suspected duplicate-targeting pages → [[jotaro-seo-keyword-cannibalization]].
  4. **Google Search Console** (most reliable): Clicks on keyword → Pages tab → see all pages Google associates with that keyword (tip from @Lamaxaw) → [[jotaro-seo-keyword-cannibalization]].
- **SERP similarity test** (12pages.com): enter two suspected-cannibalizing keywords → get SERP overlap score.
  - \> 80% overlap → same SERP → one page covers both → merge or deindex the weaker.
  - 50-79% → partial overlap → two pages possible but differentiate clearly.
  - < 50% → distinct SERPs → two separate pages with no cannibalization risk → [[jotaro-seo-content-strategy]].
- **Case study**: fitness blog with "programme musculation débutant" + "programme fitness débutant" → 82% similarity → merged into one → positions immediately improved → [[jotaro-seo-content-strategy]].

## Cas vécu — harnais-chien-expert.fr (2026-07-22) : l'erreur de ne vérifier QUE via GSC

Diagnostic initial fait uniquement via les méthodes 1/3/4 ci-dessus (comparaison des pages qui rankent dans les snapshots [[pushrank]]/GSC) pour "harnais chien" (27 100 rech/mois) vs "harnais pour chien" (4 400 rech/mois). Conclusion à ce stade : aucune cannibalisation, une seule page (`/collections/tous-les-harnais-chien`) captait de la visibilité sur les deux termes.

**Ce qui manquait** : la vérification SERP-similarity (méthode listée plus haut, 12pages.com) n'a pas été faite à cette étape — oubli méthodologique. L'utilisateur l'a faite lui-même de son côté et a trouvé **8/10 résultats communs (80% de similarité)** entre les deux requêtes — pile au seuil de fusion. Ça a permis de confirmer que "harnais chien" et "harnais pour chien" doivent être traités comme **une seule et même intention de recherche** (même page cible), pas deux mots-clés distincts qui auraient pu justifier deux pages séparées.

**Leçon retenue** : la comparaison via GSC/outil de tracking (quelles pages rankent déjà) et la comparaison SERP-similarity (est-ce que Google traite ces mots-clés comme une même intention) répondent à deux questions différentes et complémentaires :
- GSC/tracking → *"ai-je déjà un problème de cannibalisation actif ?"*
- SERP-similarity → *"ces mots-clés devraient-ils de toute façon être traités comme un seul, même si aucune page ne cannibalise encore rien ?"*

Sauter la seconde question peut faire conclure à tort "pas de souci" alors que la vraie question (combien de pages cibler) n'a pas été posée. **Les deux checks sont désormais systématiques avant de conclure une analyse de cannibalisation**, même quand la vérification GSC seule semble déjà rassurante.


## Cas vécu — PushRank `content_creation` vs collections Shopify existantes (2026-07-25)

Sur harnais-chien-expert.fr, PushRank a recommandé de créer des pages dédiées pour `harnais chien`, `harnais canicross`, `harnais en Y`, `harnais chien voiture`, `harnais chiot` et `harnais teckel`. Vérification Shopify : chaque requête avait déjà une collection dédiée. Le problème n'était donc pas l'absence de page, mais l'absence de mapping reconnu par PushRank (`primaryArticle: null`, keywords en statut `candidate`).

Décision : ne pas créer de nouvelles pages. Les opportunités ont été passées en `ignored`, car créer une seconde URL sur la même intention aurait augmenté le risque de cannibalisation. La bonne action est de conserver la collection existante comme page canonique, puis d'optimiser title/meta/contenu/maillage si les signaux GSC le justifient.

Exception maintenue ouverte : `ceinture chien voiture`. Cette intention peut être distincte de `harnais chien voiture` si le site vend une ceinture ou attache voiture dédiée. Tant que l'offre produit n'est pas claire, la recommandation reste en `todo` plutôt que d'être ignorée.

**Règle apprise** : une recommandation `content_creation` d'un outil SEO doit déclencher un mapping, pas une création automatique. Avant de créer : vérifier les collections existantes, la page cible GSC, la similarité SERP, le maillage interne et l'intention business. Si une collection transactionnelle existe déjà, elle doit rester la page cible.

## Cas vécu — fausse alerte sur "harnais anti traction chien" (2026-08-09)

Sur `/collections/harnais-anti-traction-chien` (position 55-94 sur toutes les variantes "anti traction", 0 clic malgré ~130 impressions/90j), conclusion initiale erronée : cannibalisation avec 12 fiches produits nommées "Harnais Chien Anti Traction [variante]" + la collection `harnais-grand-chien` (SEO title incluant aussi "Anti-Traction"). Cette conclusion était basée **uniquement sur la similarité des titres entre pages**, sans vérification SERP — exactement l'erreur méthodologique déjà documentée dans le cas du 22/07 ci-dessus.

**Rappel de la méthode correcte (Arezki)** : pour confirmer une cannibalisation, il faut taper les mots-clés candidats dans la SERP (Google réel, pas seulement `site:`) et vérifier si les résultats se recoupent à plus de 50% — c'est le test SERP-similarity déjà listé plus haut, pas une comparaison de titres.

Vérification faite a posteriori (GSC `query_page` sans filtre de page + recherche `site:`) : aucun des 12 produits n'apparaît en concurrence avec la collection sur les mêmes requêtes GSC — les produits ne rankent tout simplement pas sur ces termes, contrairement à la collection qui y apparaît (mal classée, mais présente). Pas de cannibalisation démontrable. Cause plus probable : "harnais anti traction chien" (8100 rech/mois) est un terme concurrentiel dominé par des sites établis (comparatifs), un jeune site n'y est pas encore compétitif — problème d'autorité, pas de cannibalisation interne.

**Leçon renforcée** : la similarité de titres/mots-clés entre deux pages du même site est un signal d'alerte à investiguer, jamais une preuve. Toujours appliquer le test SERP (méthode 2 ou 4 ci-dessus au minimum, SERP-similarity si deux mots-clés distincts sont en jeu) avant de proposer une action corrective.

## Solutions
1. **[[maillage-interne]]**: clear internal link hierarchy signals to Google which page is primary → [[jotaro-seo-keyword-cannibalization]].
2. **[[cocon-semantique]]**: thematic grouping with explicit page mère/pages filles hierarchy prevents targeting conflicts → [[jotaro-seo-keyword-cannibalization]].
3. **Merge**: consolidate two cannibalizing pages into one stronger, more comprehensive article.
4. **Deindex**: if one page is clearly weaker, remove/noindex it and 301-redirect to the primary.

## Relations
- Root cause = violating the 1-keyword/1-page rule in [[keyword-research]].
- Technical fix: [[canonical-tag]] when content is nearly identical (product variants); architectural fix: [[cocon-semantique]] for thematic targeting.
- Detection tool: [[maillage-interne]] audit → internal links reveal which page is being treated as primary.

## Tensions / open questions
- At what SERP similarity % is merging always better vs. keeping differentiated pages? (80% threshold given, but may vary by niche.)

## Relation to content pruning
- [[content-pruning]] treats cannibalization as a top reason to merge/delete: keep the most complete page — "3 strong articles > 10 mediocre on the same theme" → [[content-pruning]].

## Sources
- [[jotaro-seo-keyword-cannibalization]] — definition, dangers, detection methods, solutions.
- [[jotaro-seo-content-strategy]] — 1-keyword/1-page absolute rule; 12pages.com SERP similarity method; merger case study.
- [[content-pruning]] — cannibalization as a pruning trigger; keep the strongest page.
- Usage réel session 2026-07-22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe, gap méthodologique GSC-only corrigé grâce à une vérification manuelle de l'utilisateur).
