---
type: concept
title: "Keyword Cannibalization (Cannibalisation de Mots-Clés)"
slug: keyword-cannibalization
tags: [seo, on-page, content-strategy, keyword-research]
sources: ["[[jotaro-seo-keyword-cannibalization]]", "[[jotaro-seo-content-strategy]]", "[[content-pruning]]"]
source_count: 3
status: active
updated: 2026-06-19
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
