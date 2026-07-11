---
type: concept
title: "Google Bots (Googlebot / Crawlers)"
slug: google-bots
tags: [seo, technical-seo, crawling, indexation]
sources: ["[[jotaro-seo-google-bots]]", "[[crawl-budget-guide]]"]
source_count: 2
status: active
updated: 2026-06-18
---

# Google Bots (Googlebot / Crawlers)

**Definition:** Automated programs used by Google (also called Spiders or Crawlers) to systematically explore web pages, analyze their content, and add them to Google's index — the prerequisite for any SERP visibility.

## What we know
- **Mechanism**: Googlebots follow hyperlinks from page to page (including external links), collecting data on each: text, links, HTML tags, images, structure → [[jotaro-seo-google-bots]].
- **Why [[maillage-interne]] matters**: bots navigate via links. A page not linked from anywhere else = likely undiscovered = not indexed → [[jotaro-seo-google-bots]].
- **Categorization**: bots analyze keyword density and semantic consistency to categorize a site in Google's index (e.g., "Alimentation → Fruits frais → Fraises") → [[jotaro-seo-google-bots]].
- **Crawl frequency**: determined by site relevance and content update frequency. Sites publishing regularly = crawled more often → [[jotaro-seo-google-bots]].
- **[[crawl-budget]]**: limited resource Google allocates per site. Must be managed — wasteful pages (thin content, errors, duplicates) consume budget that should go to priority pages → [[jotaro-seo-google-bots]].
- **Image analysis**: Googlebots struggle with non-text media (video, audio, images without ALT). They rely on ALT attributes and surrounding text to understand images → [[jotaro-seo-black-hat-cloaking]], [[jotaro-seo-image-optimization]].

## Relations
- Depends on [[maillage-interne]] for navigation.
- Blocked/wasted by [[http-status-codes-seo]] errors (404, 5xx = crawl budget waste).
- Guided by [[robots-txt]] (white-hat) or deceived by cloaking (see [[black-hat-seo]]).
- Powers [[crawl-budget]] management; crawl rate responds to server [[ttfb]].

## Tensions / open questions
- How does Googlebot handle JavaScript-heavy SPAs? (Not addressed in source.)
- Does crawl frequency directly influence ranking speed, or just indexation speed?

## Sources
- [[jotaro-seo-google-bots]] — foundational explainer on crawlers, indexation, crawl frequency, crawl budget.
- [[crawl-budget-guide]] — Googlebot "follows every route"; crawl rate responds to server stability/TTFB; access control via robots.txt/noindex.
