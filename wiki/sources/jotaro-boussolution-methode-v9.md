---
title: "BOUSSOLUTION — Connaissance Jotaro Étendue v9"
slug: jotaro-boussolution-methode-v9
page-type: source-note
domain: seo
tags: [seo, jotaro, boussolution, methodology, aeo, netlinking, longue-traine, keyword-cannibalization, e-e-a-t, seo-audit, answerthepublic, cocon-semantique]
sources: []
related:
  - "[[jotaro-seo]]"
  - "[[jotaro-seo-content-strategy]]"
  - "[[jotaro-seo-strategie-ecommerce-2026]]"
  - "[[jotaro-seo-chatgpt-sales]]"
  - "[[aeo]]"
  - "[[longue-traine]]"
  - "[[keyword-cannibalization]]"
  - "[[cocon-semantique]]"
  - "[[maillage-interne]]"
  - "[[backlinks]]"
  - "[[e-e-a-t]]"
  - "[[seo-audit]]"
source-url: ""
source-type: document
author: "[[jotaro-seo]]"
date-published: 2026-04-25
date-accessed: 2026-06-25
raw-file: ""
---

# BOUSSOLUTION — Connaissance Jotaro Étendue v9

**One-liner :** Document de référence de la méthode Boussolution (agence JotaroSEO v9) — stack outils, focus AnswerThePublic, 17 principes philosophiques, 8 threads synthétisés, règles d'or Content/Netlinking/AEO, 3 types d'audit, patterns clients, glossaire.

## Overview

Document interne commun aux 8 Claude Projects Boussolution. Vise à donner à chaque "bot" de l'écosystème une connaissance unifiée de la méthode JotaroSEO. Contient les règles opérationnelles, les principes éditoriaux, les seuils et ratios issus de cas réels.

## Key Takeaways

### Stack outils agence

**Disponibles immédiatement :**
- AnswerThePublic (formule à vie) — longue traîne, questions, variantes, AEO
- GSC + GA4 (gratuit, à activer côté client)
- Scrappe SERP bookmarklet Jotaro — extraction top 10 Google
- Validator Schema.org + Google Rich Results Test
- Google Trends (saisonnalité)

**À recommander selon budget client :**

| Seuil | Outil | Prix |
|---|---|---|
| Client 600€+/mois | Semrush | ~120€/mois |
| Client 600€+/mois | Ahrefs | ~99€/mois |
| Client 500€+/mois | Majestic SEO | ~79€/mois |
| Budget serré | Ubersuggest Pro | 29€/mois |
| SEO local | BrightLocal / Moz Local | ~30€/mois |

### Focus AnswerThePublic

À partir d'un mot-clé, génère : questions (qui/quoi/comment/pourquoi/quand/où), prépositions (pour/avec/sans/vs), comparatifs, alphabet A-Z.

**Usage par bot :**
- **Bot Sémantique** : variantes, cocons sémantiques, longue traîne KD faible, effet tunnel
- **Bot Content** : liste Q à traiter, FAQ finale, H2/H3 sous forme de questions, 7 formats longue traîne
- **Bot IA Search** : FAQ → schema JSON-LD, prompts de test IA, PAA

**Limites** : pas de volumes précis, pas de KD, pas de données concurrentielles/backlinks → compléter avec Keyword Planner, Ubersuggest, Majestic/Ahrefs.

### 17 principes philosophiques Jotaro

Vision systémique · SXO > SEO pur · Vulgarisation systématique · Pragmatisme · Autonomisation client · Démonstration sur cas concret · Ton pragmatique + tutoiement · Toujours 2 solutions complémentaires · Vocabulaire FR accessible · Pédagogie en couches + résumés · Dédramatisation · Auto-citation entre bots · Dramatisation contrôlée + désamorçage · Émojis sémantiques · Vision SEO-AEO-Local unifiée · Équation "Google vous fait confiance → ChatGPT aussi" · La constance, c'est la clé.

### Règles d'or

**Content :**
- Rythme idéal : 1 article/jour · réaliste agence : 2-3/semaine · minimum viable : 1/semaine
- Article longue traîne : H1 + intro + 4-6 H2 + FAQ finale + maillage page commerciale
- Longueur : 800-1500 mots (longue traîne) / 1500-2500 mots (pilier)

**Texte de collection (pattern observé) :**
- 1 H1 + 4 H2 (intro + 2 variantes + clôture) · 400-600 mots
- Mot-clé principal en gras : 3-6 occurrences · Variantes sémantiques : 2-4
- Maillage : 1-2 liens internes ancre = mot-clé destination

**Netlinking :**
- Volume : 8-10 backlinks/mois
- Répartition ancres : 40% optimisées / 30% semi-optimisées / 30% génériques
- Phasage mensuel : Mois 1 = 100% homepage · Mois 2 = 50% HP + 50% collections · Mois 3+ = 20% HP / 30% top 7-15 / 50% top 15-25
- Budget par backlink : 120-250€ (DR 25-40, thématique alignée)

**AEO :**
- FAQ en bas de chaque page commerciale + schema JSON-LD FAQPage
- 7 formats articles longue traîne : Définition · Comparatif · Catégorisation · Origine · Pratique · Entretien · Identification
- Réponses FAQ : 40-80 mots, autonomes, factuelles
- Autoriser explicitement dans robots.txt : GPTBot · ClaudeBot + anthropic-ai · PerplexityBot · Google-Extended
- SSR obligatoire (pas de SPA non-crawlable)

**Cannibalisation :**
- Seuil alerte : 2+ pages dans le top 10 pour le même mot-clé
- Solutions : maillage interne OU cocon sémantique

**Longue traîne — progression KD par phases :**
- Phase 1 (mois 1-3) : KD < 30%
- Phase 2 (mois 4-6) : KD 30-50%
- Phase 3 (mois 6+) : KD > 50%

### 3 types d'audit (trilogie)

| Type | Périmètre | Bots responsables |
|---|---|---|
| **Interne** | Contenu SEO-friendly, maillage, UX, ancienneté | Bot Sémantique + Bot Content |
| **Externe** | Marché, concurrence, autorité, backlinks | Bot Netlinking + Bot Concurrentiel |
| **Technique** | 404, 301, sitemap, Core Web Vitals | Bot Technique |

SEO Local, Bot IA Search, Orchestrateur = transversaux aux 3 types.

### 8 threads synthétisés

| Thread | Sujet | Point clé |
|---|---|---|
| Août 2023 | Erreurs HTTP | Arbre décision 404 : 410 / 301 / 503 / 301-catégorie |
| Sept 2023 | Longue traîne effet tunnel | "café" KD60% → "tasse de café" KD26% → maillage page mère |
| Sept 2023 | Cannibalisation + cocons | Seuil 2+ pages top 10 → maillage OU cocon |
| Sept 2023 | Google Bots + crawl budget | Limiter URLs inutiles, sitemap déclaré, hiérarchie, pas de chaînes redirect |
| Oct 2023 | Redirections 301 + profondeur | Max 3 clics depuis la home pour toute page stratégique |
| Août 2024 | 6 bookmarklets SEO | site: / dup content / scrappe SERP / cache Google / Majestic / headers HTTP |
| Mai 2025 | Étude de cas textile ×9 | KD phasé 3 phases, 60 articles/4 mois, maillage systématique, netlinking 8-10/mois |
| Août 2025 | AEO ventes ChatGPT | 3 piliers : expertise + pédagogie + structure FAQ/JSON-LD/robots.txt IA |

### Patterns clients analysés

- **y2k-gorpcore.fr** : ✅ exhaustivité variantes + blocs texte 4 H2 × 400-600 mots · ❌ entité légale US sur site FR (E-E-A-T faible)
- **sparkmodel.com** : ❌ SPA JavaScript non-crawlable → invisible pour bots IA → SSR obligatoire
- **sabrmastour.com** : ✅ blog 7 formats + FAQ home 5 Q/R + transparence E-E-A-T · ❌ schema JSON-LD FAQPage absent
