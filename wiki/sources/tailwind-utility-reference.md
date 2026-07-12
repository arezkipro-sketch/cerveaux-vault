---
type: source
title: Tailwind CSS Utility Reference
slug: tailwind-utility-reference
raw: "[[raw/assets/tailwind-utility-reference]]"
author: (ckm-ui-styling skill reference)
date_published: 2026-06-14
date_ingested: 2026-06-14
tags:
  - frontend
  - css
  - tailwind
  - ui
  - reference
status: active
---

# Tailwind CSS Utility Reference — Summary

**One-liner:** A cheat-sheet of the core Tailwind CSS utility classes — layout, spacing, typography, color, borders, shadows, sizing — that demonstrates the [[utility-first-css]] approach used by [[tailwind-css]].

## Key takeaways
- **Layout** is composed from atomic classes: `flex`/`grid` containers + axis controls (`justify-*`, `items-*`), `gap-*`, positioning (`relative`/`absolute`/`sticky`), and `z-*`.
- **Spacing** uses a fixed scale (rem-based): `0, px, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 24` → `p-*`/`m-*`/`space-*`. `mx-auto` centers; negative margins via `-mt-4`.
- **Typography** scale `text-xs`→`text-5xl`, weights `font-thin`→`font-black`, plus alignment, leading, transform, decoration, and overflow (`truncate`, `line-clamp-3`).
- **Color** system: each color has 11 shades (50–950, 500 = base). Opacity modifier syntax `bg-black/75`, gradients `bg-gradient-to-r from-* via-* to-*`.
- **Borders / radius / shadows** follow the same atomic pattern; colored shadows via `shadow-lg shadow-blue-500/50`.
- **Escape hatches**: arbitrary values in square brackets — `p-[17px]`, `bg-[#bada55]`, `bg-[var(--brand-color)]`, `grid-cols-[1fr_500px_2fr]`.
- Sizing fractions/keywords: `w-1/2`, `w-full`, `w-screen`, `max-w-md`, `min-h-screen`; aspect ratios `aspect-video`, `aspect-[4/3]`.

## Notable claims (with locations)
- "Each color has 11 shades (50–950)" with 500 as the base color. — *(§ Colors → Color Scale)*
- Arbitrary values via `[...]` cover spacing, color, size, CSS vars, and complex grid templates. — *(§ Arbitrary Values)*

## Entities introduced or touched
- [[tailwind-css]] — the framework this reference documents.

## Concepts introduced or touched
- [[utility-first-css]] — the styling philosophy the whole reference embodies.

## Connections / contradictions
- First source in a new **frontend/UI** domain for this vault — no overlap with existing knowledge-management pages, no contradictions.
- Pairs naturally with future sources on design tokens, component libraries (shadcn/ui), or responsive design.

## Open questions
- Tailwind version assumed? Class names match v3.x (`bg-gradient-to-*`); v4 renamed some (`bg-linear-to-*`). Confirm on next Tailwind source.
- No responsive (`md:`/`lg:`) or state (`hover:`/`focus:`) variant prefixes covered here — gap to fill with another source.
