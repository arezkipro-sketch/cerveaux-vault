---
type: concept
title: "Black Hat SEO (Zone Noire du SEO)"
slug: black-hat-seo
tags: [seo, black-hat, link-building, risk]
sources: ["[[jotaro-seo-black-hat-cloaking]]", "[[jotaro-seo-pbn]]"]
source_count: 2
status: active
updated: 2026-06-15
---

# Black Hat SEO

**Definition:** SEO techniques that violate Google's Webmaster Guidelines to gain an artificial ranking advantage. Risk of manual or algorithmic penalties ranging from ranking drops to full deindexation of the site.

## What we know

### Cloaking ID
- **Mechanism**: detect visitor type via `User-Agent` HTTP header → serve text-heavy SEO content to Googlebot, visual/media-rich content to human users → [[jotaro-seo-black-hat-cloaking]].
- **Rationale given**: useful when site has media (video, audio, images) that Googlebots can't parse — bot gets text version, users get full experience → [[jotaro-seo-black-hat-cloaking]].
- **Risk**: Google detects inconsistencies between indexed content and live content → manual penalty or deindexation → [[jotaro-seo-black-hat-cloaking]].
- **White-hat alternative**: proper ALT attributes, transcripts, structured data (Schema) — see [[image-seo]].

### PBN (Private Blog Network)
- **Mechanism**: build/buy a network of sites (often on expired domains) in the same thematic → each satellite site links to the "site mère" → consolidates domain authority and TrustRank on the target → [[jotaro-seo-pbn]].
- **Expired domains**: preferred because they carry existing authority history; must be vetted for spam associations → [[jotaro-seo-pbn]].
- **Thematic consistency mandatory**: off-topic backlinks are worthless; all PBN sites must be in the target's niche → [[jotaro-seo-pbn]].
- **Risk**: Google explicitly targets PBN footprints. Detection = manual penalty or deindexation of target → [[jotaro-seo-pbn]].

## Relations
- Structural parallel: [[cocon-semantique]] (internal authority architecture) vs. PBN (external cross-domain authority manipulation) — both concentrate authority onto a target page, by different means.
- Shortcut for [[link-juice]] accumulation: PBN buys what organic backlinks take months/years to build.
- [[google-bots]] detection methods: Googlebot may use multiple User-Agent strings or IP ranges to detect cloaking.

## Tensions / open questions
- At what scale / sophistication does Google reliably detect PBNs? (Undocumented.)
- Is there a "gray hat" zone where these techniques are tolerated in competitive niches? (Author presents them as risky but not entirely condemning.)

## Sources
- [[jotaro-seo-black-hat-cloaking]] — cloaking ID: User-Agent manipulation.
- [[jotaro-seo-pbn]] — Private Blog Network: structure, implementation, risks.
