---
type: entity
entity_type: tool
title: Tailwind CSS
slug: tailwind-css
aliases:
  - Tailwind
  - TailwindCSS
tags:
  - frontend
  - css
  - tailwind
  - ui
sources:
  - "[[raw/assets/tailwind-utility-reference]]"
source_count: 1
status: active
updated: 2026-06-14
---

# Tailwind CSS

**Definition:** A CSS framework that styles markup through small, single-purpose **utility classes** applied directly in HTML (e.g. `flex`, `p-4`, `text-xl`, `bg-blue-500`) rather than hand-written stylesheets. It is the canonical implementation of [[utility-first-css]].

## What we know
- Provides atomic utilities across layout, spacing, typography, color, borders, shadows, and sizing → [[raw/assets/tailwind-utility-reference]].
- Uses a **fixed design scale**: rem-based spacing steps and an 11-shade (50–950) color ramp per color, with 500 as the base → [[raw/assets/tailwind-utility-reference]].
- Offers an **arbitrary-value escape hatch** with square brackets (`p-[17px]`, `bg-[#bada55]`, `bg-[var(--brand-color)]`) for one-off values outside the scale → [[raw/assets/tailwind-utility-reference]].
- Composes responsive/stateful designs from primitives; gradients and opacity have dedicated modifier syntax (`bg-black/75`, `bg-gradient-to-r`) → [[raw/assets/tailwind-utility-reference]].

## Relations
- Implements [[utility-first-css]].
- (Future) underpins component libraries like shadcn/ui — *(unsourced, candidate link)*.

## Tensions / open questions
- Version not stated in the reference; class names look like v3.x. v4 renamed gradient utilities. Confirm with a versioned source.

## Sources
- [[raw/assets/tailwind-utility-reference]] — core utility cheat-sheet.
