---
type: concept
title: "Balise Canonique (Canonical Tag)"
slug: canonical-tag
tags: [seo, technical-seo, duplicate-content, on-page]
sources: ["[[jotaro-seo-canonical-tag]]", "[[audreytips-fiche-produit-seo-ia]]"]
source_count: 2
status: active
updated: 2026-06-19
---

# Balise Canonique (Canonical Tag)

**Definition:** An HTML tag placed in a page's `<head>` that explicitly tells search engine crawlers which URL is the "primary" or "canonical" version of a page — used when similar or duplicate content exists across multiple URLs, preventing indexation confusion and ranking dilution.

## What we know
- **Syntax**: `<link rel="canonical" href="[canonical-URL]">` — placed in `<head>` → [[jotaro-seo-canonical-tag]].
- **Problem it solves**: similar pages (e.g., product variants like "tee-shirt blanc" vs "tee-shirt blanc à motif") confuse Googlebot — bot may index the wrong version, split ranking power, or fail to rank either page well → [[jotaro-seo-canonical-tag]].
- **Implementation** (no-code options): WordPress → Yoast SEO or Rank Math; Shopify → SEO Manager plugin → [[jotaro-seo-canonical-tag]].
- **Verification**: Chrome DevTools → right-click page → Inspect → find `<head>` → look for canonical tag. If missing or wrong → Search Console will flag it → [[jotaro-seo-canonical-tag]].
- **Not always required**: if two product pages are sufficiently distinct in content, canonicals aren't mandatory — Search Console notifies when there's a potential conflict → [[jotaro-seo-canonical-tag]].

## Relations
- Distinct from [[keyword-cannibalization]]: canonical fixes *content* duplication; cannibalization is about *keyword targeting* duplication. They can co-occur but have different roots and solutions.
- Related to [[http-status-codes-seo]]: both are signals to Googlebot about page priority/status.
- Connects to [[crawl-budget]]: duplicate content wastes crawl budget; canonicals direct bot attention to the right page.

## Tensions / open questions
- Does adding a canonical to a weaker page "recommend" the canonical URL but still allow the weaker page to be indexed? (Yes — canonical is a hint, not an enforcement.)
- Self-referencing canonicals (a page pointing to itself): best practice or noise?

## E-commerce : variantes produit
- Pour les variantes (taille/couleur), préférer **regrouper sur une fiche** via attributs/sélecteurs ; canonique = **signal de priorité, pas une solution de fond** (corriger d'abord le contenu si identique). Créer une page séparée seulement si l'intention de recherche diffère → [[audreytips-fiche-produit-seo-ia]], [[fiche-produit-seo]].

## Sources
- [[jotaro-seo-canonical-tag]] — full guide: problem, syntax, implementation, verification.
- [[audreytips-fiche-produit-seo-ia]] — canonique pour gestion des variantes produit e-commerce (signal de priorité).
