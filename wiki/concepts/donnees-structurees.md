---
type: concept
title: "Données structurées (Schema.org / JSON-LD)"
slug: donnees-structurees
tags: [seo, technical-seo, structured-data, schema-org, rich-snippets, e-commerce, ai-seo]
sources: ["[[audreytips-fiche-produit-seo-ia]]", "[[noiise-fiches-produits-seo]]", "[[francenum-guide-debutant-seo]]"]
source_count: 3
status: active
updated: 2026-06-19
---

# Données structurées (Schema.org / JSON-LD)

**Definition:** Balisage standardisé (vocabulaire **Schema.org**, format recommandé **JSON-LD**) ajouté au code d'une page pour décrire explicitement son contenu aux moteurs. Permet d'obtenir des **extraits enrichis (rich snippets)**, d'augmenter impressions/CTR, et d'aider Google **et les moteurs IA** à interpréter précisément la page.

## What we know
- Facilitent la compréhension du contenu → **rich snippets**, +impressions, +CTR → [[noiise-fiches-produits-seo]].
- **Types clés pour une fiche produit** → [[audreytips-fiche-produit-seo-ia]] :
  - **Product** + **Offer** : nom, prix, disponibilité (informations clés).
  - **AggregateRating** (si données fiables) : afficher les avis dans la SERP → crédibilité.
  - **BreadcrumbList** : hiérarchie du site / fil d'Ariane → navigation + compréhension.
- **Cohérence obligatoire** : les données balisées (prix, stock) doivent correspondre à l'affichage de la page. « Une donnée incohérente est ignorée, une donnée fiable est exploitée. » → [[audreytips-fiche-produit-seo-ia]].
- Implémentation possible via JSON-LD (placeholders name/url/price/priceCurrency/availability/sku/brand/image dans le prompt Gemini d'AudreyTips).
- Recommandé dès le guide débutant TPE/PME (Schema.org produit) → [[francenum-guide-debutant-seo]].

## Relations
- Composant essentiel de la [[fiche-produit-seo]] (1 des 4 : snippet / visuels / **données structurées** / contenu).
- Aide les moteurs IA à extraire les **entités** → [[ai-seo]], [[aeo]] (la FAQ structurée capte les requêtes conversationnelles).
- Distinct de la [[meta-description]] *(TODO)* et du [[canonical-tag]] : tous des signaux à Google, mais rôles différents (interprétation vs CTR vs priorité d'URL).
- Renforce [[e-e-a-t]] (avis fiables affichés).

## Tensions / open questions
- Les rich snippets ne sont pas garantis : Google décide de l'affichage.
- Poids exact en SEO « classique » vs gain réel en visibilité IA non chiffré par les sources.
- Page créée le 2026-06-19 pour combler un trou identifié lors de l'ingestion des sources fiche produit ; à enrichir avec une source dédiée Schema.org / Google Search Central.

## Sources
- [[audreytips-fiche-produit-seo-ia]] — Product/Offer/AggregateRating/BreadcrumbList, JSON-LD, cohérence des données.
- [[noiise-fiches-produits-seo]] — rich snippets, +impressions/CTR sur fiche produit.
- [[francenum-guide-debutant-seo]] — Schema.org produit recommandé aux TPE/PME.
