---
type: source
title: "Qu'est-ce que LLMs.txt et devriez-vous l'utiliser ? (Semrush)"
slug: semrush-llms-txt-guide
raw: "[[Qu’est-ce que LLMs.txt et devriez-vous l’utiliser]]"
source_url: "https://fr.semrush.com/blog/llms-txt/"
source_type: article
author: "[[semrush]]"
date_published: 2025-05-13
date_ingested: 2026-06-15
tags: [seo, ai-seo, technical-seo, llms-txt]
status: active
---

# LLMs.txt Guide — Summary

**One-liner:** LLMs.txt is a proposed standard (not yet used by OpenAI, Google, or Anthropic) that provides AI crawlers a curated Markdown index of your site's most important content — only 951 domains using it as of July 2025, and Google's John Mueller confirmed no AI system currently uses it. Worth experimenting, not prioritizing.

## Key takeaways

### What LLMs.txt is
- A Markdown file at site root (e.g., `yourdomain.com/llms.txt`) that tells AI crawlers which content to prioritize.
- Analogous to `robots.txt` (access control) and `sitemap.xml` (page discovery) — but specifically for LLM consumption.
- Problem it solves: (1) modern websites are JavaScript-heavy and hard for AI to read, (2) AI crawlers don't know which content is important and waste compute on low-value pages.

### Adoption reality
- Only **951 domains** using llms.txt as of July 2025 (NerdyData data) — a tiny fraction of the web.
- **Google's John Mueller** confirmed on Bluesky: *"For info, no AI system currently uses llms.txt."*
- OpenAI, Google, Anthropic have NOT officially announced they follow these files.
- Anthropic has a llms.txt on their own site → suggests openness to the idea.
- Semrush deployed llms.txt on Search Engine Land to test impact; will report findings.

### File structure (Markdown)
```markdown
# Company Name
> Brief description of what your company does

## Products
- [Product 1](https://example.com/product-1): Description of this product
- [Product 2](https://example.com/product-2): Description of this product

## Documentation
- [Getting started](https://example.com/docs/getting-started): Intro to our platform
- [API Reference](https://example.com/api): Full API documentation
```
Key Markdown elements:
- `#` H1 title, `##` H2 sections, `>` description/blockquote
- `-` bullet lists, `[text](url)` hyperlinks, `:` inline descriptions

### Brand examples
| Brand | Focus | Structure |
|---|---|---|
| Hugging Face | Dev documentation | Multi-level headings + code examples + extensive links; comprehensive KB feel |
| Vercel | Dev documentation | Descriptive frontmatter lines (title:, description:, tags:) + clear sections + step-by-step code |
| Zapier | Dev documentation | Simple structure — mostly a long list of links with descriptions |
| Cal.com | Dev documentation | Top headings then very long plain link list, no sub-sections |

All valid as long as Markdown syntax is correct — structure is discretionary.

### Should you use it?
- **Probably not yet**, unless you want to experiment.
- No confirmed adoption by major AI platforms.
- If you do: keep pages product, blog (current), pricing, about, contact. Place at domain root. Update regularly.

## Connections
- Updates [[llm-txt]] (existing concept page): adds John Mueller quote, 951 domains stat, brand examples table, current adoption reality.
- LLMs.txt is to AI crawlers what robots.txt is to Google → extends [[ai-seo]] technical layer.
- Low-cost experiment = worth flagging as a future signal, even if impact not proven yet.
