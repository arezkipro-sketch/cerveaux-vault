---
type: concept
title: "GA4 — Setup Harnais Chien Expert"
slug: ga4-setup-harnais-chien
tags: [analytics, ga4, gsc, shopify, setup, harnais-chien]
sources: ["[[google-analytics-4]]", "[[semrush-connect-gsc-ga4]]", "[[semrush-ai-referral-traffic]]"]
status: active
updated: 2026-06-27
---

# GA4 — Setup Harnais Chien Expert

Mise en place de la mesure pour **harnais-chien-expert.fr** (store Shopify `0h9ahn-ix`).

## Identifiants
- **Propriété GA4 — ID de mesure : `G-HKQD7S24KJ`**
- Conteneur Google Tag Manager : `GTM-PC5RGDGP` (compte « Harnais chien ») — **non utilisé** (GTM ne traque pas le checkout Shopify ; on est passé en direct).

## Méthode d'installation
- Branché via le **canal Google & YouTube** de Shopify (et non un `gtag` dans `theme.liquid`, qui ne traque pas la page de paiement).
- Couvre automatiquement les événements e-commerce : `view_item`, `add_to_cart`, `begin_checkout`, `purchase`.
- Vérifié en **Temps réel** le 2026-06-27 = OK.
- Délai rapports standards : 24-48 h (le temps réel est immédiat).

## Socle mesure + indexation (cf. [[shopify-checklist-seo-38-2025]])
- [x] **GA4** installé (canal Google & YouTube) — `G-HKQD7S24KJ`
- [x] **Search Console** vérifié (2026-06-27)
- [ ] **Bing Webmaster Tools** : `bing.com/webmasters` → Importer depuis GSC (capte aussi le trafic ChatGPT/index Bing) — **PAS ENCORE FAIT**
- [x] **Sitemap soumis dans GSC** : `https://harnais-chien-expert.fr/sitemap.xml` (à refaire côté Bing après création)
- [x] **GSC ↔ GA4** lié + rapports Search Console publiés dans GA4

*Socle presque complet — reste Bing Webmaster + son sitemap (2026-06-27).*

## Langues
- **Néerlandais (`/nl/`) DÉPUBLIÉ le 2026-06-27** via API (`shopLocaleUpdate nl published:false`) — traductions conservées, réactivable.
  - Raison : version NL publiée par erreur → doublait les URLs du sitemap (~133 → ~267). hreflang était OK + traductions réelles, donc pas un pb SEO, mais store non gréé pour servir le marché NL.
  - Propagation : le `/nl/` et le sitemap se nettoient après rafraîchissement du cache CDN Shopify (qq minutes à qq heures). Resoumettre le sitemap dans GSC + Bing une fois à jour.

## À faire ensuite (optionnel)
- [ ] **Regex trafic IA** : segment ChatGPT/Perplexity/Gemini dans GA4 (cf. [[semrush-ai-referral-traffic]]).
- [ ] Vérifier que les achats (`purchase`) remontent après les premières ventes.

## Liens
- [[google-analytics-4]] · [[google-search-console]] · [[seo-roadmap]]
