---
type: concept
title: "NavBoost"
slug: navboost
tags: [navboost, technical-seo, user-behavior, ux, google, ranking]
sources: ["[[navboost]]"]
source_count: 1
status: active
updated: 2026-06-18
---

# NavBoost

**Definition:** A Google ranking system that evaluates **navigation and user-behavior signals** in search results to dynamically adjust page rankings — a refinement layer on top of classic factors (backlinks, domain authority). Surfaced via Google internal docs / DOJ-era leaks → [[navboost]].

## Signals it watches
- **CTR** ([[click-through-rate]]) — clicks on a result vs others.
- **Pogo-sticking** — user enters a page and bounces straight back to the SERP = dissatisfaction.
- **Dwell time** — how long the user stays on the content.
- **Internal engagement** — scrolling, link clicks, media interaction.
- **Implicit satisfaction** — not returning to Google = the answer was found.
→ all from [[navboost]]

## NavDemotion (the inverse)
- Negative signals demote pages: high pogo-sticking, very low dwell time, below-average CTR, duplicate/thin content → [[navboost]].

## Query types
- Affects all queries; strongest where behavior validates relevance — informational (dwell), navigational (CTR), transactional (quick exit = unmet intent). Acts as a quality filter → [[navboost]] → [[search-intent]].

## How to adapt
- **Content for retention:** strong intros ([[hook]]), fast-readability structure, examples/data/storytelling → [[navboost]].
- **UX:** speed (slow → pogo-sticking, ties to [[core-web-vitals]]), [[mobile-seo]], clear design, no intrusive ads/popups.
- **Measure:** [[google-analytics-4]] (engagement), [[google-search-console]] (CTR/query), heatmaps/session recordings (Hotjar, Clarity).

## Relations
- Behavioral layer beside technical [[core-web-vitals]] / [[site-health]]; both feed Google's experience-first ranking.
- Makes [[click-through-rate]], retention ([[hook]]/[[headline]]), and UX direct ranking levers.

## Tensions / open questions
- Google has publicly downplayed CTR-as-ranking-factor; NavBoost specifics come from leaks, not official docs — best-available, not confirmed.
- No public weighting of behavioral vs classic signals.

## Sources
- [[navboost]] — Neil Patel FR explainer: signals, NavDemotion, query types, adaptation strategies.
