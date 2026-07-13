---
type: concept
title: AI Overviews (Aperçus IA)
slug: ai-overviews
tags:
  - seo
  - google
  - ai
  - serp
  - ai-seo
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[alexgroberman-62pct-beyond-top10]]"
  - "[[alexgroberman-page1-vs-ai-citation]]"
  - "[[irentdumpsters-google-ai-guide]]"
  - "[[semrush-ai-stats-2026]]"
  - "[[semrush-ai-search-trends-2026]]"
  - "[[apercu-ia-guide]]"
source_count: 7
status: active
updated: 2026-06-18
---

# AI Overviews (Aperçus IA)

**Definition:** Google's AI-generated answer blocks that appear at the top of search results pages, synthesizing information from multiple sources. They reduce user clicks to organic results and operate on a different citation logic than classic Google ranking.

## What we know
- AI Overviews now reduce clicks to the #1 organic result by **58 %** (was 34.5 % ten months earlier) — trend is accelerating → [[jotaro-seo-ia-x-seo]].
- **99.9 % of AI Overviews trigger on informational queries**; only 3.2 % on transactional queries → [[jotaro-seo-ia-x-seo]].
- Google AI Mode and AI Overviews agree on what to say **86 % of the time**, but cite different sources — only **13.7 % overlap** in cited pages → [[jotaro-seo-ia-x-seo]].
- Optimizing for classic Google ranking does not guarantee AI Overview inclusion, and vice versa → [[jotaro-seo-ia-x-seo]].

## Ahrefs study: Who actually gets cited in AI Overviews?

- **863,000 SERPs, 4 million AI Overview URLs** analyzed (Feb 2026) → [[alexgroberman-62pct-beyond-top10]].
- **62 %** of AIO citations go to pages NOT in top-10 organic for the original query → [[alexgroberman-62pct-beyond-top10]].
- One year prior: 76 % of citations came from top-10. Now only **38 %** → shift accelerated with Google Gemini 3 → [[alexgroberman-62pct-beyond-top10]].
- **31 %** of citations come from pages ranking beyond position 100 for the original query → [[alexgroberman-62pct-beyond-top10]].
- Separate study (55,393 searches): **30 %** of AIO-cited domains didn't appear in first-page organic results alongside them → [[alexgroberman-page1-vs-ai-citation]].
- Separate study (11,500 queries): minimal source overlap between traditional Google Search, AI Overviews, and Gemini → [[alexgroberman-page1-vs-ai-citation]].

## Root cause: Google Gemini 3 sub-query decomposition

Google AI internally decomposes queries into sub-queries, then sources each sub-query independently:
- "best CRM for small business" → sub-queries: "CRM onboarding comparison", "CRM pricing <10 people", "multi-state CRM compliance".
- Each sub-query draws from its own source pool → a business that only ranks for the main keyword misses 62 % of citation opportunities → [[alexgroberman-62pct-beyond-top10]].
- **Implication**: need 40-60 pages per category covering every buyer sub-question → [[topical-authority]].

## Google's official AIO guidance (via [[irentdumpsters-google-ai-guide]])
- AI Overviews use same core systems as traditional Google Search.
- Add media (photos, video) for AIO inclusion.
- Use Google Business Profile — GBP info can appear in AIO for local queries → [[google-business-profile]].

## Scale and growth (Semrush data)
- **2 billion monthly users** across 200+ countries → [[semrush-ai-stats-2026]].
- Trigger rate growth: **6.49 % of searches** (January 2025) → **13.1 %** (March 2025) — doubled in 2 months → [[semrush-ai-search-trends-2026]].
- Trigger conditions: complex multi-part questions, educational/comparative queries, news-rich topics.
- AI summaries cite 3-8 sources; CTR for links inside AI summaries: **only 1 %** (Pew Research) → [[semrush-ai-search-trends-2026]].
- CTR drops 15.5 % for queries where AI Overviews appear (Amsive study) → [[semrush-ai-search-trends-2026]].

## SGE framing (beginner sources)
- Marketing primers describe AI Overviews under the older label **SGE** (Search Generative Experience): "Google now uses AI to generate complete answers in-results instead of just showing links," forcing content strategy to evolve toward [[generative-engine-optimization]] → [[apercu-ia-guide]].

## Relations
- Core motivation for [[ai-seo]]: the same site can rank #1 on Google and be absent from AI Overviews.
- Informational content focus (see [[ai-seo]] Stratégie 6) is the primary lever for AIO inclusion.
- Sub-query decomposition = practical argument for [[topical-authority]] at 40-60 page depth.

## Tensions / open questions
- Will AIO click reduction stabilize or continue to accelerate?
- At what point do AIO-dominated SERPs change the fundamental ROI calculation of classic SEO?
- Gemini 3 sub-query decomposition: does this apply equally across all query types or only certain verticals?

## Sources
- [[jotaro-seo-ia-x-seo]] — click-reduction stats and informational query share.
- [[alexgroberman-62pct-beyond-top10]] — Ahrefs 863K SERPs; 62 %/38 % split; sub-query decomposition.
- [[alexgroberman-page1-vs-ai-citation]] — 55,393 searches; 30 % AIO domains not in first-page organic.
- [[irentdumpsters-google-ai-guide]] — Google official AIO guidance; GBP in AIO responses.
- [[semrush-ai-stats-2026]] — 2B monthly users, 200+ countries.
- [[semrush-ai-search-trends-2026]] — 6.49%→13.1% trigger rate (Jan→Mar 2025); CTR 1% inside summaries.
