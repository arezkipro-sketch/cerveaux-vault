---
title: "Stop Being the Loop. Here's How to Make Claude Work While You Sleep."
source: "https://x.com/raytar/article/2069212188619805179"
author:
  - "[[Raytar (@Raytar)]]"
published: 2026-06-23
created: 2026-07-17
description: "The person who built Claude Code at Anthropic stopped prompting Claude.Boris Cherny@bcherny·11 juinÀ l'origine en anglais et traduitAfficher..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HLdRbboXgAAwWuw?format=jpg&name=large)

The person who built Claude Code at Anthropic stopped prompting Claude.

> 11 juin
> 
> Salut depuis Code with Claude Tokyo !!

His name is Boris Cherny. In June 2026 he said it out loud: "I don't prompt Claude anymore."

Loops prompt Claude for him. His actual job now is writing loops.

That sounds like a flex. But no. It's the biggest shift in how people use Claude and ChatGPT right now. You've probably heard the phrase. Almost nobody does it yet.

Here is how you work right now.

- You type a prompt.
- Claude edits a file.
- You run the test.
- It breaks.
- You paste the error back.
- It tries again.

Twenty minutes later you realize you've been babysitting the exact thing you wanted to hand off.

**You are the loop.** You're the one checking the work and deciding the next step, every single time. That is the job a loop takes over.

## One example shows the whole difference

Ask Claude to write you a one page brief on any topic. Simple task. It writes something clean and confident, with sources at the bottom.

![Image](https://pbs.twimg.com/media/HLcRAF0aQAAuwrJ?format=jpg&name=large)

Now read the sources. **Some of them are fake(!!!)**. Claude made them up and has no idea it did. They look real. The links go nowhere, or they go somewhere that doesn't say what Claude claimed. This is the quiet way Claude burns you, and **a single prompt can never catch it**, because Claude stays confident it's right until something opens the link.

Now run it as a loop instead. Same brief, but you add a bar it can measure:

> every claim needs at least three sources, and every link has to open to a real page that backs up the claim.

Watch what happens. Claude writes the brief, then goes link by link. It opens each one. It throws out the dead ones and the fake ones. It finds real replacements. It keeps checking until every single source on the page is something you can open. Then it stops.

It never gets bored. It never skips the boring ones.

Here's how you'd write that in Claude Code. Don't worry about the command yet, I break it down below:

```plaintext
/goal write a one page brief on [your topic]
where every claim has at least three sources and
every link opens to a real page that supports the claim. 

Open each link to confirm it before you call it done.

Replace any source that is dead or does not back up the claim.

Stop only when every source on the page checks out.
```

# What a loop is

![Image](https://pbs.twimg.com/media/HLdPrvlWUAAVWIN?format=jpg&name=large)

A loop is a small system that prompts Claude for you, over and over, until a job is done.

Every loop, no matter how fancy, is the same five beats:

1. **Find the work.** Open tasks, failing tests, unread emails, files in a folder.
2. **Do it.** Claude handles one item at a time, like you would by hand.
3. **Check itself.** A second pass confirms the work is done and correct, not just produced.
4. **Remember.** It writes down what's finished, so it never repeats work or loses its place.
5. **Go again.** It repeats until nothing's left, then stops or pings you.

One line to keep: prompting is doing the work. **Loop engineering is managing the worker.**

## "Isn't this just a scheduled task?"

![Image](https://pbs.twimg.com/media/HLdOGUyXoAAZSoY?format=jpg&name=large)

Good question. No.

You can already make your computer run the same thing every morning at 8am. That's a cron job. It's older than most of us. It runs a fixed script. Same steps, every time, no thinking.

A loop is different because of one thing: there's **a decision-maker inside it**.

A cron job runs a script. A loop runs Claude. Claude looks at the current situation, picks the next action, does it, checks the result, and then decides what to do next. Keep going. Try again. Undo. Stop.

That decision in the middle is the entire point. A script can't look at a broken test and figure out a different fix. Claude can. This only became possible once Claude and ChatGPT got good enough to make real judgment calls mid-job.

## The two commands that run a loop

![Image](https://pbs.twimg.com/media/HLdO2TKXQAA6Omo?format=jpg&name=large)

Here's where most people go wrong. You don't build a loop by typing "do this in a loop" into a normal chat. Claude Code has two commands built in, and which one you reach for depends on the kind of loop you need.

**1\. /goal is the loop that works until it's done.**

> 11 juin
> 
> /buuuuut

But obviously not that kind of goal. xD

You saw /goal up in the brief example. You type it, then describe what "done" looks like. Claude keeps working, turn after turn, on its own. After every turn, a second copy of Claude quietly checks: are we at the goal yet? If not, it tells the first one why, and the work continues. The moment the goal is met, the loop stops by itself.

That self-check after every turn is the whole difference between a real loop and a prompt that runs once and hopes.

Use /goal when there's a finish line. Work until this is true.

**2\. /loop is the loop that repeats on a rhythm.**

Reach for this when the job isn't "finish a pile" but "keep an eye on something." You tell it how often and what to do, and Claude re-runs it for you.

```text
/loop 30m check whether my live site is back up by loading the homepage.

The moment it returns a normal page, tell me and stop checking.
```

The 30m means every 30 minutes. You can also just say "every morning, triage my inbox" and Claude will schedule it.

Use /loop when there's no finish line, just a beat. Check this again and again.

Most of the strong loops you'll build start with /goal. These are recent Claude Code features, so if you don't see the commands, update Claude Code and they'll show up.

## Your first loop, ready to paste

A one line goal is plenty for a small job. For a bigger job with lots of steps, you hand Claude a full charter: where to find the work, how to check itself, how to remember, when to stop.

Fill in the brackets and paste this into Claude Code:

You are running as a loop, not answering one prompt. Here is your charter.

```text
GOAL
[Describe the finished state in one or two sentences. 
Be specific about what DONE looks like, and make it something you can measure. 

Example: "Every product page in /pages has the new pricing and every link opens."]

WHERE THE WORK IS
[Tell Claude where to look.

Examples: "Scan the /pages folder for files with old pricing." Or "Read TODO.md and treat each unchecked box as a task.

" Or " Check my connected task board for items tagged ai."]

HOW TO WORK
- Do one item at a time. Finish it fully before starting the next.

- Match the patterns you find in existing files. Do not invent new ones.

- If an item needs a decision only I can make (spending money, deleting things, emailing a person), stop on that item, add it to a "needs me" list, and move to the next one.

HOW TO CHECK YOURSELF
After each item, prove it is done before you mark it done.

[Pick what fits: "run the tests" / "re-read the file and confirm it meets the goal" / "open the link and confirm it loads." Checking means evidence, not confidence.]

If the check fails, fix it and check again. Three tries per item, then log it as blocked and move on.

HOW TO REMEMBER
Keep a file called LOOP-STATE.md. 
After each item, write the item name, its status (done / blocked / needs me), what you changed, and anything the next run should know.

Read this file FIRST every run so you never redo finished work.

WHEN TO STOP
Stop when every item is done or logged as blocked, or when you have finished [N] items this run.

Then give me a short report: what got done, what is blocked, what needs my call.

Start by reading LOOP-STATE.md if it exists, then find the work.
```

The state file is the quiet hero. Without it, every run starts from zero. With it, the loop picks up exactly where it left off, even when it runs on a schedule.

## When not to build a loop

> Loops are not free and not for everything. Three honest things before you start.

1. **One-off tasks don't need a loop.** If the job is a single answer, a plain prompt is faster. Loops earn their setup cost on work that repeats or has many pieces.
2. **Loops cost more.** A loop that checks itself and retries is running Claude several times per item. On a Claude plan, you'll hit your usage limit faster.
3. **Vague work doesn't belong in a loop.** "Think of a better product strategy" is not a loop. Go figure out the actual goal first.

## Start this week

Pick one task you keep doing by hand, the kind with lots of small pieces. Paste the charter. Fill in the brackets. Run it once while you watch every step.

When you trust it, put it on a schedule. The first time you wake up to work that finished overnight, you'll stop typing prompts one at a time. Just like Boris.

![Image](https://pbs.twimg.com/media/HLcj4zWawAECxGg?format=jpg&name=large)

Helped? Follow me. I share this stuff so you don't have to dig for it