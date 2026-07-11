---
type: concept
title: "SEO Audit"
slug: seo-audit
tags: [seo, audit, technical-seo, strategy]
sources: ["[[jotaro-seo-4-months-textile]]", "[[jotaro-seo-strategy-broke-abroad]]", "[[jotaro-seo-6000-toys-case-study]]", "[[semrush-seo-checklist-41]]", "[[jotaro-seo-audit-simplifie]]"]
source_count: 5
status: active
updated: 2026-06-27
note: enrichi avec sections Analytics/GSC et Off-page (2026-06-27)
---

# SEO Audit

**Definition:** A structured review of a website's SEO health across multiple dimensions — the diagnostic step before building (or correcting) a strategy. Identifies what's blocking rankings, what's working, and what to prioritize.

## What we know

### JotaroSeo's 3-type audit framework (for client sites)

1. **Audit interne** — on-page: content quality, keyword targeting, internal linking structure, H1/title/meta tags, cannibalisation.
2. **Audit externe** — off-page: backlink profile, authority, toxicity.
3. **Audit technique** — crawlability, indexation, site speed, mobile-friendliness, HTTPS, redirect chains.

→ Typically run in this order; technical issues are blocking and must be fixed first → [[jotaro-seo-4-months-textile]], [[jotaro-seo-strategy-broke-abroad]]

### Semrush checklist approach (5-section operational checklist)

The 41-point checklist covers the same 3 domains reorganized as:

**Bases (setup):** GSC + Bing WMT + GA4 + sitemap + robots.txt + manual actions + indexability check.

**Technical checks:** HTTPS, canonical domain, crawl errors, site speed/CWV, broken links, HTTP→HTTPS links, mobile-friendliness, URL structure, Schema.org, page depth ≤3 clicks, 302→301 corrections, redirect chains/loops.

**On-page checks:** Duplicate/missing/truncated title tags (≤60 chars), meta descriptions, duplicate H1, keyword optimization via GSC (high impressions / low CTR), content audit, image alt tags, internal linking, keyword cannibalization, orphan pages, content freshness.

**Off-page checks:** Competitor backlink profiles, link gap analysis, unlinked brand mentions, new link-building opportunities, Google Business Profile.

→ [[semrush-seo-checklist-41]]

### Analytics & Mesure (dimension absente des audits Jotaro simplifié)

**Setup obligatoire avant tout audit :**
- Google Search Console connectée + sitemap.xml soumis
- Bing Webmaster Tools configuré + sitemap soumis (→ indexation ChatGPT via Bing)
- GA4 installé et données remontées correctement

**Ce qu'on cherche dans GSC :**
- Mots-clés avec **impressions élevées + CTR faible** → title/meta à optimiser en priorité
- Pages avec **position 4–15** → quick wins (un push de contenu peut les faire passer page 1)
- Pages **indexées mais non cliquées** → problème de title/meta ou de pertinence
- **Erreurs d'indexation** (pages bloquées par robots.txt, noindex accidentel, soft 404)

**Ce qu'on suit dans GA4 :**
- Trafic organique vs autres canaux
- Taux de rebond par page clé
- Pages qui convertissent vs pages qui n'amènent pas de trafic

→ [[semrush-seo-checklist-41]]

### Off-page — Analyse du profil backlinks

**Outils :** Semrush, Ahrefs, Ubersuggest, Moz

**Ce qu'on cherche :**
- **Domain Authority / Domain Rating** — niveau d'autorité global du site
- **Liens toxiques** → identifier et désavouer via GSC si nécessaire
- **Gap analysis** — backlinks des concurrents absents chez soi = opportunités
- **Mentions de marque sans lien** → contacter l'auteur pour réclamer le lien (easy win)
- **Profil d'ancres** — diversité des ancres (exact match / brand / générique)

→ [[backlinks]], [[off-page-seo]]

## Key operational rules

- **Page depth ≤ 3 clicks** from the home page — deeper = reduced crawl probability.
- **1 H1 per page** containing the primary keyword.
- **Title tags ≤ ~60 characters** to avoid truncation in SERPs.
- **Orphan pages** (zero internal links) = invisible to Google except via sitemap/backlinks.
- **Redirect chains** (A→B→C) must be collapsed to direct redirects (A→C).
- **302 temporaires** used instead of 301 permanents = correct when genuine; convert to 301 when the redirect is permanent.
- **GSC impressions > 100 + CTR < 2%** = title/meta sous-optimisés — intervenir en priorité.
- **Position 4–15** = quick win — enrichir le contenu + améliorer le maillage interne vers cette page.
- **Mentions sans lien** = backlinks potentiels gratuits — les repérer avec Semrush "Brand Monitoring".

## Relations
- Operationalized by [[seo-roadmap]] (what to fix, when, by whom).
- Detects [[keyword-cannibalization]], [[maillage-interne]] gaps, [[301-redirect]] issues.
- Technical layer feeds into [[crawl-budget]], [[robots-txt]], [[xml-sitemap]], [[core-web-vitals]].
- On-page layer feeds into [[article-structure]], [[keyword-mapping]], [[content-pruning]].
- Off-page layer feeds into [[backlinks]], [[off-page-seo]], [[google-business-profile]].

### Jotaro — Format audit simplifié en 5 zones (thread X, 2026-05-22)

Format arborescence immédiatement applicable, orienté e-commerce :

| Zone | Points clés |
|---|---|
| **Zones chaudes** | H1 unique + mot-clé, H2/H3 cohérents, pas de H2/H3 footer, title <60 car., meta 120-155 car., gras sémantique |
| **Contenu** | >1 500 mots, FAQ sujet précis, intro directe (pyramide inversée), champ lexical topical |
| **Collections** | Description riche, 3-4 H2 thématiques, FAQ dans la description |
| **Fiches produit** | Zone flottaison complète, 2 liens internes min., images WebP <150 Ko |
| **Technique** | Sitemap XML dans GSC, plan de site HTML (footer), lien blog footer, budget crawl préservé |

→ [[jotaro-seo-audit-simplifie]]

## Sources
- [[jotaro-seo-4-months-textile]] — 3-type audit framework (interne/externe/technique) applied in textile brand case study.
- [[jotaro-seo-strategy-broke-abroad]] — 3-type audit applied in travel agency case study.
- [[jotaro-seo-6000-toys-case-study]] — audit as starting point for toy e-commerce growth.
- [[semrush-seo-checklist-41]] — 41-point operational checklist covering the full audit scope; actionable by domain.
- [[jotaro-seo-audit-simplifie]] — checklist 5 zones format simplifié (thread X 2026-05-22).
