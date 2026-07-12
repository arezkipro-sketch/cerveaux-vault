---
type: concept
title: "Link Juice (Jus de Lien)"
slug: link-juice
tags: [seo, link-building, authority]
sources: ["[[jotaro-seo-http-errors]]", "[[jotaro-seo-exact-match-domain]]"]
source_count: 2
status: active
updated: 2026-06-14
---

# Link Juice (Jus de Lien)

**Definition:** The credibility and authority value that a hyperlink passes from one page to another, influencing the linked page's search engine ranking. Also called "link equity." Lost when the destination page returns a 4xx error or the link is broken.

## What we know
- Defined explicitly in the HTTP errors thread: "la valeur de crédibilité et d'autorité qu'un lien d'une page web peut transmettre à une autre, influençant ainsi le classement" → [[jotaro-seo-http-errors]].
- **Broken by 404 errors**: if an inbound link points to a dead page, no juice is transferred — monitoring and 301-redirecting dead pages preserves this equity → [[jotaro-seo-http-errors]].
- **Domain-level signal**: a well-known or well-linked domain (e.g. G7 Taxi) accumulates link juice via brand longevity, allowing it to outrank EMD sites → [[jotaro-seo-exact-match-domain]].
- 301 redirect transmits most (but historically not 100%) of link juice from old URL to new URL → [[jotaro-seo-http-errors]].

## Relations
- Central to [[cocon-semantique]]: pages filles send link juice to the page mère.
- Preserved by fixing [[http-status-codes-seo]] errors.
- Partly why [[exact-match-domain]] strategy cares about domain authority.

## Tensions / open questions
- Exact percentage of link juice passed by 301 redirects (Google historically said ~100% but this has varied) — not sourced here.

## Sources
- [[jotaro-seo-http-errors]] — defines and explains link juice loss via 404s.
- [[jotaro-seo-exact-match-domain]] — domain-level link juice as authority signal.
