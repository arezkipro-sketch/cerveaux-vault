---
type: source
title: "Trafic de référence IA : suivi, mesure, croissance (Semrush)"
slug: semrush-ai-referral-traffic
raw: "[[raw/assets/Comment suivre, mesurer et augmenter le trafic de référence IA.md]]"
source_url: "https://fr.semrush.com/blog/ai-referral-traffic/"
source_type: article
author: "[[semrush]]"
date_published: 2025-05-13
date_ingested: 2026-06-15
tags: [seo, ai-seo, traffic-data, analytics, chatgpt]
status: active
---

# AI Referral Traffic: Track & Grow — Summary

**One-liner:** Semrush guide on AI referral traffic: ChatGPT drives 85.79 % of all AI platform visits (July 2025), but AI traffic is often misattributed as "direct" in GA4 — fix with a regex filter. AI citations don't always produce immediate clicks; use brand search monitoring as a proxy.

## Key takeaways

### AI platform traffic shares (Semrush data, July 2025)
| Platform | Monthly visits | Traffic share |
|---|---|---|
| chatgpt.com | 5,244,855,278 | **85.79 %** |
| gemini.google.com | 287,535,861 | 4.70 % |
| perplexity.ai | 173,581,751 | 2.84 % |
| grok.com | 153,011,519 | 2.50 % |
| claude.ai | 136,577,834 | 2.23 % |
| copilot.microsoft.com | 97,802,733 | 1.60 % |
| meta.ai | 16,599,298 | 0.27 % |

→ ChatGPT = **85.79 %** of AI platform visits — more dominant than [[jespernissenseo-ai-traffic-stats]] (78 % figure, which measured only AI-referred traffic, not total platform visits).

### Why GA4 underreports AI traffic
- Many AI platforms do NOT pass referrer headers → clicks show as "Direct" in GA4.
- **You're receiving more AI traffic than your reports show.**
- AI mention → user searches brand name directly (not attributed to AI).
- AI mention → user visits later from different device (cross-device attribution gap).

### How to track AI referral traffic in GA4
- Go to Reports → Acquisition → Traffic Acquisition.
- Add filter: Dimension = Session source/medium, Type = matches regex.
- Value:
```
.*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com).*
```
- Add "Landing Page + query string" breakdown to see which pages attract AI referrals.

### AI citation → indirect traffic
- Direct click is not the only outcome. AI mention → brand awareness → direct search → subsequent visit.
- Track: branded search volume trends over time. Increase in branded searches = AI visibility signal.

## Connections
- Updates [[jespernissenseo-ai-traffic-stats]]: 85.79 % is more current/precise than the 78 % figure (different measurement methodology — platform visits vs. referred traffic share).
- Extends [[ai-seo]]: actionable tracking method now documented.
- ChatGPT dominance (85.79 %) reinforces [[citation-absorption]] finding: optimizing for ChatGPT absorption = highest leverage.
