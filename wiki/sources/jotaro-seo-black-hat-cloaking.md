---
type: source
title: "La zone noire du SEO — Cloaking ID"
slug: jotaro-seo-black-hat-cloaking
raw: "[[raw/assets/la zone noir du SEO.md]]"
source_url: "https://x.com/JotaroSeo/status/1724124943300886932"
source_type: x-thread
author: "[[jotaro-seo]]"
date_published: 2023-11-13
date_ingested: 2026-06-15
tags: [seo, black-hat-seo, cloaking, technical-seo, french]
status: active
---

# Black Hat SEO — Cloaking ID — Summary

**One-liner:** Cloaking ID is a black-hat technique that serves different content to Googlebot vs. human visitors by exploiting the `User-Agent` HTTP header, showing bots SEO-optimized text while humans see the designed experience.

## Key takeaways
- **Cloaking definition**: presenting different content based on visitor type (bot vs. human). Not all cloaking is black hat — but cloaking ID is.
- **Mechanism**: `User-Agent` HTTP header in each request identifies the visitor type. Script detects if visitor = Googlebot → serves text-heavy SEO version; if human → serves visual design version.
- **Bot version**: heavy text, optimized Hn structure, internal linking, no media bots can't parse (video, audio without transcripts).
- **Human version**: full design, images/video/audio, best UX possible.
- **Risk**: violates Google's guidelines. If detected → manual penalty or deindexation.
- **Use case given**: sites with media-heavy content (videos, images without alt) that Googlebot struggles to analyze.

## Notable claims (with locations)
- IP-based cloaking (using IP address or other server-side analysis) also exists but User-Agent is the standard method — *(tweet 2.1)*.
- Cloaking for media accessibility (videos bots can't parse) is the most common legitimate-seeming rationale — *(tweets 3-4)*.

## Entities introduced or touched
- [[jotaro-seo]] — author; presents this as educational, not as a recommendation.

## Concepts introduced or updated
- [[black-hat-seo]] — (create) techniques that violate Google guidelines.
- [[cloaking]] — (create as sub-concept or merge into black-hat-seo).

## Connections / contradictions
- Counterpart to [[image-seo]]: cloaking for media is a workaround for what proper ALT tags / structured data should solve.
- Related to [[google-bots]]: understanding how bots identify themselves via User-Agent is the prerequisite for cloaking.

## Open questions
- How reliably does Google detect cloaking in 2024? (No data given in thread.)
