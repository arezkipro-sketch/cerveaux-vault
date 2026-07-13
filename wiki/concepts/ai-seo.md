---
type: concept
title: AI SEO (Generative Engine Optimization)
slug: ai-seo
tags:
  - seo
  - ai
  - chatgpt
  - claude
  - gemini
  - geo
  - french
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[alexgroberman-62pct-beyond-top10]]"
  - "[[alexgroberman-page1-vs-ai-citation]]"
  - "[[alexgroberman-citation-absorption]]"
  - "[[alexgroberman-ai-generated-citations]]"
  - "[[jespernissenseo-ai-traffic-stats]]"
  - "[[irentdumpsters-google-ai-guide]]"
  - "[[semrush-ai-seo-traffic-study]]"
  - "[[semrush-ai-visibility-study-findings]]"
  - "[[semrush-ai-stats-2026]]"
  - "[[semrush-optimize-ai-2026]]"
  - "[[semrush-rank-in-ai-search]]"
  - "[[semrush-traditional-vs-ai-seo]]"
  - "[[semrush-ai-referral-traffic]]"
source_count: 14
status: active
updated: 2026-06-15
---

# AI SEO (Generative Engine Optimization)

**Definition:** The practice of optimizing web content to be cited, referenced, or recommended by AI systems (ChatGPT, Claude, Gemini, Google AI Overviews), as distinct from traditional Google ranking optimization. Also called GEO (Generative Engine Optimization).

## What we know
- Google SEO and AI citation are two distinct games: only **13.7 % overlap** in sources cited by Google AI Mode vs. AI Overviews — winning one doesn't guarantee winning the other → [[jotaro-seo-ia-x-seo]].
- **28.3 % of pages most cited by ChatGPT have zero organic Google visibility** — AI citation and search ranking operate on different signals → [[jotaro-seo-ia-x-seo]].
- AI crawlers (ChatGPT, etc.) visit dozens of pages per query but cite only ~50 % of them — being crawlable is necessary but insufficient → [[jotaro-seo-ia-x-seo]].
- LLM trust signals overlap with Google's [[e-e-a-t]] but are applied directly to content (an LLM reads and evaluates your text, not just external signals) → [[jotaro-seo-ia-x-seo]].
- **Key AI trust signals**: frequency of cross-site citation, [[topical-authority]] depth, content structure (extractability), and multi-platform presence → [[jotaro-seo-ia-x-seo]].
- **67 % of top ChatGPT citations** are uncontrollable sources (Wikipedia 29.7 %, homepages 23.8 %, app stores 6.6 %) — actionable territory is the remaining ~33 % → [[jotaro-seo-ia-x-seo]].

## The 7 AI SEO levers (ranked by impact)
1. **[[topical-authority]]** — consistent, comprehensive coverage of a subject domain.
2. **"Best X" list content** — 43.8 % of all ChatGPT citations come from this format → [[jotaro-seo-ia-x-seo]].
3. **Factual density** — precise, verifiable data points > well-written generalities; answer the question in the first 1–3 sentences under each heading.
4. **YouTube presence** — highest correlation with AI brand visibility: **0.737** → [[jotaro-seo-ia-x-seo]].
5. **[[llm-txt]]** — signal file at `/llm.txt` for AI crawlers.
6. **Informational intent focus** — 99.9 % of AI Overviews trigger on informational queries; target content mix: 70 % informational / 20 % commercial-hybrid / 10 % transactional → [[jotaro-seo-ia-x-seo]].
7. **[[e-e-a-t]]** — demonstrated expertise via real examples, named authors, cited sources, and clear positions on contested topics.

## Relations
- Extends [[e-e-a-t]]: same principles, now enforced by LLMs reading content directly.
- Reinforces [[topical-authority]] and [[cocon-semantique]]: deep thematic coverage remains the foundation.
- Introduces a new form of [[link-juice]]: off-site brand mentions (YouTube, forums, podcasts) function like links in building AI trust.
- Managed partly by [[llm-txt]] and [[ai-overviews]].

## AI Visibility: The 2-Layer Model

Classic SEO rank and AI citation are increasingly decoupled:
- **62 %** of AI Overview citations go to pages NOT in the organic top 10 → [[alexgroberman-62pct-beyond-top10]].
- **30 %** of AIO-cited domains not in first-page organic results (55,393 searches) → [[alexgroberman-page1-vs-ai-citation]].
- **Root cause — Google Gemini 3 sub-query decomposition**: Google AI decomposes "best CRM for small business" into internal sub-queries ("CRM onboarding comparison", "CRM pricing <10 people"), then sources each sub-query independently → [[alexgroberman-62pct-beyond-top10]].
- **Implication**: need 40-60 pages per category covering every buyer sub-question to capture the 62 % of AI citations outside top-10 → [[topical-authority]].

**2 layers required for AI visibility** → [[alexgroberman-page1-vs-ai-citation]]:
1. Traditional SEO eligibility + domain authority (baseline, still required).
2. Specific, extractable content directly answering the sub-question AI is sourcing.

## Citation Selection vs Citation Absorption

Two levels of AI visibility — being cited ≠ being influential → [[citation-absorption]]:
- **Citation selection**: URL appears in AI source list.
- **Citation absorption**: page content actually shapes the generated response body.

High-absorption content types (lift vs. pages without): code +76.88 %, stats +61.55 %, definitions +57.33 %, comparisons +55.28 %, how-to +41.20 % → [[alexgroberman-citation-absorption]].

### Platform traffic share (source: SE Ranking study)
- **ChatGPT**: 78.22 % of all AI-referred web traffic → [[jespernissenseo-ai-traffic-stats]].
- Perplexity: 9.33 %, Gemini: 6.85 %.
- AI platforms = 0.33 % of global web traffic total (doubled YoY) → [[jespernissenseo-ai-traffic-stats]].
- ChatGPT also has highest per-citation influence score (0.2713 vs. 0.0646 Perplexity) → ChatGPT = highest-priority platform → [[alexgroberman-citation-absorption]].

## Semrush research cluster (AI traffic + visibility)

### AI traffic projections
- LLM visitor value = **4.4× traditional organic** (conversion basis) → [[semrush-ai-seo-traffic-study]].
- AI traffic projected to surpass traditional organic by **early 2028** → [[semrush-ai-seo-traffic-study]].
- AI-referred traffic currently growing at **527 % YoY** → [[semrush-ai-stats-2026]].
- 60 % of AI-sourced sessions are **zero-click** (users get answer without visiting) → [[semrush-ai-stats-2026]].

### Platform dominance (July 2025 data)
- **ChatGPT: 85.79 %** of all AI platform visits (chatgpt.com alone: 5.24B monthly visits) → [[semrush-ai-referral-traffic]].
- Gemini: 4.70 %, Perplexity: 2.84 %, Grok: 2.50 %, Claude: 2.23 % → [[semrush-ai-referral-traffic]].
- Note: SE Ranking study (earlier) measured ChatGPT at 78.22 % of AI-REFERRED traffic — different denominator → [[jespernissenseo-ai-traffic-stats]].

### Community content > brand content for AI citations
- **Reddit cited in 176 % of ChatGPT financial queries** (near-twice per query on average) → [[semrush-ai-visibility-study-findings]].
- Wikipedia is top source in 4 out of 5 sectors → [[semrush-ai-visibility-study-findings]].
- Brand marketing pages rarely cited. Community/independent sources dominate → [[semrush-ai-visibility-study-findings]].
- Implication: brand presence on Reddit, Wikipedia, industry forums = AI citation lever you don't fully control but can seed.

### Semantic cooccurrence (new signal)
- LLMs rely on cooccurrence patterns from training data: terms frequently appearing together get associated.
- Brand name + target topic appearing repeatedly across multiple sources → AI associates them.
- Example: "Monday.com" near "workflow automation" across many articles → AI cites Monday.com for workflow queries.
- Actionable: PR, guest posts, and community mentions in topic-relevant contexts → [[semrush-optimize-ai-2026]].

### Content freshness signal
- **90 % of AI-cited content** was updated within the last 3 years → [[semrush-rank-in-ai-search]].
- Only 6 % of AI-cited content is older than 6 years → [[semrush-rank-in-ai-search]].
- Regular updates (stats, examples, screenshots) matter for AI citation eligibility.

### Prompt research vs keyword research
- Traditional keywords avg **4 words**. AI prompts avg **8 words** — 2× longer and more specific → [[semrush-traditional-vs-ai-seo]].
- AI sub-query decomposition ("query fan-out") makes topical breadth even more critical → [[topical-authority]].

## Google's official AI Overviews ranking guidance
- AI optimization IS SEO — same Google systems → [[irentdumpsters-google-ai-guide]].
- Experience-first content (not generic "best of") → [[e-e-a-t]].
- **"Scaled content abuse"**: new Google term for mass keyword-variation content farming → penalty risk.
- GBP content surfaces in AI responses for local queries → [[google-business-profile]].
- AI agents beginning to read DOM and accessibility trees — structural HTML = future AI citability factor.

## Tensions / open questions
- Does LLM.txt materially impact citation rates? (Author skeptical — *(unsourced beyond thread)*)
- Causal direction of YouTube correlation: does YouTube cause AI visibility, or does underlying brand authority cause both?
- How fast do LLM citation patterns update after new content is published?
- FAQ format: improves traditional SEO (featured snippets, PAA) but does NOT correlate with higher AI absorption → [[citation-absorption]]. Which to prioritize?

## Sources
- [[jotaro-seo-ia-x-seo]] — Ahrefs 1B+ data point study synthesis; 7 concrete strategies.
- [[alexgroberman-62pct-beyond-top10]] — Ahrefs 863K SERPs; 62 % AIO citations outside top-10; sub-query decomposition.
- [[alexgroberman-page1-vs-ai-citation]] — 55,393 searches; page-1 rank ≠ AI citation; 2-layer model.
- [[alexgroberman-citation-absorption]] — citation selection vs. absorption; content type influence lifts.
- [[alexgroberman-ai-generated-citations]] — ~16 % AI-cited sources are AI-generated; unique data = differentiator.
- [[jespernissenseo-ai-traffic-stats]] — ChatGPT 78 % AI traffic share; AI = 0.33 % global web traffic.
- [[irentdumpsters-google-ai-guide]] — Google official: AI optimization = SEO; scaled content abuse; GBP in AI.
- [[semrush-ai-seo-traffic-study]] — LLM visitor 4.4× conversion value; AI surpasses organic by 2028.
- [[semrush-ai-visibility-study-findings]] — community content > brand; Reddit 176 % per query; Wikipedia dominates.
- [[semrush-ai-stats-2026]] — 527 % YoY growth; ChatGPT 700M WAU; 60 % zero-click.
- [[semrush-optimize-ai-2026]] — 7-step checklist; semantic cooccurrence; definition→detail→example pattern.
- [[semrush-rank-in-ai-search]] — 6 tactics; 90 % AI-cited content ≤3 years old; brand authority predicts AI mentions.
- [[semrush-traditional-vs-ai-seo]] — task mapping table; prompt avg 8 words; unlinked mentions count.
- [[semrush-ai-referral-traffic]] — ChatGPT 85.79 % platform visits; GA4 tracking regex method.
