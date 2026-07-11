# Build — Créer la démo avec Claude Code

> Source : @bounceidc — "Google Maps + Claude Code = $2,000 website deals" (2026-07-02)

**Le mouvement central :** on ne pitch pas. On arrive avec le site déjà construit. Un message froid avec une démo finie est lu ; un message froid avec une promesse est supprimé.

---

## Setup initial (une seule fois)

1. Claude Pro ($20/mois) → télécharger l'**app desktop** → passer en **mode code**
2. Créer un dossier vide comme workspace, l'ouvrir dans l'app
3. Installer les deux skills depuis leurs liens GitHub :
   - **`frontend-design`** (Anthropic, officiel) → "Install this skill globally" — bannit les polices et layouts AI sur-utilisés, tourne en arrière-plan automatiquement
   - **`UI/UX Pro Max`** (communauté) → "Install this plugin using npm, globally" → Autoriser les modifications — dizaines de styles UI, palettes et associations de polices
4. Passer le sélecteur en **auto mode** → Claude agit sans demander permission à chaque étape

---

## Récolter les références visuelles

Avant de coder : aller sur Dribbble, Awwwards ou Pinterest → chercher "modern [niche] website design" → sauver 3-5 screenshots dans un dossier `/reference`.

On montre une direction, on ne copie pas.

---

## Prompt de build

```
/ui-ux-pro-max

Build a single-page website for [BUSINESS TYPE + CITY,
ex: a family-run Thai restaurant in Austin].

Direction: [la vibe en propres mots — ex: warm, modern,
appetite-driven. PAS un look template générique.]

Sections dans l'ordre: hero, story, menu/services,
the space, contact. Une page, scroll de haut en bas.

J'attache des screenshots de référence depuis /reference.
Suis le feeling, ne les copie pas.

Tech stack: HTML/CSS/JS statique en fichier unique.

Avant d'écrire du code, pose-moi des questions de clarification.
```

**La dernière ligne est la plus importante.** Claude pose 5-7 questions sur le style, les sections, le ton et le niveau d'animation. Répondre avec précision — ces réponses deviennent les fondations du site. Première version en ~10 minutes.

---

## Les 3 passes de polish

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

**Pass 2 — Rendre cher (tout en batch, pas un par un) :**
```
The lower sections feel a bit generic. We don't need to make them busier,
just more expensive. Propose a batch of subtle micro-interactions and
refinements and apply them all at once.
```

**Pass mobile dédié :**
```
Decide what hides, tightens and resizes on small screens;
this is the version most people will see.
```

---

## Règles d'efficacité

- **Une démo par niche**, pas une par business — la démo restaurant thaï sert les 20 restaurants thaï de la liste
- Enregistrer une **capture vidéo de 40 secondes** (scroll desktop + mobile) → c'est la munition d'outreach
- **Ne pas héberger avant le oui** — screenshots + vidéo suffisent à vendre
- Erreur technique à l'upload : zipper les fichiers *à l'intérieur* du dossier, pas le dossier lui-même. `index.html` doit être à la racine du zip.

---

## Stack recommandée

- Format : HTML/CSS/JS statique en **fichier unique**
- Hébergement : $40-45/an avec domaine première année incluse (commander seulement après le deal)
