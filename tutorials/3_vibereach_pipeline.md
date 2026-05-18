# Building Your First Pipeline in VibeReach — Turn Funnel Leads Into a System

*A continuation of the funnel tutorial. Your funnel is live, your form is collecting names, and your thank-you page is doing its job. Now we build the next thing that has to exist for any of that traffic to actually turn into money: a pipeline.*

---

## Why You Need a Pipeline (Before You Get Another Lead)

In the funnel tutorial we built a system that captures leads. That's half the job. The other half — the half that decides whether you get paid — is what happens to each lead *after* they hit submit. Without a pipeline, leads pile up in your contacts list as a flat, undifferentiated mass. You forget who's hot. You forget who you promised to call back yesterday. You discover three weeks later that a $5,000 deal went cold because nobody followed up on day two.

**Think of a pipeline as a Kanban board for your sales process.** If you've ever used Trello, Asana, Jira, ClickUp, or a literal whiteboard with sticky notes, you already understand pipelines. You have columns (stages). You have cards (opportunities). Cards move left to right as work progresses. At any glance, you can see who's where, what's stuck, and what's about to close.

In VibeReach, a **pipeline** is the whole board. A **stage** is one of the columns. An **opportunity** is a single card — one lead, one deal, one potential outcome — and it carries with it a contact record, an estimated dollar value, an assigned owner, notes, and a history of which stages it has passed through. That's a lot more than a sticky note.

The pipeline is what lets you stop thinking about leads as individuals and start thinking about them as a flow. Once you have a flow, you can measure it. Once you can measure it, you can fix the leaks. That is the entire game.

---

## Step 1 — Plan the Pipeline on Paper First (Do Not Skip This)

I'm going to ask you to do something that feels unnecessary: close the browser tab with VibeReach open, grab a piece of paper and a pen, and plan the pipeline by hand before you build anything.

There's a reason. The number-one mistake people make with pipelines is building them in software first. They open the pipelines screen, click Create New, start typing stage names that sound reasonable, and end up with a Frankenstein board that mixes activities ("Called Lead"), states ("Hot Lead"), and outcomes ("Closed") in the same column system. That pipeline can't be measured because the stages aren't comparable. Worse, the team using it argues constantly about when to move a card because the rules aren't clear.

Planning on paper takes ten minutes and forces you to think before you build. Here's the framework.

### Draw Three Boxes on Your Paper

Across the top of the page, draw three boxes labeled **START**, **MIDDLE**, and **END**. We're going to fill them in this order.

**START — What event creates an opportunity?** This is the trigger. For your CRM funnel from the last tutorial, the answer is probably: *a person submitted the opt-in form on the landing page.* That's your start event. Other businesses might use *a booking was made on the calendar,* or *a payment was received,* or *a contact was tagged as "Hot Lead."* Whatever it is, write it down. **An opportunity should be created automatically the moment this event happens.** If you have to remember to do it manually, you'll forget, and your data will be unreliable forever.

**END — What does WON look like? What does LOST look like?** These are your two terminal states. *Won* is the outcome you want — they paid, they signed, they showed up to the appointment, the deal closed. *Lost* is the outcome you don't want — they ghosted, they bought from a competitor, they said no, they unsubscribed. Define these specifically. "They paid the deposit" is specific. "They became a customer" is vague. The good news: **VibeReach automatically adds Won and Lost stages to every pipeline you create.** You don't have to build them. You just have to be clear about what qualifies an opportunity to land in each one.

**MIDDLE — What has to be true before they reach Won?** This is where the real thinking happens. Walk yourself through the journey. What state must the lead pass through? What needs to happen, in order, before they can possibly close? Write each state down as a noun, not a verb. Not "Call the lead." Instead: "Discovery Call Scheduled." Not "Send the proposal." Instead: "Proposal Sent." The difference matters because a stage describes *where the lead is*, not what *you're doing*. The lead is the one moving. You're the one tending to the board.

### Choose Three or Four Middle Stages (No More)

The temptation is to over-engineer. Don't. Three or four middle stages is the right number for almost any business getting started. Here is a clean, proven set for our CRM funnel scenario:

1. **New Lead** — opt-in just happened, no contact has been made yet.
2. **Call Booked** — the lead has scheduled or confirmed a discovery call on the calendar.
3. **Proposal Sent** — the discovery call happened and a written offer is now in their hands.

Then VibeReach adds **Won** and **Lost** at the end automatically. That's it. Five stages total. Five columns on your Kanban board. Anyone on your team can look at it and instantly understand where every deal is.

If you're tempted to add "Contacted," "Following Up," "Nurturing," or "Maybe Later" — resist. Those are activities or feelings, not states. A lead is either in *New Lead* (no call booked) or in *Call Booked* (call is on the calendar). The activity of *contacting* the lead happens between those two states; it isn't a state itself.

### Write Entry and Exit Criteria for Each Stage

For each middle stage, write two single sentences on your paper:

- **"A lead enters this stage when..."**
- **"A lead leaves this stage when..."**

For example, for *Call Booked*: enters when the calendar event is created; leaves when the call is completed (move to Proposal Sent) or the lead no-shows twice and stops responding (move to Lost). This little exercise forces you to make decisions about how the board operates *before* you and your team start arguing about it in real time. The clarity is worth ten times what it costs.

### Estimate Time-in-Stage

Last paper step: next to each stage, write how many days a lead should reasonably stay there before something is wrong. *New Lead → 1 day.* *Call Booked → 7 days.* *Proposal Sent → 14 days.* These numbers become the trigger for automated follow-ups later. When a lead sits in Proposal Sent for 15 days, that's the signal something has gone cold and you need to reach out, drop the price, or kill the deal.

Done? Your paper now has more strategic value than 90% of the pipelines I've audited in client accounts. Now we build it.

---

## Step 2 — Create the Sales Pipeline in VibeReach

Inside your sub-account, click **Opportunities** in the left navigation. You'll see the main opportunities dashboard. In the top right, click **Pipelines.** This brings you to a list of every pipeline that exists in this sub-account (probably none yet).

Click **Create New Pipeline.** A creation panel opens. Here's what to fill in:

**Pipeline Name.** Give it a clear, specific name. Not "Pipeline 1." Not "Sales." Instead, something descriptive like *"CRM Setup — Service Business Funnel — 2026."* Why so specific? Because the moment you create your second or third pipeline (and you will — different funnels, different services, different client accounts, all need their own boards), generic names become useless. Pipeline names must be unique within a sub-account, so this also avoids collisions later.

**Visibility Toggles.** You'll see options to show or hide the pipeline in the dashboard funnel chart and pie chart. Keep these on for now — they're how the pipeline appears in your reporting widgets. You can also toggle visibility per-stage, which becomes useful once your pipeline matures (you might hide *Lost* from the chart so it doesn't visually dominate the report).

That's it for creation. Click **Save**, and the pipeline exists. Now we add the stages.

---

## Step 3 — Add Stages to the Pipeline

Open the pipeline you just created. You'll see a stage editor. Click **Add Stage** to create your first stage, then repeat for each of the middle stages from your paper plan.

Add these in this exact order:

1. **New Lead**
2. **Call Booked**
3. **Proposal Sent**

You don't add Won or Lost — VibeReach adds them automatically as the terminal stages. They're already there.

A few details worth knowing as you go:

**Stage order matters.** Stages flow left to right on the Kanban board, mirroring your sales process. Use the drag handles (or the up/down arrows, depending on your VibeReach UI version) to reorder if you put one in the wrong place. The order on screen is the order leads will move through.

**Stage names matter.** Use the names from your paper plan exactly. Don't soften them, don't make them cute. *Proposal Sent* is better than *Negotiating* because it describes a binary state — either you sent it or you didn't. *Negotiating* is fuzzy. Fuzzy stages get gamed by salespeople who don't want to admit a deal is stuck.

**You can hide individual stages from dashboard charts** by clicking the visibility icon next to each stage. The early stages of an experiment, or the *Lost* column, can clutter your reporting — hide them if they distract.

**Stages can be deleted later without losing data.** When you delete a stage, VibeReach asks which other stage to move the existing opportunities into. Nothing gets orphaned. This means you can refine the pipeline structure as you learn, without fear of breaking your historical records.

Click **Save**. Your pipeline now exists as a real Kanban board with five total stages. Navigate back to **Opportunities** and select your new pipeline from the dropdown to see the empty board.

---

## Step 4 — Connect the Funnel to the Pipeline (The Critical Wire)

Here is where this tutorial becomes the extension of the funnel tutorial. Right now, your funnel is collecting leads but those leads are going *nowhere*. They're sitting in your contacts list as anonymous rows. We need to wire the funnel form submission to automatically create an opportunity in the *New Lead* stage of your new pipeline. Once we do that, every future opt-in lands on the board the moment it happens. No manual entry. No forgetting.

This wire is built with a VibeReach **Workflow.** A workflow is a trigger (the event that starts it) plus one or more actions (what should happen). Here's the build:

1. From the left navigation, go to **Automation → Workflows.**
2. Click **+ Create Workflow** and choose **Start from Scratch** (or pick a relevant template if you see one that fits — the lead-capture templates are good starting points).
3. Click **+ Add New Trigger** and choose **Form Submitted.** A configuration panel appears.
4. From the **Form** dropdown, select the specific form you placed on your funnel's landing page (the one from the funnel tutorial). Click **Save Trigger.** This tells the workflow: *"Run me every time this specific form is submitted, and nothing else."*
5. Click the **+** button below the trigger to add an action. Choose **Opportunity → Create/Update Opportunity.**
6. Fill in the action configuration:
   - **Pipeline:** select the pipeline you just built.
   - **Stage:** select **New Lead.** Every new opt-in will land here.
   - **Status:** set to **Open.** This means "still in play."
   - **Value:** if you have a sense of the average deal value (say $1,500 for a CRM setup engagement), enter it. This populates revenue forecasting in your reports. If you don't know yet, leave it blank — you can always fill it in later when the lead becomes real.
   - **Allow Opportunity to Move:** toggle this on if you want the same contact to be able to re-enter and have the record updated rather than duplicated. For most funnels, toggle this on.
7. Click **Save Action.**
8. In the top right of the workflow editor, toggle the workflow from **Draft → Publish.**

That's it. Every form submission from this point forward automatically creates a new opportunity in the *New Lead* stage of your pipeline. The leads now appear on the board the instant they opt in.

A useful detail: the **Create/Update Opportunity** action stays the same regardless of which trigger fires it. The trigger is what changes based on how leads enter your world. If you also want to create opportunities when someone books a call on your calendar, add a second workflow with the trigger **Customer Booked Appointment** and the same action — except point it to the *Call Booked* stage instead of *New Lead*. Now the booking event automatically moves the lead one column to the right without any human touching the board. This is how a pipeline becomes self-driving.

---

## Step 5 — Practice Moving Opportunities

Now we drive the board manually for a minute so you understand the mechanics. Even if most movement will eventually be automated, you need to know how to operate the cards by hand because there will always be edge cases.

### Create a Test Opportunity Manually

Before you have real leads pouring in, seed the board with one or two test cards so you can practice.

1. Go to **Opportunities** and make sure your new pipeline is selected from the dropdown.
2. Click **+ Add Opportunity** in the top right.
3. **Primary Contact:** select an existing test contact from your list, or click to create a new one (you can put your own name and an alternate email).
4. **Opportunity Name:** something descriptive like *"Test — Dr. Lee — CRM Setup."*
5. **Pipeline:** confirm it's your new pipeline.
6. **Stage:** set to **New Lead.**
7. **Status:** Open.
8. **Value:** enter a dollar amount — say $1,500.
9. **Owner:** assign to yourself.
10. Click **Create.**

The opportunity card now appears on your board, sitting in the *New Lead* column. Create a second test opportunity the same way so you have two to play with.

### Move Opportunities Across Stages (The Kanban Move)

This is the moment the Kanban analogy becomes literal. Click and hold any opportunity card, then drag it sideways to a different column. Drop it. Done. The opportunity is now in the new stage, the move is logged in the opportunity's history, and any automations you've wired to stage changes fire automatically.

Try it now:

1. Drag your first test opportunity from **New Lead** to **Call Booked.** Notice the column lights up as you hover over it.
2. Drag the second one all the way to **Proposal Sent.** Then drag it to **Won.**
3. When you drop into Won or Lost, VibeReach may prompt you to confirm. Confirm.

That's the entire mechanic. The whole pipeline operates this way — drag cards to the right as deals progress, drag them to *Lost* when they die, drag them to *Won* when they close. Every move is timestamped, every move is searchable, every move is reportable.

### Click Into an Opportunity Card

Click on any card to open its detail drawer. This is where the opportunity lives in full — the linked contact, the value, the owner, the followers, the notes, the tasks, the conversation history with that contact (every email, every SMS, every call), and the full stage-change history. **The detail drawer is the single most useful screen in VibeReach for anyone doing sales work.** Spend a minute clicking around it. Add a note to your test opportunity. Add a task ("Follow up on Tuesday"). Change the value. Get comfortable.

### Things to Practice Once

Run through these motions at least once, so they're not strangers the day you have a real hot lead and your hands are shaking:

- Drag a card forward.
- Drag a card backward (yes, you can — sometimes a "Proposal Sent" deal goes back to "Call Booked" because they want a second discovery call).
- Mark a card as **Won.** Notice the celebration animation, then notice the entry in your reports.
- Mark a card as **Lost.** When you do, VibeReach will ask for a reason — *Price, Competitor, Timing, No Response, Not a Fit.* **Always fill this in.** The reasons you lose are the most valuable data in your whole business. After 50 lost deals, the patterns are unmistakable.
- Reassign an opportunity to a different owner (useful when you have a team).
- Add a follower (someone who should be notified but isn't the owner).
- Add a note documenting why you moved the card. Future-you will thank present-you for this habit.

---

## Step 6 — Wire Up Automation on Stage Changes (Optional but High-Leverage)

Once you've used the board manually for a few days and you understand its rhythm, the next leap is to automate what happens *when an opportunity moves*. This is where pipelines stop being a tracking tool and become a follow-up engine.

A few high-leverage examples:

**When an opportunity moves to *Call Booked*** → trigger a workflow that sends an SMS confirmation with the meeting link, an email with a pre-call questionnaire, and a calendar reminder 24 hours before the call. *Result: fewer no-shows.*

**When an opportunity sits in *Proposal Sent* for more than 7 days** → trigger a follow-up email written like a polite nudge, then a second email 7 days later with a different angle, then assign a task to the owner to make a personal call on day 21. *Result: deals don't die in silence.*

**When an opportunity moves to *Won*** → trigger an onboarding email sequence, send an internal Slack notification to the operations team, create a task to send a thank-you note, and add the contact to a "Customer" tag. *Result: a smooth handoff from sales to delivery, every time.*

**When an opportunity moves to *Lost*** → trigger a re-engagement workflow that drops the contact into a long-term nurture sequence (one email per month for twelve months) so that when their situation changes, you're still in their inbox. *Result: 5-10% of "lost" deals revive themselves in year two.*

The trigger for each of these is a workflow with a **Pipeline Stage Changed** or **Opportunity Status Changed** trigger, filtered to the specific pipeline and stage you care about. The action is whatever you want to happen. You don't need to build all of these on day one — but bookmark this list. As your pipeline matures, each automation you add multiplies the value of every lead that enters the system.

---

## Step 7 — Read the Board Daily for the First Two Weeks

Here is the practice that separates people who build pipelines from people who *use* pipelines: spend ten minutes every morning, coffee in hand, looking at the board.

What you're looking for:

- **What's stuck?** Any card that's been sitting in a stage longer than your paper-plan time-in-stage estimate is a deal that's going cold. Reach out today, not tomorrow.
- **What's hot?** Cards that have moved forward recently are the deals that need your best attention. Don't waste your sharpest hour of the day on a *New Lead* when there's a *Proposal Sent* card from yesterday waiting for a response.
- **What's the bottleneck?** Is the *New Lead → Call Booked* conversion slow? Your form copy or your follow-up timing is the issue. Is *Call Booked → Proposal Sent* slow? Your discovery call needs work. Is *Proposal Sent → Won* slow? Your proposal or your pricing is off. The board tells you exactly which step of your sales process to fix next.

After two weeks of doing this every morning, you will know things about your business that you didn't know existed. That is the entire purpose of building this system.

---

## Closing Thought — Funnels Bring Them, Pipelines Convert Them

The funnel tutorial built the front door. This tutorial built the room they enter once they're inside. One without the other is half a business. A great funnel without a pipeline produces a chaotic pile of leads you can't keep up with; a great pipeline without a funnel is an empty board waiting for someone to fill it.

Together, they form the most important loop in any service business: traffic enters the funnel, becomes a contact, becomes an opportunity, moves through stages, becomes a customer, becomes a referral, becomes more traffic. The whole loop runs on one platform, with one source of truth, with every step measurable and every gap fixable.

You now have both halves built. Go put a real lead through it end-to-end. Submit your own form. Watch the opportunity appear. Move the card. Mark it Won. Then do the same thing with your first paying customer, and again, and again, until the rhythm is automatic and the board fills itself.

That's the system. The hard part is now behind you.

---

*Sources: HighLevel Support Portal — "Getting Started: Setup Pipelines and Opportunities," "Step-by-Step Guide: Creating Pipelines," "Understanding Pipelines," and "Step-by-Step Guide to Creating Opportunities." Verified May 2026.*
