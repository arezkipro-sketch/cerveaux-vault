---
type: entity
entity_type: product
title: PushRank
slug: pushrank
aliases:
  - pushrank.io
  - Pushrank
tags:
  - seo
  - tool
  - ai-seo
  - french
sources:
  - "[[jotaro-seo-ia-x-seo]]"
  - "[[jotaro-seo-content-strategy]]"
  - "[[jotaro-seo-chatgpt-sales]]"
source_count: 3
status: active
updated: 2026-07-26
note: "MAJ 2026-07-22 : sorti de pré-lancement, usage réel confirmé sur harnais-chien-expert.fr via intégration MCP Claude Code. Voir section Usage réel."
---

# PushRank

**Definition:** Outil de monitoring et de recommandations SEO piloté par IA, développé par @JotaroSeo (Souleymane) et une équipe de devs (dont @hamada_fahari et @ArbieuL). Analyse quotidienne du site, monitoring concurrentiel, recommandations personnalisées actionnables.

## Ce qu'on sait (mis à jour après usage réel)

- **Sorti de la phase pré-lancement** décrite en 2026-06 → outil accessible via connecteur MCP dans Claude Code (`claude mcp add`), avec authentification OAuth côté claude.ai.
- **Connexion Google Search Console** : PushRank lit des snapshots GSC retenus (jamais d'appel live/URL Inspection). Rétention ~90 jours, jusqu'à 50 périodes disponibles.
- **Moteur d'opportunités** : classe chaque problème détecté en `type` + `severity` (high/medium/low) + `priorityScore`. Types rencontrés :
  - `quick_win` — page qui ranke déjà avec un défaut on-page corrigible.
  - `decay` — signal de baisse de performance. **Peu fiable sur un jeune projet** : nécessite un vrai historique GSC (volume absolu d'impressions), pas juste du temps écoulé — voir note fiabilité ci-dessous.
  - `winner` — page qui performe bien, recommandation de renforcement (CTA, maillage interne).
  - `new_query` — nouvelle requête détectée dans GSC, pas encore couverte par une page dédiée.
  - `ai_recommendation` — audits variés générés par IA (title trop long/court, meta hors fourchette, mot-clé absent du title, contenu insuffisant, CTR à améliorer). Le plus utile en pratique mais le moins prévisible dans son format (`pageUrl` parfois `null`).
  - `cannibalization`, `indexation`, `sitemap`, `internal_linking`, `content_creation`, `site_drop`, `trending_query`, `low_ctr` — types listés dans le schéma mais peu vus en usage réel.
- **Workflow de statut** : `todo` → `in_progress` / `done` / `ignored`. **Piège découvert** : un item marqué `ignored` peut être remis en `todo` automatiquement si PushRank le re-détecte lors d'un scan ultérieur — le statut "ignoré" n'est pas permanent, il faut le re-fermer à chaque réapparition.
- **Bug outil connu** : le paramètre `severity=low` (et `priority=low/high/medium`) de l'outil de listing renvoie systématiquement 0 résultat quel que soit le `status`, alors que le compteur global (`get_project_overview`) affiche bien des dizaines d'items en `low`. Aucun contournement trouvé via les paramètres disponibles — les items priorité basse restent inaccessibles par l'API/MCP, consultables seulement dans l'interface web.
- **Écart de comptage** : le total affiché par `get_project_overview` peut largement dépasser ce que `list_seo_opportunities` peut effectivement énumérer (ex: 136 annoncés vs 25 récupérables) — probablement des doublons d'historique de (re-)détection côté PushRank, pas un vrai delta d'items uniques.
- Panneau web **"Santé SEO technique"** (pages orphelines, meta trop longues, maillage insuffisant, heading hierarchy skip, title=H1...) — **non exposé** par les outils MCP disponibles ; consultation uniquement via l'interface web, aucun outil pour lister les URLs concernées par ce biais.
- Aucun outil MCP pour **relancer un crawl/audit manuellement** — tous les outils disponibles sont en lecture (ou changent un statut). Le rescan semble automatique/périodique côté PushRank (nouvelles opportunités observées apparaître spontanément entre deux sessions).

## Fiabilité du signal `decay` — leçon opérationnelle

Sur un projet PushRank jeune (GSC connecté depuis <48h au moment du diagnostic), la quasi-totalité des opportunités `decay` se sont révélées être du bruit statistique, pas une vraie tendance : les pages concernées avaient un volume d'impressions trop faible (2 à 15 sur 3 mois) pour qu'une comparaison avant/après ait un sens. **Ce n'est pas une question de temps écoulé** (PushRank retient jusqu'à ~3 mois d'historique GSC dès la connexion) mais de **volume absolu** — une page à 2 impressions/semaine reste bruitée même après plusieurs mois d'attente si son trafic ne grossit pas.

**Règle pratique retenue** : avant de traiter un item `decay`, croiser avec le volume réel de la page (dimension `page` du snapshot GSC) — n'agir/revérifier que sur les pages ayant déjà une base d'impressions notable (ex: >30-40 sur 3 mois). Sous ce seuil, ignorer et ne pas re-prioriser tant que le volume de base n'a pas grossi.

## Usage réel — harnais-chien-expert.fr (session 2026-07-21/22)

Premier gros audit + corrections réalisé sur ce store (voir aussi contexte [[maillage-interne]] pour les sessions précédentes sur le même site).

**Corrections appliquées suite aux recommandations PushRank :**
- Meta descriptions manquantes (`/blogs/news`) → ajoutées.
- H1 dupliqué sur 15 pages (14 pages statiques + 1 fiche produit, cause commune : bannière de thème + H1 dans le contenu) → détail complet dans [[h1-heading-tag]].
- Title trop long sur 108 pages → cause racine unique : bug de suffixe de marque dupliqué dans le thème Shopify (voir [[h1-heading-tag]] et [[canonical-tag]] pour les cas connexes), pas 108 corrections manuelles séparées. Retombé à 29 après le fix.
- 73 meta descriptions produits hors fourchette 150-160 caractères → réécrites en lot, voir [[meta-description]].
- Cannibalisation du mot-clé principal ("harnais chien" home vs collection) → analysée en profondeur, voir [[keyword-cannibalization]] pour le cas complet et l'erreur méthodologique commise (check SERP-similarity oublié initialement).
- Titre SEO ne contenant pas le mot-clé exact visé (mot inséré au milieu cassant le match exact, ex: "Harnais **Anti-Traction** Bouledogue Français" ne matche pas "harnais bouledogue français") → pattern à surveiller systématiquement sur les titles SEO e-commerce.

**Constat sur les recommandations `ai_recommendation` de type "renforcer le CTR"** : une reformulation orientée accroche (format question, bénéfice) peut faire perdre le mot-clé principal de la meta description si on n'y prête pas attention — corrigé après coup sur l'article guide des tailles. Toujours vérifier qu'une réécriture CTR conserve le mot-clé cible, pas seulement l'accroche.

## Session 2026-07-22 — vague prioritaire HCE

PushRank remonte plusieurs recommandations sur harnais-chien-expert.fr, mais le site ayant environ 2 mois, les signaux `decay` doivent être traités avec prudence. La décision retenue n'est pas de corriger toutes les alertes, mais de prioriser les pages à intention commerciale directe : collections Spitz, Golden Retriever, Cavalier King Charles, Accessoires, Anti-Traction, puis l'article support "chien qui tire en laisse".

**Règle appliquée** : chaque suggestion PushRank est documentée avec 4 éléments : signal détecté, décision prise, raison SEO/business, changement appliqué. Cette règle évite d'obéir mécaniquement à l'outil : PushRank sert de déclencheur d'analyse, pas de pilote automatique.

| Page | Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- | --- |
| Collection Spitz | `decay` et `quick_win` sur `harnais spitz`, `harnais spitz nain`, `harnais pour spitz`, `harnais pour spitz allemand` | Traité | Plusieurs signaux sur une même money page + intention d'achat claire | Contenu race/taille déjà présent ; title/meta renforcés sur `Spitz nain` et `Spitz allemand`, sans dupliquer les blocs existants |
| Collection Golden Retriever | `decay` sur `harnais pour golden retriever` et variantes | Traité | Page collection commerciale proche d'une opportunité page 1, mais CTR faible/nul | Contenu choix/taille/anti-traction déjà présent ; title SEO ajouté et meta description renforcée pour rassurer l'achat |
| Collection Cavalier King Charles | `decay` + opportunité mesurée sur l'intention race | Traité | Requêtes proches de la page 1, intention d'achat spécifique | Contenu race/cou/FAQ déjà présent ; title/meta alignés sur la requête exacte et le guide taille |
| Collection Accessoires | `ai_recommendation` : contenu insuffisant | Traité | Page collection trop générique, peut soutenir l'écosystème harnais | Ajout de sections usages/conseils, FAQ 4 questions, liens vers harnais, poignée et anti-traction, title/meta renforcés |
| Collection Anti-Traction | `decay` sur `harnais pour chien qui tire` | Traité en optimisation légère | Intention transactionnelle forte, mais pas besoin de refonte complète | Contenu éducatif/FAQ déjà riche ; title/meta renforcés sur `chien qui tire` et lien depuis l'article conservé |
| Article chien qui tire en laisse | `decay` sur requête informationnelle | Traité comme support, pas money page | Potentiel informationnel utile pour pousser vers la collection Anti-Traction | Article déjà doté d'une transition et d'un CTA interne ; summary, title tag et description tag renforcés vers le choix du harnais anti-traction |
| Pages secondaires | Alertes moyennes isolées | Reporter sauf correction légère évidente | Site jeune + risque de dispersion | Pas de grosse réécriture sur Berger Australien, Bouledogue Français, Chiot, Handicapé, Tactique |

Leçon associée : sur un jeune site e-commerce, l'ordre de correction doit combiner [[pushrank]], volume/impressions GSC, [[search-intent]], rôle commercial et [[maillage-interne]]. Une alerte `decay` seule ne suffit pas.


## Session 2026-07-25 — `content_creation` déjà couvert et mapping canonique HCE

PushRank a remonté 7 opportunités `content_creation` issues de `keyword_strategy`. Après vérification Shopify, 6 ne nécessitent pas de création de page : les collections existent déjà et doivent rester les pages cibles. Le signal ne veut donc pas dire "page absente", mais plutôt "PushRank n'a pas associé automatiquement ce mot-clé à une page canonique" (`primaryArticle: null`, statut keyword `candidate`).

**Règle appliquée** : avant de créer une page suite à une recommandation PushRank `content_creation`, vérifier les collections/pages existantes, le mapping d'intention et le risque de [[keyword-cannibalization]]. Si une page collection existe déjà, ne pas créer de doublon : optimiser ou mapper la page existante.

| Mot-clé PushRank | Page cible existante | Décision prise | Raison SEO/business | Statut PushRank |
| --- | --- | --- | --- | --- |
| `harnais chien` | `/collections/tous-les-harnais-chien` | Ne pas créer de page | Collection mère déjà dédiée à l'intention catalogue/achat | `ignored` |
| `harnais canicross` | `/collections/harnais-canicross` | Ne pas créer de page | Collection dédiée existante avec produits | `ignored` |
| `harnais en Y` | `/collections/harnais-chien-y` | Ne pas créer de page | Collection dédiée existante ; créer une page concurrente brouillerait l'intention | `ignored` |
| `harnais chien voiture` | `/collections/harnais-chien-voiture` | Ne pas créer de page | Collection dédiée existante ; priorité à renforcer la page si besoin | `ignored` |
| `harnais chiot` | `/collections/harnais-chiot` | Ne pas créer de page | Collection dédiée existante ; éviter doublon article/collection sur intention achat | `ignored` |
| `harnais teckel` | `/collections/harnais-teckel` | Ne pas créer de page | Collection race dédiée existante | `ignored` |
| `ceinture chien voiture` | À clarifier, proche de `/collections/harnais-chien-voiture` | Garder ouvert | Intention possiblement différente : accessoire ceinture/attache voiture. À traiter seulement si produit ou angle dédié réel | `todo` |

Contrôle cannibalisation associé : PushRank ne remonte aucune opportunité `cannibalization`. Les données GSC montrent surtout des chevauchements normaux article/collection (article = support informationnel, collection = intention achat). Les URLs produits Shopify en forme `/collections/.../products/...` canonisent bien vers `/products/...`, donc pas de cannibalisation technique constatée sur ce point.


## Session 2026-07-25 — santé SEO technique HCE

PushRank a remonté dans le panneau web "Santé SEO technique" plusieurs alertes sur harnais-chien-expert.fr : pages orphelines, meta descriptions manquantes, liens internes cassés, pages faiblement liées, liens produits insuffisants et canonical 404. Le détail complet n'est pas exposé par le MCP PushRank : l'interface donne les compteurs, mais pas toujours une liste exploitable par action.

**Décision méthodologique** : séparer les signaux sûrs des signaux de crawl potentiellement bruités. Les alertes massives `broken internal link` et `canonical 404` ne doivent pas déclencher une correction en bloc tant que les URLs ne sont pas confirmées en vraie 404. Un audit indépendant a montré surtout des réponses `429` lors de contrôles rapides, ce qui indique probablement un rate-limit/crawl limit plutôt qu'un vrai lien cassé. Voir aussi [[site-health]], [[http-status-codes-seo]], [[crawl-budget]] et [[maillage-interne]].

| Signal PushRank | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- |
| `meta description manquante` / titres SEO produits | Traité sur les produits clairement identifiés | Les fiches produits indexables ont une intention commerciale directe ; corriger le title/meta est peu risqué | Titres SEO ajoutés/normalisés sur `harnais-tactique-chien-pochettes`, `harnais-chiot-respirant-multicolore`, `laisse-tactique-amortissante-double-poignee` |
| Articles avec résumé Shopify vide ou nul | Traité | Le résumé aide les extraits, les cartes de blog et la compréhension de la page sans toucher au HTML complet | Résumés ajoutés sur guide taille, chien handicapé, chien en laisse en forêt, Husky, avion, chien réactif, train, anti-fugue, Golden Retriever, voiture |
| `Page orpheline` / `Page faiblement liée` | Partiellement traité, maillage complet à planifier | Le vrai correctif doit être un lien entrant contextuel depuis une page pertinente, pas un lien artificiel dans un menu au hasard | Pas de modification massive des articles HTML ; prochaine passe recommandée : ajouter 1 lien éditorial par page orpheline/faiblement liée confirmée |
| `broken internal link` x volume élevé | À confirmer avant correction | Le volume est incompatible avec l'état réel du site et les URLs clés semblaient surtout renvoyer `429` sous crawl rapide | Aucune correction en bloc ; demander/exporter la liste des URLs réellement en 404 avant action |
| `canonical 404` | À confirmer avant correction | `429` peut être confondu avec un échec de crawl par certains outils ; modifier les canonicals sans preuve peut créer un vrai problème | Aucune modification canonique ; vérifier lentement quelques URLs avant d'agir |
| `insufficient product links` | À traiter au cas par cas | Ajouter des liens produits doit servir l'intention de la page, pas seulement satisfaire un compteur | Pas de liens artificiels ajoutés dans cette session ; priorité future aux articles commerciaux ou guides proches d'une collection |

**Leçon apprise** : sur un site Shopify jeune, le panneau santé technique PushRank doit être lu comme un déclencheur d'audit, pas comme une to-do list automatique. Corriger immédiatement les champs SEO sûrs ; vérifier les gros volumes techniques avec statuts HTTP réels ; traiter le maillage par liens contextuels, page par page.


## Session 2026-07-26 — correction ciblée guide taille HCE

PushRank a remonté un signal `decay` prioritaire sur l'article `/blogs/news/blogs-guide-taille-harnais-chien`, requête `taille harnais chien` (score 72). Après vérification, la page avait déjà un contenu riche, un title SEO et une meta description cohérents. Le problème retenu n'était donc pas un manque de contenu, mais un ordre de lecture trop bruité : gros quiz de recommandation, bloc de résumé IA et second quiz apparaissaient avant la réponse directe.

**Décision prise** : correction légère de structure, sans réécriture massive. Sur un site jeune, ne pas traiter le `decay` comme une preuve de chute définitive ; agir seulement sur une friction claire pour l'utilisateur et pour Google.

| Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- |
| `decay` PushRank sur `taille harnais chien` | Traiter en optimisation légère | L'utilisateur qui cherche une taille veut d'abord savoir où mesurer et quelle taille choisir ; Google doit voir rapidement l'intention principale de la page | Ajout de deux phrases d'introduction ciblées, suppression du second quiz `blog-quiz`, maintien de la réponse SEO en premier, puis bloc résumé IA avant le quiz principal `blog-quiz-multi` |

**À surveiller** : cette correction ne prouve pas que la baisse vient uniquement de l'ordre des blocs. Elle réduit une friction évidente. La performance doit être relue dans GSC/PushRank après nouveau crawl et accumulation de données. Le statut PushRank n'a pas pu être passé en `done` pendant la session car l'OAuth MCP a redemandé une autorisation.

## Relations
- Built by [[jotaro-seo]].
- Complements the strategies taught in [[jotaro-seo-ia-x-seo]] (AI SEO monitoring) and [[jotaro-seo-content-strategy]].
- Usage croisé avec [[ubersuggest]] sur le même projet (harnais-chien-expert.fr) : les deux outils remontent des listes de problèmes qui se recoupent partiellement (ex: title trop long) mais avec des seuils/méthodologies différents — utile de croiser les deux plutôt que de se fier à un seul.
- Voir [[seo-audit]] pour la méthodologie générale d'audit dans laquelle PushRank s'inscrit.

## Tensions / open questions
- Pricing toujours non confirmé en usage réel.
- Fiabilité du signal `decay` sur jeune domaine à réévaluer une fois plus de volume accumulé (voir section dédiée ci-dessus).
- Panneau "Santé SEO technique" (pages orphelines, maillage) reste une boîte noire côté API — dépendant de captures d'écran manuelles de l'utilisateur pour être exploité.

## Sources
- [[jotaro-seo-ia-x-seo]] — AI SEO monitoring positioned as a use case.
- [[jotaro-seo-content-strategy]] — fullest description of planned features.
- [[jotaro-seo-chatgpt-sales]] — mentioned in context of SEO automation.
- Usage réel session 2026-07-21/22 sur harnais-chien-expert.fr (pas de source `raw/` — expérience directe via l'intégration MCP).


Note d'exécution : toutes les opportunités PushRank de cette vague ont été passées en `done` après vérification Shopify. Les alertes non prioritaires (Berger Australien, Bouledogue Français, Chiot, Handicapé, Tactique, backlinks) restent hors périmètre.
