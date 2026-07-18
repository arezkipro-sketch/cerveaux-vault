# Log — Cerveaux Wiki

Chronological, append-only. Header format: `## [YYYY-MM-DD] <op> | <title>` where `<op>` ∈ {ingest, query, lint, schema, maint}. Newest at the bottom.

Quick view of recent activity: `grep "^## \[" log.md | tail -5`

---

## [2026-06-14] schema | Vault bootstrapped
- Created `CLAUDE.md` (schema + operating rules), `index.md`, `log.md`, `wiki/overview.md`.
- Established folder tree: `raw/` (+`assets/`), `wiki/{sources,entities,concepts,topics}`.
- Wiki language default: English. Open question flagged (vault locale is French).

## [2026-06-14] ingest | LLM Wiki — A Pattern for Personal Knowledge Bases
- Source filed → `raw/llm-wiki-idea.md`; summary → [[llm-wiki-pattern]].
- Created concepts [[persistent-wiki]], [[retrieval-augmented-generation]]; entity [[memex]].
- Updated `index.md` (5 pages) and `wiki/overview.md` (set current thesis).
- Worked example: demonstrates one ingest touching summary + 2 concepts + 1 entity + overview + index.

## [2026-06-14] ingest | Tailwind CSS Utility Reference
- Source type: markdown file. Raw file: `raw/tailwind-utility-reference.md`.
- Pages created: [[raw/assets/tailwind-utility-reference]], [[tailwind-css]], [[utility-first-css]].
- Opens new **frontend/CSS** domain; no overlap/contradiction with existing pages.
- Open questions logged: Tailwind version (looks v3.x), responsive/state variants not covered.

## [2026-06-14] maint | Flatten vault to canonical layout
- Detected vault had been reorganized: whole wiki nested under `raw/wiki/`; a second `wiki/` at root; duplicate llm-wiki source; 4 empty command stubs under `raw/assets/.Claude/commande/`.
- Moved `CLAUDE.md`/`index.md`/`log.md` → root; `overview.md`+sources/entities/concepts → root `wiki/`.
- Dedup: kept Obsidian clip (real Karpathy gist URL) as `raw/llm-wiki-idea.md`; dropped hand-typed copy. Updated [[llm-wiki-pattern]] frontmatter with `source-url` + author.
- Removed empty `raw/wiki/` tree and stray `.Claude/commande/` stubs.
- Created real slash-commands → `.claude/commands/{ingest,query,lint,save}.md`.

## [2026-06-14] ingest | JotaroSeo X Threads — HTTP Errors, EMD, Long-Tail (batch)
- Source type: X thread × 3 (French). Raw files: `raw/jotaro-seo-http-errors-x-thread.md`, `raw/jotaro-seo-exact-match-domain-x-thread.md`, `raw/jotaro-seo-long-tail-strategy-x-thread.md`.
- Pages created: [[jotaro-seo-http-errors]], [[jotaro-seo-exact-match-domain]], [[jotaro-seo-long-tail-strategy]], [[jotaro-seo]], [[http-status-codes-seo]], [[exact-match-domain]], [[long-tail-keywords]], [[cocon-semantique]], [[link-juice]].
- Opens 3rd domain: SEO (French-language). Original files were in `raw/assets/` (wrong location) and had a typo (`artciel`); copied to `raw/` with descriptive names.
- TODOs flagged: `maillage-interne`, `technical-seo` pages; Penguin history; cocon sémantique originator (Laurent Bourrelly, unverified).

## [2026-06-15] ingest | IA x SEO — JotaroSeo guide to AI citation (ChatGPT, Claude, Gemini)
- Source type: X thread (French). Raw file: `raw/jotaro-seo-ia-x-seo.md` (original clip in `raw/assets/IA X SEO.md`).
- Pages created: [[raw/assets/jotaro-seo-ia-x-seo]], [[ai-seo]], [[ai-overviews]], [[topical-authority]], [[llm-txt]], [[e-e-a-t]].
- Pages updated: [[jotaro-seo]] (source_count 3→4), [[cocon-semantique]] (cross-ref to topical-authority), [[index]], [[overview]].
- Key insight: AI citation and Google ranking are distinct games — only 13.7 % overlap. 28.3 % of top ChatGPT-cited pages rank nowhere on Google. YouTube (0.737 correlation) and topical authority are top levers.
- TODOs added: `pushrank` entity page.

## [2026-06-15] ingest | @JotaroSeo raw/assets/ batch — 16 threads
- Source type: X threads × 16 (French, all @JotaroSeo). Raw files in `raw/assets/`.
- **Source pages created (16)**: [[jotaro-seo-google-bots]], [[jotaro-seo-content-strategy]], [[jotaro-seo-keyword-cannibalization]], [[jotaro-seo-301-redirects]], [[jotaro-seo-canonical-tag]], [[jotaro-seo-black-hat-cloaking]], [[jotaro-seo-pbn]], [[jotaro-seo-chatgpt-sales]], [[jotaro-seo-4-months-textile]], [[jotaro-seo-strategy-broke-abroad]], [[jotaro-seo-6000-toys-case-study]], [[jotaro-seo-semantic-opportunities]], [[jotaro-seo-google-news]], [[jotaro-seo-bookmarklets]], [[jotaro-seo-learn-seo]], [[jotaro-seo-image-optimization]].
- **Concept pages created (12)**: [[maillage-interne]], [[keyword-research]], [[search-intent]], [[keyword-cannibalization]], [[google-bots]], [[crawl-budget]], [[canonical-tag]], [[301-redirect]], [[black-hat-seo]], [[seo-audit]], [[article-structure]], [[google-news-seo]].
- **Entity pages created (1)**: [[pushrank]] (pre-launch AI SEO tool by @JotaroSeo).
- **Pages updated**: [[jotaro-seo]] (source_count 4→20; real name + background disclosed), [[index]], [[overview]].
- Key new knowledge: complete 8-step content strategy (0€→400k thread), 3-type SEO audit framework, black hat techniques (PBN + cloaking), Google News SEO, keyword cannibalization detection methods.
- TODOs: `optimize-ton-seo.fr` entity, `image-seo` content-side expansion (source clip was near-empty), re-ingest `jotaro-seo-image-optimization` from original URL for full content.

## [2026-06-15] ingest | raw/assets/ batch — 9 new sources (5 authors: @alexgroberman, @OneLegchris, @JespernissenSEO, @irentdumpsters, @bloggersarvesh)
- Source type: X threads × 9 (English + French). Raw files in `raw/assets/`. 1 file skipped (Ahrefs blog homepage — navigation-only, no content).
- **Source pages created (9)**: [[alexgroberman-62pct-beyond-top10]], [[alexgroberman-citation-absorption]], [[alexgroberman-page1-vs-ai-citation]], [[alexgroberman-ai-generated-citations]], [[jespernissenseo-ai-traffic-stats]], [[irentdumpsters-google-ai-guide]], [[bloggersarvesh-hvac-case-study]], [[bloggersarvesh-claude-local-seo]], [[onelegchris-multiple-gbp]].
- **Concept pages created (3)**: [[citation-absorption]], [[local-seo]], [[google-business-profile]].
- **Entity pages created (2)**: [[alex-groberman]], [[sarvesh-alventra]].
- **Concept pages updated (4)**: [[ai-seo]] (7 src), [[ai-overviews]] (4 src; 62 % stat + sub-query decomposition added), [[e-e-a-t]] (3 src; Google official experience-first + scaled content abuse), [[topical-authority]] (2 src; 40-60 page depth quantified, open question resolved).
- **New domains**: Local SEO cluster (4 sources, 2 new concepts). AI Citation Research cluster (4 @alexgroberman sources, 1 new concept).
- Key new knowledge: Google Gemini 3 decomposes queries into sub-queries → 62 % of AIO citations from non-top-10; citation absorption ≠ citation selection; ChatGPT = 78 % of AI traffic + highest absorption score; 8-prompt Claude GBP system; HVAC 27k→3.2M case study; dual GBP profile tactic.
- Tension flagged: FAQ format improves classic SEO (featured snippets) but does NOT correlate with AI absorption → [[citation-absorption]] vs [[article-structure]].
- TODOs carried over: `optimize-ton-seo.fr` entity; `image-seo` re-ingest. New TODO: `@JespernissenSEO` and `@OneLegchris` and `@irentdumpsters` entity stubs (not yet created — low priority).

## [2026-06-15] ingest | raw/assets/ batch — 14 Semrush Blog articles (AI SEO cluster)
- Source type: Semrush Blog articles × 14 (French translations of English originals). Raw files in `raw/assets/`. ~64 non-AI articles and duplicates excluded.
- **Source pages created (14)**: [[semrush-ai-seo-traffic-study]], [[semrush-ai-visibility-study-findings]], [[semrush-ai-visibility-trends-3mo]], [[semrush-ai-stats-2026]], [[semrush-aeo-vs-seo]], [[semrush-google-ai-mode]], [[semrush-ai-referral-traffic]], [[semrush-geo-definition]], [[semrush-optimize-ai-2026]], [[semrush-traditional-vs-ai-seo]], [[semrush-rank-in-ai-search]], [[semrush-ai-search-trends-2026]], [[semrush-llms-txt-guide]], [[semrush-ai-seo-beginner-guide]].
- **Concept pages created (2)**: [[aeo]] (AEO vs SEO distinction; 77% ChatGPT users = search engine), [[google-ai-mode]] (full AI Mode vs AI Overviews comparison; 100M users; weighted SoV 80/20).
- **Entity pages created (1)**: [[semrush]] (major AI SEO research publisher; commercial bias noted).
- **Concept pages updated (4)**: [[ai-seo]] (7→14 src; community>brand; cooccurrence; 4.4×; prompt 8w vs keyword 4w), [[ai-overviews]] (4→6 src; 2B users; 6.49%→13.1% trigger rate; 1% CTR inside summaries), [[llm-txt]] (1→2 src; 951 domains; John Mueller quote; llms.txt examples added), [[citation-absorption]] (3→4 src; ChatGPT 85.79% platform visits added).
- Key new knowledge: LLM visitor = 4.4× traditional organic; community content >> brand for AI citations (Reddit 176% per query in finance); semantic cooccurrence as AI ranking signal; content freshness critical (90% AI-cited pages ≤3 years); AIO doubling trigger rate; AI Mode = separate surface requiring distinct tracking; LLMs.txt — 951 domains, not used by any major AI platform yet.
- Tensions: "top-ranked pages cited more" (Semrush) vs "62% of citations outside top-10" (Ahrefs) — resolution: Google AIO = rank matters more; ChatGPT = rank matters less.

## [2026-06-16] ingest | Copywriting CRO batch — Frameworks + Psychology (fills e-commerce copy gap)
- Sources filed (2): [[copywriting-frameworks-2026]] (Giovanna Romano, ~16 frameworks incl. FAB/AIDA/PAS/4C's), [[haddington-copywriting-psychology]] (emotional triggers, proof, scarcity, ethics).
- Concept pages created (2): [[copywriting-frameworks]], [[copywriting-psychology]].
- Topic page created (1): [[product-bullet-points]] — synthesis filling the previously-missing CRO/conversion layer; Feature→Benefit rule + audit scorecard for product bullets.
- Cross-links: [[citation-absorption]] (numbers drive absorption AND conversion), [[article-structure]] (bullets for enumeration), [[e-e-a-t]] (honest claims).
- NOTE: prior ingest run (interrupted) created low-value freelance-career pages (frw-ep280→284, copy-posse career, awai blog-index) while leaving the high-value CRO articles un-ingested. Several raw/assets copywriting articles still pending: Marketing Emotional Triggers, 12 tactiques de marketing, What's a CTA, Land Clients 35 Tips, Best Copywriting Blogs.

## [2026-06-17] ingest | Copywriting : définition et exemples concrets
- Source type: markdown clipping (academiecopywriting.fr), moved Clippings/ → raw/
- Raw file: raw/Copywriting - definition et exemples concrets.md
- Pages created: [[academie-copywriting-definition]], [[copywriting]] (base concept), [[academie-copywriting]] (entity)
- Pages updated: [[copywriting-frameworks]] (1→2 src), [[copywriting-psychology]] (2→3 src), index.md (stats 48 src / 85 pages)
- Note: thin definitional source (lead-magnet for paid training); value = clean entry-point for the copywriting concept cluster. First copywriting ingest of the SERP batch (~40 clippings).
---

## [2026-06-17] ingest | Copywriting fundamentals batch (academie x4)
- Source type: markdown clippings (academiecopywriting.fr) from raw/assets
- Raw files: Les 5 types de copywriting / AIDA PAS FAB / Méthode FAB / Différence copywriting et rédaction web
- Pages created: [[academie-5-types-copywriting]], [[academie-aida-pas-fab]], [[academie-methode-fab]], [[academie-copywriting-vs-redaction-web]], [[copywriting-types]] (concept), [[copywriting-vs-redaction-web]] (topic)
- Pages updated: [[copywriting]] (1→3 src, resolved web-writing open Q), [[copywriting-frameworks]] (2→4 src, format-fit + FAB 5-step), [[academie-copywriting]] entity (1→5 src), index.md (52 src / 91 pages)
- Run context: autonomous batch of raw/assets (~150 real sources after dedup); copywriting cluster first. Progress this turn: 5 copywriting files done (incl. earlier definition).
---

## [2026-06-17] ingest | Copywriting attention+CTA batch (5 sources)
- Source type: markdown clippings (academiecopywriting.fr x4 + filthyrichwriter.com x1)
- Raw files: 7 formules headlines / hook accroche / capter attention première ligne / CTA 2025 / What's a CTA (FRW)
- Pages created: [[academie-7-formules-headlines]], [[academie-hook-accroche]], [[academie-capter-attention-premiere-ligne]], [[academie-cta-2025]], [[frw-what-is-cta]]; concepts [[headline]], [[hook]], [[call-to-action]]; entity [[nicki-krawczyk]]
- Pages updated: [[copywriting-psychology]] (3→4 src, risk-reduction lever), [[academie-copywriting]] entity (5→9 src), index.md (57 src / 100 pages)
- Progress: copywriting cluster ~10/67 done. Core shared concepts (headline/hook/CTA) now exist → later files compound onto them.
---

## [2026-06-17] ingest | Copywriting psychology+emotion batch (4 sources)
- Source type: markdown clippings (academiecopywriting.fr x4)
- Raw files: 5 biais cognitifs / 3 émotions achat / copywriting émotionnel / storytelling
- Pages created: [[academie-5-biais-cognitifs]], [[academie-3-emotions-achat]], [[academie-copywriting-emotionnel]], [[academie-storytelling]]; concepts [[cognitive-biases]], [[emotional-copywriting]], [[storytelling]]
- Pages updated: [[copywriting-psychology]] (4→6 src; added 3-emotion sequence + named biases), [[academie-copywriting]] entity (9→13 src), index.md (61 src / 107 pages)
- Progress: copywriting cluster ~14/67. Psychology hub now well-developed.
---

## [2026-06-17] ingest | Copywriting persuasion-levers batch (4 sources)
- Source type: markdown clippings (academiecopywriting.fr x4)
- Raw files: urgence sans agressivité / effet de rareté / preuve sociale / ancrage mental
- Pages created: [[academie-urgence-sans-agressivite]], [[academie-effet-rarete]], [[academie-preuve-sociale]], [[academie-ancrage-mental]]; concepts [[scarcity-urgency]], [[social-proof]], [[value-anchoring]]; entity [[theo-rossi]]
- Pages updated: [[copywriting-psychology]] (6→10 src), [[cognitive-biases]] (deep-dive links), [[academie-copywriting]] entity (13→17 src, founder Théo Rossi resolved), index.md (65 src / 115 pages)
- Progress: copywriting cluster ~18/~53 sources.
---

## [2026-06-17] ingest | Copywriting conversion-structure batch (3 sources)
- Source type: markdown clippings (academiecopywriting.fr x3)
- Raw files: structurer texte de vente / landing page / tunnel de vente
- Pages created: [[academie-structurer-texte-vente]], [[academie-landing-page]], [[academie-tunnel-de-vente]]; concepts [[sales-page-structure]], [[landing-page]], [[sales-funnel]]
- Pages updated: [[academie-copywriting]] entity (17→20 src), index.md (68 src / 121 pages)
- Loop: dynamic /loop self-paced. Progress: copywriting cluster ~21/~53 sources.
---

## [2026-06-17] ingest | Copywriting conversion-assets batch (4 sources)
- Source type: markdown clippings (academiecopywriting.fr x4)
- Raw files: emails qui vendent / lead magnet / page À propos / B2B vs B2C
- Pages created: [[academie-emails-qui-vendent]], [[academie-lead-magnet]], [[academie-page-a-propos]], [[academie-b2b-vs-b2c]]; concepts [[email-copywriting]], [[lead-magnet]], [[about-page]]; topic [[copywriting-b2b-vs-b2c]]
- Pages updated: [[academie-copywriting]] entity (20→24 src), index.md (72 src / 129 pages)
- Loop iteration 2. Progress: copywriting cluster ~25/~53 sources.
---

## [2026-06-17] ingest | Copywriting psychology-deep batch (4 sources)
- Source type: markdown clippings (academiecopywriting.fr x4)
- Raw files: biais de confirmation / frustration et désir / neurosciences & vente / effet miroir
- Pages created: [[academie-biais-confirmation]], [[academie-frustration-desir]], [[academie-neuroscience-vente]], [[academie-effet-miroir]]; concepts [[frustration-desire]], [[mirror-effect]], [[neuroscience-selling]]
- Pages updated: [[cognitive-biases]] (+confirmation bias, 1→2 src), [[copywriting-psychology]] hub (lever + neuro links), [[academie-copywriting]] entity (24→28 src), index.md (76 src / 136 pages)
- Loop iteration 3. Progress: copywriting cluster ~29/~53 sources.
---

## [2026-06-17] ingest | Copywriting attention/visual/micro batch (4 sources)
- Source type: markdown clippings (academiecopywriting.fr x4)
- Raw files: psychologie de l'attention / couleurs et achat / micro-copywriting / bullet points
- Pages created: [[academie-psychologie-attention]], [[academie-couleurs-achat]], [[academie-micro-copywriting]], [[academie-bullet-points]]; concepts [[color-psychology]], [[micro-copywriting]], [[bullet-points]]
- Pages updated: [[hook]] (2→3 src, 3-second rule), [[product-bullet-points]] (4→5 src), [[academie-copywriting]] entity (28→32 src), index.md (80 src / 143 pages)
- Loop iteration 4. Progress: copywriting cluster ~33/~53 sources.
---

## [2026-06-17] ingest | Copywriting quality/USP/ethics batch (4 sources)
- Source type: markdown clippings (academie x2 + jeremy-allard.com + projectfork.net)
- Raw files: 7 erreurs débutant / 10 expressions à bannir / USP (Jérémy Allard) / copywriting éthique (projectfork)
- Pages created: [[academie-7-erreurs-debutant]], [[academie-10-expressions-bannir]], [[jeremy-allard-usp]], [[projectfork-copywriting-ethique]]; concepts [[copywriting-mistakes]], [[usp]], [[ethical-copywriting]]; entity [[jeremy-allard]]
- Pages updated: [[academie-copywriting]] entity (32→34 src), index.md (84 src / 151 pages)
- Loop iteration 5. Progress: copywriting cluster ~37/~53 sources.
---

## [2026-06-17] ingest | Copywriting formats/persuasion batch (3 sources)
- Source type: markdown clippings (jeremy-allard.com + academie x2)
- Raw files: 15 techniques écriture persuasive / script vidéo persuasif / Instagram captions
- Pages created: [[jeremy-allard-ecriture-persuasive]], [[academie-script-video]], [[academie-instagram-captions]]; topic [[persuasive-writing]]; concepts [[video-script]], [[instagram-copywriting]]
- Pages updated: [[jeremy-allard]] entity (1→2 src), [[academie-copywriting]] entity (34→36 src), index.md (87 src / 157 pages)
- Loop iteration 6. Progress: copywriting cluster ~40/~53 sources.
---

## [2026-06-17] ingest | Copywriting AI/visual batch (3 sources)
- Source type: markdown clippings (academie x3)
- Raw files: 7 prompts ChatGPT page de vente / améliorer textes avec ChatGPT / copywriting visuel
- Pages created: [[academie-prompts-chatgpt-page-vente]], [[academie-chatgpt-textes-vente]], [[academie-copywriting-visuel]]; concepts [[ai-assisted-copywriting]], [[visual-copywriting]]
- Pages updated: [[academie-copywriting]] entity (36→39 src), index.md (90 src / 162 pages)
- Loop iteration 7. Progress: copywriting cluster ~43/~53 sources.
---

## [2026-06-17] ingest | Copywriting authority/ebook batch (2 sources)
- Source type: markdown clippings (academie x2). Skipped "Conversion (...)" = jeremy-allard category index page (noise → skip-list, now 38)
- Raw files: autorité en copywriting / vendre un ebook
- Pages created: [[academie-autorite-copywriting]], [[academie-vendre-ebook]]; concepts [[brand-authority]], [[ebook-selling]]
- Pages updated: [[academie-copywriting]] entity (39→41 src), index.md (92 src / 166 pages)
- Loop iteration 8. Progress: copywriting cluster ~45/~51 sources (FR academie set nearly complete).
---

## [2026-06-17] ingest | Copywriting career/niches batch (2 sources)
- Source type: markdown clippings (copyposse.com + filthyrichwriter.com)
- Raw files: 13 Profitable Niches (Copy Posse) / Land Clients 35 Tips (FRW)
- Pages created: [[copyposse-profitable-niches]], [[frw-land-clients-35-tips]]; concepts [[copywriting-niches]], [[client-acquisition]]; entity [[alex-cattoni]]
- Pages updated: [[nicki-krawczyk]] entity (+1 src), index.md (94 src / 171 pages)
- Loop iteration 9. Opened copywriting-business sub-cluster. Copywriting cluster ~47/~51.
---

## [2026-06-17] ingest | Copywriting sales-page deep-dives (2 sources)
- Source type: markdown clippings (academie + jeremy-allard.com)
- Raw files: meilleures pages de vente analysées / secrets pages de vente (tunnel)
- Pages created: [[academie-meilleures-pages-vente]], [[jeremy-allard-secrets-pages-vente]] (reinforce, no new concepts)
- Pages updated: [[sales-page-structure]] (2→4 src; +9 traits +value proposition), [[jeremy-allard]] (2→3), [[academie-copywriting]] (41→42), index.md (96 src / 173 pages)
- Loop iteration 10. Copywriting cluster ~49/~51 — tail = a few EN career pieces, then SEO cluster.
---

## [2026-06-17] ingest | Copywriting AI-career batch (2 sources + synthesis)
- Source type: markdown clippings (copyposse.com x2)
- Raw files: AI Replacing Writers Won't Kill / Psychological Triggers (discovery calls)
- Pages created: [[copyposse-ai-replacing-writers]], [[copyposse-psychological-triggers]]; topic [[ai-vs-human-writing]] (5-source synthesis)
- Pages updated: [[client-acquisition]] (1→2 src), [[alex-cattoni]] (1→3 src), index.md (98 src / 176 pages)
- Loop iteration 11. Copywriting cluster nearly done; ai-vs-human-writing synthesis ties 5 AI-career sources.
---

## [2026-06-17] ingest | Copywriting learning/web-mistakes batch (2 sources)
- Source type: markdown clippings (academie + jeremy-allard.com)
- Raw files: apprendre le copywriting sans expérience / erreurs copywriting contenu web
- Pages created: [[academie-apprendre-sans-experience]], [[jeremy-allard-erreurs-web]]; concept [[learning-copywriting]]
- Pages updated: [[copywriting-mistakes]] (2→3 src), [[client-acquisition]] (1→2), [[jeremy-allard]] (3→4), [[academie-copywriting]] (42→43), index.md (100 src / 179 pages)
- Loop iteration 12. Milestone: 100 sources ingested. Copywriting tail: a few EN career/tools left, then SEO cluster.
---

## [2026-06-17] ingest | Copywriting tools/email-role batch (2 sources)
- Source type: markdown clippings (academie x2)
- Raw files: 10 outils gratuits copywriting / Email Copywriter Guide
- Pages created: [[academie-outils-gratuits-copywriting]], [[academie-email-copywriter]]; concept [[copywriting-tools]]
- Pages updated: [[email-copywriting]] (1→2 src, +role/income), [[academie-copywriting]] (43→45 src), index.md (102 src / 182 pages)
- Loop iteration 13. Copywriting tail almost done (few EN career/misc left), then SEO cluster.
---

## [2026-06-17] ingest | SEO cluster start: off-page/backlinks (2 sources)
- Source type: markdown clippings (Semrush x2). COPYWRITING CLUSTER ~complete (45 academie + FRW/CopyPosse/jeremy-allard).
- Raw files: off-page SEO guide / find backlinks
- Pages created: [[semrush-off-page-seo]], [[semrush-find-backlinks]]; concepts [[off-page-seo]], [[backlinks]]
- Pages updated: index.md (104 src / 186 pages). TODO(lint): bump [[semrush]] entity source_count (+2) and add these 2 to its sources list.
- Loop iteration 14. Pivoted to SEO cluster.
---

## [2026-06-17] ingest | SEO off-page/technical (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: backlinks toxiques / redirection 302
- Pages created: [[semrush-toxic-backlinks]], [[semrush-302-redirect]]; concepts [[toxic-backlinks]], [[302-redirect]]
- Pages updated: index.md (106 src / 190 pages). TODO(lint): semrush entity source_count + sources list (now +4 this session uncounted).
- Loop iteration 15. SEO cluster building (off-page + redirects).
---

## [2026-06-17] ingest | SEO mobile/SEM (2 sources)
- Source type: markdown clippings (Semrush x2). Skipped "Architecture de site web" = category index page (noise → skip-list 39).
- Raw files: référencement mobile / SEM
- Pages created: [[semrush-mobile-seo]], [[semrush-sem]]; concepts [[mobile-seo]], [[sem]]
- Pages updated: index.md (108 src / 194 pages)
- Loop iteration 16.
---

## [2026-06-17] ingest | SEO keyword sub-cluster (2 sources, reinforce)
- Source type: markdown clippings (Semrush x2)
- Raw files: intention de mots clés / mots-clés organiques
- Pages created: [[semrush-keyword-intent]], [[semrush-organic-keywords]] (reinforce, no new concepts)
- Pages updated: index counts for [[search-intent]] (4 src) + [[keyword-research]] (5 src); index.md (110 src / 196 pages). TODO(lint): add these to concept pages' sources lists + semrush entity.
- Loop iteration 17.
---

## [2026-06-17] ingest | SEO content-arch/migration (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: topic clusters / migration de site
- Pages created: [[semrush-topic-clusters]], [[semrush-site-migration]]; concepts [[topic-clusters]], [[site-migration]]
- Pages updated: index.md (112 src / 200 pages)
- Loop iteration 18. Milestone: 200 wiki pages.
---

## [2026-06-17] ingest | SEO local sub-cluster (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: citations locales / mots-clés près de moi
- Pages created: [[semrush-local-citations]], [[semrush-near-me-keywords]]; concept [[local-citations]]
- Pages updated: index counts [[local-seo]] (6 src); index.md (114 src / 203 pages). TODO(lint): local-seo/GBP source lists + semrush entity.
- Loop iteration 19.
---

## [2026-06-17] ingest | SEO analytics (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: pages vues GA4 / erreurs GSC
- Pages created: [[semrush-ga4-pageviews]], [[semrush-gsc-errors]]; concepts [[google-analytics-4]], [[google-search-console]]
- Pages updated: index.md (116 src / 207 pages)
- Loop iteration 20.
---

## [2026-06-18] ingest | SEO sitemap/roadmap (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: soumettre sitemap / feuille de route SEO
- Pages created: [[semrush-submit-sitemap]], [[semrush-seo-roadmap]]; concepts [[xml-sitemap]], [[seo-roadmap]]
- Pages updated: index.md (118 src / 211 pages). Note: Obsidian linter reformatting some source frontmatter; queue-diff made robust to shortened wikilinks.
- Loop iteration 21.
---

## [2026-06-18] ingest | SEO site-health/new-site (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: santé du site / SEO nouveau site 9 étapes
- Pages created: [[semrush-site-health]], [[semrush-new-website-seo]]; concepts [[site-health]], [[new-site-seo]]
- Pages updated: index.md (120 src / 215 pages)
- Loop iteration 22.
---

## [2026-06-18] ingest | SEO GEO-tools/question-keywords (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: 10 outils GEO / mots-clés des questions
- Pages created: [[semrush-geo-tools]], [[semrush-question-keywords]]; concepts [[geo-tools]], [[question-keywords]]
- Pages updated: index.md (122 src / 219 pages)
- Loop iteration 23.
---

## [2026-06-18] ingest | SEO PAA/negative-keywords (2 sources)
- Source type: markdown clippings (Semrush x2)
- Raw files: People Also Ask / mots-clés négatifs
- Pages created: [[semrush-people-also-ask]], [[semrush-negative-keywords]]; concepts [[people-also-ask]], [[negative-keywords]]
- Pages updated: index.md (124 src / 223 pages)
- Loop iteration 24.
---

## [2026-06-18] ingest | SEO internal-links/domain-change (2 sources, reinforce)
- Source type: markdown clippings (Semrush x2)
- Raw files: 11 erreurs liens internes / changement nom de domaine
- Pages created: [[semrush-internal-linking-mistakes]], [[semrush-domain-change-seo]] (reinforce)
- Pages updated: index counts [[maillage-interne]] (6 src) + [[site-migration]] (2 src); index.md (126 src / 225 pages). TODO(lint): concept source lists.
- Loop iteration 25.
---

## [2026-06-18] ingest | SEO fundamentals/landing-SEO (2 sources) + skip-list cleanup
- Skip-listed 6 noise (Semrush category index pages + EMD/HTTP dups). Skip-list now 45.
- Raw files: Qu'est-ce que le SEO (intro) / SEO pour pages de destination
- Pages created: [[semrush-what-is-seo]], [[semrush-seo-landing-pages]]; concepts [[what-is-seo]] (hub), [[landing-page-seo]] (copy↔SEO bridge)
- Pages updated: index.md (128 src / 229 pages)
- Loop iteration 26.
---

## [2026-06-18] ingest | SEO GBP-posts/GSC-links (2 sources, reinforce) + skip AI-rank dup
- Skipped "se positionner recherche IA 6 tactiques" = dup of [[semrush-rank-in-ai-search]]. Skip-list 46.
- Raw files: publications GBP / rapport liens GSC
- Pages created: [[semrush-gbp-posts]], [[semrush-gsc-links-report]] (reinforce)
- Pages updated: index counts [[google-business-profile]] (5) + [[google-search-console]] (2); index.md (130 src / 231 pages)
- Loop iteration 27.
---

## [2026-06-18] ingest | SEO Google-News/GA4-sources (2 sources, reinforce)
- Raw files: 5 tactiques Google Actualités / sources de trafic GA4
- Pages created: [[semrush-google-news-seo]], [[semrush-ga4-traffic-sources]] (reinforce)
- Pages updated: index counts [[google-news-seo]] (2) + [[google-analytics-4]] (2); index.md (132 src / 233 pages)
- Loop iteration 28.
---

## [2026-06-18] ingest | Marketing cluster start (2 sources)
- Source type: markdown clippings (Semrush x2). SEO cluster ~complete; pivoted to marketing/tools.
- Raw files: 12 tactiques marketing / analyse concurrents social media
- Pages created: [[semrush-marketing-tactics]], [[semrush-social-competitor-analysis]]; concepts [[marketing-tactics]], [[competitor-analysis]]; new index section "Marketing & Tools"
- Pages updated: index.md (134 src / 237 pages)
- Loop iteration 29.
---

## [2026-06-18] ingest | Marketing content-calendar/display-ads (2 sources)
- Raw files: 4 exemples calendriers contenu / 13 bonnes pratiques pub display
- Pages created: [[semrush-content-calendar-examples]], [[semrush-display-ads]]; concepts [[content-calendar]], [[display-advertising]]
- Pages updated: index.md (136 src / 241 pages)
- Loop iteration 30.
---

## [2026-06-18] ingest | Marketing tools landscape (3 sources + topic)
- Raw files: 11 outils mots-clés / 22 outils création contenu / 12 outils analyse social
- Pages created: [[semrush-keyword-research-tools]], [[semrush-content-creation-tools]], [[semrush-social-analytics-tools]]; topic [[marketing-tools-landscape]] (aggregator for tool listicles)
- Pages updated: index.md (139 src / 245 pages)
- Loop iteration 31. Strategy: fold remaining tool-listicles into the landscape topic as ingested.
---

## [2026-06-18] ingest | Marketing tools (3 sources) + ORM concept
- Raw files: outils performance web / outils veille social / outils ORM
- Pages created: [[semrush-website-performance-tools]], [[semrush-social-monitoring-tools]], [[semrush-orm-tools]]; concept [[online-reputation-management]]
- Pages updated: [[marketing-tools-landscape]] topic (3→6 src), index.md (142 src / 249 pages)
- Loop iteration 32.
---

## [2026-06-18] ingest | Marketing CI/ads tools + social-posting study (3 sources)
- Raw files: 14 outils veille concurrentielle / 10 outils publicitaires / étude que&quand publier
- Pages created: [[semrush-competitive-intelligence-tools]], [[semrush-advertising-tools]], [[semrush-social-posting-study]]; concept [[social-media-strategy]]
- Pages updated: [[marketing-tools-landscape]] (6→8 src), index.md (145 src / 252 pages)
- Loop iteration 33.
---

## [2026-06-18] ingest | Productivity-tools topic + competitor ad-spend (2 sources)
- Raw files: Trello vs Notion vs Obsidian / dépenses pub concurrents
- Pages created: [[academie-trello-notion-obsidian]], [[semrush-competitor-ad-spend]]; topic [[productivity-tools]]
- Pages updated: [[competitor-analysis]] (1→2 src), index.md (147 src / 255 pages). TODO(lint): academie entity +1 (trello).
- Loop iteration 34.
---

## [2026-06-18] ingest | Marketing lead-gen/Amazon-funnel (2 sources)
- Raw files: contacts qualifiés (Jérémy Allard) / Amazon Funnel Insights
- Pages created: [[jeremy-allard-contacts-qualifies]], [[semrush-amazon-funnel]]; concepts [[lead-generation]], [[amazon-funnel]]
- Pages updated: index.md (149 src / 259 pages). TODO(lint): jeremy-allard entity +1.
- Loop iteration 35.
---

## [2026-06-18] ingest | idea-validation/SEO-certifications (2 sources)
- Raw files: comment savoir si idée bonne (Jérémy Allard) / Top 11 certifications SEO
- Pages created: [[jeremy-allard-bonne-idee]], [[semrush-seo-certifications]]; concepts [[idea-validation]], [[seo-certifications]]
- Pages updated: index.md (151 src / 263 pages). TODO(lint): jeremy-allard entity +2 (contacts + bonne-idee).
- Loop iteration 36.
---

## [2026-06-18] ingest | AI-search-engines + product-page checklist (2 sources) + skip dups
- Skip-listed 11 SEO dups (keyword-research/landing/llms.txt/PBN/title/AI-study FR translations). Skip-list 57.
- Raw files: meilleurs moteurs IA / checklist fiche produit
- Pages created: [[semrush-best-ai-search-engines]], [[academie-checklist-fiche-produit]]; concept [[ai-search-engines]]
- Pages updated: [[product-bullet-points]] (5→6 src), index.md (153 src / 266 pages)
- Loop iteration 37.
---

## [2026-06-18] ingest | Reinforcement batch x4
- Raw files: marketing emotional triggers (Copy Posse) / exemples copywriting pub / calendrier éditorial vente / outils visuels Canva-Figma-PS
- Pages created: [[copyposse-marketing-emotional-triggers]], [[academie-exemples-copywriting-pub]], [[academie-calendrier-editorial-vente]], [[academie-outils-visuels]] (all reinforce existing concepts)
- Pages updated: index.md (157 src / 270 pages). TODO(lint): bump source lists on emotional-copywriting, content-calendar, visual-copywriting, copywriting, alex-cattoni, academie-copywriting.
- Loop iteration 38.
---

## [2026-06-18] ingest | SEO/marketing reinforcement x4
- Raw files: checklist off-page / connecter GSC↔GA4 / infos concurrentielles social / 8 outils SEO IA
- Pages created: [[semrush-off-page-checklist]], [[semrush-connect-gsc-ga4]], [[semrush-social-competitive-insights]], [[semrush-ai-seo-tools]] (reinforce)
- Pages updated: [[marketing-tools-landscape]] (8→9 src), index.md (161 src / 274 pages)
- Loop iteration 39.
---

## [2026-06-18] ingest | SEO-2026/Alexa/marketing-system/blogs reinforcement x4
- Raw files: optimisation SEO 2026 (Incremys) / Amazon Alexa local / Simple Marketing System (Copy Posse) / best copywriting blogs
- Pages created: [[incremys-optimisation-seo-2026]], [[semrush-amazon-alexa-local]], [[copyposse-simple-marketing-system]], [[brandnewcopy-best-copywriting-blogs]] (reinforce)
- Pages updated: index.md (165 src / 278 pages)
- Loop iteration 40. ~13 left (mostly career/mindset + a couple SEO studies).
---

## [2026-06-18] ingest | Career/mindset reinforcement x5 (Copy Posse + FRW)
- Raw files: 6 questions business / lessons on marketing / starting a substack / connect past clients / social consistency
- Pages created: [[copyposse-6-questions-business]], [[copyposse-lessons-on-marketing]], [[copyposse-starting-substack]], [[frw-connect-past-clients]], [[copyposse-social-consistency]] (reinforce)
- Pages updated: index.md (170 src / 283 pages). TODO(lint): alex-cattoni +4, nicki-krawczyk +1, marketing-tactics/client-acquisition/social-media-strategy source lists.
- Loop iteration 41.
---

## [2026-06-18] ingest | query-fan-out + competitor/local reinforcement x4
- Raw files: query fan-out experiment / comparer sites / données historiques / Complete Local SEO cleaning
- Pages created: [[semrush-query-fan-out]], [[semrush-compare-websites]], [[semrush-historical-data]], [[local-seo-cleaning-guide]]; concept [[query-fan-out]]
- Pages updated: index.md (174 src / 288 pages)
- Loop iteration 42. ~4 marginal left (Semrush Pro/Guru, IA keyword update, agency insider, goals mindset).
---

## [2026-06-18] ingest | Final marginal batch x4 → QUEUE EMPTY
- Raw files: défis agences / IA keyword update / Semrush Pro vs Guru / setting goals
- Pages created: [[semrush-agency-challenges]], [[semrush-keyword-research-ai-update]], [[semrush-pro-vs-guru]], [[copyposse-setting-goals]] (reinforce)
- raw/assets queue = 0. Total: 189 source pages / 311 wiki pages.

## [2026-06-18] lint | Full-vault lint after bulk ingest
- **Entity source_count reconciled** (were stale from deferred updates): [[semrush]] 14→72, [[academie-copywriting]] 45→50, [[alex-cattoni]] 3→12, [[jeremy-allard]] 4→6, [[nicki-krawczyk]] 1→11. [[theo-rossi]] left at 1 (named in 2 sources).
- **Dangling wikilinks (TODO stubs, not errors)** — concepts referenced but no page yet: [[benefits-over-features]], [[direct-response-copywriting]], [[creative-brief]], [[fab-framework]], [[brand-identity]], [[email-marketing]] (alias of [[email-copywriting]]), [[geo]] (covered by [[aeo]] + [[semrush-geo-definition]]), [[ecommerce]], [[sales-page]] alias. Valid TODO markers per CLAUDE.md §8; create on next relevant ingest.
- **False-positive "orphans"**: `raw/assets/*.md` links are `raw:` frontmatter pointers (resolve to raw files), not missing wiki pages — expected.
- **Skip-list**: 61 raw files excluded = numbered duplicates (" 1"/" 2"), Obsidian category-index pages (Semrush blog category stubs), already-covered dups (EMD/HTTP/PBN/landing/llms.txt/keyword-research FR translations), and noise (Group Chat, Feedspot, jotaro x-thread raw copies, llm-wiki-idea).
- **Known tensions already flagged inline**: SEO-copywriting boundary ([[copywriting-vs-redaction-web]]); single-CTA vs repeat-CTA ([[emotional-copywriting]] ↔ [[call-to-action]]); educator commercial bias noted across academie/Copy Posse/FRW pages.
- Suggested next: create the TODO concept stubs above; triangulate academie (single-publisher) copywriting claims against EN sources; consider a [[geo]] concept consolidating AEO/GEO.
---

## [2026-06-18] ingest | Aperçu de l'IA : guide pour comprendre l'IA (Neil Patel)
- New source [[apercu-ia-guide]] (neilpatel.com FR, 2025-10-10) — beginner AI overview for business.
- New concepts: [[artificial-intelligence]], [[machine-learning]], [[deep-learning]], [[natural-language-processing]], [[ai-marketing]], [[generative-engine-optimization]] (seeds the vault's AI-fundamentals cluster).
- New entities: [[neil-patel]], [[np-digital]], [[ubersuggest]].
- Updated [[ai-overviews]] (+SGE beginner framing, source_count 6→7).
- index.md: new "Neil Patel / NP Digital" source section + "AI & Machine Learning (fundamentals)" concept section; stats 189→190 sources.
- Batch: source 1/18 of new raw/assets backlog.
---

## [2026-06-18] ingest | Apprenez à booster vos vidéos avec l'algorithme YouTube (Neil Patel)
- New source [[youtube-algorithme]] (neilpatel.com FR, 2025-09-09).
- New concepts: [[youtube-algorithm]], [[click-through-rate]]. New entity: [[youtube]].
- Updated [[machine-learning]] (1→2 src), [[social-media-strategy]] (1→2 src).
- index.md: +2 concepts, +1 entity, source under Neil Patel section; stats 190→191 sources.
- Batch: source 2/18.
---

## [2026-06-18] ingest | Comment créer une newsletter ? Guide pratique (Neil Patel)
- New source [[newsletter-guide]] (neilpatel.com FR, 2025-09-30).
- New concepts: [[newsletter]], [[email-marketing]] (resolves prior dangling [[email-marketing]] TODO from 06-18 lint).
- Updated [[lead-magnet]], [[email-copywriting]], [[lead-generation]], [[sales-funnel]] (+1 src each).
- index.md: +2 CRO concepts, source under Neil Patel section; stats 191→192.
- Batch: source 3/18.
---

## [2026-06-18] ingest | Core Web Vitals : c'est quoi ? (Neil Patel)
- New source [[core-web-vitals]] (neilpatel.com FR, 2025-10-31) — technical SEO.
- New concept: [[core-web-vitals]] (LCP/INP/CLS, thresholds, field vs lab data, tools, per-metric fixes).
- Updated [[mobile-seo]], [[site-health]], [[google-search-console]] (+1 src each; FID→INP March 2024 noted).
- index.md: +1 technical-SEO concept, source under Neil Patel section; stats 192→193.
- Batch: source 4/18.
---

## [2026-06-18] ingest | Crawl Budget : guide pour optimiser votre SEO (Neil Patel)
- New source [[crawl-budget-guide]] (neilpatel.com FR, 2025-10-30) — technical SEO.
- New concepts: [[robots-txt]], [[robots-meta-directives]] (noindex + X-Robots-Tag), [[ttfb]].
- Major expansion of [[crawl-budget]] (Rate Limit × Demand model, Crawl Waste, access-control levers; 1→2 src).
- Updated [[google-bots]], [[http-status-codes-seo]] (503), [[xml-sitemap]], [[maillage-interne]], [[core-web-vitals]] (TTFB link).
- index.md: +3 technical-SEO concepts, source under Neil Patel section; stats 193→194.
- Batch: source 5/18.
---

## [2026-06-18] ingest | Le Pouvoir du Prompt ChatGPT (Neil Patel)
- New source [[prompt-chatgpt]] (neilpatel.com FR, 2025-09-30).
- New concept: [[prompt-engineering]]. New entities: [[chatgpt]], [[openai]].
- Updated [[artificial-intelligence]] (1→2), [[aeo]] (2→3, +GEO cross-link), [[ai-assisted-copywriting]] (2→3).
- index.md: +1 AI concept, +2 entities, source under Neil Patel; stats 194→195.
- Batch: source 6/18.
---

## [2026-06-18] ingest | Meilleurs Outils d'AI Visibility en 2026 (Neil Patel)
- New source [[ai-visibility-tools]] (neilpatel.com FR, 2025-11-28).
- New entities: [[ahrefs]], [[profound]], [[scrunchai]], [[perplexity]], [[claude]].
- Expanded [[geo-tools]] (Top-5 tool comparison, metrics, zero-click/Gartner; 1→2 src).
- Updated [[ubersuggest]] (+AI Visibility), [[semrush]] (72→73, AI Visibility positioning), [[ai-search-engines]] (+platform entities), [[aeo]] (Gartner −25%).
- index.md: +5 entities, source under Neil Patel; stats 195→196.
- Note: entities/claude.md picked up by harness as a CLAUDE.md (lowercase filename) — harmless, own content.
- Batch: source 7/18.
---

## [2026-06-18] ingest | NavBoost : ce que c'est et comment il fonctionne (Neil Patel)
- New source [[navboost]] (neilpatel.com FR, 2025-10-21) — technical SEO / user-behavior ranking.
- New concept: [[navboost]] (CTR/pogo-sticking/dwell/implicit satisfaction; NavDemotion; adaptation).
- Updated [[click-through-rate]] (1→2), [[search-intent]] (3→4), [[core-web-vitals]] (pogo link), [[google-analytics-4]] (1→2).
- index.md: +1 technical-SEO concept, source under Neil Patel; stats 196→197.
- Batch: source 8/18.
---

## [2026-06-18] ingest | Omnichannel : définition, différences et comment l'appliquer (Neil Patel)
- New source [[omnichannel]] (neilpatel.com FR, 2025-07-23) — marketing/CX.
- New concept: [[omnichannel]] (3 pillars; vs multichannel/single; build steps; HBR 70%+ stat).
- Updated [[ai-marketing]] (1→2 src; omnichannel personalization).
- index.md: +1 marketing concept, source under Neil Patel; stats 197→198.
- Batch: source 9/18.
---

## [2026-06-18] ingest | Reddit SEO : Guide pour augmenter le trafic et la visibilité (Neil Patel)
- New source [[reddit-seo]] (neilpatel.com FR, 2025-09-05).
- New concept: [[reddit-seo]]. New entity: [[reddit]] (also linked to existing [[semrush-ai-visibility-study-findings]] Reddit-176% finding → 2 src).
- Updated [[off-page-seo]] (1→2), [[keyword-research]] (4→5, Reddit as 6th source), [[online-reputation-management]] (1→2).
- index.md: +1 concept, +1 entity, source under Neil Patel; stats 198→199.
- Batch: source 10/18.
---

## [2026-06-18] ingest | SEO Copywriting : optimiser le contenu et générer des conversions (Neil Patel)
- New source [[seo-copywriting]] (neilpatel.com FR, 2026-01-14).
- New concept: [[seo-copywriting]] (vs content writing; 8-step on-page workflow; 4 intents). New entity: [[gemini]].
- Updated [[copywriting-vs-redaction-web]] topic (2→3), [[search-intent]] (4→5; 4-intent model), [[headline]] (2→3; title-tag role), [[geo-tools]] count fix.
- index.md: +1 CRO concept, +1 entity, source under Neil Patel; stats 199→200 (vault hits 200 sources).
- Batch: source 11/18.
---

## [2026-06-18] ingest | Search Everywhere Optimization : Le nouveau SEO (Neil Patel)
- New source [[search-everywhere-optimization]] (neilpatel.com FR, 2025-12-12) — umbrella framework.
- New concepts: [[search-everywhere-optimization]], [[app-store-optimization]]. New entities: [[instagram]], [[tiktok]], [[pinterest]].
- Updated [[generative-engine-optimization]] (1→2, +LLM tactics), [[social-media-strategy]] (2→3, social-as-search), [[e-e-a-t]] (3→4, cross-platform constant).
- index.md: +2 concepts, +3 entities, source under Neil Patel; stats 200→201.
- Batch: source 12/18.
---

## [2026-06-18] ingest | Stratégie de marque : pourquoi elle est clé et comment la créer (Neil Patel)
- New source [[strategie-de-marque]] (neilpatel.com FR, 2025-07-22) — branding hub (cross-linked by many batch sources).
- New concepts: [[brand-strategy]], [[brand-identity]] (resolves prior dangling [[brand-identity]] TODO from 06-18 lint).
- Updated [[brand-authority]] (relation), [[usp]] (relation), [[competitor-analysis]] (brand-strategy step 2 link).
- index.md: +2 branding concepts, source under Neil Patel; stats 201→202; +Branding domain.
- Batch: source 13/18.
---

## [2026-06-19] ingest | Vidéo marketing : qu'est-ce que c'est et pourquoi investir ? (Neil Patel)
- New source [[video-marketing]] (neilpatel.com FR, 2025-07-22).
- New concept: [[video-marketing]] (resolves prior dangling [[video-marketing]] TODO from youtube/CTR pages).
- Updated [[video-script]] (production step 1 link), [[youtube-algorithm]] (distribution engine link).
- index.md: +1 concept, source under Neil Patel; stats 202→203.
- Batch: source 14/18.
---

## [2026-06-19] ingest | Website redesign : transformez votre site en machine à résultats (Neil Patel)
- New source [[website-redesign]] (neilpatel.com FR, 2025-09-05).
- New concepts: [[website-redesign]], [[ab-testing]] (cross-cutting "always test" backstop).
- Updated [[site-migration]] (UX/brand sibling link).
- index.md: +2 concepts (1 technical-SEO, 1 CRO), source under Neil Patel; stats 203→204.
- Batch: source 15/18.
---

## [2026-06-19] ingest | Pinterest Ads : comment ça fonctionne et pourquoi investir (Neil Patel)
- New source [[pinterest-ads]] (neilpatel.com FR, 2025-12-10) — raw file mistitled "interest Ads".
- New concept: [[pinterest-ads]] (inspiration ads; early-funnel; intention targeting; ROAS; creative).
- Updated [[pinterest]] (1→2, +paid side), [[display-advertising]] (paid sibling link), [[ab-testing]] (1→2).
- index.md: +1 marketing concept, source under Neil Patel; stats 204→205.
- Batch: source 16/18.
---

## [2026-06-19] ingest | llms.txt : à quoi sert ce fichier et pourquoi il devient stratégique (Neil Patel)
- New source [[llms-txt]] (neilpatel.com FR, 2026-01-15).
- Expanded existing [[llm-txt]] concept (NP Digital bullish framing: piloting-not-blocking, oblivion-not-penalty, when-to-use, dense-context/entity-mapping tips; 2→3 src).
- Added confidence-split tension: NP Digital "strategic lever" vs Mueller "no AI uses it" vs Jotaro "un peu bullshit".
- index.md: source under Neil Patel; llm-txt count 2→3; stats 205→206.
- Batch: source 17/18.
---

## [2026-06-19] ingest | Élagage de contenu : la stratégie SEO pour 2025 (Neil Patel)
- New source [[content-pruning]] (neilpatel.com FR, 2025-10-22).
- New concept: [[content-pruning]] (what to prune, 4 benefits, 6-step process, best practices).
- Updated [[keyword-cannibalization]] (2→3), [[topical-authority]] (2→3), [[crawl-budget]] (2→3).
- index.md: +1 SEO-strategy concept, source under Neil Patel; stats 206→207; **batch complete (18/18), raw/assets fully ingested**.
- Batch: source 18/18 DONE.

## [2026-06-19] ingest | Neil Patel FR batch complete
- Ingested 18 new neilpatel.com FR sources (the new raw/assets backlog). 2 Feedspot RSS dumps added to .ingest-skip.txt (link lists, no single-topic value).
- New "Neil Patel / NP Digital (neilpatel.com FR)" source section in index.md.
- Major new clusters: AI/ML fundamentals (AI/ML/DL/NLP, prompt-engineering), AI-visibility/GEO tooling, technical SEO (CWV, crawl-budget+robots/noindex/TTFB, NavBoost), branding (brand-strategy/identity), channels (newsletter/email-marketing, video-marketing, pinterest-ads, omnichannel, search-everywhere-optimization), content-pruning.
- New entities: neil-patel, np-digital, ubersuggest, youtube, chatgpt, openai, claude-ai, perplexity, gemini, ahrefs, profound, scrunchai, reddit, instagram, tiktok, pinterest.
- Resolved prior dangling TODO links: email-marketing, brand-identity, video-marketing.
- Note: entities/claude.md renamed → claude-ai.md (CLAUDE.md filename collision on Windows).

## [2026-06-19] ingest | SEO pour IA : guide complet du GEO pour optimiser votre visibilité en 2026
- Source type: web article (markdown clipping). Raw file: `raw/assets/SEO pour IA  guide complet du GEO pour optimiser votre visibilité en 2026.md`
- Author: Natural-Net (agence Bordeaux). Published: 2026-03-26.
- Pages created: [[natural-net-geo-guide-2026]] (source note), [[natural-net]] (entity)
- Pages updated: [[generative-engine-optimization]] (2→3 src; enrichi des 5 piliers, plan 7 étapes, chiffres McKinsey/Gartner/IDC, taux conversion LLM par plateforme, GEO local), [[e-e-a-t]] (4→5 src), [[geo-tools]] (2→3 src; + tableau outils sémantique GEO)
- Index: +1 source, +2 pages, nouvelle section "SEO — GEO & IA (Natural-Net)", nouvelle entité [[natural-net]]
- Key new data: ChatGPT 15,9 % / Perplexity 10,5 % / Claude 5 % / Gemini 3 % conversion rates ; visiteur LLM = ×4,4 organique ; −25 % volume search d'ici 2026 (Gartner) ; robots.txt doit autoriser GPTBot/Google-Extended/PerplexityBot/ClaudeBot.
---

## [2026-06-19] ingest | Checklist SEO : 41 Conseils pour Optimiser votre Site Web
- Source type: web article (markdown clipping). Raw file: `raw/assets/Checklist SEO  41 Conseils pour Optimiser votre Site Web.md`
- Author: Semrush FR (Olivier Amici). Published: 2022-08-01.
- Pages created: [[semrush-seo-checklist-41]] (source note), [[keyword-mapping]] (nouveau concept), [[url-structure]] (nouveau concept), [[seo-audit]] (concept manquant créé — était référencé dans l'index sans fichier)
- Pages updated: [[what-is-seo]] (1→2 src + lien checklist), [[maillage-interne]] (6→7 src + section pages orphelines)
- Index: +1 source, +4 pages, nouvelle section "SEO — Checklists & Opérationnel", nouveaux concepts keyword-mapping et url-structure
- Key new data: profondeur page max 3 clics ; title ≤ 60 chars ; 1 H1 par page ; pages orphelines = invisibles pour Google ; mentions sans lien = levier link building à faible friction.
---

## [2026-06-19] ingest | Comment écrire un article de blog optimisé SEO en 2026
- Source type: web article (markdown clipping). Raw file: `raw/assets/Comment écrire un article de blog optimisé SEO en 2026.md`
- Author: Sédestral (sedestral.com). Date non renseignée, clipping 2026-06-19.
- Pages créées: [[sedestral-blog-article-seo-2026]] (source note), [[article-structure]] (concept manquant créé), [[sedestral]] (entité)
- Pages mises à jour: [[seo-copywriting]] (1→2 src + CTR benchmarks par balise, méthode PAS, densité 1-2 %, quick wins 11-20), [[maillage-interne]] (tension documentée : JotaroSeo 1-2 max vs Sédestral 2-3 min)
- Index: +1 source, +3 pages, nouvelle section "SEO — Rédaction & On-Page", nouvelle entité [[sedestral]]
- Key insights: title tag optimisé = CTR +30-50% ; cibler positions 11-20 pour quick wins ; mise à jour trimestrielle indispensable ; densité mot-clé 1-2% = 15-30 occurrences/1500 mots.
---

## [2026-06-19] ingest | Guide du débutant en référencement naturel (SEO)
- Source type: web article (markdown clipping). Raw file: `raw/assets/Guide du débutant en référencement naturel (SEO).md`
- Author: Rémi Brandini (Consultant Google, Activateur France Num) / Direction générale des Entreprises. Published: 2023-07-03, màj 2025-10-24.
- Pages créées: [[francenum-guide-debutant-seo]] (source note)
- Pages mises à jour: [[what-is-seo]] (2→3 src + tableau comparatif 3-leviers vs 4-piliers), [[backlinks]] (2→3 src + section netlinking/tissage de liens FR + tactiques TPE/PME)
- Index: +1 source, +1 page, nouvelle section "SEO — Guide officiel FR (France Num)"
- Key insights: terme FR officiel "netlinking" = backlinks ; modèle 3 leviers (technique/mots-clés/popularité) vs 4 piliers Semrush ; Schema.org produit (Product/Offer/Review/AggregateRating) pour e-commerce ; GBP prioritaire sur données structurées custom pour le local.
---

## [2026-06-19] lint | Post-batch health-check (Neil Patel FR batch)
- **Fixed broken links introduced by batch:** [[le-pouvoir-du-prompt-chatgpt]] → [[prompt-chatgpt]] (2 links in deep-learning, apercu-ia-guide).
- **Resolved stale danglings now that pages exist:** [[geo]] → [[generative-engine-optimization]] (3 links: query-fan-out, semrush-best-ai-search-engines, semrush-geo-tools).
- **Orphans:** 0 among the 44 new batch pages — every new concept/entity has ≥1 inbound link.
- **Remaining dangling links (~32):** all pre-existing TODO stubs (copywriting stubs: benefits-over-features, fab-framework, creative-brief, direct-response-copywriting, sales-page, bullet-points-copywriting; entity stubs: awai, copy-posse, filthy-rich-writer, jespernissenseo, irentdumpsters, onelegchris; technical-seo, image-seo, sxo, pbn, cloaking, ecommerce, topical-seo, trello-notion-obsidian) + france-num (from externally-added source). None from this batch.
- **Format nit (pre-existing):** [[wiki/sources/jotaro-seo-ia-x-seo]] and [[wiki/sources/tailwind-utility-reference]] use full paths instead of bare slugs.
- **Two extra sources added externally** (not in the 18): [[sedestral-blog-article-seo-2026]] (CTR benchmarks → seo-copywriting), [[natural-net-geo-guide-2026]] (semantic GEO tools → geo-tools). Source pages exist; wired correctly.
- **Tools mentioned but pageless** (candidates if they recur): Surfer SEO, Frase, MarketMuse, YourTextGuru, MarketBrew, Moz.
- **Tensions already flagged inline:** llms.txt confidence split (NP Digital vs Mueller vs Jotaro); GEO/AEO/AI-SEO terminology overlap; NavBoost CTR-as-ranking-factor (leak-based, not official).
- Suggested next: promote [[search-everywhere-optimization]] to a topics/ synthesis when a 2nd source lands; create the 3 demo topics (technical-SEO-2026 / GEO-strategy / owned-audience) on request.

## [2026-06-19] ingest | Rédaction SEO de fiches produits e-commerce (Benjamin Thiers)
- Source type: web article (raw/assets/, benjaminthiers.net, 2023-09-28)
- Pages created: [[benjamin-thiers-fiches-produits]], [[benjamin-thiers]], [[fiche-produit-seo]]
- Pages updated: [[seo-copywriting]] (1→4 src)
- Focus: title/meta par patterns à variables, h1 référence produit, champ lexical utilisateur, tableau caractéristiques
---

## [2026-06-19] ingest | Comment bien rédiger ses fiches produits pour le SEO (NOIISE / François Besson)
- Source type: web article (raw/assets/, noiise.com, 2022-06-21)
- Pages created: [[noiise-fiches-produits-seo]], [[noiise]]
- Pages updated: [[fiche-produit-seo]], [[seo-copywriting]], [[http-status-codes-seo]] (ajout code 410 Gone, 2→3 src)
- Focus: 12 étapes + checklist, intention transactionnelle, FAQ structurée, données structurées, gestion rupture stock (301/410), maillage silo
- Trous identifiés (non comblés, marqués TODO): page [[donnees-structurees]] (Schema.org), pas de page 410 dédiée (intégré à http-status-codes-seo)
---

## [2026-06-19] ingest | Fiche produit SEO : optimiser pour Google et l'IA (AudreyTips)
- Source type: web article (raw/assets/, audreytips.com, 2026-04-03)
- Pages created: [[audreytips-fiche-produit-seo-ia]], [[audrey-tips]], [[donnees-structurees]]
- Pages updated: [[fiche-produit-seo]] (3→4 src, +angle IA/chunking, variantes, industrialisation), [[canonical-tag]] (1→2 src, variantes produit)
- Focus: comprendre > optimiser ; chunking/blocs autonomes pour IA ; JSON-LD Product/Offer/AggregateRating/BreadcrumbList ; gestion variantes ; templates SEO ; prompt Gemini
- Trou comblé: [[donnees-structurees]] créée (Schema.org/JSON-LD), résout les TODO des 2 ingests précédents
---

## [2026-06-19] ingest | Comment être premier sur Google : viser le Top 3 (David Bardy / 410-gone)
- Source type: web article (raw/assets/, 410-gone.fr, 2025-12-23)
- Pages created: [[410-gone-premier-google-top3]], [[david-bardy]], [[410-gone]], [[facteurs-de-classement]]
- Pages updated: [[click-through-rate]] (2→3 src, CTR par position 2025 + IA Overview), [[e-e-a-t]] (5→6 src, montré-dans-la-page), [[off-page-seo]] (2→3 src, autorité interne + linkable assets)
- Focus: triptyque pertinence→qualité→autorité ; méthode 5 étapes ; "respirer l'odeur de la SERP" (Laurent Bourelly) ; paliers top10→5→3→1 ; SEO vs SEA (Ads nourrit SEO)
- Nouveau TODO link: laurent-bourelly (expert SEO cité, pas de page)
---

## [2026-06-20] ingest | Qu'est-ce que le netlinking, pilier essentiel du référencement de votre site web ?
- Source type: web article (markdown clipping). Raw file: `raw/assets/Qu'est-ce que le netlinking, pilier essentiel du référencement de votre site web ?.md`
- Author: Stan De Jesus Oliveira (createur2site.fr), Activateur France Num. Published: 2025-01-13, màj 2025-10-06.
- Pages créées: [[francenum-netlinking-guide]] (source note), [[anchor-text]] (nouveau concept : 4 types d'ancres), [[createur2site]] (entité)
- Pages mises à jour: [[backlinks]] (3→4 src ; stat Backlinko 3.8x, métriques DR/TF/DA/AS, 5 techniques d'acquisition, plateformes FR, prix médian 87€, erreurs à proscrire, pointeur vers [[anchor-text]])
- Index: +1 source, +3 pages
- Key insights: page 1 = 3.8x plus de backlinks que page 2 (Backlinko 2020) ; DR > 30 = benchmark PME ; croiser TF (Majestic) + DR (Ahrefs) ; prix médian backlink FR = 87€ ; 4 types d'ancres (exacte/diluée/marque/neutre) → diversification obligatoire ; plateformes FR : Semjuice, Linksgarden, Getfluence, Rocketlinks.
---

## [2026-06-20] ingest | 17 techniques pour trouver un backlink et faire un lien vers son contenu
- Source type: web article (markdown clipping). Raw file: `raw/assets/17 techniques pour trouver un backlink et faire un lien vers son contenu.md`
- Author: Bruno Fontanet (SEOQuantum). Published: 2021-11-04.
- Pages créées: [[seoquantum-17-techniques-backlinks]] (source note), [[seoquantum]] (entité)
- Pages mises à jour: [[backlinks]] (4→5 src ; mentions sans lien + requête Google gratuite, plateformes complètes FR, signaux de pénalité)
- Index: +1 source, +2 pages
- Key insights: technique des mentions sans lien = ROI élevé (requête gratuite : `"monsite.com" -inanchor:"monsite.com" -site:"monsite.com"`) ; 8 nouvelles techniques absentes du vault (interviews, infographies, jeux-concours, réseau clients/fournisseurs, sites de regroupement) ; 4 nouvelles plateformes FR (Develink, Vipseo, Soumettre, Nextlevel.link).
---

## [2026-06-20] ingest | Comment obtenir des backlinks : 11 stratégies
- Source type: web article (markdown clipping). Raw file: `raw/assets/Comment obtenir des backlinks  11 stratégies.md`
- Author: Kelly Lyons (Semrush FR). Published: 2022-11-28.
- Pages créées: [[semrush-11-strategies-backlinks]] (source note)
- Pages mises à jour: [[backlinks]] (5→6 src ; tableau catalogue complet 19 techniques, RP numériques + John Mueller quote, resource pages, HARO/Authority Sources FR, link gap analysis, listicles, témoignages)
- Index: +1 source, +1 page
- Key insights: RP numériques = technique éditoriale prioritaire (John Mueller : "tout aussi importantes que le SEO technique") ; resource pages = trouver via Semrush filtre "ressource" sur backlinks concurrents ; HARO/Authority Sources FR = liens presse gratuits via expertise citée par journalistes ; link gap = cibler qui lie aux concurrents mais pas à soi.
---

## [2026-06-20] ingest | What is Topical Authority? (+ How to Build It)
- Source type: web article (markdown clipping). Raw file: `raw/assets/What is Topical Authority? (+ How to Build It).md`
- Author: Sydney Go, Chris Shirlow, Simon Fogg (Semrush). Published: 2023-09-14.
- Pages créées: [[semrush-topical-authority]] (source note)
- Pages mises à jour: [[topical-authority]] (3→4 src ; ajout : 3 bénéfices SEO, timeline Google algo Panda→Core 2024, 4 étapes build pratique, PKD% comme proxy mesure, AlsoAsked.com, score TA Low/Moderate/Relevant/High)
- Index: +1 source, +1 page
- Key insights: PKD% (Personal Keyword Difficulty) = proxy mesure de TA — baisse quand TA croît ; AlsoAsked.com = outil PAA pour trouver sous-questions non couvertes ; principe "niché > large" ; Hummingbird 2013 = naissance de la recherche sémantique (racine du concept TA).
---

## [2026-06-20] ingest | Autorité thématique : Le guide ultime pour acquérir votre topical authority en 2026
- Source type: web article (markdown clipping). Raw file: `raw/assets/Autorité thématique  Le guide ultime pour acquérir votre topical authority en 2026.md`
- Author: Julien Gourdon (julien-gourdon.fr). Published: 2025-11-15.
- Pages créées: [[julien-gourdon-topical-authority-2026]] (source note), [[julien-gourdon]] (entity)
- Pages mises à jour: [[topical-authority]] (4→5 src ; ajout : preuves brevets MS/Google, Google Leaks siteFocusScore + siteAuthority, TA multiplateforme +50% AI Overviews, 3 piliers IA, entités > mots-clés, TA vs DA tableau, backlinks thématisés, 6-18 mois timeline)
- Index: +2 sources (source note + entity), +2 pages
- Key insights: siteFocusScore (Google Leaks 2024) = proxy mesurable de la focalisation thématique ; A(s,t) = équation Microsoft pour mesurer la TA ; entités nommées > mots-clés car Google indexe en knowledge graph depuis 2012 ; marques sur 3+ plateformes = +50% visibilité AI Overviews.
---

## [2026-06-20] ingest | Les 10 méthodes pour obtenir des backlinks naturellement (deux.io)
- Source type: web article. Raw file: `raw/assets/Les 10 méthodes pour obtenir des backlinks naturellement.md`
- Author: Alexandre Flament (deux.io). Published: 2024-09-19.
- Source introductive vs. sources backlinks déjà en vault — valeur ajoutée limitée mais réelle sur 2 points.
- Pages créées: [[deux-io-10-methodes-backlinks]] (source note)
- Pages mises à jour:
  - [[backlinks]] (7→8 src ; ajout : taxonomie types de backlinks en tableau, framework audit 4 scénarios)
- Index: 222→223 sources, 415→416 pages
- Key insights: seul ajout vraiment nouveau = le tableau de classification des types (dofollow/nofollow/éditorial/commentaire/sponsorisé/forum) et le framework d'audit 4 scénarios avec remédiation par cas (404 → redirection ; non pertinent → désavouer ; toxique → désavouer ; redirigé → demander URL directe). Les 10 méthodes sont déjà toutes couvertes dans les sources précédentes.
---

## [2026-06-20] ingest | Stratégie SEO Jotaro 2026 — Un demi-million en un an (PDF)
- Source type: PDF 24 pages. Raw file: `raw/assets/jotaro-seo-strategie-ecommerce-2026.md`
- Author: @JotaroSEO. Source: `/Users/utilisateur/Downloads/Stratégie-SEO-Jotaro-2026.pdf`
- Pages créées:
  - [[jotaro-seo-strategie-ecommerce-2026]] (source note)
  - [[strategie-concurrentielle-seo]] (concept nouveau — "[Concurrent] avis/alternative" articles)
  - [[jotaro-seo]] (entité — agrège tous les threads + ce PDF)
- Pages mises à jour:
  - [[maillage-interne]] (7→8 src ; ajout : structure silo 3 niveaux, règle des 2 liens sur fiches produit)
  - [[backlinks]] (6→7 src ; ajout : stratégie 8-10/mois, répartition 40% optimisée / 30% semi / 30% générique)
  - [[e-e-a-t]] (6→7 src ; ajout : checklist 7 points e-commerce, 4 piliers traduits pour boutique)
  - [[keyword-research]] (5→6 src ; ajout : stratégie sémantique ×10 avec exemples cagoule/ours en briques)
  - [[search-intent]] (5→6 src ; ajout : collection vs page produit — règle SERP décision e-commerce)
  - [[topical-authority]] (5→6 src ; ajout : 7 catégories de silos thématiques, champ lexical carburant TA)
- Index: 221→222 sources, 412→415 pages
- Key insights: répartition ancres backlinks 40/30/30 (jamais vu aussi précis dans le vault) ; règle des 2 liens sur fiches produit (produit suivant + collection parente) = lever d'autorité très concret ; stratégie concurrentielle "[Concurrent] avis" = interception en bas du tunnel, quasi ignorée des concurrents ; timeline SEO formalisée : 3 mois discrets → 6 mois décollage → 12 mois autonome ; 200k CA × 60% marge = 120k net sans ads > 500k CA × 15% marge après ads.
---

## [2026-06-20] ingest | Bay' Salam en e-commerce (PDF — La Meute)
- Source type: PDF ebook. Raw file: `raw/assets/lameute-bay-salam-ecommerce.md`
- Author: La Meute. Date de publication inconnue.
- Domaine nouveau : e-commerce islamique (première source du vault sur ce sujet)
- Pages créées:
  - [[lameute-bay-salam-ecommerce]] (source note)
  - [[bay-salam]] (concept : définition, 5 conditions, clauses CGV, erreurs, règle linguistique)
  - [[dropshipping-halal]] (concept : checklist conformité + marketing halal)
  - [[la-meute]] (entité)
- Pages mises à jour: index (nouveau domaine "E-commerce islamique" ajouté)
- Index: +1 source, +4 pages, +1 domaine
- Key insights: le Bay' Salam = exception islamique à "ne vends pas ce que tu ne possèdes pas" → 5 conditions : description précise, paiement intégral immédiat, délai fixé, produit générique (non spécifique), damân (responsabilité vendeur) ; règle linguistique : "le/la/les" (générique) vs "ce/cette/ces" (spécifique = interdit) ; Klarna/PayPal 4× invalide le contrat Salam ; damân = vendeur responsable jusqu'à livraison même si fournisseur coupable.
---

## [2026-06-20] ingest | Debugging common causes for slow loading in Shopify Liquid storefronts
- Source type: web article. Raw file: `raw/assets/Debugging common causes for slow loading in Shopify Liquid storefronts.md`
- Author: Sia Karamalegos (performance.shopify.com). Date: 2024-01-11.
- Langue source : anglais → note source en anglais dans frontmatter, corps en français (convention vault).
- Pages créées:
  - [[shopify-debug-slow-loading]] (source note)
  - [[shopify-liquid-performance]] (concept nouveau — diagnostic + 13 causes par métrique)
- Pages mises à jour:
  - [[core-web-vitals]] (1→2 src ; ajout : FCP comme métrique diagnostique intermédiaire, méthode RUM gap analysis)
  - [[ttfb]] (1→2 src ; ajout : causes Shopify — Liquid complexe/nested loops, Theme Inspector)
- Index: 223→224 sources, 416→418 pages
- Key insights: méthode RUM gap analysis = trier par gap (TTFB→FCP→LCP) avant d'optimiser quoi que ce soit (évite "optimiser 10 choses à l'aveugle") ; lazy-load sur l'image LCP = +1.0 s de LCP médian sur Shopify (chiffre concret) ; transitions/animations sur l'image LCP = LCP retardé même si l'image est téléchargée (counter-intuitif) ; anti-flicker snippets A/B test = FCP assassiné → toggle Liquid dans settings_schema.json comme solution propre ; storefronts Liquid Shopify = parmi les plus rapides côté serveur (le problème est presque toujours dans le code du thème ou les apps tierces).
---

## [2026-06-20] ingest | Improving your online store performance
- Source type: web article (documentation officielle). Raw file: `raw/assets/Improving your online store performance.md`
- Author: Shopify (help.shopify.com). Date accès: 2026-06-20.
- Pages créées:
  - [[shopify-improve-store-performance]] (source note)
- Pages mises à jour:
  - [[shopify-liquid-performance]] (1→2 src ; ajout : table optimisations natives Shopify, 3 facteurs d'impact, INP/JS excessif, workflow 3 étapes, Web Performance Reports natif, Chrome DevTools)
- Index: 224→225 sources, pages inchangées
- Key insights: les outils de scan tiers suggèrent souvent des optimisations déjà intégrées dans Shopify (CDN/Gzip/cache/WebP/minification) → ne pas perdre de temps sur ces recommandations ; ordre de priorité officiel Shopify = thème d'abord, apps ensuite, code tiers en dernier ; INP dégradé sur Shopify = JS excessif (thème + apps + tag managers) comme cause quasi-systématique ; désinstaller une app ne supprime pas son code du thème (piège fréquent) ; Shopify a ses propres Web Performance Reports dans l'admin = source RUM native à utiliser avant les outils tiers.
---

## [2026-06-20] maint | Mise à jour workflow blog — session pratique harnais-chien-expert.fr
- Pages mises à jour :
  - [[workflow-creation-blog]] (v1→v2) : répartition mots par section, tableau erreurs HTML Shopify, template schema Article complet avec logo, checklist étendue en 3 blocs (contenu / HTML / après publication), règle méta description dans champ SEO Shopify
  - [[article-structure]] : répartition mots par bloc, tableau erreurs Shopify (meta tags, JSON-LD, rel noopener noreferrer, publisher logo)
- Apprentissages validés en session (analyse HTML réel) :
  - `<meta charset>` / `<meta viewport>` / `<meta description>` ne doivent JAMAIS être dans l'éditeur HTML Shopify — la meta description va dans le champ SEO Shopify
  - `<script type="application/ld+json">` se colle à la racine de l'éditeur HTML, jamais dans un `<p>`
  - `publisher.logo` obligatoire dans le schema Article pour que Google accepte le rich snippet
  - Liens externes `target="_blank"` → `rel="noopener noreferrer"` (sécurité + signal SEO)
  - Article sous 1 200 mots → ajouter une H2 thématique (ex : "Quand changer/renouveler X ?")
  - Répartition cible validée : intro 100-150 mots, H3 80-120 mots, FAQ 60-100 mots/réponse, conclusion 80-120 mots
---

## [2026-06-21] query | ma-vanity product naming fix
- Corrigé 164 fiches produits Shopify (puwww1-vg) via Admin GraphQL : 166 seo.title réécrits (≤60, finissent par `| Ma-Vanity`, 0 tronqué, 0 dup) + 166 méta uniques (≤160, 0 dup, bénéfice persona voyage/organisation). Baseline 147 dup → 0.
- Couleurs : 3 titres corrigés (Or Rose, Rose Poudré, Blanc Cassé) + variante "Coloris photo"→"Assorti". Anglais option values (Inches/mm/lock/Tote/Handbag/Small) → FR ; collection "Vanity with mirror & lights" → "Vanity miroir lumineux LED".
- Phase 4 (OK humain) : fusion Miroir Lumineux→LED, 2 produits supprimés + 2× 301. Handles junk laissés (OK humain). 4 autres doublons différenciés sans fusion.
- Livrable : [[ma-vanity-naming-audit]]. Changelog rollback dans `_mavanity/`. Cocon préservé (mère=tête, fille=couleur). Token shop à révoquer (exposé en clair dans le prompt).

## [2026-06-22] ingest | Réussir son référencement web — Andrieu (10e éd. 2020-2021)
- Source type: PDF scannérisé 809 pages (images + texte mixte), lecture visuelle page par page
- Raw file: raw/reussir-referencement-web-2020-2021.pdf (103 MB original)
- Pages créées:
  - [[reussir-referencement-web-andrieu-2020]] (source note — 16 chapitres synthétisés)
  - [[olivier-andrieu]] (entity — fondateur Abondance.com)
  - [[duplicate-content]] (concept — causes, solutions, règle canonique)
  - [[google-algorithmic-filters]] (concept — Panda/Penguin/EMD/Core Updates)
  - [[hreflang]] (concept — multilingue, syntaxe, 3 structures internationales)
  - [[longue-traine]] (concept — définition, évaluation compétition, outils)
- Index: 225→226 sources, 418→423 pages
- Apprentissages clés du livre :
  - Concurrence mot-clé estimable via nb résultats : <1000=faible, 5000-10000=moyen, >10000=difficile
  - Panda (contenu) vs Penguin (liens) : distinction fondamentale, souvent confondus
  - répertoires `/fr/` recommandés sur ccTLD pour sites internationaux (mutualise l'autorité)
  - Balise title = zone chaude n°1, meta description = pas de ranking mais CTR
  - Fautes d'orthographe = source de trafic réelle à ne pas ignorer
  - PDF 809 pages entièrement scannérisé (0 texte extractible) — outil PyMuPDF + vision utilisé
---

## [2026-06-25] ingest | Checklist SEO complète : 38 conseils pour 2025
- Source type: web-article (clipping Obsidian)
- Raw file: raw/assets/Checklist SEO complète  38 conseils pour 2025.md
- Source: Shopify FR (shopify.com/fr/blog), publié 2024-11-04
- Pages créées: [[shopify-checklist-seo-38-2025]]
- Pages mises à jour: index.md (227 sources, 424 pages)
- Différentiel vs [[semrush-seo-checklist-41]] : orienté e-commerce Shopify débutant ; + section Local SEO ; + bonus 2025 (IA, formats SERP, UX) ; - robots.txt, cannibalisation, redirections 302 ; FID encore cité ⚠️ (remplacé par INP mars 2024)
---

## [2026-06-25] ingest | Comment optimiser votre visibilité dans les réponses des IA génératives en 2026 ?
- Source type: web-article (clipping Obsidian)
- Raw file: raw/assets/Comment optimiser votre visibilité dans les réponses des IA génératives en 2026 ?.md
- Source: Minddex.ai (Thibaut Fitoussi, co-fondateur), publié 2026-02-25
- ⚠️ Biais commercial fort : auteur = CEO de Minddex, outil recommandé à chaque étape
- Pages créées: [[minddex-geo-2026]], [[thibaut-fitoussi]], [[minddex]]
- Pages mises à jour: [[generative-engine-optimization]] (+ table longueur réponse par plateforme IA + tactiques IndexNow/OpenAI/Wikipedia)
- Apports uniques vs [[natural-net-geo-guide-2026]] : longueur de réponse par IA (ChatGPT 280-340 mots, Gemini 490-590, Perplexity 350-450, Claude 400-500), soumission catalogue OpenAI, stratégie Wikipedia/Wikidata, IndexNow pour Bing/ChatGPT, avis clients comme signal GEO
---

## [2026-06-25] ingest | Référencement prédictif — Méthode Google Trends (Jotaro)
- Source type: document (MD, batch Downloads)
- Raw file: Downloads/Tweet Jotaro - Referencement predictif Google Trends.md (ou PDF équivalent)
- Pages créées: [[jotaro-referencement-predictif-google-trends]]
- Index: +1 source (228→229)
---

## [2026-06-25] ingest | BOUSSOLUTION — Connaissance Jotaro Étendue v9
- Source type: document (MD, batch Downloads)
- Raw file: Downloads/BOUSSOLUTION - Connaissance Jotaro Etendue.md
- Pages créées: [[jotaro-boussolution-methode-v9]]
- Index: +1 source (229→230)
---

## [2026-06-25] ingest | BOUSSOLUTION — Patterns sites clients Jotaro
- Source type: document (MD, batch Downloads)
- Raw file: Downloads/Patterns sites clients.md
- Pages créées: [[jotaro-boussolution-patterns-clients]]
- Index: +1 source (230→231)
---

## [2026-06-25] ingest | Système contenu SEO 0€ → +400 000€ (Jotaro)
- Source type: twitter-thread clipping (MD, batch Downloads)
- Raw file: Downloads/Tweet Jotaro - Système contenu SEO 400K.md
- Pages créées: [[jotaro-seo-content-strategy]] (fichier manquant créé — slug déjà référencé dans index)
- Index: source déjà comptée, +0
---

## [2026-06-25] ingest | Guide Dropshipping SEO (Halal)
- Source type: ebook-pdf (23 pages)
- Raw file: Downloads/GUIDE DROPSHIPPING SEO (HALAL).pdf
- ⚠️ Biais commercial : auteur = mimine-ecom-seo.com, promeut ebook 79,90€
- ⚠️ Backlinks via SEO Pepper mentionnés = black hat (ne pas appliquer)
- Pages créées: [[guide-dropshipping-seo-halal]]
- Pages mises à jour: [[dropshipping-halal]] (+1 src → 2 src), [[pinterest]] (+stratégie organique 20-30 pins/jour)
- Apports uniques : SpeedFly theme Shopify, Flippa pour niche selection, AliExpress DS Center, concept jus SEO + breadcrumbs, Pinterest Trends comme signal prédictif, template page produit (H2+H3 specs+tailles+entretien)
- Index: 228→232 sources, 427→431 pages
---

## [2026-06-25] ingest | Comment trouver des fournisseurs sur Aliexpress
- Source type: ebook-pdf (10 pages)
- Raw file: Downloads/Comment trouver des fournisseurs sur Aliexpress.pdf
- Auteur: mimine-ecom-seo (même auteur que guide-dropshipping-seo-halal)
- Pages créées: [[mimine-aliexpress-fournisseurs]]
- Apports uniques : 4 extensions Chrome AliExpress (AliTools/Asify/AliSave/Search by Image), checklist 9 critères fournisseur (seuil 95%+, ≥10k abonnés, ≥1 an), checklist 8 critères produit, règle fournisseur fiable→tous produits OK, piège "choice" sans boutique = collection interne AliExpress
- Index: 232→233 sources, 431→432 pages
---

## [2026-06-25] ingest | Ebook Business Halal (Adam + Mimine)
- Source type: ebook-pdf (70 pages)
- Raw file: Downloads/EBOOK_BUSINESS_HALAL.pdf
- Auteurs: Adam (business/logistique, parties 1-23) + Mimine (SEO, parties 24-70) — même Mimine que guide-dropshipping-seo-halal et mimine-aliexpress-fournisseurs
- ⚠️ Lien affilié Linkuma (fpr=m4qxu) dans la partie SEO → biais commercial
- ⚠️ Conflit Pinterest : ce guide dit 5-15 épingles/jour vs 20-30 dans guide-dropshipping-seo-halal (mêmes auteurs, guides différents)
- Pages créées: [[ebook-business-halal]]
- Pages mises à jour: [[dropshipping-halal]] (+1 src → 3 src), [[pinterest]] (conflit volumes, +données plateforme 454M/60% femmes, +process 9 étapes)
- Apports uniques : 3 modèles logistiques (domicile/3PL/agent), 3 types produits (générique/ODM/OEM) + progression stratégique, 10 critères agent chinois, sourcing Alibaba (template email, règle 30/70, contrôle qualité SGS/V-Trust), EORI obligatoire (douane.fr), DDP incoterm, stratégie 70/30 transport bateau/avion, micro-entreprise (plafond 188700€, ACRE, CFE), Authority Score Semrush (<20 faible, 20-30 moyen, >30 sérieux), shop.app niche US→FR transfer trick, SpeedFly trick 30€ abandon cart
- Index: 233→234 sources, 432→433 pages
---

## [2026-06-27] ingest | JotaroSEO — Audit simplifié en 5 zones
- Source type: tweet (X)
- Source URL: https://x.com/JotaroSeo/status/2057867668015731083
- Raw file: 01 - SEO/9 - Audit SEO/01 - jotaro-seo-audit-simplifie.md
- Pages créées: [[jotaro-seo-audit-simplifie]]
- Pages mises à jour: [[seo-audit]] (nouvelle section + table 5 zones), [[jotaro-seo]] (source_count 6→7)
---

## [2026-06-27] ingest | Julien CTR — Framework SEO Complet (taxonomie 15 catégories)
- Source type: tweet (X)
- Source URL: https://x.com/CTRBooster75/status/2064228300646437052
- Raw file: 01 - SEO/1 - Fondamentaux/18 - julien-ctr-framework-seo-complet.md
- Pages créées: [[julien-ctr-framework-seo-complet]], [[julien-ctr]], [[google-discover]]
- Pages mises à jour: [[seo-roadmap]] (source_count 1→2, section Julien CTR ajoutée)
- Nouveaux concepts signalés (stubs à enrichir): Google Discover, Automatisation SEO, Validation business de niche, Revenu par page
---

## [2026-06-28] ingest | RayEcom — Guide complet E-commerce FREE
- Source type: article Notion (markdown)
- Raw file déplacé: `07 - Méthode e-com Meta/1 - Fondations et Stratégie/01 - rayecom-guide-ecom-complet.md`
- Pages créées: [[rayecom-guide-ecom-complet]], [[rayecom]], [[meta-ads-ecom]], [[winning-product]], [[creatif-ecom]], [[cro-ecom]]
- Section thématique créée: `07 - Méthode e-com Meta/` avec 7 sous-dossiers + `00 - Vue d'ensemble — Méthode e-com Meta.md`
- Nouveau domaine ajouté au vault: E-commerce Meta Ads (dropshipping / boutique de niche brandée)
- Contenu couvre: fondations (budget/stratégie), recherche produit (4 critères + TrendTrack), Meta Ads (ROAS BE/Target, CBO), créatives (TOFU/MOFU/BOFU, static/vidéo/native), site Shopify (config + email Klaviyo), CRO (bundles/upsells/A-B tests), agents sourcing
---

## [2026-07-06] ingest | JotaroSEO — Comment avoir de gros résultats en SEO sans backlinks ?
- Source type: article long-forme (X/Twitter)
- Source URL: https://x.com/JotaroSeo/article/2074157486710329829
- Raw file déplacé: `01 - SEO/5 - Contenu et Rédaction/19 - jotaro-seo-sans-backlinks.md`
- Pages créées: [[jotaro-seo-sans-backlinks]], [[angle-produit-seo]]
- Pages mises à jour: [[jotaro-seo]] (source_count 7→8), [[keyword-research]] (source_count 6→7, avis clients comme 7e source + règle "tout volume est bon" + check format SERP), [[off-page-seo]] (source_count 3→4, section "Marketing 360 comme levier off-page"), [[topical-authority]] (source_count 6→7, cadence de publication par stade + indexation manuelle GSC)
- Nouveau concept: [[angle-produit-seo]] — 6 types d'angles produit (direct / occasion / destinataire / émotionnel / matériaux / comparatif) à cartographier AVANT toute recherche de mots-clés ; absent du vault avant cet ingest
- Thèse centrale: "les backlinks amplifient ce qui existe déjà. Si la base est mauvaise, les backlinks ne changeront rien."
---

## [2026-07-07] ingest | @bounceidc — Google Maps + Claude Code = $2,000 website deals. The complete loop.
- Source type: article X/Twitter
- Source URL: https://x.com/bounceidc/status/2072654466403438983
- Raw file déplacé: `08 - Création de site web/1 - Prospection et Leads/01 - bounceidc-google-maps-claude-code-loop.md`
- Pages créées: [[bounceidc-google-maps-claude-code-loop]], [[bounceidc]], [[prospection-google-maps]], [[freelance-web-loop]], [[claude-code-build-workflow]]
- Section thématique créée: `08 - Création de site web/` avec 4 sous-dossiers + `00 - Vue d'ensemble — Création de site web.md`
- Nouveau domaine ajouté au vault: Création de site web (freelance / commerces locaux)
- Contenu couvre: prospection Google Maps (4 filtres), build Claude Code + design skills, outreach démo-first, pricing $500-2 500 + care plan $50/mois
---

## [2026-07-11] schema | CLAUDE.md créé + vault versionné
- `CLAUDE.md` créé à la racine (manquait alors que le skill `ingest` le lit au Step 4) : sémantique des dossiers, règle backlinks obligatoires (≥3 dont 1 ancien), checklist maintenance.
- `git init` dans le vault + premier commit (l'auto-commit du skill `ingest` échouait silencieusement faute de repo).
---

## [2026-07-11] maint | Correction lien cassé [[overview]]
- `wiki/overview.md` n'existait pas alors que `index.md` le référence comme point d'entrée principal depuis le bootstrap (2026-06-14).
- Page créée : thèse du vault, domaines couverts, stats, guide de navigation.
---

## [2026-07-07] ingest | @VengeonsP — 12 agents : système SEO IA
- Source type: article X/Twitter
- Source URL: https://x.com/vengeonsp/article/2075499608495600054
- Raw file déplacé: `01 - SEO/1 - Fondamentaux/20 - vengeonsp-12-agents-seo-ia.md`
- Pages créées: [[vengeonsp-12-agents-seo-ia]], [[vengeonsp]], [[agent-seo-ia]]
- Pages mises à jour: [[google-search-console]] (source_count 2→3, 6 analyses GSC), [[keyword-research]] (source_count 7→8, ranking relatif + content hubs), [[maillage-interne]] (source_count 8→9, max 5 liens + liste à-ne-pas-lier + fuites d'autorité)
- Nouveau concept: [[agent-seo-ia]] — quarterback pattern, framework ICE (Impact/Confiance/Facilité), principe Levier > Création, taxonomie des 12 agents avec inputs/outputs
- Thèse centrale: "la différence entre ceux qui essaient et ceux qui en tirent des € = le process que l'IA suit"
---

## [2026-07-11] maint | Maintenance hebdo automatisée
- **Liens cassés trouvés** :
  - ~100 wikilinks dans `wiki/` pointent vers des cibles sans fichier `.md` correspondant dans `wiki/` (ex : `academie-3-emotions-achat`, `alexgroberman-62pct-beyond-top10`, `jotaro-seo-301-redirects`, `semrush-ai-referral-traffic`, `copy-posse-ai-for-writers-2026`, `shopify`, `copywriting`, `ecommerce`, `technical-seo`, `local-seo`…). Beaucoup sont des citations précises (stats, claims) attribuées à des sources jamais ingérées comme pages `wiki/sources/` — **non corrigés automatiquement** : créer ~100 stubs à l'aveugle risquerait de légitimer des citations non vérifiées, et satisfaire la règle des 3 backlinks/stub pour chacun dépasse le cadre d'une passe de maintenance automatisée. **À trancher par l'utilisateur** : soit ingérer les sources manquantes, soit corriger les citations dans les pages concernées.
  - ~140 liens `raw/assets/...` sont cassés car le dossier `raw/` n'existe plus sur disque : les fichiers sources ont été réorganisés dans l'arborescence par domaine (`01 - SEO/`, `02 - GEO et IA/`, `07 - Méthode e-com Meta/`, `08 - Création de site web/`, etc. — cf. log 2026-06-28 et suivants, "Raw file déplacé"). Ce n'est pas une perte de données : le contenu existe toujours, sous un chemin différent. **Non corrigé** : `raw/` est une couche jamais éditée par règle CLAUDE.md, et la correction en masse de ~140 chemins dans des pages existantes dépasse le "trivial et sûr" — à faire en session dédiée avec vérification page par page.
- **Pages orphelines repérées et corrigées** (aucun backlink entrant depuis une autre page du graphe wiki) :
  - [[ga4-setup-harnais-chien]] → lien ajouté depuis [[google-analytics-4]] (exemple concret d'installation).
  - [[workflow-creation-blog]] → lien ajouté depuis [[maillage-interne]] (application concrète de la règle des 2-3 liens internes).
  - [[la-meute]] → lien ajouté depuis [[dropshipping-halal]] (organisme source de l'ebook Bay' Salam) ; la page apparaissait déjà dans `index.md` mais sans lien entrant depuis le graphe wiki lui-même.
- **Entrées `index.md` ajoutées** (fichiers présents sur disque mais absents du catalogue) :
  - Concepts (9) : [[anchor-text]], [[duplicate-content]], [[google-algorithmic-filters]], [[hreflang]], [[longue-traine]], [[strategie-concurrentielle-seo]], [[google-discover]], [[ga4-setup-harnais-chien]], [[workflow-creation-blog]].
  - Entités (7) : [[createur2site]], [[julien-ctr]], [[julien-gourdon]], [[minddex]], [[olivier-andrieu]], [[seoquantum]], [[thibaut-fitoussi]].
- **Non traité, à surveiller** : le volume de citations non sourcées (~100 liens) suggère soit des ingestions incomplètes, soit des synthèses ayant anticipé du contenu pas encore ingéré — recommandé de traiter au prochain `ingest` ou `synthesis`.
---

## [2026-07-12] ingest | @NicholasDulait — The guide to Rank #1 with Parasite SEO (Automated with Claude)
- Source type: article X/Twitter
- Source URL: https://x.com/nicholasdulait/article/2075482174824857704
- Raw file déplacé: `01 - SEO/1 - Fondamentaux/21 - nicholasdulait-parasite-seo-guide.md`
- Pages créées: [[nicholasdulait-parasite-seo-guide]], [[nicholasdulait]], [[parasite-seo]]
- Pages mises à jour: [[off-page-seo]] (source_count 4→5, section Parasite SEO ajoutée)
- Nouveau concept: [[parasite-seo]] — utiliser DR90+ de X/LinkedIn/GitHub/YouTube pour ranker sur requêtes commerciales Google sans site web ; format post X (1re phrase = title SEO, gras = H2) ; indexation forcée 2-24h ; monétisation 60% codes promo / 30% referrals / 10% CPA ; scaling 500-5 000€/mois
- Entité: [[nicholasdulait]] — @NicholasDulait, spécialiste parasite SEO affiliation sans site web
---

## [2026-07-12] maint | Nettoyage liens cassés (session dédiée)
- Réaudit complet post-fusion : le chiffre initial de la routine automatisée (~240 liens) était partiellement obsolète (calculé avant la fusion du contenu local). Vrai chiffre recalculé : 163 liens réellement cassés, puis 57 restants après ce nettoyage.
- **21 corrections de nommage** (alias/slug incohérents vers des pages déjà existantes) : ex. `Benjamin Thiers`→[[benjamin-thiers]], `Neil Patel`→[[neil-patel]], `Stan De Jesus Oliveira`→[[createur2site]], `L'académie`→[[academie-copywriting]], `copy-posse`→[[alex-cattoni]], `filthy-rich-writer`→[[nicki-krawczyk]], `Semrush Team`→[[semrush]], + 5 typos d'apostrophe dans des chemins `raw/assets/`.
- **6 nouvelles fiches entités créées** (sources déjà ingérées, page manquante) : [[irentdumpsters]], [[jespernissenseo]], [[onelegchris]], [[awai]], [[france-num]], [[shopify]].
- **~215 wikilinks débracketés** (bylines d'auteurs cités une seule fois dans un article — Aida Knezevic, Ajdin Perco, etc. — + artefacts de template `comp1.com`/`^`/liens vides) : texte conservé, juste retiré des `[[...]]` pour ne pas polluer le graphe de pages à sur-créer, conforme à la règle du vault.
- **Non traité, laissé en l'état** :
  - ~24 concepts très cités mais jamais rédigés (`sales-page` 19×, `image-seo`, `freelance-copywriting`, `technical-seo`, `pbn`, `cloaking`...) — nécessitent une vraie rédaction, hors périmètre de cette session.
  - ~13 chemins `raw/assets/...` génuinement introuvables (pas de correspondance même approximative) — petit volume, à vérifier individuellement si besoin.
  - `@alexgroberman` / `@bloggersarvesh` cassés uniquement à l'intérieur de `raw/assets/` (frontmatter) — non touché, conforme à la règle « raw/ jamais édité » ; les liens équivalents dans `wiki/` pointent déjà correctement vers [[alex-groberman]] / [[sarvesh-alventra]].
- **Bug détecté et corrigé en cours de route** : un remplacement automatique trop large avait accidentellement corrompu la commande d'exemple dans `CLAUDE.md` (règle de maintenance) en confondant le caractère `^` isolé (item de nettoyage légitime) avec son occurrence dans une regex. Corrigé immédiatement, aucun autre cas détecté après vérification du diff complet.
---

## [2026-07-12] synthesis | Synthèse semaine 2026-W28
- Sources couvertes : [[jotaro-seo-sans-backlinks]], [[bounceidc-google-maps-claude-code-loop]], [[vengeonsp-12-agents-seo-ia]], [[nicholasdulait-parasite-seo-guide]]
- Thèmes : Claude/Claude Code comme moteur d'automatisation transverse (agents SEO, build de sites freelance, production Parasite SEO) ; vitesse d'indexation comme levier différencié (GSC manuel vs outil tiers) ; pattern "construire/publier avant de vendre".
- Tension repérée : autorité SEO propre et durable ([[jotaro-seo-sans-backlinks]], [[topical-authority]]) vs autorité empruntée à des plateformes tierces DR90+, rapide mais fragile ([[parasite-seo]]).
- Questions ouvertes : robustesse du Parasite SEO face aux CGU/algos plateformes ; généralisabilité de l'indexation forcée à des sites établis ; domaine "Création de site web" encore mono-source.
- Page créée : [[synthese-2026-w28]]. index.md mis à jour (459 pages).

---

## [2026-07-13] maint | Maintenance hebdo automatisée
- **Liens cassés corrigés (14)** :
  - `[[raw/assets/jotaro-seo-ia-x-seo]]` et `[[wiki/sources/jotaro-seo-ia-x-seo]]` (9 fichiers) + `[[raw/assets/tailwind-utility-reference]]` (2 fichiers, dont `index.md`) → redirigés vers `[[jotaro-seo-ia-x-seo]]` / `[[tailwind-utility-reference]]`, pages désormais existantes suite à des ingests postérieurs à la dernière passe de nettoyage raw/.
  - 5 renommages vers une cible existante déjà présente dans le vault : `[[bullet-points-copywriting]]`→`[[bullet-points]]`, `[[checklist-fiche-produit]]`→`[[fiche-produit-seo]]`, `[[netlinking]]`→`[[backlinks]]`, `[[trello-notion-obsidian]]`→`[[productivity-tools]]`, alias inversé `[[confirmation bias|cognitive-biases]]`→`[[cognitive-biases|confirmation bias]]` (bug de pipe-alias dans `mirror-effect.md`).
  - 1 débracketage : `[[source]]` (mot générique, pas une cible réelle) dans `minddex-geo-2026.md`.
- **18 stubs créés** pour des concepts/entités explicitement marqués TODO dans le vault (`(create)`, `(TODO)`, `(when ingested)`) et cités par ≥1 source déjà ingérée : concepts [[sales-page]] (19 refs), [[freelance-copywriting]] (9), [[image-seo]] (6 — déjà référencé dans index.md), [[ai-for-writers]] (4), [[technical-seo]], [[ecommerce]], [[fab-framework]], [[direct-response-copywriting]], [[benefits-over-features]], [[cloaking]], [[pbn]], [[sxo]], [[meta-description]], [[collection-page-seo]], [[creative-brief]], [[gharar]] ; entités [[aliexpress]], [[chatseo-app]]. Chacun : frontmatter minimal + 1-2 lignes de contexte, aucun contenu existant modifié.
- **Non touché (conforme à la règle « raw/ jamais édité »)** : ~200 liens `raw/assets/*.md` restants + 9 auto-références dans le champ frontmatter `raw:` (5 titres d'articles longs, 3 `-x-thread`, `llm-wiki-idea`) — pattern identique à celui documenté le 2026-07-11/12, aucune nouvelle occurrence.
- **Pages orphelines** : 0 (vérifié après création des stubs — chaque nouvelle page reçoit au moins le backlink de sa source citante).
- **index.md** : 0 fichier manquant après cette passe. Entrées ajoutées : 13 sources déjà présentes sur disque mais non cataloguées (AWAI, Copy Posse ×2, FRW ×7, `jotaro-seo-ia-x-seo`, `tailwind-utility-reference`), 15 concepts + 2 entités correspondant aux stubs créés ci-dessus. Stats mises à jour (241 sources · 479 pages · maj 2026-07-13).
- Commit + push effectués.

## [2026-07-17] ingest | @sairahul1 — How To Build a Multi-Model AI Team in 2026
- Source type: article X/Twitter
- Source URL: https://x.com/sairahul1/article/2077642705686122743
- Raw file: raw/assets/How To Build a Multi-Model AI Team in 2026.md (déjà clippé par Obsidian)
- Pages créées: [[sairahul1-multi-model-ai-team]], [[sairahul1]], [[multi-model-ai-workflow]]
- Nouveau concept: [[multi-model-ai-workflow]] — spécialisation par outil IA + couche mémoire partagée (Unibase Memory) ; lien avec le vault Cerveaux comme mémoire structurée complémentaire
- Insight clé: "Tu es l'API entre tes propres AIs" — la solution est une infrastructure mémoire externe cross-tools
---

## [2026-07-17] ingest | @Raytar — Stop Being the Loop. Here's How to Make Claude Work While You Sleep.
- Source type: article X/Twitter
- Source URL: https://x.com/raytar/article/2069212188619805179
- Raw file: raw/assets/Stop Being the Loop. Here's How to Make Claude Work While You Sleep..md (clippé par Obsidian)
- Pages créées: [[raytar-loop-engineering-claude]], [[raytar]], [[loop-engineering]]
- Nouveau concept: [[loop-engineering]] — /goal (boucle jusqu'à état final, vérification par 2e instance Claude) + /loop (rythme), charter template complet, LOOP-STATE.md comme héros silencieux
- Insight clé: "Prompting is doing the work. Loop engineering is managing the worker." (Boris Cherny, Anthropic)
---

## [2026-07-18] ingest | Le jugement de l'usage du système drop shipping et les moyens de régularisation de l'opération (Islam Q&A)
- Source type: article web (fatwa)
- Source URL: https://islamqa.info/fr/answers/334744
- Raw file: raw/assets/Le jugement de l'usage du système dropshipping et les moyens de régularisation de l'opération - Islam en questions et réponses.md (déjà clippé par Obsidian)
- Pages créées: [[islamqa-dropshipping-regularisation]], [[islamqa]], [[mourabaha]], [[wikala]]
- Pages mises à jour: [[dropshipping-halal]] (+2 voies de régularisation alternatives au Bay' Salam)
- Insight clé: confirmation indépendante (école/raisonnement différents, angle possession/qabd) de l'interdit du dropshipping classique déjà documenté via [[bay-salam]] ; 2 alternatives non couvertes jusqu'ici — mourabaha (achat réel + revente à marge) et wikala (mandat de gérance, client ou fournisseur) — utiles si le paiement intégral à l'avance du Salam est trop contraignant pour le flux logistique Wildone
---
