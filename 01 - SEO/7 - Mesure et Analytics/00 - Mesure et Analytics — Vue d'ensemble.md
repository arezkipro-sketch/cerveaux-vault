# Mesure et Analytics — Vue d'ensemble

Les outils de mesure sont à configurer AVANT de commencer le SEO — pas après.
Sans données, impossible de savoir ce qui fonctionne ni quoi corriger.

---

## 1 · Les 3 outils obligatoires

| Outil | Rôle | Gratuit |
|---|---|---|
| **Google Search Console (GSC)** | Visibilité dans Google : impressions, clics, positions, erreurs d'indexation | ✅ |
| **Google Analytics 4 (GA4)** | Comportement des visiteurs : trafic, pages vues, taux de rebond, conversions | ✅ |
| **Bing Webmaster Tools** | Même rôle que GSC mais pour Bing + ChatGPT (ChatGPT indexe via Bing) | ✅ |

---

## 2 · Google Search Console — ce qu'on surveille

**Setup :** soumettre sitemap.xml dès l'ouverture du site.

**Ce qu'on regarde chaque semaine :**

- **Impressions élevées + CTR faible** → ta page apparaît mais personne ne clique → title ou meta-description à retravailler en priorité
- **Positions 4–15** → quick wins : tu es proche du TOP 3, un enrichissement de contenu peut suffire
- **Erreurs de couverture** → pages bloquées par robots.txt, noindex accidentel, soft 404 → à corriger immédiatement
- **Rapport Core Web Vitals** → pages "à améliorer" ou "médiocres" → problème de vitesse
- **Rapport Liens** → tes backlinks gratuits, sans outils payants

**Règle opérationnelle :**
> Impressions > 100 + CTR < 2% = title/meta sous-optimisés → intervenir.
> Position 4–15 = enrichir le contenu + améliorer le maillage interne vers cette page.

---

## 3 · Google Analytics 4 — ce qu'on surveille

**Ce qu'on regarde chaque mois :**

- **Pages les plus visitées** → confirmer que le bon contenu attire le trafic
- **Taux de rebond par page** → une page avec beaucoup de rebond = contenu décevant ou mauvaise intention
- **Source du trafic** → organique vs direct vs réseaux sociaux → quelle proportion vient du SEO
- **Pages qui convertissent** → mettre en avant dans le maillage interne

---

## 4 · Bing Webmaster Tools — pourquoi c'est important

Bing indexe le web et ChatGPT utilise l'index de Bing pour ses réponses. Si ton site est dans Bing WMT :
- Soumission du sitemap → indexation plus rapide
- Bots IA non bloqués dans robots.txt (GPTBot, ClaudeBot, PerplexityBot)
- Ton contenu peut être cité par ChatGPT

**Setup :** bing.com/webmasters → ajouter le site → soumettre sitemap.xml

---

## 5 · Checklist de configuration (à faire une fois)

- [ ] Google Search Console configurée + propriété vérifiée
- [ ] Sitemap.xml soumis dans GSC
- [ ] GA4 installé sur le site (balise ou Shopify Analytics)
- [ ] Bing Webmaster Tools configuré + sitemap soumis
- [ ] robots.txt vérifié : GPTBot, ClaudeBot, PerplexityBot non bloqués

---

*Concepts détaillés dans le wiki : [[google-search-console]] · [[google-analytics-4]] · [[click-through-rate]] · [[xml-sitemap]] · [[robots-txt]]*
