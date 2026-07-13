---
type: concept
title: E-E-A-T (Experience, Expertise, Authority, Trust)
slug: e-e-a-t
tags:
  - seo
  - content-quality
  - google
  - ai-seo
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[irentdumpsters-google-ai-guide]]"
  - "[[alexgroberman-citation-absorption]]"
  - "[[search-everywhere-optimization]]"
  - "[[natural-net-geo-guide-2026]]"
  - "[[410-gone-premier-google-top3]]"
  - "[[jotaro-seo-strategie-ecommerce-2026]]"
source_count: 7
status: active
updated: 2026-06-19
---

# E-E-A-T (Experience, Expertise, Authority, Trust)

**Definition:** Google's framework for evaluating content quality: Experience (first-hand knowledge), Expertise (subject-matter depth), Authority (recognized standing in the field), and Trust (accuracy, transparency, verifiability). Originally a Google quality signal; now also applied by LLMs when deciding what content to cite.

## What we know
- Popularized by Google for evaluating page quality in organic ranking → [[jotaro-seo-ia-x-seo]].
- **LLM extension**: AI models apply the same underlying logic — they read content directly to assess whether the author genuinely knows the subject, rather than inferring it from external signals alone → [[jotaro-seo-ia-x-seo]].
- **Key difference from classic Google E-E-A-T**: Google can infer authority from backlinks and brand mentions; LLMs evaluate the content itself for signals of real expertise → [[jotaro-seo-ia-x-seo]].
- Practical signals for AI E-E-A-T: real-practice examples (not generic), clear positions on contested topics, named author + author page, explicitly cited studies and data → [[jotaro-seo-ia-x-seo]].
- Generic content that adds nothing new will be ignored; content demonstrating intimate domain knowledge (precise examples, nuances only a practitioner would know) is naturally favored → [[jotaro-seo-ia-x-seo]].

## Google's official E-E-A-T for AI Overviews (via [[irentdumpsters-google-ai-guide]])
- **"Write from experience"**: not generic "best of" lists. Personal/expert experience is what Google's AI favors → [[irentdumpsters-google-ai-guide]].
- **"Scaled content abuse"** (new Google term, 2026): mass-producing near-identical content targeting keyword variations. Now penalized. E-E-A-T antithesis → [[irentdumpsters-google-ai-guide]].
- Implication: each piece of content should add unique, experience-derived information — not variation on the same template.

## E-E-A-T signals for AI citation absorption
Content types correlated with higher AI citation influence — same properties that signal E-E-A-T:
- Code / technical demonstrations: +76.88 % absorption → [[alexgroberman-citation-absorption]].
- Numbers / statistics (original data): +61.55 % → [[alexgroberman-citation-absorption]].
- Definitions (authoritative): +57.33 % → [[alexgroberman-citation-absorption]].
- Comparisons (expert judgment): +55.28 % → [[alexgroberman-citation-absorption]].
- How-to (practical expertise): +41.20 % → [[alexgroberman-citation-absorption]].

## E-E-A-T « montré dans la page » (méthode 410-gone)
- E-E-A-T n'est **pas qu'une bio d'auteur** : il se démontre dans le contenu sur 4 niveaux → [[410-gone-premier-google-top3]] :
  - **Expérience** : vécu, cas, retours terrain, exemples.
  - **Expertise** : techniquement juste, précis, nuancé.
  - **Autorité** : d'autres sites/marques/sources vont dans votre sens.
  - **Fiabilité** : transparent, sourcé, à jour, sans promesses bullshit.
- Signaux qualité récurrents en haut de SERP : promesse explicite d'emblée, structure scannable, réponses aux objections (FAQ/cas limites), confiance (auteur/date/màj/sources). Le 2ᵉ étage du triptyque [[facteurs-de-classement]].
- Outil : auto-évaluation par scoring E-E-A-T avant publication (« mon contenu mérite-t-il la 1ère place ? »).

## Application e-commerce (JotaroSEO — étude de cas 394 849 €)

4 piliers traduits en signaux concrets pour une boutique e-commerce, et checklist article de blog en 7 points.

**E — Expérience (ajouté par Google en 2022) :**
- Avis clients réels et vérifiables (Trustpilot, Google Reviews)
- Photos authentiques du produit en situation réelle (pas visuels stock génériques)
- Descriptions basées sur usages concrets et retours clients réels
- Articles montrant connaissance terrain (ex : différence de confort entre courir à -5°C et à 0°C avec une cagoule mérinos)

**E — Expertise :**
- Profondeur réelle, pas des articles de 300 mots vides
- Vocabulaire expert du secteur (ex : mérinos 150g vs 200g, coefficient de respirabilité, couture plate)
- Couvrir les aspects que seul un vrai professionnel connaît

**A — Autorité :** backlinks depuis d'autres sites du secteur → voir [[backlinks]]

**T — Fiabilité (pilier le plus important selon Google) :**
- Site en HTTPS
- Mentions légales claires et complètes
- Page "À propos" présentant qui vous êtes vraiment
- Informations de contact facilement accessibles
- Descriptions produits honnêtes, sans promesses excessives
- Sources citées quand données ou chiffres avancés

### Checklist E-E-A-T pour chaque article de blog (7 points)

```
☐ L'introduction répond directement à la question posée dès les 2-3 premières phrases (Expérience + Fiabilité)
☐ Le contenu couvre le sujet en profondeur avec le vocabulaire expert (Expertise)
☐ Des exemples concrets issus du terrain ou de retours clients sont donnés (Expérience)
☐ Des liens vers des sources fiables si données ou chiffres cités (Fiabilité)
☐ Une FAQ avec des réponses autonomes est présente en fin d'article (Fiabilité)
☐ Des avis clients vérifiés sont accessibles depuis le site (Fiabilité)
☐ La page "À propos" est complète et crédible (Autorité)
```

→ [[jotaro-seo-strategie-ecommerce-2026]]

## The cross-platform constant
- [[search-everywhere-optimization]] names E-E-A-T as the one signal that works **everywhere** (not just Google) — the platform-agnostic foundation across search, social, AI, and marketplaces → [[search-everywhere-optimization]].

## Relations
- Foundational to [[ai-seo]] strategy (Stratégie 7).
- Closely linked to [[topical-authority]]: depth of coverage is how expertise manifests at site level.
- Supported structurally by [[cocon-semantique]]: comprehensive coverage signals expertise to both Google and LLMs.
- "Write from experience" directly opposes "scaled content abuse" → validates quality-over-quantity model.

## Tensions / open questions
- Does E-E-A-T for LLMs correlate with the same signals Google uses, or are the weights substantially different?
- How is "Experience" (first-hand knowledge) distinguishable from fabricated personal anecdotes in AI-generated content?
- At what content volume does site-wide scaling begin to trigger "scaled content abuse" signals?

## Sources
- [[jotaro-seo-ia-x-seo]] — frames E-E-A-T as the underlying logic of LLM citation trust; practical application guidance.
- [[irentdumpsters-google-ai-guide]] — Google official: "write from experience"; scaled content abuse penalty.
- [[alexgroberman-citation-absorption]] — quantifies absorption lift for each content type (code, stats, definitions, comparisons, how-to).
- [[search-everywhere-optimization]] — E-E-A-T as the cross-platform constant of the "new SEO".
- [[natural-net-geo-guide-2026]] — confirms E-E-A-T as pilier #2 du GEO : biographies auteurs, études citées, expérience terrain, backlinks de confiance.
- [[410-gone-premier-google-top3]] — E-E-A-T « montré dans la page » sur 4 niveaux + signaux qualité + auto-scoring ; 2ᵉ étage du triptyque de classement.
