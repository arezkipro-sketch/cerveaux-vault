---
type: concept
title: "Agents SEO IA spécialisés"
slug: agent-seo-ia
tags: [seo, ia, agents, claude, system-prompt, workflow, gsc, keyword-research, maillage-interne]
sources: ["[[vengeonsp-12-agents-seo-ia]]"]
source_count: 1
status: active
updated: 2026-07-07
---

# Agents SEO IA spécialisés

**Définition :** Approche SEO basée sur des agents Claude distincts, chacun avec un system prompt dédié et une méthodologie précise pour un domaine SEO spécifique. Chaque agent = une nouvelle conversation. L'agent 1 (stratégie) est toujours le quarterback — il passe avant tout autre.

**Pourquoi des agents spécialisés plutôt qu'un prompt générique :** un prompt générique donne des conseils génériques. Un agent spécialisé avec une méthodologie contrainte (diagnostiquer avant prescrire, outputs formatés, règles explicites) donne des actions concrètes directement applicables.

## Ce qu'on sait (source : [[vengeonsp-12-agents-seo-ia]])

### Le quarterback pattern

**Agent 1 (Stratégie SEO) doit TOUJOURS être utilisé en premier**, avant tout autre agent. Il pose les questions nécessaires sur le site, le business model, les ressources, et produit une roadmap 90 jours avant que n'importe quel travail spécialisé commence.

### Le Framework ICE — priorisation des initiatives SEO

Chaque initiative SEO est notée sur 3 critères (1-10 chacun) :

| Critère | Question |
|---|---|
| **I — Impact** | Si ça marche, à quel point ça change les métriques ? |
| **C — Confiance** | À quel point on est sûr que ça va marcher ? |
| **E — Facilité** | Combien d'effort / de ressources ça demande ? |

Score ICE = I × C × E (ou somme, selon implémentation). **Trier les initiatives par score ICE avant de choisir par où commencer.**

Exemple : corriger 10 titles en striking distance (I:7 / C:9 / E:8 = score 504) bat écrire 10 nouveaux articles (I:6 / C:5 / E:4 = score 120).

### Principe "Levier > Création"

**Réparer le contenu existant bat presque toujours créer du contenu neuf.** Par défaut, orienter les initiatives vers le levier :
- Mots-clés en striking distance (positions 4-15) → optimisation on-page
- Pages mourantes (déclin de clics) → mise à jour ou consolidation
- Liens internes cassés → réparation
- Titres faibles → réécriture title/meta
- Pages orphelines → maillage interne

Ne créer du nouveau contenu que quand les opportunités de levier sont épuisées ou insuffisantes.

### Anti-vanity metrics

Sortir de ces métriques retardées :
- ❌ Impressions totales (ne génèrent pas de revenus)
- ❌ Domain Rating / Authority Score seul

Entrer dans ces indicateurs avancés :
- ✅ Clics sur requêtes à intention commerciale
- ✅ Pages en striking distance (positions 4-15)
- ✅ Volume de recherche brandé (signal de notoriété)

### Taxonomie des 12 agents

| # | Agent | Données en entrée | Output principal |
|---|---|---|---|
| 1 | **Stratégie SEO** (quarterback) | Site, niche, trafic, business model, ressources | Roadmap 90j (Top 3 ICE + actions) |
| 2 | **Recherche de mots-clés** | URL, niche, client cible | 4-6 clusters + table KW tagués par intention |
| 3 | **Analyse GSC** | Export GSC 90j (Page + Requête CSV) | 6 analyses : striking distance / déclin / CTR / fuites / intention cachée / cannibalisation |
| 4 | **Analyse concurrentielle** | URL site + 2-4 concurrents + sujet focal | Gaps contenu, KW à voler, avantage asymétrique |
| 5 | **Rédaction** | Mot-clé, audience, ton de référence, objectif | Article complet + title/meta/FAQ/liens internes |
| 6 | **On-page** | URL + contenu + KW primaire + top 3 concurrents | Audit 9 points + diff exact des changements |
| 7 | **Maillage interne** | Dump sitemap + money pages + clusters | Plan 15 liens (source/cible/ancre/raison/position) |
| 8 | **Backlinks** | URL + niche + concurrents + assets + temps | 5 catégories prospects + templates outreach |
| 9 | **Audit indexation** | URLs indexées + sitemap + robots.txt | Classification GARDER/DÉSINDEXER/CONSOLIDER/MANQUANTE |
| 10 | **Données structurées** | URL + type de page + contenu | JSON-LD complet prêt à coller |
| 11 | **Analyse de marque** | Nom de marque + founder + URL + socials | Audit SERP de marque + plan entité + défense |
| 12 | **SEO local** | Nom + adresse + catégorie + zone + concurrents | Scorecard 6 piliers + top 5 corrections |

### Règle d'utilisation

- **Une nouvelle conversation par agent** (les system prompts ne se mélangent pas)
- Commencer par Agent 1 (Stratégie) pour obtenir les priorités
- L'Agent 3 (GSC) nécessite un export CSV réel — ne pas procéder sans données

## Relations

- Le Framework ICE s'applique à la [[topical-authority]] (prioriser les clusters à plus fort ICE)
- Le principe "Levier > Création" renforce [[content-pruning]] (optimiser > ajouter)
- Les 6 analyses GSC étendent [[google-search-console]]
- L'Agent 7 documente les règles de [[maillage-interne]] (max 5 liens / liste à-ne-pas-lier)
- L'Agent 2 enrichit [[keyword-research]] (ranking relatif, content hubs)
- L'Agent 8 rejoint [[backlinks]] (link intersect comme priorité max)
- L'Agent 9 rejoint [[crawl-budget]] et [[canonical-tag]]

## Sources
- [[vengeonsp-12-agents-seo-ia]] — 12 system prompts complets avec méthodologie et outputs formatés
