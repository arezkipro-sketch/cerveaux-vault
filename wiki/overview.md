---
title: Overview
page-type: topic
domain: knowledge-management
tags: [meta, overview]
related: ["[[llm-wiki-pattern]]", "[[persistent-wiki]]"]
---

# Overview — Vault Cerveaux

Point d'entrée du vault. Voir [[llm-wiki-pattern]] pour le pattern fondateur (Karpathy) et `CLAUDE.md` pour les règles opérationnelles.

## Thèse actuelle

Ce vault n'est pas un carnet de pensée brute (voice notes, journal) : c'est une **base de connaissance construite par ingestion de sources externes** (threads X, PDF, articles, guides) via le skill `ingest`. Chaque source produit une note dans `wiki/sources/`, qui alimente des pages `wiki/concepts/` et `wiki/entities/` réutilisables à travers domaines. Le but : ne jamais relire deux fois la même leçon, et pouvoir répondre "qu'est-ce que je sais déjà sur X" sans re-chercher.

**Stats (au 2026-07-07) :** 239 sources · 451 pages wiki.

## Domaines couverts

- **SEO** — technique, on-page, off-page, local, IA-search, e-commerce, méthode de classement, audit. Le domaine le plus dense (Semrush, Jotaro SEO, France Num, @alexgroberman AI-citation research).
- **GEO / AI Overviews** — optimisation pour citation par ChatGPT/Claude/Gemini/AI Overviews ; distinct du SEO classique mais chevauchant.
- **E-commerce Shopify** — performance Liquid, fiches produit, checklist 38 points.
- **E-commerce Meta Ads (RayEcom)** — méthode boutique de niche brandée : recherche produit → CBO testing → créatives → CRO.
- **Business halal** — conformité Bay' Salam, dropshipping halal, sourcing.
- **Copywriting & CRO** — L'Académie™, Jérémy Allard, Alex Cattoni/Copy Posse : frameworks, psychologie, structure de page.
- **Marketing & outils** — catalogue d'outils par fonction (recherche mots-clés, contenu, social, perf, ORM, competitive intel).
- **Branding** — architecture de marque, identité.
- **Email / Vidéo / Social** — email marketing, script vidéo, stratégie social.
- **Knowledge management** — le pattern du vault lui-même ([[llm-wiki-pattern]], [[persistent-wiki]]).
- **Création de site web (freelance)** — prospection Google Maps → build Claude Code → outreach → pricing.

## Comment naviguer

1. Chercher d'abord dans `index.md` (catalogue complet, à jour à chaque ingest).
2. Une page `concepts/` répond "qu'est-ce que c'est / comment on l'applique" ; une page `sources/` garde la trace complète d'une source précise ; une page `entities/` capitalise sur une personne/outil/organisation citée dans plusieurs sources.
3. Avant d'ingérer une nouvelle source, consulter [[llm-wiki-pattern]] et `CLAUDE.md` — en particulier la règle des backlinks obligatoires.

## Liens cassés connus (à corriger au prochain `maint`)

- Aucun autre repéré à ce stade — premier `maint` effectué le 2026-07-11 en même temps que la création de cette page.
