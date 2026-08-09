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
- **Bug outil désormais résolu (confirmé 2026-08-09)** : le paramètre `severity=low` de `list_seo_opportunities` renvoyait systématiquement 0 résultat au 22/07 ; au 09/08, il retourne bien des items (25 `todo` par ex.). Ne plus supposer ce bug actif sans re-tester.
- **`severity` ≠ `priorityScore`, à ne jamais confondre** : un item `severity: "low"` peut avoir un `priorityScore` (81) supérieur à des items `severity: "high"` (61 max observé) ou `severity: "medium"` (59 max observé) sur ce projet. Trier/filtrer par `severity` seul peut faire manquer de vraies priorités. **Règle candidate** : pour prioriser réellement, trier par `priorityScore` toutes sévérités confondues plutôt que de traiter `high` puis `medium` puis `low` en silos étanches — via le paramètre `priorityMin` de `list_seo_opportunities`.
- **Mais `priorityScore` seul reste aussi trompeur sur petit volume** : le item `low_ctr` le plus prioritaire du projet au 2026-08-09 (score 81, le plus haut score todo restant) portait sur une page à 10 impressions/90 jours, 0 clic. Un CTR de 0/10 est du bruit statistique, pas un signal — même règle de seuil que pour `decay` (~30-40 impressions minimum avant d'agir). **Aucun score PushRank (priorité ou sévérité) ne dispense de vérifier le volume GSC réel avant d'agir.**
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


## Session 2026-07-26 — test title/meta Anti-Traction HCE

| Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- |
| PushRank `decay` / optimisation légère sur la collection `/collections/harnais-anti-traction-chien`, requête `harnais chien anti traction` + règle title/meta HCE | Traité en test contrôlé | Page collection commerciale à intention forte ; persona principal = maître au bras arraché ; objectif : garder le mot-clé, la marque rendue automatiquement et améliorer le CTR sans surpromettre | SEO title Shopify passé à `Harnais Anti-Traction Chien Qui Tire` ; rendu public vérifié : `Harnais Anti-Traction Chien Qui Tire – Harnais chien expert` (59 caractères). Meta finale passée à 155 caractères : `Harnais anti-traction pour chien qui tire fort : tension répartie, gorge libre, attache frontale et sorties moins éprouvantes sans forcer le cou en balade.` H1 public inchangé et unique. |

Leçon associée : quand le thème Shopify ajoute automatiquement `– Harnais chien expert`, ne pas inclure la marque dans le champ SEO si cela crée un doublon. Optimiser le champ saisi pour que le rendu public complet reste sous 60 caractères.

Leçon copy associée : la douleur primaire du persona n'est pas `bras tendu`, mais `chien qui tire fort`. En meta description, partir du problème que le client exprime lui-même, puis ajouter une promesse crédible et non absolue : tension répartie, gorge libre, sorties moins éprouvantes.

## EXP-2026-08-09 — position du quiz interactif (avant vs après la réponse rapide) sur les articles race/besoin

**Hypothèse** : sur les articles générés depuis le template "guide race/besoin", placer le bloc quiz interactif avant la section "Réponse rapide" (plutôt qu'après) nuit à l'engagement lecteur et/ou à la performance SEO — cause probable derrière plusieurs alertes `decay` PushRank.

**Ampleur découverte en creusant cette hypothèse** : 43 articles sur 53 (81% du blog) ont ce pattern quiz-en-tout-premier (`blog-quiz` en position <100 caractères du body). Un seul article (`blogs-guide-taille-harnais-chien`) a déjà été corrigé le 2026-07-26, mais **sans suivi de résultat enregistré depuis** — première leçon : ne pas refaire cette erreur, toujours poser une baseline datée avant tout changement destiné à être mesuré.

**Décision** : ne pas généraliser le correctif aux 43 articles d'un coup (changement de structure en masse, catégorie sensible du protocole, hypothèse non encore prouvée). Traiter comme une expérience contrôlée sur les 4 articles ayant un vrai signal `decay` + volume GSC confirmé, mesurer, puis seulement ensuite statuer sur un déploiement plus large.

**Baseline (données GSC 90 jours, cache PushRank au 2026-08-08, avant changement)**

| Page | Impressions/90j | Clics | Position | Requête principale |
|---|---|---|---|---|
| `/blogs/news/harnais-border-collie` | 133 | 4 | 10.02 | harnais border collie |
| `/blogs/news/harnais-berger-allemand` | 104 | 2 | 8.81 | harnais pour chien berger allemand |
| `/blogs/news/harnais-cavalier-king-charles` | 90 | 4 | 7.1 | harnais pour cavalier king charles |
| `/blogs/news/harnais-anti-fugue-pour-chien-...` | 36 | 3 | 8.28 | (query non précisée par PushRank) |

**Action** : déplacement du bloc quiz interactif pour qu'il apparaisse après la section "Réponse rapide" (aucun contenu supprimé ni réécrit, uniquement réordonné), sur ces 4 pages uniquement.

**Date du changement** : 2026-08-09.

**Suivi prévu** : J+14 (2026-08-23), J+28 (2026-09-06), J+56 (2026-10-04) — comparer clics/impressions/position via `get_gsc_snapshot` sur ces 4 URLs. Si amélioration nette et cohérente sur les 4, envisager un déploiement progressif au reste des 43 articles (par lots, pas d'un coup). Si aucun effet mesurable, invalider l'hypothèse et ne pas toucher aux 39 articles restants.

**Rétroactif — `blogs-guide-taille-harnais-chien`** : même changement appliqué le 2026-07-26, jamais suivi. À vérifier en même temps que les 4 ci-dessus (données déjà à J+14 au moment de cette expérience).

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

## Session 2026-07-27 — batch 1 title/meta collections HCE avec GSC direct

Batch publié sur Shopify après validation utilisateur, en croisant trois sources : audit public title/meta, recommandations PushRank précédentes et export Google Search Console direct `harnais-chien-expert.fr-Performance-on-Search-2026-07-27.zip`.

Méthode appliquée : les pages ont été classées par opportunité GSC réelle avant publication. L'export GSC contenait les dimensions `Pages` et `Requêtes` séparées, pas un export croisé `page + requête`. Décision : utiliser `Pages.csv` pour prioriser les URL, `Requêtes.csv` pour ajuster les formulations, et PushRank seulement en appoint lorsqu'une requête devait être reliée à une page.

| Page | Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- | --- |
| `/collections/harnais-grand-chien` | GSC direct : 290 impressions, 0 clic, position 23.87 ; requêtes fortes `harnais gros chien`, `harnais grand chien`, `harnais chien xxl` | Traité en priorité haute | Beaucoup d'impressions sans clic ; intention commerciale claire sur grand/gros chien | SEO title : `Harnais Gros Chien | Grand & XXL` ; meta 153 caractères centrée gros chien, grand chien, XXL, maintien et contrôle |
| `/collections/harnais-bouledogue-francais` | GSC direct : 248 impressions, 0 clic, position 23.96 ; requêtes `harnais bouledogue français`, `harnais chien bouledogue francais`, `harnais anti traction bouledogue français` | Traité en priorité haute | Volume élevé sans clic ; title public trop long avant correction | SEO title : `Harnais Bouledogue Français` ; meta 151 caractères avec anti-traction, cou dégagé et gorge libre |
| `/collections/harnais-cavalier-king-charles` | GSC direct : 165 impressions, 2 clics, position 11.48 ; requête `harnais pour cavalier king charles` | Traité | Page proche de la page 1, faible CTR ; intention race claire | SEO title : `Harnais pour Cavalier King Charles` ; meta 157 caractères sur légèreté, poitrail, cou libre, chiot/adulte |
| `/collections/harnais-spitz` | GSC direct : 131 impressions, 2 clics, position 13.16 ; requêtes `harnais spitz`, `harnais spitz nain`, `harnais pour spitz allemand` | Traité | Page proche page 1/2 ; PushRank avait déjà signalé l'opportunité race | SEO title : `Harnais Spitz | Nain & Allemand` ; meta 154 caractères sur poitrail fourni, cou sensible et pelage |
| `/collections/harnais-golden-retriever` | GSC direct : 85 impressions, 1 clic, position 19.33 ; requêtes `harnais golden retriever`, `harnais pour golden retriever` | Traité | Intention commerciale race ; besoin d'aligner le title sur la formulation GSC `harnais pour...` | SEO title : `Harnais pour Golden Retriever` ; meta 153 caractères sur maintien, épaules libres, chien qui tire |
| `/collections/harnais-chiot` | GSC direct : 61 impressions, 1 clic, position 31.49 ; requête notable `harnais chiot 2 mois` | Traité | Requête spécifique utile pour primo-maître ; title/meta auparavant trop génériques | SEO title : `Harnais Chiot | Dès 2 Mois` ; meta 154 caractères sur premières sorties, cou libre, croissance |
| `/collections/tous-les-harnais-chien` | GSC direct : 44 impressions, 1 clic, position 21.82 ; requête générique `harnais chien` faible mais collection mère stratégique | Traité léger | Page hub commerciale, utile pour l'architecture et le maillage | SEO title : `Harnais Chien | Tous les Modèles` ; meta 151 caractères par taille, usage et morphologie |
| `/collections/harnais-petit-chien` | GSC direct : 34 impressions, 0 clic, position 48.65 ; requêtes `harnais chien petite taille`, `harnais pour petit chien` | Traité | Faible maturité mais intention commerciale claire ; améliorer le match `petite taille` | SEO title : `Harnais Petit Chien | Petite Taille` ; meta 152 caractères sur petits gabarits sensibles |
| `/collections/harnais-chien-voiture` | GSC direct : 19 impressions, 0 clic, position 37.16 ; requêtes `harnais chien voiture`, `harnais pour chien en voiture` ; collection contenant surtout des ceintures/attaches | Traité | Ne pas abandonner `harnais` car GSC le remonte, mais intégrer `ceinture` car c'est l'offre réelle | SEO title : `Harnais & Ceinture Chien Voiture` ; meta 152 caractères sur chien à sa place et pas d'attache au collier |
| `/collections/accessoires` | GSC direct : 5 impressions, 0 clic, position 22.4 ; audit public : title trop long, meta courte | Traité léger | Page faible en données GSC mais utile pour soutenir les accessoires et la promenade | SEO title : `Accessoires Chien | Promenade Sûre` ; meta 153 caractères sur promenade, sécurité, contrôle et gabarit |

Vérification post-publication : les 10 pages servent bien un title public sous 60 caractères avec `– Harnais chien expert` ajouté par le thème, des metas entre 151 et 157 caractères, et un H1 unique.

Leçon : avant de publier un batch title/meta, croiser l'audit technique avec l'export GSC direct quand il est disponible. PushRank reste utile pour détecter et structurer, mais l'export GSC complet priorise mieux les pages à fort potentiel de CTR.



## Session 2026-07-27 — batch 2 title/meta collections HCE avec GSC direct

Batch 2 publié sur Shopify après validation utilisateur. Ce batch poursuit la règle du batch 1 : partir des pages collection qui ressortent dans l'export Google Search Console direct, puis corriger les SEO titles/metas signalés comme trop courts ou faibles par l'audit public/PushRank. Les formulations ont été ajustées après discussion : ne pas choisir seulement des mots génériques comme `Actif` ou `Solide`, mais faire apparaître la douleur ou le bénéfice client quand c'est utile au clic.

Règle appliquée : le côté gauche du title garde le mot-clé GSC principal ; le côté droit après `|` porte une promesse courte orientée persona, sans surpromettre. Le champ Shopify ne contient pas la marque quand le thème l'ajoute déjà au rendu public.

| Page | Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- | --- |
| `/collections/harnais-cocker` | GSC direct : 123 impressions, 0 clic, position 12.34 ; requêtes `harnais cocker`, `harnais pour cocker`, `harnais chiot cocker` | Traité | Page proche page 1/2 sans clic ; doute utilisateur fort sur taille, chiot/adulte et confort du pelage | SEO title : `Harnais Cocker | Taille & Confort` ; meta 152 caractères sur poitrail, cou dégagé et taille ajustable |
| `/collections/harnais-border-collie` | GSC direct : 118 impressions, 0 clic, position 27.52 ; requêtes `harnais border collie`, `harnais chien border collie` | Traité | Race active ; le terme `Actif` était trop faible, la douleur utile est le contrôle/traction | SEO title : `Harnais Border Collie | Contrôle` ; meta 152 caractères sur chien actif, maintien, épaules libres et traction |
| `/collections/harnais-chien-handicape` | GSC direct : 79 impressions, 2 clics, position 13.09 ; requêtes `harnais chien hernie discale`, `harnais chien handicapé` | Traité prudemment | Intention sensible et proche page 1 ; besoin de soutien sans promesse médicale | SEO title : `Harnais Chien Handicapé | Soutien` ; meta 160 caractères avec soutien, portage, train arrière et avis vétérinaire conseillé |
| `/collections/harnais-labrador` | GSC direct : 73 impressions, 0 clic, position 14.71 ; requêtes `harnais labrador`, `harnais pour labrador` | Traité | Race puissante, proche page 1/2 sans clic ; douleur persona fréquente : chien qui tire | SEO title : `Harnais Labrador | Chien Qui Tire` ; meta 156 caractères sur maintien, épaules libres et contrôle si le chien tire fort |
| `/collections/harnais-malinois` | GSC direct : 70 impressions, 0 clic, position 20.86 ; requêtes `harnais pour malinois`, `harnais malinois` | Traité | Race puissante ; `Chien Puissant` parle mieux au besoin réel que `Solide` seul | SEO title : `Harnais Malinois | Chien Puissant` ; meta 154 caractères sur maintien, poignée selon modèle et contrôle stable |
| `/collections/harnais-chien-y` | GSC direct : 53 impressions, 0 clic, position 30.72 ; requête `harnais y` | Traité | La valeur spécifique d'un harnais en Y est la liberté de mouvement | SEO title : `Harnais Chien Y | Épaules Libres` ; meta 157 caractères sur coupe confortable, pression répartie et mouvement naturel |
| `/collections/harnais-berger-allemand` | GSC direct : 51 impressions, 0 clic, position 22.39 ; requêtes `harnais berger allemand`, `harnais pour berger allemand` | Traité | Race puissante ; l'angle `Contrôle` répond mieux à la douleur de balade qu'un bénéfice vague | SEO title : `Harnais Berger Allemand | Contrôle` ; meta 157 caractères sur maintien, confort et chien qui tire fort |
| `/collections/harnais-teckel` | GSC direct : 50 impressions, 0 clic, position 11.36 ; requêtes `meilleur harnais pour teckel`, `harnais teckel` | Traité | Page proche page 1 ; inquiétude spécifique : dos long et confort | SEO title : `Harnais Teckel | Dos & Confort` ; meta 151 caractères sur cou dégagé, poitrail et coupe adaptée au dos long |
| `/collections/harnais-tactique-chien` | GSC direct : 49 impressions, 1 clic, position 31.08 ; requêtes `harnais tactique pour chien`, `harnais tactique` | Traité | Intention d'achat liée au maintien, à la poignée et au chien puissant | SEO title : `Harnais Tactique Chien | Contrôle` ; meta 158 caractères sur sangles, maintien, poignée et sortie active maîtrisée |
| `/collections/harnais-a-poignee-chien` | GSC direct : 47 impressions, 0 clic, position 27.30 ; requêtes `harnais pour chien avec poignée`, `poignée contrôle chien` | Traité | La poignée porte une promesse claire : contrôle ponctuel et aide en passage difficile | SEO title : `Harnais Chien Poignée | Contrôle` ; meta 151 caractères sur contrôle ponctuel, maintien et promenade active |

Leçon associée : les mots à droite du séparateur `|` ne doivent pas être choisis seulement parce qu'ils sonnent SEO. Ils doivent compléter le mot-clé GSC par une douleur ou un bénéfice client : `chien qui tire`, `chien puissant`, `soutien`, `dos & confort`, `épaules libres`, `contrôle`.

Vérification Shopify admin : les 10 mutations `collectionUpdate` ont été acceptées sans `userErrors` et les champs `seo.title` / `seo.description` relus côté Admin correspondent aux valeurs publiées. La vérification publique peut être retardée par cache/propagation Shopify ; raisonner d'abord sur la valeur admin, puis relancer un crawl public ensuite.

Vérification publique ajoutée : les 10 pages affichent bien les metas publiées. Les titles publics décodés avec `– Harnais chien expert` restent entre 53 et 57 caractères ; l'entité HTML `&ndash;` peut gonfler artificiellement le comptage brut si elle n'est pas décodée.

## Session 2026-07-27 — batch 3 title/meta articles HCE avec GSC + PushRank

Batch 3 publié sur Shopify après validation utilisateur. Ce batch traite surtout des articles qui ressortent dans l'export Google Search Console direct, avec un contrôle PushRank page par page avant publication. Objectif : améliorer le CTR potentiel sans changer les URLs, les H1 visibles ni la structure des articles.

Règle appliquée : pour les articles et pages Shopify, les SEO title/meta sont stockés en métadonnées globales `title_tag` / `description_tag`. Pour les collections, le champ SEO natif est utilisé. Le champ saisi ne contient pas la marque quand le thème ajoute déjà `– Harnais chien expert` au rendu public.

| Page | Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- | --- |
| `/blogs/news/blogs-guide-taille-harnais-chien` | GSC direct : 250 impressions, 7 clics ; PushRank : 3 actions déjà done, 1 alerte slug trop long encore todo | Traité title/meta seulement | Le guide taille a déjà été restructuré ; ne pas changer l'URL maintenant sans plan de redirect | SEO title : `Taille Harnais Chien | Guide XS-XXL` ; meta 157 caractères sur mesure du poitrail, guide XS-XXL et réglage deux doigts |
| `/blogs/news/harnais-husky` | GSC direct : 140 impressions, 1 clic ; PushRank ignoré sur cette page | Traité léger | Article informatif avec impressions réelles ; renforcer le match taille/traction/sorties sportives | SEO title : `Harnais Husky | Guide Taille` ; meta 153 caractères sur coupe solide, réglage, traction et épaules libres |
| `/pages/guide-des-tailles-harnais-chien` | GSC direct : 126 impressions, 0 clic ; aucun champ meta description côté Shopify | Traité prudemment | Risque de cannibalisation avec l'article guide ; correction limitée à la meta manquante | Title public conservé ; meta créée : 150 caractères sur mesure du poitrail, tour de cou et choix entre deux tailles |
| `/blogs/news/harnais-pour-golden-retriever-quel-modele-choisir-guide-2026` | GSC direct : 62 impressions, 3 clics ; PushRank decay `quelle taille de harnais pour un golden retriever` | Traité et passé done PushRank | Article race utile pour soutenir la collection Golden ; requête taille à forte intention d'achat | SEO title : `Harnais Golden Retriever | Guide` ; meta 158 caractères sur modèle solide, mesure du poitrail et chien qui tire |
| `/blogs/news/chien-tire-en-laisse` | GSC direct : 56 impressions, 1 clic ; PushRank déjà done | Traité title uniquement | Article support stratégique vers anti-traction ; douleur claire `chien qui tire` | SEO title : `Chien Qui Tire En Laisse | Solutions` ; meta existante conservée car déjà alignée persona |
| `/blogs/news/harnais-cocker` | GSC direct : 53 impressions, 0 clic ; PushRank decay `harnais chiot cocker` | Traité et passé done PushRank | Requête race + chiot ; besoin fort de taille/confort | SEO title : `Harnais Cocker | Guide Taille` ; meta existante conservée, déjà complète sur cocker, chiot et anti-traction |
| `/blogs/news/harnais-chien-qui-tire-fort` | GSC direct : 52 impressions, 0 clic ; PushRank ignoré | Traité title uniquement | Douleur persona très directe ; title précédent trop long et moins cliquable | SEO title : `Harnais Chien Qui Tire Fort` ; meta existante conservée car déjà centrée anti-traction |
| `/blogs/news/harnais-bouledogue-francais` | GSC direct : 40 impressions, 1 clic ; PushRank decay `taille harnais bouledogue francais` | Traité et passé done PushRank | Race sensible, respiration/cou délicat ; éviter les promesses médicales | SEO title : `Harnais Bouledogue Français | Guide` ; meta 153 caractères sur cou libre, respiration et chien qui tire |
| `/blogs/news/harnais-berger-australien` | GSC direct : 40 impressions, 3 clics ; PushRank decay `harnais berger australien` | Traité et passé done PushRank | Article race actif ; garder la requête principale et guider vers types Y/H/anti-traction | SEO title : `Harnais Berger Australien | Guide` ; meta existante conservée car déjà riche sémantiquement |
| `/collections/harnais-beagle` | GSC direct : 39 impressions, 0 clic ; PushRank decay `harnais beagle` et `harnais pour beagle` | Traité et 2 actions passées done PushRank | Collection commerciale race, impressions sans clic ; besoin d'un bénéfice taille/confort | SEO title : `Harnais Beagle | Taille & Confort` ; meta 151 caractères sur chien actif, poitrail, cou dégagé et sorties où il suit les odeurs |

Vérification post-publication : les 10 URLs répondent en 200. Les titles publics décodés avec `– Harnais chien expert` font 50 à 59 caractères. Les metas font 150 à 159 caractères. Les actions PushRank liées à Golden, Cocker, Bouledogue Français, Berger Australien et Beagle ne ressortent plus en todo.

Point laissé ouvert : l'alerte PushRank `slug trop long` du guide taille reste volontairement en todo. Une modification d'URL doit être traitée à part avec analyse de risque, redirect 301 et contrôle de cannibalisation.

## Session 2026-08-08 — premier lot via [[project_seo_harnais_workspace]], titres produits (faux positif) + template meta description policies

Premier lot exécuté depuis le nouveau workspace `~/seo-harnais`. 8 opportunités `high` priority traitées.

**Titre Google manquant (3 produits, faux positif PushRank)** : `laisse-tactique-amortissante-double-poignee`, `harnais-chiot-respirant-multicolore`, `harnais-tactique-chien-pochettes` avaient déjà un `seo.title`/`seo.description` correct en admin ET publiés (vérifié en direct). Confirme le pattern déjà noté en session 2026-07-27 batch 4 : une correction faite pendant une session où le connecteur PushRank devient indisponible reste en `todo` côté PushRank tant que le statut n'est pas repassé manuellement. **Règle renforcée** : avant de "corriger" un `quick_win` de type titre/meta manquant, toujours vérifier l'état admin réel — si déjà correct, fermer l'opportunité sans y retoucher plutôt que de la retraiter.

**Résumé Google manquant (5 pages `/policies/*`)** : contrairement à l'hypothèse initiale ("juste un champ à remplir"), Shopify n'expose **aucun champ SEO description sur l'objet `ShopPolicy`** (GraphQL Admin API) et le thème (`wildone-final-theme`, live) n'affichait strictement aucune balise `<meta name="description">` sur le template `policy` (`request.page_type == 'policy'`), quel que soit le contenu du `body` de la policy. Root cause = template, pas contenu.

**Correction appliquée** : ajout dans `layout/theme.liquid` d'un fallback `page_description` par `case request.path` pour les 5 policies (`privacy-policy`, `refund-policy`, `terms-of-service`, `terms-of-sale`, `legal-notice`), avec des descriptions rédigées à la main — pas d'auto-troncature du `body`. Sauvegarde de l'asset original dans `seo-harnais/reports/backups/2026-08-08_theme-liquid_AVANT_meta-policy.liquid` avant déploiement.

**Pourquoi rédigé à la main plutôt qu'auto-généré depuis le `body`** : en prévisualisant une troncature automatique du `body` de chaque policy, le texte obtenu exposait du contenu non finalisé directement dans le body Shopify — voir alerte séparée ci-dessous. Une auto-génération aurait publié ce contenu cassé dans le snippet Google.

**Vérification** : 3/5 pages (`refund-policy`, `terms-of-service`, `legal-notice`) ont affiché la nouvelle meta immédiatement après déploiement de l'asset. 2/5 (`privacy-policy`, `terms-of-sale`) sont restées sur l'ancien rendu (`meta` absente) plusieurs dizaines de secondes après — cause identifiée via l'en-tête `etag: page_cache:...:PolicyDetailsController:...` : Shopify a une couche de cache serveur propre au contrôleur des pages policy, indépendante du déploiement de thème (qui lui-même n'a pas de cache côté Cloudflare, `cf-cache-status: DYNAMIC`). **Règle candidate** : sur les pages `/policies/*` spécifiquement, prévoir un délai de propagation plus long que pour collections/produits/articles avant de valider visuellement une correction de thème. Confiance 70% (observé une seule fois, à confirmer sur un futur déploiement theme.liquid touchant ces pages).

**Suite du lot, même session** : le reste des opportunités `high` todo (9 restantes après le premier passage) a révélé le même pattern de faux positifs à plus grande échelle — sur les 3 produits déjà corrigés (titre+meta), PushRank avait aussi des opportunités séparées "H1 manquant" et "résumé manquant" non fermées, alors que H1 et meta étaient déjà corrects en production (vérifié en direct). **Règle renforcée** : PushRank crée une opportunité distincte par type de champ (title/meta/H1) même sur la même URL ; corriger une URL ne ferme pas automatiquement les autres opportunités liées à cette même URL — bien vérifier `pageUrl` en filtrant plutôt que de supposer qu'une correction couvre tout.

**`content_creation` "ceinture chien voiture" — résolu par évolution du catalogue, mais H1 collection à corriger (catch d'Arezki)** : en session 2026-07-25 cette opportunité était volontairement laissée `todo` faute d'angle produit dédié. Au 2026-08-09, deux produits actifs existent désormais (`ceinture-chien-voiture-elastique`, `ceinture-chien-voiture-2-en-1`, H1 exact-match confirmés), et la collection `harnais-chien-voiture` a déjà un `seo.title` optimisé "Harnais & Ceinture Chien Voiture" (batch 1, session 2026-07-27). Fermé sans créer de nouvelle page — décision maintenue.

Mais Arezki a repéré que le **H1 réellement affiché** sur cette collection restait "Harnais chien voiture" (le `seo.title` ne concerne que le `<title>`, pas le H1 visible) : `collection.title` est utilisé en dur pour le H1 dans `sections/collection-seo-test-intro.liquid`, sans override possible — contrairement au texte d'intro qui a déjà un mécanisme de metafield (`custom.intro_text`). **Correction appliquée** : ajout du même pattern d'override pour le H1 (`collection.metafields.custom.seo_heading | default: collection.title`), 100% rétrocompatible (aucun changement si le metafield n'est pas défini). Metafield posé sur cette collection avec la valeur "Harnais & Ceinture Chien Voiture" (alignée sur le `seo.title` existant). **Ce mécanisme est réutilisable sur toute autre collection utilisant cette section** si un futur écart H1/intention de recherche est détecté.

**Leçon générale** : une opportunité `content_creation` laissée ouverte doit être revérifiée périodiquement — le catalogue évolue plus vite que le nettoyage des opportunités PushRank. Et surtout : `seo.title`/`seo.description` corrigés ne garantissent pas que le **H1 visible** suit — toujours vérifier le rendu réel de la page, pas seulement les champs SEO admin, avant de considérer un écart de mot-clé comme résolu.

**`/cart` — recommandation PushRank écartée (erreur de pertinence)** : PushRank recommande une meta description sur `/cart`. Décision : `ignored`, pas traité. Une page panier n'a pas de contenu unique justifiant une meta description marketing, et `/cart` (sans slash final) n'est même pas couverte par le `Disallow: /cart/` du robots.txt actuel — donc théoriquement indexable, ce qui est le vrai problème sous-jacent (elle ne devrait probablement pas être indexable du tout). Un `noindex` serait le correctif pertinent, mais c'est une opération sensible (catégorie "modification d'indexation", validation utilisateur requise avant d'agir) — non traité de façon autonome, à proposer explicitement si le sujet revient.

**Piège Shopify découvert au passage** : la mutation `shopPolicyUpdate` (GraphQL Admin API) peut être refusée avec `userErrors: "Automatic management for Privacy Policy must be turned off in order to make changes."`. La Politique de confidentialité peut avoir une case "gestion automatique" activée (Réglages > Politiques côté admin UI) qui bloque toute écriture via API tant qu'elle est active — et ce toggle n'est pas exposé comme champ dans le type `ShopPolicy` (`body/title/type/url/translations` seulement, rien pour le lire ou le changer via GraphQL). Si cette erreur apparaît, la seule solution est que le marchand désactive la gestion automatique dans l'UI admin avant toute correction API.

## Session 2026-07-27 — batch 4 title/meta articles et pages HCE

Batch 4 publié sur Shopify après validation utilisateur. Ce batch cible surtout des articles/pages avec title public trop long, meta trop courte/longue ou mauvais title SEO, en croisant GSC direct, audit public et PushRank quand l'action était visible avant publication.

| Page | Signal détecté | Décision prise | Raison SEO/business | Changement appliqué |
| --- | --- | --- | --- | --- |
| `/blogs/news/voyager-train-chien-sncf` | GSC direct : 31 impressions, 1 clic, position 8.97 ; title public 73 caractères, meta 142 | Traité title/meta | Page déjà proche haut de SERP ; clarifier l'intention `train avec chien` et SNCF sans title trop long | SEO title : `Train Avec Chien | SNCF 2026` ; meta 158 caractères sur règles SNCF, sac/muselière, tarifs et voyage sans mauvaise surprise |
| `/blogs/news/harnais-anti-fugue-pour-chien-comment-empecher-votre-chien-de-sechapper` | GSC direct : 27 impressions, 1 clic, position 8.37 ; PushRank decay actif ; title 92, meta 136 | Traité | Page informationnelle proche page 1, liée à une intention équipement anti-fugue | SEO title : `Harnais Anti-Fugue Chien` ; meta 150 caractères sur causes de fuite, coupe sécurisée et réglage |
| `/blogs/news/harnais-y-h-t-comparatif` | GSC direct : 26 impressions, 1 clic, position 9.77 ; title 78, meta 133 | Traité | Comparatif utile pour choisir entre coupes ; renforcer clarté du résultat Google | SEO title : `Harnais Y H ou T | Comparatif` ; meta 155 caractères sur épaules, maintien, usages et choix de coupe |
| `/blogs/news/comment-attacher-son-chien-en-voiture-loi-equipements-et-conseils-2026` | GSC direct : 22 impressions, 1 clic, position 6.86 ; PushRank decay actif ; title 78, meta 166 | Traité | Page très proche haut de SERP ; besoin de réponse claire loi/sécurité sans surcharge | SEO title : `Chien En Voiture | Loi & Sécurité` ; meta 158 caractères sur loi, ceinture, harnais, caisse/grille et trajet plus serein |
| `/blogs/news/harnais-cavalier-king-charles` | GSC direct : 21 impressions, 1 clic, position 6.71 ; PushRank decay `harnais pour cavalier king charles`; title 80, meta 145 | Traité | Article race proche haut de SERP ; title trop long, requête race claire | SEO title : `Harnais Cavalier King Charles` ; meta 151 caractères sur cou sensible, taille et frottements adulte/chiot |
| `/blogs/news/harnais-chiot` | GSC direct : 24 impressions, 2 clics ; requêtes `harnais chiot 2 mois`, `harnais chiot`; meta 147 | Traité léger | Article support pour la collection chiot ; améliorer title/meta sans changer l'article | SEO title : `Harnais Chiot | Guide Taille` ; meta 152 caractères sur âge, taille, habituation, modèle léger dès 8 semaines |
| `/blogs/news/vivre-avec-chien-handicape` | GSC direct : 10 impressions, 2 clics ; PushRank decay actif ; title 81, meta 167 | Traité prudemment | Sujet sensible ; garder promesse d'aide quotidienne sans promesse médicale | SEO title : `Chien Handicapé | Guide Vie` ; meta 150 caractères sur sorties, soutien, rampes, suivi santé et avis vétérinaire |
| `/pages/contact` | GSC direct : 26 impressions, 0 clic, position 4.77 ; title public erroné affichant FAQ | Traité | Mauvais signal utilisateur et Google : une page Contact ne doit pas apparaître comme FAQ | SEO title : `Contact | Aide & Commande` ; meta 153 caractères sur taille, commande, livraison, choix de harnais et WhatsApp |
| `/pages/faq` | GSC direct : 21 impressions, 0 clic, position 4.86 ; title trop court, meta auto extraite 320 | Traité | Page aide proche haut de SERP mais snippet trop brut ; créer des champs SEO propres | SEO title : `FAQ Harnais Chien | Aide` ; meta 157 caractères sur taille, choix, livraison, retours et commande |
| `/blogs/news/harnais-berger-allemand` | GSC direct : 20 impressions, 0 clic, position 10.05 ; PushRank decay `harnais pour berger allemand` et `harnais pour chien berger allemand`; title 74 | Traité | Article race proche page 1 ; renforcer bénéfice contrôle sans gêner épaules | SEO title : `Harnais Berger Allemand | Guide` ; meta 154 caractères sur modèle solide, poitrail, chien puissant et épaules |

Vérification post-publication : les 10 URLs répondent en 200. Les titles publics décodés avec `– Harnais chien expert` font 47 à 56 caractères. Les metas font 150 à 158 caractères.

Statut PushRank : les corrections couvrent 6 opportunités PushRank vues avant publication (Anti-Fugue, Voiture, Cavalier King Charles, Chien handicapé, Berger Allemand x2), mais le connecteur PushRank n'était plus exposé au moment de passer les statuts en `done`. À retenter dès que l'outil redevient disponible.

