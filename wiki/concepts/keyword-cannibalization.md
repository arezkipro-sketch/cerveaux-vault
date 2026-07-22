---
type: concept
title: "Keyword Cannibalization (Cannibalisation de Mots-Clés)"
slug: keyword-cannibalization
tags: [seo, on-page, content-strategy, keyword-research]
sources: ["[[jotaro-seo-keyword-cannibalization]]", "[[jotaro-seo-content-strategy]]", "[[content-pruning]]"]
source_count: 3
status: active
updated: 2026-07-22
note: "MAJ 2026-07-22 : cas vécu harnais-chien-expert.fr, gap méthodologique GSC-only vs SERP-similarity."
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
