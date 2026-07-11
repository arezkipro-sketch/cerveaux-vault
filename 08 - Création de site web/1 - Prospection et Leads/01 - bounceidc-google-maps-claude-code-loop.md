---
title: "Google Maps + Claude Code = $2,000 website deals. The complete loop."
source: "https://x.com/bounceidc/status/2072654466403438983?s=12"
author:
  - "[[@bounceidc]]"
published: 2026-07-02
created: 2026-07-10
description: "Everyone is teaching you how to build a $10,000-looking website with AI. Almost nobody is teaching you the part that pays: who buys it, how ..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HMML33wa0AAsYVo?format=jpg&name=large)

Everyone is teaching you how to build a $10,000-looking website with AI. Almost nobody is teaching you the part that pays: who buys it, how you find them, and what you say. The build stopped being the hard half. This guide covers the whole loop: find, build, ship, sell.

No "I got rich in one afternoon" story. Just the system, broken down so you can run it this week.

One note before we start: the outreach message near the bottom matters more than any prompt in here. Every step above it exists so you can send it.

![Image](https://pbs.twimg.com/media/HMMNHObbQAAw5RO?format=jpg&name=large)

## The honest part first

What's real:

- Claude Code writes the full code for a custom site from scratch. No template, no Wix-clone look. It's included in the Claude Pro plan at $20/month. You do not need a more expensive plan for this.
- Two free skills fix the default "AI look". frontend-design, built by Anthropic, runs in the background and bans the overused fonts and layouts. UI/UX Pro Max, community-built, ships with dozens of UI styles, palettes and font pairings you call on demand.
- Hosting with a free first-year domain runs about $40-45 for the year.
- Local businesses pay real money for this. Restaurants, dentists, gyms, contractors and realtors routinely pay $1,000-5,000 for a premium one-page site. That range is what agencies charge today.

What's not real: nobody pays you for knowing how to build. The $2,000 is what the work sells for after you do outreach, and a realistic first deal takes two to four weeks of actually sending demos. If you want a "press button, receive money" toy, close this now.

## Why this window exists right now

Three things happened close together:

1. Claude Code moved from developer-only tooling into the $20 consumer plan. The build cost of a custom site collapsed to a subscription and an afternoon.
2. The design skills shipped. Before them, AI sites had a recognizable cheap look. With frontend-design plus UI/UX Pro Max, the output clears the bar that agencies charge five figures for.
3. Local businesses didn't get the memo. Open Google Maps in any mid-size city: thousands of profitable businesses with sites from 2015, broken mobile layouts, or no site at all.

Collapsed build cost + closed quality gap + a market that hasn't noticed = the window. It stays open until enough people run this loop. They haven't yet.

## Part 1: Find buyers on Google Maps (15 minutes)

You're not looking for businesses that need a website. You're looking for businesses that make money and have a bad one. Those are different searches.

Open Google Maps, pick one niche in one city, and filter with this:

```text
THE 4 FILTERS

1. Niche where a site drives revenue:
   restaurants, dental clinics, gyms, med spas,
   contractors, real estate. Skip hobby shops.
2. Rating 4.4+ with 50+ reviews
   (proof they have customers and cash flow)
3. Website: dated, broken on mobile, or missing
4. City big enough that one niche has 20+ candidates
```

![Image](https://pbs.twimg.com/media/HMMPgT-aYAARtme?format=jpg&name=large)

Build a list of 20 in a spreadsheet: business name, contact (owner email or Instagram), and one line on what's wrong with their current site. That last column becomes your opener later.

Why 4.4+ stars and not the strugglers: a failing business won't spend $1,500 on a site. A thriving one with an embarrassing site already knows it's embarrassing. You're not creating demand, you're catching it.

## Part 2: Build the demo before anyone asks for it

This is the core move of the whole system. You don't pitch. You show up with the site already built. A cold message with a finished demo gets read; a cold message with a promise gets deleted.

Setup, once:

1. Claude Pro at [claude.com](https://claude.com/), install the desktop app, switch to code mode.
2. Create an empty folder as your workspace and open it in the app.
3. Install both skills by pasting their GitHub links into Claude Code: frontend-design ("Install this skill globally") and UI/UX Pro Max ("Install this plugin using npm, globally"). Allow the edits.
4. Switch the mode selector to auto mode so Claude works without asking permission at every step.

Then gather taste. Don't describe design in words, show it: grab 3-5 screenshots from Dribbble, Awwwards or Pinterest that match the direction (search "modern \[niche\] website design"). Drop them in a /reference folder. You're showing direction, not copying.

![Image](https://pbs.twimg.com/media/HMMPowVa4AAqYP9?format=jpg&name=large)

Now the build prompt. Adapt the brief, keep the structure:

```text
/ui-ux-pro-max

Build a single-page website for [BUSINESS TYPE + CITY, e.g. a
family-run Thai restaurant in Austin].

Direction: [the vibe in your own words. e.g. warm, modern,
appetite-driven. NOT a generic template look.]

Sections in order: hero, story, menu/services, the space,
contact. One page, scrolls top to bottom.

I'm attaching reference screenshots from the /reference folder.
Match the feeling, don't copy them.

Tech stack: single-file static HTML/CSS/JS. Keep it simple.

Before you write any code, ask me clarifying questions.
```

The last line is the highest-value sentence in this article's prompts. Claude stops, asks 5-7 questions about style, sections, copy tone and animation level, and your answers become the foundation of the site. Be specific here and you barely fight it later.

First version lands in about 10 minutes. Then two polish passes:

Pass 1, grade it. Paste this:

```text
Review this site against these criteria and be honest about
what needs work:
- Typography (are we on overused AI fonts like Inter?)
- Color (restrained palette, 4-5 values max?)
- Hierarchy (does sizing guide the eye 1st, 2nd, 3rd?)
- Motion (intentional micro-interactions or static?)
- Mobile (designed for phones or just shrunk?)
- Copy (specific and sensory, or adjective soup?)
```

Pass 2, make it expensive. Don't fix things one at a time, lead with intent and ask for a batch:

Finish with a dedicated mobile pass ("decide what hides, tightens and resizes on small screens; this is the version most people will see"). One evening, one demo that looks like an agency invoice.

```text
The lower sections feel a bit generic. We don't need to make
them busier, just more expensive. Propose a batch of subtle
micro-interactions and refinements and apply them all at once.
```

One efficiency trick: you build one demo per niche, not per business. The Thai restaurant demo works for all 20 Thai restaurants on your list. Record a 40-second screen capture scrolling through it on desktop and phone. That video is your outreach ammo.

## Part 3: Ship it only after the yes

Don't buy hosting for demos. Screenshots and the screen recording are enough to sell. When a deal closes, hosting with a free first-year domain is $40-45, and there's exactly one mistake that produces a blank page: when you upload, zip the files inside your project folder, not the folder itself. index.html has to sit at the top level of the zip. Everyone hits this once.

## Part 4: The outreach (the part every build guide skips)

You have a list of 20 and a demo video. Here's the message. Email or Instagram DM, wherever the owner actually is:

\[Your name\]

```text
Subject: made this for [Business Name]

Hi [Name], I redesign websites for [niche] in [city].
I already built a concept for [Business Name]. 40-second
video attached.

Your current site [one specific problem: doesn't load right
on phones / doesn't show the menu / looks older than the food].
This one fixes that.

If you like it, it's live on your domain this week.
Flat $[price], no subscriptions, no agency retainer.
If not, no hard feelings, the video's yours to keep.

[Your name]
```

![Image](https://pbs.twimg.com/media/HMMP3EJbIAAJnDa?format=jpg&name=large)

Rules that make this work: lead with the video, not credentials. Name one specific problem with their current site, that's the column from your spreadsheet. Flat price, stated plainly. And never say "AI-built". Not because it's a secret, but because you're selling the outcome, not the method. The site either looks expensive or it doesn't.

Pricing for a one-pager: $500-800 in small markets, $1,000-2,500 in metro areas. Then the part that compounds: a $50/month care plan (hosting, edits, updates). Ten care-plan clients is $500/month of recurring income for a few hours of work.

```text
Claude Pro (month)              $20
Hosting + domain (year)         $45
Your cost, all-in               $65

One-pager, small market        $800
One-pager, metro             $2,000
Care plan, monthly           $50/mo

Margin on the first deal    ~90%+
```

Realistic ramp: 20 sends gets you 3-6 replies and 0-2 deals. Most yeses arrive after the follow-up, not the first message. Two clients a month at $1,500 is $3,000/month on part-time hours, and the demo library you accumulate makes every next month easier.

## What kills 90% of attempts

1. Polishing one demo for a week instead of sending it. The demo sells at 90% done. Send.
2. Pitching the technology instead of the outcome. Owners don't buy "AI website", they buy "customers stop bouncing off your broken mobile menu".
3. Picking niches you like instead of niches that pay. Your favorite vinyl shop has no budget. The med spa does.
4. No follow-up. One message three days later ("did the video land?") roughly doubles reply rate. Silence is not a no, it's an inbox.
5. Pricing at $200 to feel safe. It signals junk and attracts the worst clients. The work looks like $2,000. Charge like it.

## The actual point

The build is commoditized now. Anyone with $20 and this article can produce agency-grade output. What's not commoditized is the loop: a list, a demo, a message, a follow-up, run every week without drama.

Most people will bookmark this, install the skills, build one beautiful demo for an imaginary client and never message a real one. The ones making money send twenty ugly-personalized emails with a 40-second video attached.

Reply "loop" and I'll send you the follow-up message template for the deals the first message doesn't close.