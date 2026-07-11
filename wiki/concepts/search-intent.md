---
type: concept
title: Search Intent (Intention de Recherche)
slug: search-intent
tags:
  - seo
  - content-strategy
  - keyword-research
  - serp
sources:
  - "[[jotaro-seo-content-strategy]]"
  - "[[jotaro-seo-6000-toys-case-study]]"
  - "[[raw/assets/jotaro-seo-ia-x-seo]]"
  - "[[navboost]]"
  - "[[seo-copywriting]]"
  - "[[jotaro-seo-strategie-ecommerce-2026]]"
source_count: 6
status: active
updated: 2026-06-18
---

# Search Intent (Intention de Recherche)

**Definition:** The underlying purpose behind a search query — what the user actually wants to accomplish. Google infers intent from the query and reflects it in the SERP format (article, product page, list, video). Mismatching content format to intent = failure to rank regardless of content quality.

## What we know

### Intent types (3-type vs 4-type model)
- **Informational**: user wants to learn or understand. SERP shows articles, guides, definitions. Queries: "comment", "pourquoi", "qu'est-ce que", "meilleur" (informational "best"). Drives 99.9 % of AI Overviews → [[raw/assets/jotaro-seo-ia-x-seo]].
- **Transactional/Commercial**: user wants to buy or compare. SERP shows product pages, e-commerce collections, comparison tables. Amazon in TOP 3 = strong transactional signal → [[jotaro-seo-6000-toys-case-study]].
- **Navigational**: user wants a specific site (less relevant for content strategy).
- **4-type refinement** ([[seo-copywriting]]): splits the middle into **commercial** (compare before deciding — "meilleurs outils X", "X course") vs **transactional** (ready to act — "acheter X", "X prix/service"). Align message + structure + CTA with the dominant intent.

### SERP format = intent signal
- The type of page dominating a SERP tells you what to create:
  - Mostly e-commerce collections → create a collection page.
  - Mostly blog articles → create an article.
  - Mostly product pages → create a product page.
  - Video thumbnails → also consider a video.
- "If Google wants to display articles for this keyword and you create a product page, you will never rank. No matter the content quality. You chose the wrong format." → [[jotaro-seo-content-strategy]].

### Practical analysis method
- Search the keyword in private browsing (incognito) → analyze TOP 10 results → identify the dominant page type → create that type.
- Also analyze TOP 3 H2 structure: what they cover + what they DON'T cover = your competitive angle → [[jotaro-seo-content-strategy]].

### Collection vs page produit — règle de décision e-commerce

Pour les mots-clés transactionnels e-commerce, la SERP tranche. Regarder les 10 premiers résultats organiques (hors pub) :

| Ce que la SERP montre | Ce qu'il faut créer |
|---|---|
| Majorité de pages de collection (plusieurs produits) | Page de collection |
| Majorité de pages produit individuelles | Page produit (fiche produit) |
| Articles de blog / tutoriels | Article de blog avec lien vers la page commerciale |
| Mélangé | Regarder le TOP 3 uniquement — copier leur approche structurelle (pas leur contenu) |

**Exemples concrets :**
- "cagoule en laine" → SERP montre collections → page de collection avec plusieurs modèles
- "cagoule laine mérinos homme taille L grise" (requête très précise) → SERP montre pages produit → fiche produit
- "ours en Lego" → SERP montre articles de blog → article informatif qui répond à "existe-t-il un ours en Lego" + présente le produit comme alternative

**Pourquoi c'est critique :** si on crée une page produit sur un mot-clé pour lequel Google veut montrer des collections, le meilleur contenu du monde ne permettra jamais de se positionner en première page. Le format prime sur la qualité.

→ [[jotaro-seo-strategie-ecommerce-2026]]

### Content mix targets
- For AI visibility: 70 % informational, 20 % commercial-hybrid, 10 % transactional → [[raw/assets/jotaro-seo-ia-x-seo]].
- For classic SEO: prioritize informational long-tail for blog, commercial for collection/product pages.

## Relations
- [[navboost]] validates intent-match by behavior: a transactional query with a quick exit signals unmet intent → demotion.
- Core input for [[keyword-research]]: SERP analysis = step 5 of the 5 keyword sources.
- Determines [[article-structure]]: informational queries need structured educational articles; transactional need product comparison formats.
- Linked to [[ai-overviews]]: AI Overviews almost exclusively surface on informational queries.

## Tensions / open questions
- Can a single piece of content satisfy both informational and transactional intent? (Some hybrid articles do, but SERP signals usually favor one type.)

## Sources
- [[jotaro-seo-content-strategy]] — SERP format matching; dominant intent analysis methodology.
- [[jotaro-seo-6000-toys-case-study]] — Amazon in SERP as transactional intent signal.
- [[raw/assets/jotaro-seo-ia-x-seo]] — 99.9 % AI Overviews on informational queries; recommended content mix.
- [[navboost]] — query types (info/nav/transactional) and how behavior validates each.
- [[seo-copywriting]] — 4-intent model (commercial split from transactional); align message/structure/CTA.
