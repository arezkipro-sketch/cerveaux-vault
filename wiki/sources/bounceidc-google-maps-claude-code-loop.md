---
type: source-note
title: "Google Maps + Claude Code = $2,000 website deals. The complete loop."
slug: bounceidc-google-maps-claude-code-loop
page-type: source-note
domain: creation-site-web
tags: [freelance, claude-code, google-maps, prospection, outreach, local-business, pricing, website-creation]
sources: []
related: ["[[bounceidc]]", "[[prospection-google-maps]]", "[[freelance-web-loop]]", "[[claude-code-build-workflow]]"]
source-url: "https://x.com/bounceidc/status/2072654466403438983"
source-type: article
author: "[[bounceidc]]"
date-accessed: 2026-07-07
raw-file: "08 - Création de site web/1 - Prospection et Leads/01 - bounceidc-google-maps-claude-code-loop.md"
source_count: 0
status: active
updated: 2026-07-07
---

# Google Maps + Claude Code = $2,000 website deals. The complete loop.

## Overview

Article publié sur X (2026-07-02) par @bounceidc. Guide complet d'un business de création de sites web pour des commerces locaux, de la prospection à l'encaissement. Utilise Claude Code + skills de design pour produire des sites qualité agence à $20/mois de coût.

**Thèse centrale :** *"The build stopped being the hard half."* Ce qui était auparavant une compétence rare (développement + design) est maintenant accessible via Claude Code. La valeur se déplace vers le loop complet : trouver les clients → construire la démo → envoyer le bon message.

---

## La fenêtre d'opportunité (pourquoi maintenant)

3 choses ont convergé :
1. **Claude Code accessible à $20/mois** (Claude Pro) — le coût de build d'un site custom s'est effondré
2. **Les skills de design ont comblé le gap qualité** — avant eux, les sites AI avaient un look reconnaissable et bon marché. Avec `frontend-design` + `UI/UX Pro Max`, le rendu passe la barre des agences à 5 chiffres
3. **Les commerces locaux n'ont pas encore eu le memo** — ouvrir Google Maps dans n'importe quelle ville : des milliers de businesses profitables avec des sites de 2015, cassés sur mobile, ou sans site du tout

Coût effondré + gap qualité comblé + marché qui n'a pas encore réagi = la fenêtre. Elle reste ouverte jusqu'à ce qu'assez de gens exploitent ce loop.

---

## Le loop complet : 4 parties

### Partie 1 — Trouver les acheteurs sur Google Maps → [[prospection-google-maps]]

**Ce qu'on cherche :** pas des businesses qui ont besoin d'un site. Des businesses qui gagnent de l'argent et ont un mauvais site. Ce ne sont pas les mêmes.

**Les 4 filtres :**
1. **Niche où un site génère du CA** : restaurants, dentistes, salles de sport, med spas, artisans, immobilier. Pas les boutiques hobby.
2. **Note 4.4+ avec 50+ avis** → preuve qu'ils ont des clients et une trésorerie
3. **Site : daté, cassé sur mobile, ou inexistant**
4. **Ville assez grande** pour que la niche ait 20+ candidats

Construire une liste de 20 dans un tableur : nom du business, contact (email propriétaire ou Instagram), et une ligne sur ce qui ne va pas avec leur site actuel. Cette dernière colonne devient l'ouverture du message.

**Pourquoi 4.4+ et non les galériens** : un business en difficulté ne dépensera pas $1 500 pour un site. Un business qui tourne bien avec un site embarrassant sait déjà que c'est embarrassant. On ne crée pas la demande, on la capte.

---

### Partie 2 — Construire la démo avant qu'on la demande → [[claude-code-build-workflow]]

**Le mouvement central du système :** on ne pitch pas. On arrive avec le site déjà construit. Un message froid avec une démo finie est lu ; un message froid avec une promesse est supprimé.

**Setup (une fois) :**
1. Claude Pro sur claude.com → desktop app → mode code
2. Dossier vide comme workspace, ouvert dans l'app
3. Installer les deux skills depuis leurs liens GitHub :
   - `frontend-design` (Anthropic) : "Install this skill globally"
   - `UI/UX Pro Max` (communauté) : "Install this plugin using npm, globally"
4. Mode sélecteur → **auto mode** (Claude agit sans demander permission à chaque étape)

**Récolter des références visuelles :** 3-5 screenshots de Dribbble, Awwwards ou Pinterest qui correspondent à la direction (chercher "modern [niche] website design"). Les déposer dans un dossier `/reference`. On montre une direction, on ne copie pas.

**Prompt de build :**
```
/ui-ux-pro-max

Build a single-page website for [BUSINESS TYPE + CITY].

Direction: [la vibe en propres mots — ex: warm, modern, appetite-driven. PAS un look template générique.]

Sections dans l'ordre: hero, story, menu/services, l'espace, contact. Une page, scroll de haut en bas.

J'attache des screenshots de référence depuis le dossier /reference.
Suis le feeling, ne les copie pas.

Tech stack: HTML/CSS/JS statique en fichier unique. Garder simple.

Avant d'écrire du code, pose-moi des questions de clarification.
```

**La dernière ligne est la plus importante :** Claude s'arrête, pose 5-7 questions sur le style, les sections, le ton du texte et le niveau d'animation. Les réponses deviennent les fondations du site → moins de corrections après.

**2 passes de polish :**

Pass 1 — Grader :
```
Review this site against these criteria and be honest about what needs work:
- Typography (are we on overused AI fonts like Inter?)
- Color (restrained palette, 4-5 values max?)
- Hierarchy (does sizing guide the eye 1st, 2nd, 3rd?)
- Motion (intentional micro-interactions or static?)
- Mobile (designed for phones or just shrunk?)
- Copy (specific and sensory, or adjective soup?)
```

Pass 2 — Rendre cher :
```
The lower sections feel a bit generic. We don't need to make them busier, just more expensive.
Propose a batch of subtle micro-interactions and refinements and apply them all at once.
```

Terminer par un pass mobile dédié : "decide what hides, tightens and resizes on small screens; this is the version most people will see."

**Trick d'efficacité :** on construit **une démo par niche**, pas une par business. La démo restaurant thaï marche pour les 20 restaurants thaï de la liste. Enregistrer une capture d'écran de 40 secondes (desktop + mobile). Cette vidéo est la munition d'outreach.

---

### Partie 3 — Shipper seulement après le oui

Ne pas acheter d'hébergement pour les démos. Les screenshots et la vidéo suffisent à vendre. Quand le deal est signé :
- Hébergement + domaine première année : **$40-45**
- **Erreur classique :** quand on upload, zipper les fichiers *à l'intérieur* du dossier projet, pas le dossier lui-même. `index.html` doit être au niveau racine du zip.

---

### Partie 4 — L'outreach → [[freelance-web-loop]]

**L'email/DM :**
```
Sujet : made this for [Business Name]

Hi [Name], I redesign websites for [niche] in [city].
I already built a concept for [Business Name]. 40-second video attached.

Your current site [un problème précis : ne charge pas sur mobile / ne montre pas le menu / semble plus vieux que la nourriture].
This one fixes that.

If you like it, it's live on your domain this week.
Flat $[price], no subscriptions, no agency retainer.
If not, no hard feelings, the video's yours to keep.

[Your name]
```

**Règles qui font fonctionner ce message :**
- Mettre en avant la vidéo, pas les credentials
- Nommer **un problème précis** avec leur site actuel (la colonne du tableur)
- Prix fixe, formulé clairement
- Ne jamais dire "AI-built" — on vend l'outcome, pas la méthode. Le site a l'air cher ou non.

---

## Pricing et business model → [[freelance-web-loop]]

| Poste | Montant |
|---|---|
| Claude Pro (mois) | $20 |
| Hébergement + domaine (an) | $45 |
| **Coût total** | **$65** |
| One-pager, petit marché | $800 |
| One-pager, ville métropole | $2 000 |
| Care plan mensuel | $50/mois |
| **Marge premier deal** | **~90%+** |

**Care plan :** $50/mois (hébergement, modifications, mises à jour). 10 clients care plan = $500/mois de revenus récurrents pour quelques heures de travail.

**Ramp réaliste :** 20 envois → 3-6 réponses → 0-2 deals. La plupart des oui arrivent après le follow-up, pas le premier message. Un message de suivi 3 jours plus tard ("did the video land?") double approximativement le taux de réponse.

---

## Les 5 erreurs qui tuent 90% des tentatives

1. **Polir une démo une semaine au lieu d'envoyer.** La démo se vend à 90% de finition. Envoyer.
2. **Pitcher la technologie plutôt que l'outcome.** Les propriétaires n'achètent pas "site AI", ils achètent "les clients arrêtent de repartir de votre menu mobile cassé".
3. **Choisir des niches qu'on aime au lieu des niches qui paient.** Le disquaire préféré n'a pas de budget. Le med spa, oui.
4. **Pas de follow-up.** Un seul message ne suffit pas.
5. **Pricer à $200 pour se sentir en sécurité.** Ça signal de la camelote et attire les pires clients. Le travail ressemble à $2 000. Charger comme tel.

---

## Ce que cette source apporte au vault

| Concept | Statut avant | Statut après |
|---|---|---|
| Prospection locale via Google Maps (4 filtres) | ❌ Absent | ✅ [[prospection-google-maps]] créé |
| Loop complet find→build→ship→sell | ❌ Absent | ✅ [[freelance-web-loop]] créé |
| Workflow Claude Code pour site client | ❌ Absent | ✅ [[claude-code-build-workflow]] créé |
| Pricing one-pager + care plan | ❌ Absent | ✅ Intégré dans [[freelance-web-loop]] |

## Sources
- [[bounceidc]] — auteur de l'article
