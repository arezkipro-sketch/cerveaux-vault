---
title: "Hreflang — Référencement international multilingue"
slug: hreflang
page-type: concept
domain: seo
tags: [seo, international, multilingue, hreflang, technique]
sources:
  - "[[reussir-referencement-web-andrieu-2020]]"
related:
  - "[[duplicate-content]]"
  - "[[canonical-tag]]"
  - "[[xml-sitemap]]"
  - "[[reussir-referencement-web-andrieu-2020]]"
---

# Hreflang

Attribut HTML (ou entrée sitemap) indiquant à Google la langue et le pays cible d'une page. Empêche que les versions linguistiques soient traitées comme du contenu dupliqué.

## Syntaxe HTML
```html
<link rel="alternate" hreflang="fr-FR" href="https://exemple.com/fr/page/" />
<link rel="alternate" hreflang="fr-BE" href="https://exemple.com/be/page/" />
<link rel="alternate" hreflang="en-GB" href="https://exemple.com/en/page/" />
<link rel="alternate" hreflang="x-default" href="https://exemple.com/page/" />
```

## Règles clés
- Chaque page doit pointer vers **toutes ses variantes** (y compris elle-même)
- `x-default` = version de repli quand aucune autre ne correspond
- Doit être **réciproque** : si FR pointe vers EN, EN doit pointer vers FR
- Peut être implémenté dans `<head>`, dans le sitemap XML, ou via HTTP header

## Quand utiliser
- Site multilingue (même langue, pays différents : fr-FR / fr-BE / fr-CH)
- Site multinational (langues différentes : fr / en / de / es)
- **Ne pas utiliser** pour des traductions partielles ou du contenu machine sans relecture

## Structures pour un site international (par ordre de recommandation)
1. **Répertoires** : `domaine.com/fr/` — recommandé (mutualise l'autorité)
2. **Sous-domaines** : `fr.domaine.com` — géolocalisation possible dans GSC
3. **ccTLD** : `domaine.fr` — signal géographique fort mais coûteux à maintenir
