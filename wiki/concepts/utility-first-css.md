---
type: concept
title: Utility-First CSS
slug: utility-first-css
tags:
  - frontend
  - css
  - methodology
  - ui
sources:
  - "[[raw/assets/tailwind-utility-reference]]"
source_count: 1
status: active
updated: 2026-06-14
---

# Utility-First CSS

**Definition:** A styling methodology where UI is built by composing many small, single-purpose CSS classes (each setting one property — `flex`, `p-4`, `text-center`) directly in markup, instead of writing semantic, component-scoped stylesheets. [[tailwind-css]] is its dominant implementation.

## What we know
- Designs are assembled from **atomic primitives** combined on an element, not from bespoke CSS rules → [[raw/assets/tailwind-utility-reference]].
- Relies on a **constrained design scale** (fixed spacing steps, a 50–950 color ramp) to keep ad-hoc styling consistent → [[raw/assets/tailwind-utility-reference]].
- Provides **escape hatches** (arbitrary `[...]` values) so the constrained scale doesn't block one-off needs → [[raw/assets/tailwind-utility-reference]].

## Relations
- Implemented by [[tailwind-css]].
- Trade-off cousin of component-scoped / semantic CSS (BEM, CSS Modules) — *(unsourced, candidate comparison page)*.

## Tensions / open questions
- Classic critique (verbose markup vs. no context-switching, smaller CSS) not yet sourced here — worth a dedicated source to balance the page.

## Sources
- [[raw/assets/tailwind-utility-reference]] — demonstrates the approach across every utility category.
