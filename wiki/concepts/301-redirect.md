---
type: concept
title: "Redirection 301 (Permanent Redirect)"
slug: 301-redirect
tags: [seo, technical-seo, http, link-building]
sources: ["[[jotaro-seo-301-redirects]]", "[[jotaro-seo-http-errors]]"]
source_count: 2
status: active
updated: 2026-06-15
---

# Redirection 301 (Permanent Redirect)

**Definition:** An HTTP 301 status code that signals to browsers and search engines that a page has been permanently moved to a new URL. It transfers most of the [[link-juice]] and SERP ranking signals from the old URL to the new one.

## What we know
- **How it works**: any request to the old URL is automatically redirected to the new URL. Search engines update their index to use the new URL → [[jotaro-seo-301-redirects]].
- **Link juice transfer**: the primary SEO benefit. All inbound links to the old URL pass their authority to the new URL via the 301 → [[jotaro-seo-301-redirects]].
- **Without 301**: moved page loses all its ranking, traffic, and SERP visibility. Inbound links become dead weight → [[jotaro-seo-301-redirects]].
- **When to use**: URL structure changes, domain migration, page mergers, site refactoring, language/locale restructuring → [[jotaro-seo-301-redirects]].
- **Avoid overusing**: each 301 loses a small % of link juice. Redirect chains (A→B→C) compound the loss. Don't add redirects blindly or without auditing the chain → [[jotaro-seo-301-redirects]].
- **User experience**: visitors are sent automatically to the new URL, avoiding 404 frustration → [[jotaro-seo-301-redirects]].
- Technical audit always includes: "correct 404s with 301 redirects" — [[jotaro-seo-4-months-textile]], [[jotaro-seo-http-errors]].

## Relations
- Preserves [[link-juice]]: the main reason 301s are preferred over simply removing old pages.
- Fixes [[http-status-codes-seo]] problems: 301 is the proper resolution for pages that have moved.
- Maintains [[maillage-interne]]: when internal links point to old URLs, they should be updated to new URLs OR 301s should cover the chain.

## Tensions / open questions
- What exact % of link juice is lost per 301 redirect? (Google claims ~100% but practitioners observe variability — not sourced here.)
- 302 (temporary redirect) vs. 301: 302 doesn't transfer link juice, used for A/B tests or temporary moves.

## Sources
- [[jotaro-seo-301-redirects]] — full explainer: definition, benefits, when to use, risks of chains.
- [[jotaro-seo-http-errors]] — 301 as the technical remedy for moved pages.
