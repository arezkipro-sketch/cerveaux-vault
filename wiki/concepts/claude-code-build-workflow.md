---
type: concept
title: "Workflow de build site web avec Claude Code"
slug: claude-code-build-workflow
tags: [claude-code, website-creation, freelance, design, frontend, workflow]
sources: ["[[bounceidc-google-maps-claude-code-loop]]"]
source_count: 1
status: active
updated: 2026-07-07
---

# Workflow de build site web avec Claude Code

**Définition :** Processus complet pour construire un site web d'aspect professionnel (qualité agence) avec Claude Code, en utilisant deux skills de design pour éliminer le "look AI générique". Conçu pour le contexte freelance où le site doit convaincre un propriétaire de commerce local en 40 secondes de vidéo.

## Ce qu'on sait (source : [[bounceidc-google-maps-claude-code-loop]])

### Setup initial (une seule fois)

1. Claude Pro ($20/mois) → télécharger l'app desktop → passer en mode code
2. Créer un dossier vide comme workspace, l'ouvrir dans l'app
3. Installer les deux skills depuis leurs liens GitHub :
   - **`frontend-design`** (Anthropic, officiel) — bannit les polices et layouts AI sur-utilisés, tourne en arrière-plan automatiquement
   - **`UI/UX Pro Max`** (communauté) — dizaines de styles UI, palettes et associations de polices appelables à la demande
   - Installation : coller les liens GitHub dans Claude Code → "Install this skill globally" / "Install this plugin using npm, globally" → Autoriser les modifications
4. Passer le sélecteur de mode en **auto mode** → Claude agit sans demander permission à chaque étape

### Récolte des références visuelles

Avant de coder : aller sur Dribbble, Awwwards ou Pinterest, chercher "modern [niche] website design", sauver 3-5 screenshots dans un dossier `/reference`. Objectif : montrer une direction, pas copier. Les images permettent à Claude de calibrer le niveau de sophistication visuelle attendu.

### Prompt de build

```
/ui-ux-pro-max

Build a single-page website for [BUSINESS TYPE + CITY,
ex: a family-run Thai restaurant in Austin].

Direction: [la vibe en propres mots — ex: warm, modern,
appetite-driven. PAS un look template générique.]

Sections dans l'ordre: hero, story, menu/services,
the space, contact. Une page, scroll de haut en bas.

J'attache des screenshots de référence depuis le dossier /reference.
Suis le feeling, ne les copie pas.

Tech stack: HTML/CSS/JS statique en fichier unique. Garder simple.

Avant d'écrire du code, pose-moi des questions de clarification.
```

**La dernière ligne est la phrase à la valeur la plus élevée du prompt.** Claude s'arrête, pose 5-7 questions sur le style, les sections, le ton et le niveau d'animation. Les réponses deviennent les fondations du site → moins de corrections après. La première version sort en ~10 minutes.

### Les 2 passes de polish

**Pass 1 — Grader honnêtement :**
```
Review this site against these criteria and be honest about what needs work:
- Typography (are we on overused AI fonts like Inter?)
- Color (restrained palette, 4-5 values max?)
- Hierarchy (does sizing guide the eye 1st, 2nd, 3rd?)
- Motion (intentional micro-interactions or static?)
- Mobile (designed for phones or just shrunk?)
- Copy (specific and sensory, or adjective soup?)
```

**Pass 2 — Rendre cher (batch, pas un par un) :**
```
The lower sections feel a bit generic. We don't need to make them busier,
just more expensive. Propose a batch of subtle micro-interactions and refinements
and apply them all at once.
```

**Pass mobile dédié :**
```
Decide what hides, tightens and resizes on small screens;
this is the version most people will see.
```

### Règle d'efficacité : une démo par niche

On build **une démo par niche** (ex: restaurants thaï), pas une démo par business. La même démo sert les 20 prospects de la liste. Après le build :
- Enregistrer une capture vidéo de 40 secondes (scroll desktop + mobile)
- Cette vidéo est la pièce jointe du message d'outreach

### Ne pas héberger avant le oui

Les screenshots et la vidéo suffisent à vendre. L'hébergement ($40-45/an avec domaine première année) ne se commande qu'après le deal signé.

**Erreur technique à éviter lors de l'upload :** zipper les fichiers *à l'intérieur* du dossier projet, pas le dossier lui-même. `index.html` doit être au niveau racine du zip.

### Stack recommandée

- **Format :** HTML/CSS/JS statique en **fichier unique** (simple à livrer, simple à héberger)
- **Hébergement :** $40-45/an avec domaine première année incluse
- **Skills :** frontend-design (Anthropic) + UI/UX Pro Max (communauté)

## Relations
- S'inscrit dans l'étape "Build" du [[freelance-web-loop]]
- Les leads viennent de [[prospection-google-maps]] (étape "Find")
- Output du workflow = démo + vidéo 40s → input de l'outreach (étape "Sell")

## Sources
- [[bounceidc-google-maps-claude-code-loop]] — setup complet, prompt de build, 2 passes polish, règle 1 démo/niche
