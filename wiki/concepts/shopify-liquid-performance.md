---
type: concept
title: "Shopify Liquid — Performance et débogage"
slug: shopify-liquid-performance
tags: [seo, technical-seo, performance, shopify, liquid, core-web-vitals, ecommerce]
sources: ["[[shopify-debug-slow-loading]]", "[[shopify-improve-store-performance]]"]
source_count: 2
status: active
updated: 2026-06-20
---

# Shopify Liquid — Performance et débogage

**Définition :** Ensemble des causes de lenteur spécifiques aux storefronts Shopify Liquid et des techniques pour les diagnostiquer et les corriger. S'appuie sur l'analyse des gaps entre TTFB, FCP et LCP (méthode RUM) pour cibler les optimisations.

**Note sur Liquid vs headless :** contrairement à certaines idées reçues, les storefronts Liquid Shopify sont très rapides côté serveur. Les problèmes viennent presque toujours du code du thème ou des applications tierces, pas de Shopify lui-même.

## Optimisations déjà intégrées dans Shopify (ne rien faire)

Les outils de scan tiers (Lighthouse, GTMetrix) suggèrent parfois des optimisations **déjà actives** sur Shopify. Ne pas perdre de temps sur ces recommandations — se concentrer sur le thème, les apps, et le code tiers.

| Optimisation | Shopify l'intègre nativement |
|---|---|
| CDN | CDN mondial Cloudflare, HTTP/2 |
| Browser caching | 1 an pour toutes les ressources cacheables |
| Gzip compression | CSS, JS, HTML, pages |
| Image CDN / WebP | Compression + redimensionnement automatiques |
| Minification CSS/JS | À la demande, automatique |

→ [[shopify-improve-store-performance]]

## Les 3 facteurs d'impact (ordre de priorité)

1. **Thème** — premier levier
2. **Apps installées** — chaque app charge des assets
3. **Code tiers manuel** — tag managers et leurs tags

→ [[shopify-improve-store-performance]]

## Méthode de diagnostic : RUM gap analysis

Principe : lire les données RUM (Real User Monitoring) pour identifier **quel gap** est problématique avant de tenter quoi que ce soit.

| TTFB | FCP | LCP | Problème ciblé |
|---|---|---|---|
| Lent | FCP/LCP rapides après | — | Serveur / Liquid complexe |
| Rapide | Très lent | Juste après FCP | Rendu initial (anti-flicker, render-blocking) |
| Rapide | Rapide | Bien plus tard | Élément LCP spécifique (lazy-load, transition, etc.) |

Outil recommandé : TREO sitespeed (données CrUX gratuites). Analyser chaque type de page (homepage, collection, fiche produit) et mobile vs desktop séparément.

## TTFB — Causes et remédiations

### Liquid complexe (cause principale)

Boucles imbriquées (loops dans loops) ou appel de données inutiles → rendu côté serveur lent.

**Diagnostic :** Theme Inspector Chrome Extension → flame graph → repérer les barres répétées dans des barres répétées (nested loops).

**Remédiations :**
- Simplifier le code Liquid (supprimer les données non utilisées)
- Architecture hybride : Liquid pour le contenu visible immédiatement → JS asynchrone pour le reste (ex : mega menu complet)

### Problèmes serveur Shopify

Rares, hors du contrôle du développeur. Signal : baisse simultanée sur plusieurs boutiques Shopify. Récupération rapide.

## FCP — Causes et remédiations

### Ressources render-blocking

Le navigateur pause le parsing HTML à chaque `<link>` CSS ou `<script>` synchrone.

- CSS above-the-fold = render-blocking **intentionnel** (ne pas toucher)
- JS non nécessaire au rendu → différer avec `defer`

```html
<script src="non-critical.js" defer></script>
```

**Diagnostic :** Lighthouse / PageSpeed Insights → audit "Eliminate render-blocking resources".

### Anti-flicker snippets (A/B tests)

Snippets qui cachent toute la page jusqu'à un trigger JS → FCP très retardé.

**Diagnostic :** FCP tardif malgré HTML/CSS rapides + scripts `googleoptimize.com` / `visualwebsiteoptimizer.com` dans le waterfall.

**Remédiation Liquid** : supprimer complètement le code hors tests actifs :

```json
// config/settings_schema.json
{
  "name": "Third parties",
  "settings": [{
    "type": "checkbox",
    "id": "enable_vwo",
    "label": "Enable VWO (A/B testing)",
    "default": false
  }]
}
```

```liquid
{% comment %} layout/theme.liquid {% endcomment %}
{% if settings.enable_vwo %}
  <!-- script A/B testing provider -->
{% endif %}
```

### Connexions vers de multiples domaines (assets critiques)

Chaque domaine = DNS lookup + SSL handshake avant téléchargement.

**Diagnostic :** waterfall WebPageTest → barres orange/rose "nouvelle connexion" avant FCP.

**Remédiations :**
- Héberger les assets sur le CDN Shopify autant que possible
- `<link rel="preconnect" href="https://domaine-externe.com">` pour les domaines inévitables

### Abus de preloads et fetchpriority="high"

Trop de preloads → contention de bande passante → les ressources prioritaires sont ralenties. Trop de `fetchpriority="high"` → le navigateur ne peut plus prioriser.

**Règle pratique :** ≤ 2 preloads + ≤ 2 `fetchpriority="high"` (toujours tester avant/après).

Ne pas preloader les ressources déjà dans le HTML — le scanner du navigateur les trouve seul.

**Diagnostic :** bookmarklet "Loading Priorities Scanner" (Sia Karamalegos).

### HTML excessif — double mega menu

Dupliquer le markup navigation mobile/desktop → milliers de DOM nodes.

**Diagnostic :** DevTools → sélectionner l'élément → `$0.querySelectorAll('*').length`

**Remédiations :**
- Unifier mobile/desktop avec CSS responsive
- Liquid pour le visible → JS pour le reste (tout en conservant au moins un menu côté serveur pour les bots)

## LCP — Causes et remédiations

### Lazy-loading de l'image LCP ← cause n°1

L'image ne charge qu'après l'IntersectionObserver → délai garanti.

**Impact mesuré sur Shopify :** +1.0 s de LCP médian.

**Diagnostic :**
```html
<!-- lazy natif -->
<img src="photo.jpg" loading="lazy">
<!-- lazy via librairie JS -->
<img data-src="photo.jpg" class="lazyloaded">
```

**Remédiation Liquid :** utiliser `section.index` pour détecter si la section est au-dessus du fold, et ne pas appliquer `loading="lazy"` sur l'image LCP.

### Transitions/animations sur l'image LCP

Fade-in ou blur-in → LCP retardé même si l'image est téléchargée.

**Diagnostic :** WebPageTest → image téléchargée bien avant le LCP event ; filmstrip à 0.1s ; DevTools → propriétés `opacity` et `transition` sur l'image ou son conteneur.

**Remédiation :** supprimer la transition sur l'image LCP. Les animations ont de la valeur, mais pas sur l'image LCP.

### Images découvertes tardivement

Image en `background-image` CSS ou chargée via JS → "critical request chain" → le navigateur ne la découvre qu'après parsing CSS/JS.

**Remédiation :** toujours utiliser `image_tag` Liquid dans les fichiers HTML pour l'image LCP.

### JavaScript pour le rendu (React/Vue avec Liquid)

Le navigateur attend le download + exécution JS avant tout rendu.

**Diagnostic :** désactiver JS → si la page ne se rend pas → JS rendering.

**Règle :** architecture HTML-first (Liquid rend le contenu visible), JS pour les fonctionnalités dynamiques. Utiliser React/Vue avec un storefront Liquid = lenteur garantie + pire INP.

Différer JS non critique :
```html
<script src="non-critical.js" defer></script>
```

Ne pas différer le JS nécessaire au rendu (A/B test) — ça aggraverait le problème.

### Cookie banner plus grand que le contenu principal

Pop-up chargé via JS tardivement → si plus grand que le vrai LCP → capture l'événement LCP.

**Remédiation :** réduire la taille du cookie banner.

### Pop-ups email/promo avant interaction

Modale newsletter avant scroll → capte le LCP.

**Remédiation :** déclencher après interaction (scroll). La plupart des apps ont ce réglage.

### Priorisation incorrecte

Même problème que pour FCP : trop de preloads → contention → l'image LCP est ralentie. Ou pas de `fetchpriority="high"` sur l'image LCP → le navigateur ne la priorise pas.

```html
<!-- Image LCP → fetchpriority="high" obligatoire -->
<img src="hero.jpg" fetchpriority="high" alt="...">
```

## INP — Responsivité (Interaction to Next Paint)

INP mesure la réactivité de la page aux interactions utilisateur. Seuil "good" : < 100 ms.

**Cause principale sur Shopify :** trop de JavaScript — code du thème + code des apps + code tiers / tag managers.

**Démarche :**
1. Identifier les pires offenseurs JS (voir performance.shopify.com : "3 ways to find your worst JavaScript offenders for page load")
2. Supprimer ou différer le JS non critique
3. Utiliser l'architecture HTML-first + JS uniquement pour les fonctionnalités dynamiques (voir section "JavaScript pour le rendu" ci-dessus)

**Recommandation générale :** ne pas utiliser de framework JS frontend (React, Vue) avec un storefront Liquid — lenteur garantie + pire INP.

→ [[shopify-improve-store-performance]]

## Workflow de troubleshooting en 3 étapes (vision marchand)

### 1. Vérifier le problème

- Tester depuis différents appareils et connexions
- Faire tester par d'autres personnes (exclure un problème local)
- Utiliser PageSpeed Insights pour des métriques précises

### 2. Identifier la cause

| Symptôme | Cause probable |
|---|---|
| Trop d'apps installées | Assets de multiples apps chargés |
| Images volumineuses | Nombreuses images haute qualité |
| Page blanche puis chargement d'un coup | Script lent — identifier avec DevTools |

### 3. Agir

- **Apps :** supprimer les apps non essentielles ; désinstaller ne supprime pas le code du thème → contacter le développeur pour nettoyage complet
- **Images :** JPG pour photos, PNG pour transparence ; redimensionner à la taille affichée
- **Thème :** passer à un thème optimisé si c'est lui la cause

→ [[shopify-improve-store-performance]]

## Récapitulatif — tableau de diagnostic rapide

| Symptôme | Cause probable | Outil de vérification |
|---|---|---|
| TTFB lent | Liquid complexe (boucles imbriquées) | Theme Inspector |
| FCP lent, TTFB OK | Anti-flicker snippet / render-blocking JS | Waterfall WebPageTest |
| FCP lent, beaucoup de domaines | Multi-domaine assets critiques | Waterfall WebPageTest |
| LCP lent, FCP OK | Lazy-load image LCP | DevTools / Priorities Bookmarklet |
| LCP lent, image déjà chargée | Transition/animation sur l'image LCP | Filmstrip WebPageTest 0.1s |
| LCP = cookie banner | Cookie banner trop grand | Observation visuelle |
| LCP = modale email | Pop-up avant interaction | Observation visuelle |
| Tout lent, JS désactivé = page vide | JS rendering (React/Vue) | Désactiver JS |

## Outils

| Outil | Gratuit | Usage |
|---|---|---|
| TREO sitespeed | Oui | Données RUM / CrUX par page type |
| **Web Performance Reports** (Shopify natif) | Oui | RUM natif dans l'admin Shopify — à utiliser en premier |
| Theme Inspector (Chrome) | Oui | Flame graph Liquid rendering |
| Loading Priorities Scanner (bookmarklet) | Oui | Scan preloads + fetchpriorities |
| Responsive Image Linter (Chrome) | Oui | Vérification `sizes` attribut |
| WebPageTest | Oui | Waterfall, filmstrip, multi-step |
| PageSpeed Insights / Lighthouse | Oui | Audits, scores lab + field |
| Chrome DevTools | Oui | Identifier les scripts lents (INP / page blanche) |

## Relations
- Contexte technique : [[core-web-vitals]] — seuils LCP/INP/CLS
- Métrique serveur : [[ttfb]] — TTFB comme signal crawl + UX
- Écosystème e-commerce : [[fiche-produit-seo]] — impact performance sur fiches produit

## Sources
- [[shopify-debug-slow-loading]] — guide de diagnostic complet, Sia Karamalegos (performance.shopify.com, 2024-01-11)
- [[shopify-improve-store-performance]] — guide officiel Shopify : optimisations natives, 3 facteurs d'impact, workflow 3 étapes, INP/JS excessif
