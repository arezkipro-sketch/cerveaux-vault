---
title: "Debugging common causes for slow loading in Shopify Liquid storefronts"
slug: shopify-debug-slow-loading
page-type: source-note
domain: seo
tags: [seo, technical-seo, performance, shopify, liquid, core-web-vitals, lcp, fcp, ttfb, ecommerce]
sources: []
related:
  - "[[shopify-liquid-performance]]"
  - "[[core-web-vitals]]"
  - "[[ttfb]]"
source-url: "https://performance.shopify.com/blogs/blog/debugging-common-causes-for-slow-loading-in-shopify-liquid-storefronts"
source-type: web-article
author: "Sia Karamalegos (performance.shopify.com)"
date-published: 2024-01-11
date-accessed: 2026-06-20
raw-file: "raw/assets/Debugging common causes for slow loading in Shopify Liquid storefronts.md"
---

# Debugging common causes for slow loading in Shopify Liquid storefronts

Article de Sia Karamalegos (performance.shopify.com). Guide de diagnostic de performance pour boutiques Shopify Liquid basé sur les données RUM (Real User Monitoring). Présente une méthode de triage par "directional clues" (lecture des gaps TTFB→FCP→LCP) puis liste les causes les plus fréquentes par métrique.

**Valeur spécifique :** première source du vault couvrant les causes concrètes et Shopify-spécifiques de lenteur de chargement. Apporte : la méthode RUM gap analysis comme outil de diagnostic, FCP comme métrique intermédiaire manquante dans le vault, et un catalogue des problèmes les plus fréquents sur les storefronts Liquid (Liquid complexe, anti-flicker, lazy-load image LCP, mega menus, popups, etc.).

## Thèse centrale

Plutôt que d'optimiser aveuglément 10 choses à la fois (comme le suggère un long audit Lighthouse), utiliser les données RUM pour identifier quel gap (TTFB/FCP/LCP) est le plus problématique, puis cibler les causes connues pour ce gap spécifique.

## Les 3 métriques de chargement

| Métrique | Définition | Seuil "good" |
|---|---|---|
| **TTFB** | Temps entre la requête et le premier octet reçu du serveur | < 0.8 s |
| **FCP** | Temps jusqu'au premier rendu de contenu à l'écran | < 1.8 s |
| **LCP** | Temps jusqu'au rendu complet du plus grand élément visible | < 2.5 s |

Elles ont le même point de départ (début de la requête) mais des points d'arrivée différents. La lecture des **gaps entre elles** oriente le diagnostic.

## Méthode : RUM gap analysis ("directional clues")

Lire les données RUM (ex : TREO sitespeed + CrUX) page type par page type (homepage, fiche produit, collection) et mobile vs desktop séparément.

| Pattern observé | Problème probable |
|---|---|
| TTFB lent + FCP/LCP rapides après | Problème de réponse serveur (ex : Liquid complexe) |
| TTFB rapide + FCP très lent + LCP juste après FCP | Problème de rendu initial (ex : anti-flicker snippet) |
| TTFB et FCP rapides + LCP bien plus tard | Problème spécifique à l'élément LCP (ex : lazy-load de l'image LCP) |
| TTFB lent + gaps FCP/LCP normaux | Rare sur Shopify Liquid — problème serveur passager |

Outil recommandé : **TREO sitespeed** (gratuit, utilise l'API CrUX publique).

## Causes fréquentes par métrique

### TTFB — 2 causes

**1. Liquid code complexe**
- Boucles imbriquées (loops dans loops) → rendu Liquid lent côté serveur
- Appel de données non nécessaires
- Exemple : centaines de vérifications de metadata produit sur une fiche
- **Diagnostic :** Theme Inspector Chrome Extension → flame graph → identifier nested loops
- **Remédiation :** simplifier le code ; ou architecture hybride (Liquid pour le contenu visible + JS asynchrone pour le reste)

**2. Problèmes serveur Shopify temporaires**
- Rare et hors du contrôle du développeur
- Signal : baisse de TTFB simultanée sur plusieurs boutiques Shopify
- Récupération rapide en général

### FCP — 5 causes

**1. Ressources render-blocking**
- Le navigateur pause le parsing HTML à chaque fichier CSS ou JS synchrone trouvé
- CSS above-the-fold = render-blocking intentionnel (utile)
- JS inutile au rendu = doit être différé (`defer`)
- **Diagnostic :** Lighthouse / PageSpeed Insights → audit "Eliminate render-blocking resources"

**2. Anti-flicker snippets**
- Utilisés pour les A/B tests (éviter le FOUC / FOOC)
- Cachent toute la page jusqu'à un trigger JS → impact fort sur FCP
- **Diagnostic :** FCP très tardif malgré HTML et CSS rapides dans le waterfall → chercher des scripts de type `googleoptimize.com` ou `visualwebsiteoptimizer.com`
- **Remédiation Liquid :** encapsuler dans un `{% if settings.enable_vwo %}` contrôlé par un toggle dans `config/settings_schema.json` → supprime complètement le code quand aucun test n'est actif

**3. Connexions vers de multiples domaines pour les assets critiques**
- Chaque domaine externe = DNS lookup + handshake SSL avant téléchargement
- **Diagnostic :** waterfall WebPageTest → compter les barres "nouvelles connexions" (orange/rose) avant FCP
- **Remédiation :** héberger les assets sur le CDN Shopify autant que possible ; `preconnect` pour les domaines inévitables

**4. Abus de preloads et fetchpriority="high"**
- Preloader des ressources déjà dans le HTML = inutile (le scanner du navigateur les trouve déjà)
- Trop de preloads → contention de bande passante → ralentit les ressources prioritaires
- Trop de `fetchpriority="high"` → le navigateur ne peut plus prioriser → tout est urgent = rien ne l'est
- **Règle pratique :** max 2 preloads et max 2 fetchpriority="high" (pas une règle absolue — toujours tester)
- **Diagnostic :** bookmarklet "Loading Priorities Scanner" (Sia Karamalegos)

**5. HTML excessif (mega menus doubles)**
- Mega menus avec mobile + desktop = markup dupliqué → milliers de DOM nodes supplémentaires
- Exemple documenté : 5 000+ nodes rien que pour la navigation (sur 6 800 total)
- **Diagnostic :** DevTools → `$0.querySelectorAll('*').length` sur l'élément sélectionné
- **Remédiation :** unifier mobile/desktop avec CSS ; ou Liquid pour le visible + JS asynchrone pour le reste

### LCP — 6 causes

**1. Lazy-loading de l'image LCP**
- L'image LCP ne charge qu'après l'IntersectionObserver → délai garanti
- **Impact mesuré :** +1.0 s de LCP médian sur les boutiques Shopify qui lazy-loadent l'image LCP
- **Diagnostic :** `<img loading="lazy">` ou `data-src` avec class `lazyloaded` sur l'image LCP
- **Remédiation Liquid :** utiliser `section.index` et le lazy loading par défaut de `image_tag` pour varier la stratégie selon la position above/below fold

**2. Transitions/animations sur l'image LCP**
- Fade-in ou blur-in → le navigateur considère l'image non "fully rendered" jusqu'à la fin de la transition → LCP retardé même si l'image est déjà téléchargée
- **Diagnostic :** WebPageTest → image téléchargée bien avant le LCP event ; filmstrip à 0.1s pour observer la transition ; DevTools → inspecter `opacity` et `transition` sur l'image ou son conteneur
- **Remédiation :** supprimer la transition sur l'image LCP

**3. Images découvertes tardivement**
- L'image est référencée dans un CSS (background-image) ou chargée via JS → le navigateur ne la découvre qu'après le parsing complet → "critical request chain"
- **Remédiation :** toujours utiliser `image_tag` dans les fichiers Liquid HTML pour les images LCP ; architecture HTML-first

**4. JavaScript pour le rendu**
- Frameworks JS (React, Vue) avec Liquid storefront = attente du download + exécution JS avant tout rendu
- **Diagnostic :** désactiver JS dans le navigateur → si la page ne se rend pas → JS rendering
- **Remédiation :** stratégie HTML-first ; JS pour les fonctionnalités dynamiques uniquement
- Note : utiliser un framework JS frontend avec Liquid = site plus lent + pire INP

**5. Cookie banners plus grands que le contenu principal**
- Pop-up cookies chargé via JS → arrive tard → si plus grand que le contenu réel → devient l'élément LCP
- **Remédiation :** réduire la taille du cookie banner pour qu'il reste sous la taille du vrai LCP

**6. Pop-ups email/promo avant interaction utilisateur**
- Modales newsletter qui s'affichent avant tout scroll → capturent l'événement LCP
- **Remédiation :** déclencher la modale uniquement après interaction (scroll) → la plupart des apps ont ce réglage

## Outils de diagnostic

| Outil | Usage |
|---|---|
| **TREO sitespeed** | Données CrUX (RUM) gratuites, comparaison par page type |
| **Theme Inspector** (Chrome Extension) | Flame graph du rendu Liquid, détection des boucles imbriquées |
| **Loading Priorities Scanner** (bookmarklet, Sia Karamalegos) | Scan rapide de tous les preloads et fetchpriorities |
| **Responsive Image Linter** (Chrome Extension) | Vérification des attributs `sizes` des images responsive |
| **WebPageTest** | Waterfall chart, filmstrip (jusqu'à 0.1s), analyse multi-step |
| **PageSpeed Insights / Lighthouse** | Audits render-blocking, CWV lab data |

## Voir aussi
- [[shopify-liquid-performance]] — concept opérationnel créé depuis cette source
- [[core-web-vitals]] — définitions LCP/INP/CLS + seuils
- [[ttfb]] — TTFB comme métrique serveur
