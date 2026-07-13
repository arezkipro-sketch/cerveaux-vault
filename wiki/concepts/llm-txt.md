---
type: concept
title: LLM.txt
slug: llm-txt
tags:
  - seo
  - ai-seo
  - technical-seo
  - crawling
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[semrush-llms-txt-guide]]"
  - "[[llms-txt]]"
source_count: 3
status: active
updated: 2026-06-19
---

# LLM.txt

**Definition:** A plain-text file placed at the root of a domain (`/llm.txt`) that communicates structured metadata to AI crawlers — equivalent to `robots.txt` but for LLMs rather than traditional search bots. Signals site identity, important pages, thematic positioning, and citation preferences.

## What we know
- Placed at `[domain]/llm.txt` — AI crawlers read it during indexation → [[jotaro-seo-ia-x-seo]].
- Recommended content: company description (one precise sentence), list of most important URLs, thematic positioning (subjects of authority), citation instructions, links to primary data sources → [[jotaro-seo-ia-x-seo]].
- Implementation effort: ~30 minutes → [[jotaro-seo-ia-x-seo]].
- **Author's assessment**: "un peu bullshit" — direct citation impact not yet documented definitively, but adoption by advanced sites creates a structuring signal → [[jotaro-seo-ia-x-seo]].
- Google has communicated about it; still early-adoption phase as of 2026-06-09 → [[jotaro-seo-ia-x-seo]].

## NP Digital perspective (the bullish camp)
- Framed as **"piloting tool, not mass blocking"**: steer AI to strategic content; prioritize > exclude → [[llms-txt]].
- **Blocking ≠ disappearing** — it's leaving the LLM's field of view: blocked pages aren't analyzed/cited and stop feeding your expertise signal. You can rank on Google yet be invisible in AI answers. **Risk = oblivion, not penalty.** Block legal/obsolete/low-value pages, never pillar content → [[llms-txt]].
- **Bridge** between SEO and [[generative-engine-optimization]]; amplifies (doesn't replace) good SEO → [[llms-txt]].
- **When to use:** expert/educational content, controlling how the brand is cited, competitive niches, future-proofing → [[llms-txt]].
- **Content tips that actually matter** (more than syntax): dense context (one idea/section), answer-importance hierarchy ([[aeo]]), explicit tone of voice, **entity mapping** (LLMs reason in entities → reinforces [[e-e-a-t]]) → [[llms-txt]].

## Relations
- Part of the [[ai-seo]] technical checklist; complements [[robots-txt]] (crawl) and [[generative-engine-optimization]] (citation).
- Analogous to `robots.txt` in classic [[technical-seo]] *(TODO: create page)*.

## Semrush/NerdyData data (July 2025)
- **951 domains** using llms.txt as of July 2025 (NerdyData) — tiny fraction of the web → [[semrush-llms-txt-guide]].
- **Google's John Mueller** confirmed on Bluesky: *"For info, no AI system currently uses llms.txt."* → [[semrush-llms-txt-guide]].
- OpenAI, Google, Anthropic: NO official announcement they follow these files.
- Anthropic has llms.txt on their own site → possibly signals future openness.
- Early adopters: Hugging Face, Vercel, Zapier, Cal.com — all documentation-heavy dev tools.
- Correct filename: `llms.txt` (plural) at domain root → older wiki used `llm.txt` (singular) based on early source.

## File structure
```markdown
# Company Name
> Brief description

## Products
- [Product 1](https://example.com/product-1): Description
- [Product 2](https://example.com/product-2): Description

## Blog
- [Article title](https://example.com/post): What it covers
```

## Tensions / open questions
- **Confidence split:** NP Digital ([[llms-txt]]) calls it a "strategic lever"; John Mueller (via [[semrush-llms-txt-guide]]) says "no AI system currently uses llms.txt"; Jotaro ([[jotaro-seo-ia-x-seo]]) calls it "un peu bullshit." Same file, opposite confidence → forward-bet, not proven.
- Does LLMs.txt actually improve citation rates? No controlled evidence.
- Correct slug: **llms.txt** (plural) is the standard; this wiki page uses `llm-txt` as slug for historical continuity.

## Sources
- [[jotaro-seo-ia-x-seo]] — introduces the concept, recommends implementation despite personal skepticism.
- [[semrush-llms-txt-guide]] — adoption data; John Mueller quote; brand examples; step-by-step implementation.
- [[llms-txt]] — NP Digital "strategic lever" framing; piloting-not-blocking; when-to-use; content-structuring tips (dense context, entity mapping).
