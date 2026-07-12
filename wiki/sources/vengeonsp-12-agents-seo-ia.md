---
type: source-note
title: "Paul Vengeons — 12 agents : système SEO IA"
slug: vengeonsp-12-agents-seo-ia
page-type: source-note
domain: seo
tags: [seo, ia, agents, claude-code, system-prompt, workflow, gsc, maillage-interne, keyword-research, backlinks, schema, seo-local]
sources: []
related: ["[[vengeonsp]]", "[[agent-seo-ia]]", "[[keyword-research]]", "[[maillage-interne]]", "[[google-search-console]]", "[[seo-audit]]", "[[backlinks]]", "[[donnees-structurees]]"]
source-url: "https://x.com/vengeonsp/article/2075499608495600054"
source-type: article
author: "[[vengeonsp]]"
date-accessed: 2026-07-07
raw-file: "01 - SEO/1 - Fondamentaux/20 - vengeonsp-12-agents-seo-ia.md"
source_count: 0
status: active
updated: 2026-07-07
---

# Paul Vengeons — 12 agents : système SEO IA

## Overview

Article publié sur X (2026-07-10) par @VengeonsP (Paul Vengeons). Présente un système complet de 12 agents Claude spécialisés couvrant l'intégralité du workflow SEO, issu de l'expérience sur chatseo.app.

**Thèse centrale :** *"La différence entre ceux qui essaient et ceux qui en tirent des € ? Le process que l'IA suit."* Les system prompts génériques donnent des résultats génériques. Des agents spécialisés avec une méthodologie précise donnent des résultats actionnables.

**Règle d'utilisation :** chaque agent = une NOUVELLE conversation Claude. Toujours commencer par l'Agent 1 (Stratégie SEO).

---

## Les 12 agents — synthèse

### Agent 1 — Stratégie SEO (le quarterback)

**À utiliser EN PREMIER, avant tout autre agent.**

Méthodologie :
1. **Diagnostiquer avant prescrire** — pose des questions sur le site, la niche, le trafic, le business model, les ressources disponibles (heures/semaine, budget)
2. **Framework ICE** — chaque initiative notée sur Impact (1-10) / Confiance (1-10) / Facilité (1-10), triée par score total → [[agent-seo-ia]]
3. **Levier > Création** — réparer le contenu existant (striking distance, pages mourantes, liens internes cassés, titres faibles) bat presque toujours créer du neuf. Par défaut : orienter vers le levier.
4. **Honnêteté sur les délais** — 30 / 60 / 90 jours de délais explicites
5. **Tuer les vanity metrics** — exit impressions totales → enter clics sur requêtes à intention commerciale, pages en striking distance, volume de recherche brandé

**Outputs :** Top 3 priorités ICE + 3 actions concrètes par priorité + résultats attendus 30/60/90j + LISTE À-NE-PAS-FAIRE + 1 question d'accountability hebdo

---

### Agent 2 — Recherche de mots-clés

**Principe : ranking est relatif.** Un mot-clé KD-30 est impossible pour un site tout neuf et trivial pour un site établi. Toujours calibrer par rapport à l'autorité thématique réelle du site.

Méthodologie :
1. Comprendre le site d'abord (URL, niche, sujets rankés, client cible, objectif business du ranking)
2. Classer par **intention** : Informationnel / Commercial / Transactionnel / Navigationnel
3. Regrouper en **4-6 clusters thématiques** → chacun devient un content hub (1 article pilier + 4-8 articles de soutien)
4. Calibrer la difficulté honnêtement : "gagnable en 3 mois" / "gagnable en 6-12 mois" / "jeu long terme"
5. Prioriser le **long-tail + le sous-servi** : requêtes à intention claire dont le top ranking est faible (pages minces, périmées, hors sujet, E-E-A-T faible)

→ [[keyword-research]]

---

### Agent 3 — Analyse de performance GSC

**Principe : 80% des gains du prochain trimestre se cachent dans les pages déjà existantes.**

**Les 6 analyses à exécuter dans l'ordre :**

| # | Analyse | Description |
|---|---|---|
| a | **Striking distance** | Pages/requêtes aux positions 4-15. À 1-2 optimisations de la page 1. |
| b | **Pages en déclin** | Pages perdant le plus de clics vs période précédente. Diagnostiquer la cause (algo / concurrent / content decay / cannibalisation). |
| c | **Outliers CTR** | Pages qui rankent bien (top 10) mais CTR sous benchmark de position → réécriture title/meta. |
| d | **Fuites d'impressions** | Requêtes à fortes impressions mais peu de clics → mismatch d'intention ou feature SERP absente. |
| e | **Intention cachée** | Requêtes sur lesquelles la page rank sans les avoir intentionnellement ciblées → parfois la plus grosse opportunité. |
| f | **Cannibalisation** | Plusieurs URLs qui se battent pour la même requête → [[keyword-cannibalization]] |

**Input nécessaire :** export GSC rapport Performance, 90 derniers jours vs 90 jours précédents, dimensions Page + Requête, format CSV.

→ [[google-search-console]]

---

### Agent 4 — Analyse concurrentielle

**Principe : n'innove pas là où tu peux imiter. Trouve ce qui marche pour eux, fais-le mieux avec un angle unique, puis ajoute ce qu'ils sont trop gros pour faire.**

5 dimensions d'analyse :
- **Empreinte de contenu** : clusters thématiques qu'ils possèdent et pas moi
- **Gaps de mots-clés** : requêtes top 20 chez eux, absent chez moi (prioriser intention commerciale)
- **Wins de format** : quel format rank systématiquement (long-form, listicle, calculateur, comparatif, vidéo)
- **Signaux E-E-A-T** : bios d'auteur, citations, data originales, experts cités
- **Avantage structurel** : patterns de maillage interne, schema, page speed, architecture

Output inclut : "mon avantage asymétrique" (ce que je peux faire qu'eux NE PEUVENT PAS à cause de leur taille/positionnement).

→ [[e-e-a-t]], [[maillage-interne]], [[topical-authority]]

---

### Agent 5 — Rédaction IA

**Principe : l'objectif n'est pas d'écrire un article. C'est d'écrire L'article qui devrait ranker #1 sur le mot-clé cible.**

Méthodologie :
1. Clarifier avant d'écrire (mot-clé, audience précise, ton du site avec pages de référence, objectif business)
2. Reconnaissance SERP : modéliser les 3 pages en top → quel angle MANQUE à toutes ? → c'est le hook unique
3. Structurer selon l'intention :
   - "Comment X" → pas-à-pas avec captures
   - "Meilleur X pour Y" → tableau comparatif + sélections par critères
   - "X vs Y" → comparaison neutre + recommandation
   - "Qu'est-ce que X" → définition + exemples + applications
4. Écrire comme un humain : pas de "plongeons dans", pas de "dans le monde rapide d'aujourd'hui", phrases courtes, voix active, exemples concrets
5. Intégrer E-E-A-T : données précises avec sources, vrais exemples, citations d'experts, opinions originales, histoires perso

Output : TITLE (< 60 car.) + META (< 155 car.) + H1 + article complet + FAQ (5 questions PAA) + 3 suggestions liens internes + angle unique (1 §)

→ [[article-structure]], [[search-intent]], [[e-e-a-t]]

---

### Agent 6 — Optimisation on-page

**Principe : je n'ai presque certainement pas besoin d'une nouvelle page. J'ai besoin que celle que j'ai déjà fasse mieux son job.**

Ordre d'audit (impact décroissant) :
1. Balise TITLE (mot-clé primaire + raison de cliquer)
2. META DESCRIPTION (< 155 car., mot-clé, vend le clic, CTA implicite)
3. H1 (unique, couvre mot-clé + angle)
4. Hiérarchie H2/H3 (intention de recherche + PAA + sous-titres concurrents)
5. Qualité de l'intro (réponse directe dans les 100 premiers mots)
6. Couverture sémantique (termes/entités du top ranking absents dans ma page)
7. Liens internes (3-5 vers pages pertinentes, ancres descriptives)
8. Médias (alts images, noms de fichiers, transcripts)
9. Schema (quel JSON-LD pour feature SERP ?)

→ [[article-structure]], [[donnees-structurees]], [[maillage-interne]]

---

### Agent 7 — Maillage interne

**Principe : Google distribue l'autorité via les liens internes. Si les money pages ne sont pas bien liées depuis les pages d'autorité, on fuite de la puissance de ranking.**

4 checks :
- **Orphelines** : pages sans lien interne entrant → réparer
- **Fuites d'autorité** : pages à forte autorité qui ne lient pas vers les money pages → boucher les fuites
- **Câblage des clusters** : chaque cluster doit avoir une page pilier + articles de soutien liés en hub-and-spoke
- **Diversité d'ancres** : variées, descriptives, conscientes des mots-clés (jamais "clique ici")

Règles opérationnelles :
- **Max 5 liens internes sortants par page** — au-delà, le signal se dilue
- **Liste à-ne-pas-lier** : ne pas lier vers /about, /privacy, /mentions-légales — ces pages ne méritent pas l'autorité
- Toujours préciser OÙ dans la page le lien doit être ajouté (quel paragraphe)

→ [[maillage-interne]], [[link-juice]]

---

### Agent 8 — Analyse de backlinks

**Principe : les meilleurs prospects de liens sont les sites qui linkent déjà vers mes concurrents mais pas vers moi.**

5 catégories de prospects :
1. **Link intersect** : sites qui linkent vers plusieurs concurrents mais pas moi (priorité max)
2. **Pages de ressources** : listes "meilleurs outils/guides de [niche]" qui ne me listent pas
3. **Remplacement de liens cassés** : pages obsolètes dans ma niche où mon contenu peut remplacer
4. **Mentions non liées** : ma marque citée sans lien → demander la conversion
5. **Digital PR** : contenu data-driven à pitcher à des journalistes de la niche

Matrice effort/impact pour solo founder à temps limité : mention non liée > link intersect > pages ressources > liens cassés > digital PR.

Output inclut des templates d'outreach < 100 mots pour chaque catégorie.

→ [[backlinks]], [[off-page-seo]]

---

### Agent 9 — Audit d'indexation

**Principe : chaque URL indexée concurrence pour le crawl budget et dilue les signaux de qualité. Un index propre rank mieux qu'un index gonflé.**

Classification de chaque URL :
- **Garder & optimiser** : précieuse, indexée, peut être améliorée
- **Désindexer** : minces, dupliquées, low-quality, URL de paramètres
- **Consolider** : plusieurs URLs sur contenu similaire → 1 canonical
- **Manquante** : pages importantes non indexées (check GSC "Crawlée : actuellement non indexée")

Pour chaque correction : préciser si c'est noindex, robots.txt disallow, canonical, 301, ou retrait du sitemap.

→ [[crawl-budget]], [[canonical-tag]], [[robots-txt]], [[xml-sitemap]]

---

### Agent 10 — Données structurées

**Principe : le schema ne booste pas directement les rankings, mais les rich results (FAQ, étoiles, miniatures, breadcrumbs) doublent souvent le CTR.**

Règle : ne jamais implémenter un schema FAQ si la page n'a pas de contenu FAQ visible (Google a pénalisé cette pratique).

Stack typique : BreadcrumbList + schema spécifique au contenu + Organization site-wide.

Output : JSON-LD complet prêt au copier-coller + checklist de validation pour le Rich Results Test Google.

→ [[donnees-structurees]]

---

### Agent 11 — Analyse de marque (SERP de marque)

**Principe : la SERP sur ton propre nom de marque est ta page la plus importante sur internet.** C'est la première chose que voient les investisseurs, partenaires, clients, journalistes.

7 éléments audités :
- Knowledge panel (existe-t-il, est-il correct ?)
- Sitelinks (les bons liens profonds s'affichent ?)
- People Also Ask (quelles questions, qui y répond ?)
- Onglet Images (logo, produit, founder ?)
- Résultats News/X (couverture positive, négative, absente ?)
- Intrusion concurrent (annonces, pages "alternatives à X" ?)
- Signaux d'entité (Wikipedia, Wikidata, Crunchbase, LinkedIn)

→ [[e-e-a-t]], [[topical-authority]]

---

### Agent 12 — SEO local

**Principe : les rankings locaux viennent d'un stack précis de 6 signaux. Maîtriser les 6 bat 95% des concurrents.**

Les 6 piliers :
1. **Google Business Profile** : complétude (nom/adresse/téléphone/horaires/catégories/services/produits/attributs/photos/posts)
2. **Cohérence NAP** : nom/adresse/téléphone identiques sur les 30 principaux sites de citations
3. **Reviews** : nombre, vélocité, note, taux de réponse, mots-clés dans les reviews
4. **On-page local** : page de localisation par zone de service, nom de ville dans title/H1/contenu/schema
5. **Contenu local** : articles, guides, pages de quartier
6. **Liens locaux** : citations + presse locale + sponsorings + chambre de commerce

→ [[google-search-console]] (GSC local), [[donnees-structurees]] (LocalBusiness schema)

---

## Ce que cette source apporte au vault

| Concept | Statut avant | Statut après |
|---|---|---|
| Framework multi-agent SEO (12 agents spécialisés) | ❌ Absent | ✅ [[agent-seo-ia]] créé |
| Framework ICE pour priorisation SEO | ❌ Absent | ✅ Dans [[agent-seo-ia]] |
| 6 analyses GSC structurées | ❌ Absent | ✅ Ajouté à [[google-search-console]] |
| "Ranking est relatif" + calibration par autorité | ⚠️ Partiel | ✅ Enrichi dans [[keyword-research]] |
| Content hub (1 pilier + 4-8 soutien par cluster) | ⚠️ Mentionné | ✅ Structuré dans [[keyword-research]] |
| Liste à-ne-pas-lier (/about /privacy) | ❌ Absent | ✅ Ajouté à [[maillage-interne]] |
| Max 5 liens sortants par page | ❌ Absent | ✅ Ajouté à [[maillage-interne]] |

## Sources
- [[vengeonsp]] — auteur de l'article
