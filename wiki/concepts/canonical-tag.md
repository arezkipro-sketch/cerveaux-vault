---
type: concept
title: "Balise Canonique (Canonical Tag)"
slug: canonical-tag
tags: [seo, technical-seo, duplicate-content, on-page]
sources: ["[[jotaro-seo-canonical-tag]]", "[[audreytips-fiche-produit-seo-ia]]"]
source_count: 2
status: active
updated: 2026-07-22
note: "MAJ 2026-07-22 : cas Shopify policies/pages dupliquées, harnais-chien-expert.fr."
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

## Cas Shopify : pages légales dupliquées `/policies/*` vs `/pages/*`

Piège spécifique à Shopify, détecté via un audit [[ubersuggest]] (`have_title_duplicates`) sur harnais-chien-expert.fr (2026-07-22) : Shopify génère automatiquement des pages système à `/policies/{handle}` (confidentialité, CGV, mentions légales, livraison, remboursement...) à partir des réglages légaux de la boutique — **en plus** de toute page `/pages/*` équivalente créée manuellement par le marchand avec le même contenu. Les deux versions coexistent, indexables, avec des titres identiques → duplicate content classique.

**Piège dans le mapping** : ne pas assumer une correspondance 1-pour-1 évidente entre les deux jeux de pages. Sur ce site, deux pages `/pages/livraison-*` existaient (une page "de préparation" au contenu resté provisoire/non mis à jour, une page réellement à jour) — le canonical devait pointer vers la page à jour, pas la première trouvée par similarité de nom. Toujours comparer le **contenu réel** (dates de mise à jour, présence de texte placeholder du type "à compléter") avant de choisir la cible canonique, pas juste le nom du handle.

**Solution appliquée** : ajout d'un bloc conditionnel dans `layout/theme.liquid` (basé sur `request.path`, pas sur un objet `policy.handle` — plus fiable car ne dépend pas de la disponibilité de cet objet dans le contexte Liquid) qui surcharge `canonical_url` uniquement sur les 6 chemins `/policies/*` concernés, pointant chacun vers son équivalent `/pages/*`. Les pages sans équivalent clair (ex: "Terms of service" générique sans page CGV réellement dédiée) sont laissées sans surcharge — mieux vaut une page auto-canonique que forcer un mapping approximatif.

## Sources
- [[jotaro-seo-canonical-tag]] — full guide: problem, syntax, implementation, verification.
- [[audreytips-fiche-produit-seo-ia]] — canonique pour gestion des variantes produit e-commerce (signal de priorité).
- Usage réel session 2026-07-22 sur harnais-chien-expert.fr (pas de source `raw/` — cas Shopify /policies/* vs /pages/*, via [[ubersuggest]] et l'API Shopify Admin).
