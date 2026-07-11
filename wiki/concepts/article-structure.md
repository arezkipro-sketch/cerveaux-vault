---
type: concept
title: "Article Structure (SEO)"
slug: article-structure
tags: [seo, on-page, content, html, structure, readability]
sources: ["[[jotaro-seo-content-strategy]]", "[[sedestral-blog-article-seo-2026]]"]
source_count: 2
status: active
updated: 2026-06-20
---

# Article Structure (SEO)

**Definition:** The HTML hierarchy and content layout of a blog post or article, optimized for both search engines (crawlability, semantic signals) and readers (scannability, engagement). Structure is what Google reads before content.

## Règles de balisage (consensus des sources)

| Balise | Règle absolue | Contenu |
|---|---|---|
| H1 | 1 unique par page | Mot-clé principal ; 50-60 chars ; accrocheur |
| H2 | Sections majeures | Terme du champ sémantique |
| H3 / H4 | Sous-parties | Variantes longue traîne / questions |
| Strong | Tous les 50-100 mots max | Points essentiels uniquement |

- **Pas de sauts de niveaux** : H2 → H4 directement = interdit. Google et lecteurs en souffrent.
- Mot-clé cible dans H1, premier paragraphe, et balises meta → [[seo-copywriting]]

## Format scannable

- **Paragraphes courts** : 2-4 phrases, 1 idée par paragraphe → [[sedestral-blog-article-seo-2026]]
- **Listes à puces / numérotées** → augmentent les chances de **featured snippet**
- **Tableaux** → appréciés pour les **extraits enrichis** (rich snippets) Google
- **Image / citation / extrait de code** tous les 3-4 paragraphes → engagement maintenu
- **Table des matières** avec ancres HTML pour articles > 1 500 mots → navigation rapide + signal de structure pour Google

## Longueur cible

- Minimum 1 500-2 000 mots pour traiter un sujet en profondeur → [[sedestral-blog-article-seo-2026]]
- Éviter trop court (sujet effleuré) et trop long sans valeur (ennuyeux + dilue le signal)
- La longueur idéale est dictée par l'analyse des pages qui rankent sur le mot-clé cible

### Répartition cible par bloc (validé en session pratique)

| Bloc | Mots cibles |
|---|---|
| Intro (avant table des matières) | 100-150 mots |
| Chapeau d'introduction de chaque H2 | 20-30 mots |
| Chaque H3 | 80-120 mots |
| Section tableau / comparatif | 50-80 mots (hors contenu du tableau) |
| FAQ — chaque réponse H3 | 60-100 mots |
| Conclusion + CTA | 80-120 mots |

> Si l'article est sous 1 200 mots après rédaction, ajouter une section H2 thématique : "Quand renouveler/changer X ?", "Les erreurs courantes", ou un H3 supplémentaire sur un cas particulier (race, usage, profil utilisateur).

## Introduction

- Méthode **PAS** (Problème → Agitation → Solution) pour créer un lien émotionnel immédiat → [[sedestral-blog-article-seo-2026]]
- Mot-clé principal dans les 100 premiers mots de façon naturelle
- Les 100 premiers mots sont capitaux pour retenir l'attention (et signaler le sujet à Google)

## Données structurées (Schema.org)

- `Article` : pour articles classiques → booste les rich snippets
- `FAQPage` : pour les sections Q&R → apparaissent dans PAA et featured snippets
- Tester avec l'outil de validation Google avant de déployer

### Erreurs fréquentes sur Shopify (validé en session)

| Erreur | Impact | Correction |
|---|---|---|
| `publisher` sans `logo` | Rich snippet Article rejeté par Google | Ajouter `"logo": {"@type": "ImageObject", "url": "..."}` dans publisher |
| `<meta description>` dans l'éditeur HTML | Ignorée ou dupliquée | Saisir dans le champ SEO Shopify uniquement |
| `<meta charset>` / `<meta viewport>` dans le body | HTML invalide | Supprimé — Shopify les gère dans `theme.liquid` |
| `<script>` JSON-LD dans un `<p>` | HTML invalide | JSON-LD directement à la racine, sans balise block autour |
| Lien externe `target="_blank"` sans `rel` | Faille sécurité + signal SEO dégradé | `rel="noopener noreferrer"` obligatoire |

## Structure dans la stratégie JotaroSeo

JotaroSeo formalise la hiérarchie de mots-clés dans un système à 3 niveaux :
1. Page pilier (mot-clé principal fort → priorité commerciale)
2. Pages de cluster (longue traîne → alimentent la page pilier via liens internes)
3. Articles supports (questions / informationnel → apportent du trafic et renforcent l'autorité)

→ La structure interne d'un article (H1/H2/H3) doit refléter ce positionnement hiérarchique → [[jotaro-seo-content-strategy]]

## Relations
- Contenu opérationnel de [[seo-copywriting]] (comment on applique la stratégie à l'article).
- H1/H2/H3 + ancres = pilier du [[maillage-interne]] (texte d'ancre des liens internes).
- FAQ + listes → signaux pour [[people-also-ask]] et featured snippets.
- Longueur + profondeur → composante de [[topical-authority]].
- Schema Article/FAQ → renforce [[generative-engine-optimization]] (LLMs lisent les données structurées).

## Tensions / open questions

- Longueur optimale varie par niche et intention : 1 500 mots pour informatif, mais comparatif ou guide complet peut nécessiter 3 000+.
- Les featured snippets valorisent les listes et tableaux mais leur apparition reste imprévisible.

## Sources
- [[jotaro-seo-content-strategy]] — hiérarchie mots-clés 3 niveaux ; H1/H2/H3 ; structure = pilier de la stratégie contenu.
- [[sedestral-blog-article-seo-2026]] — règles HTML détaillées (H1-H4, pas de sauts, strong, tableaux, listes, PAS intro, longueur 1 500-2 000 mots, table des matières).
