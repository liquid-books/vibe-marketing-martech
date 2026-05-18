# Building Your First Workflow in VibeReach — Automate the Follow-Up

*Part four of the funnel → forms → pipeline → workflow series. Your funnel captures attention. Your forms collect clean, mapped data. Your pipeline organizes the leads. Now we build the automation that contacts each new lead the moment they opt in, tags them, drops them onto your pipeline, and follows up the next day — without you touching the keyboard. Includes an optional advanced section on If/Else conditional logic.*

---

## What This Tutorial Assumes

This is the fourth piece of the curriculum, and it depends on the first three:

- **Funnel Part 1** built the pages, attached a domain, and locked in the SEO.
- **Funnel Part 2** built the form and survey, created the custom fields, and mapped everything back to the contact record.
- **Pipeline** built the Kanban board with stages for New Lead, Call Booked, Proposal Sent, plus the automatic Won and Lost columns.

If any of those pieces aren't in place, the workflow we're about to build will have nothing to fire from, no data to merge into emails, and nowhere to drop the resulting opportunities. The single most common reason new VibeReach users find their workflows "not working" is that the form isn't actually wired to the right fields — which is exactly why Part 2 exists. If you haven't completed it, do that first.

Assuming all four pieces are in place, here's what we're about to build:

```
[Form Submitted]  ←  trigger from Funnel Part 2
    ↓
[Tag the contact: "crm-funnel-lead"]
    ↓
[Create opportunity in pipeline → New Lead stage]  ←  ties to Pipeline tutorial
    ↓
[Send Email 1: Welcome + what to expect]
    ↓
[Wait 1 day]
    ↓
[Send Email 2: Helpful follow-up + soft CTA]

(Optional advanced) — Insert an If/Else after the Wait that checks
whether the lead has booked a call, and routes accordingly.
```

Six nodes in a straight line. Then an optional branch. Let's go.

---

## Why Workflows Are the Whole Game

Before we click anything, a minute on what we're actually doing and why it matters more than it looks.

Every business has a list of tasks that *should* happen every time a new lead arrives. *Tag them so they show up in the right segment. Add them to the pipeline so the sales team sees them. Send a confirmation email so they know we got their submission. Send a follow-up tomorrow because most people who opt in today won't act today.* If you're running a small operation, you do those tasks yourself. If you're growing, you hand them to a virtual assistant. Either way, those tasks consume human attention, and human attention is the most expensive thing you own.

A workflow does those tasks for you. Not as a metaphor — *literally.* Every email that goes out at the right time, every lead that lands on the board before you've finished your coffee, every tag that gets applied without anyone remembering to apply it — those are tasks that used to require a person. Now they don't.

The catch is that a workflow is only as smart as the data feeding it. Bad form fields produce broken merge fields produce embarrassing emails. Bad tag naming produces reports nobody can read. Bad branching logic silently routes the wrong leads to the wrong place for months before anyone notices. The previous three tutorials existed to give this one a clean foundation to stand on. Now we use that foundation.

---

## Step 1 — Plan the Workflow on Paper

Same discipline from the pipeline tutorial. Before you click anything, sketch the flow on paper. Two minutes here saves an hour of rework.

The shape we're building is the diagram above. Six nodes, top to bottom. No branches yet, no decisions. Get the linear version working first. The advanced If/Else section comes only after the simple workflow is tested and trusted.

While you're sketching, write down two things next to each email step:

- **What's the one outcome this email should produce?** (Open? Click the calendar link? Reply? Forward?)
- **What's the one sentence at the top that earns continued reading?**

The same way the funnel landing page lives or dies on its headline, every email in a workflow lives or dies on its subject line and first sentence. Plan those *before* you open the email editor, because once you're inside the editor it's tempting to start writing and forget that you're writing toward a specific outcome.

---

## Step 2 — Create the Workflow and Add the Trigger

Go to **Automation → Workflows** in the left navigation. Click **+ Create Workflow.** VibeReach will offer pre-built templates ("New Lead Follow-Up," "Missed Call Text-Back," and similar) or a blank canvas. For learning, choose **Start from Scratch.**

Name the workflow at the top — *"CRM Funnel — Lead Capture + 2-Email Follow-Up — 2026."* The name will show up in lists, in reports, and in the workflow-history view. Generic names like "Workflow 1" become a problem fast.

Now add the trigger:

1. Click **+ Add New Trigger.**
2. From the trigger list, choose **Form Submitted.**
3. In the **Form Is** dropdown, select the specific form you built in Funnel Part 2 (the one named *"CRM Funnel — Main Opt-In — 2026"*).
4. Leave the **Form Type** filter set to *Normal* — this excludes chat-widget submissions and survey submissions, which deserve their own workflows.
5. Click **Save Trigger.**

The trigger now says, precisely: *"Run this workflow every time someone submits the CRM Funnel main opt-in form, and not for any other reason."* Tight scope, predictable behavior. This is the part most people get wrong by leaving the form filter blank — which means every form on the entire account fires this workflow, including forms you haven't built yet.

---

## Step 3 — Action One: Tag the Lead

Tags are the cheapest, most useful labels you can apply to a contact. They cost nothing, they're searchable, they segment your audience, and they trigger or filter other workflows. Tagging the lead as it enters is the first thing the workflow should do, because every downstream tool — smart lists, reports, other workflows — can then ask, *"Show me everyone who came through the CRM funnel."*

1. Click the **+** button below the trigger to add an action.
2. From the action picker, search for and select **Add Contact Tag.**
3. Configure:
   - **Action Name:** *"Tag — CRM Funnel Lead."* Action names are visible on the canvas. Name them well.
   - **Tags:** type `crm-funnel-lead`. If the tag doesn't exist yet, VibeReach creates it automatically. (One convention that saves you grief: lowercase, hyphens not spaces, no parentheses or special characters. `crm-funnel-lead` is better than `CRM Funnel Lead (Q2)`.)
4. Click **Save Action.**

Why tag *before* doing anything else? Because if any later action in the workflow fails — a bad email send, a broken merge field, an SMS to a number that doesn't accept texts — you still have the tag applied. You can find the lead later, see they came through the CRM funnel, and recover the situation manually. Tag early. Tag is cheap. Tag is permanent.

---

## Step 4 — Action Two: Tie Back to the Pipeline (Create the Opportunity)

This is the moment the workflow stops being a notification system and becomes a sales tool. We're going to create an opportunity card on the pipeline board the instant the lead opts in, with a meaningful name, a dollar value, and an owner.

In the Pipeline tutorial, we built a small standalone workflow that did this single action — fire on form submission, create the opportunity, done. Now we're folding that single action into this larger workflow so everything lives in one place. If you built the standalone workflow earlier, you can either disable it or delete it after this one is published. We don't want two workflows creating the same opportunity twice.

1. Click the **+** below the tag action.
2. From the action picker, find **Opportunity → Create/Update Opportunity.**
3. Configure:
   - **Action Name:** *"Create Opportunity — New Lead Stage."*
   - **Pipeline:** select the CRM pipeline you built in the Pipeline tutorial.
   - **Stage:** **New Lead.**
   - **Status:** **Open.**
   - **Opportunity Name:** type `{{contact.first_name}} {{contact.last_name}} — CRM Setup`. The merge fields resolve at runtime, so each card on your Kanban board shows up labeled with the actual lead's name and the deal type. *This only works because Funnel Part 2 mapped First Name and Last Name to standard fields on the form.* If you had stored the visitor's name as a single combined "Name" field, this would still work but produce uglier output.
   - **Value:** enter your estimated deal value (say $1,500). This populates revenue forecasting in pipeline reports.
   - **Owner:** assign to yourself, or to whichever team member handles sales for this funnel.
   - **Allow Opportunity to Move:** toggle ON. If the same person submits the form again later (which happens more than you'd think), the existing card updates instead of a duplicate being created.
4. Click **Save Action.**

Open the pipeline board in another browser tab while you're testing later. You'll see new cards appear in the New Lead column in real time as test submissions come through. It's genuinely satisfying. More importantly: any teammate looking at the board now sees every fresh lead the moment it arrives, with a meaningful name and a dollar value, without anyone having to type a single character.

---

## Step 5 — Action Three: Send the First Email (The Welcome)

Now the moment of maximum attention. They just submitted the form. They're sitting there expecting something from you. The first email should land within sixty seconds.

1. Click **+** and choose **Send Email.**
2. Configure:
   - **Action Name:** *"Email 1 — Welcome + What to Expect."*
   - **From Name:** a real person's name. *Dr. Ernesto Lee.* Not a company name. Email open rates are dramatically higher when the sender field looks human. Brand names trigger people's "this is marketing" filter.
   - **From Email:** your dedicated sending email on a verified sending subdomain (configured separately in Settings → Email Services). Don't send from a Gmail address — your deliverability will collapse within a week.
   - **Subject:** *"Welcome, {{contact.first_name}} — here's your next step."* Short, personal, and action-flavored. The `{{contact.first_name}}` merge field makes the subject feel written for them. *This only works because the form actually captured First Name as a separate field.*
   - **Email Body:**

```
Hi {{contact.first_name}},

Thanks for opting in. I wanted to write to you personally to confirm
I got your details and tell you exactly what happens next.

In the next 24 hours, you'll get a second email from me with one
specific thing you can do today to start fixing your CRM follow-up
problem. No pitch, no upsell — just one practical step.

If you'd rather skip ahead and book a 20-minute setup call right now,
here's my calendar: [your booking link]

Talk soon,
Ernesto

P.S. — If this email landed in your Promotions tab or spam folder,
please drag it to your main inbox so you don't miss tomorrow's note.
```

3. Click **Send Test Mail** with your own email in the test field. Confirm the formatting looks right, the merge field resolved to your actual first name (not the literal string `{{contact.first_name}}`), and the calendar link works.
4. Click **Save Action.**

A note on what just happened with the merge fields: every `{{contact.first_name}}` you see in the email is a placeholder that VibeReach replaces at send time with the actual value from the recipient's contact record. The contact record only has that value because the form *collected* First Name as a separate standard field in Funnel Part 2. This is why we kept emphasizing the data layer underneath. If you had merged the visitor's name into a single combined field, you'd be writing "Hi Ernesto Lee, Dr." in every email and wondering why nobody trusts you.

---

## Step 6 — Action Four: The Wait Step

This is the action that turns a one-shot autoresponder into a real sequence. The Wait pauses the workflow at this point in the flow for a specified time. Everything after the Wait runs only after that time has passed.

1. Click **+** and choose **Wait.**
2. Configure:
   - **Action Name:** *"Wait 1 Day."*
   - **Wait Type:** **Time Delay.**
   - **Duration:** *1 day.*
3. *Optional but recommended:* expand the **Advance Window** settings. Set **Resume On** to weekdays only (Mon–Fri) and **Resume Between Hours** to your local business hours (say 9:00 AM to 5:00 PM). This prevents your follow-up email from arriving at 3:00 AM on a Sunday because someone opted in at 3:00 AM on a Saturday. Email arrival time has a measurable effect on open rates — emails that land during business hours get opened more.
4. Click **Save Action.**

The wait step is the single feature that turns VibeReach from a single-message responder into a follow-up engine that runs for days, weeks, or months. Without it, every action below it would fire instantly. With it, you can build sequences that span any timeframe — each step timed precisely for human attention spans.

Other Wait types worth knowing about (for later, not now):

- **Event/Appointment Time** — pause until a specific number of minutes/hours/days before or after a scheduled appointment. Useful for booking reminders.
- **Condition** — pause until a specific condition becomes true (or for a max time, whichever comes first). Useful for "wait until they reply, but no longer than 3 days."
- **Contact Reply** — pause until the contact replies to an email or SMS. The most powerful Wait type for two-way conversations.

For our simple sequence, Time Delay is what we need.

---

## Step 7 — Action Five: Send the Second Email (The Follow-Up)

One day after the lead opts in (during business hours, if you configured the Advance Window), this email goes out automatically.

1. Click **+** and choose **Send Email.**
2. Configure:
   - **Action Name:** *"Email 2 — Day 1 Follow-Up."*
   - **From Name** and **From Email:** same as Email 1. Consistency matters — a different sender confuses people.
   - **Subject:** something curiosity-driven. *"{{contact.first_name}}, the one thing most people skip"* or *"Quick follow-up on your CRM setup"*. Avoid the dead-on-arrival "Just checking in" — it signals you have nothing valuable to say.
   - **Email Body:** deliver the specific practical step you promised in Email 1. Don't pitch yet. Give value. End with the same soft CTA — the calendar link, no pressure. The structure that works:

```
Hi {{contact.first_name}},

Yesterday I promised you one specific thing you could do today to
start fixing your CRM follow-up problem. Here it is:

[One concrete, useful tip — three to four sentences.]

That's it. If you try it and it helps, terrific. If you want to skip
ahead to "let me just show you how I'd set this up for you," here's
my calendar: [booking link]

— Ernesto
```

3. Send a test email. Confirm the merge field resolves.
4. Click **Save Action.**

That's the simple workflow. Trigger → Tag → Opportunity → Email 1 → Wait → Email 2. Six nodes top to bottom.

---

## Step 8 — Publish, Test, and Watch It Run

In the top right of the workflow editor, toggle from **Draft → Publish.** The workflow is now live.

**Test it end-to-end before you trust it.** Open your funnel in an incognito browser window, fill out the form with a test email you own (a Gmail trick that helps here: `ernesto+test@yourdomain.com` delivers to `ernesto@yourdomain.com` but creates a unique-looking address that's easy to spot in your inbox).

Watch what happens, in order:

1. Within a few seconds, a new contact should appear in your Contacts list with all the field values from Funnel Part 2 properly populated.
2. The contact should have the `crm-funnel-lead` tag.
3. A new opportunity card should appear on the New Lead column of your pipeline, named after the test contact with the deal name suffix.
4. The welcome email should arrive in your inbox within a minute or two, with your first name properly merged into both the subject and the body.
5. Tomorrow at the resume time you specified, the second email should arrive.

To watch the workflow execute in real time, go back to **Automation → Workflows**, click into the workflow, and click the **History** tab. You'll see every execution, every action that ran, every action still pending, and any errors. The history view is your debugging tool. If something didn't fire, the history tab is where it'll tell you why.

If everything works on the test contact, run a second test from a different email — maybe even on a different device — to make sure it works for someone whose contact record didn't already exist.

---

## Step 9 (Optional) — Advanced: Adding If/Else Conditional Logic

You wanted advanced. Here it is. If/Else is where workflows graduate from "do these things in order" to "do different things depending on what's true about this contact." Powerful. Worth doing. Also genuinely tricky — and worth being honest about why.

### The Problem We're Solving

Imagine your one-day follow-up email arrives, but the recipient already booked a call with you four hours after opting in. Your follow-up email lands in their inbox saying *"yesterday I promised you one specific thing..."* — and they're sitting there looking at a calendar invite they already accepted, thinking *"this guy isn't paying attention."*

You just lost trust for no reason. The fix is to *not send the follow-up email if they already booked the call.* That's an If/Else decision.

This is the most useful If/Else pattern for a beginner workflow, because it solves a real problem and the logic is simple: did the contact take the action we wanted? If yes, congratulate. If no, nudge.

### Where to Place the If/Else

Open your workflow. We're going to insert the If/Else **after the Wait step but before Email 2.** At that point, 24 hours have passed and we want to check: *did they book a call yet?*

1. Click the **+** between the Wait action and Email 2.
2. From the action picker, search for and select **If/Else Condition.**
3. The If/Else configuration panel opens. You'll see at least one branch (called Branch #1 by default) and a **None** branch that catches everything not matching.

### Building the Condition

We want Branch #1 to fire when **the contact has booked an appointment.** Configure it:

1. In Branch #1, click **Add Condition** (or the equivalent button in your UI version).
2. **Field type:** Appointment (or "Has Appointment," depending on the picker).
3. **Condition:** *Appointment Status is Confirmed* (or *Appointment Exists*, depending on what your account version exposes).
4. Some accounts will require you to specify *Calendar* — choose the specific calendar you use for discovery calls so the rule doesn't accidentally fire on appointments from other calendars.
5. Click **Save Condition.**

Rename the branch for clarity. Click the branch label and rename it to **"Booked a Call."** Visual workflows get harder to read fast as they grow — naming branches is a small habit that pays off when you come back to this in three months.

### Filling the Branches

Each branch is now an independent path. Whatever actions you put in each branch happen only to contacts who follow that path. **Branches do not automatically reconverge** — once a contact enters a branch, they stay in that branch's actions for the rest of the workflow.

**In the "Booked a Call" branch:** add a Send Email action with a different message. *"{{contact.first_name}}, looking forward to our call tomorrow."* Maybe also add an SMS reminder with the meeting link. This is the path for engaged leads — give them what they need for the call, don't try to convince them again.

**In the "None" branch (the default):** drop in the original Email 2 that was already there. This is the path for leads who haven't booked yet — they need the soft follow-up nudge. To move the existing email, you can either drag it into the None branch or copy its configuration into a new Send Email action and delete the original.

### Why If/Else Is Tricky (You Remembered Right)

Three things trip people up. Knowing them in advance saves you a lot of staring at a broken workflow:

**Conditions are evaluated at the moment the contact reaches the If/Else node, not before, not after.** If the contact books a call ten seconds *after* the If/Else evaluates their state, they're already locked into the "None" branch and will get the cold-lead email. This is why you place the If/Else *after* the Wait — to give the condition enough time to become true. Putting If/Else conditions immediately after the trigger almost never works, because nothing has had time to happen yet.

**Branches don't reconverge.** If you want both branches to end with the same final action (say, applying a "Day 1 Sequence Complete" tag), you have to add that final action *separately to the end of each branch.* It's easy to forget. The result is an asymmetric workflow where some contacts get tagged and others don't, and you don't notice for weeks.

**The None branch catches everything you didn't write a condition for, *including* unexpected states.** If your condition is "Has Appointment = TRUE," the None branch fires for contacts with no appointment, contacts with a *cancelled* appointment, contacts whose appointment data didn't sync correctly, and contacts whose state the system genuinely can't determine. Make the None branch your safe default — whatever action would be reasonable for a lead in an ambiguous state. Usually that's "send the standard follow-up email," because the worst case is they're slightly over-contacted. Don't put your scariest, most aggressive action in the None branch — it'll fire on contacts you didn't expect.

### The General Pattern for If/Else

You can chain multiple If/Else nodes for complex logic, but I'd resist that on your first workflow. The pattern that works for almost every business case:

```
[Wait]
   ↓
[If/Else: Did they take the desired action?]
   ├── YES branch → reinforce / accelerate / thank
   └── NO branch  → nudge / re-engage / follow up softly
```

That single pattern, applied at each step of a long sequence, builds remarkably sophisticated automations without ever requiring more than one decision at a time. *Did they open the email? Did they click the link? Did they book the call? Did they reply? Did they pay?* Each is a simple yes/no question. Each can be a single If/Else. Five of them stacked end-to-end is a multi-week nurture that adapts to every lead's behavior.

### AND vs OR Logic Inside a Condition

Inside any branch's condition editor, you can add **Segments** — groups of rules combined with AND or OR. *AND* means all rules in the segment must be true. *OR* means any one rule being true is enough. Use AND when you're narrowing the criteria ("contact has booked AND is a paying customer AND opened the last email"). Use OR when you're broadening ("contact has booked OR has paid OR has clicked the calendar link").

Most beginner workflows need neither — a single condition is enough. Reach for AND/OR only when you find yourself building multiple separate branches that share a lot of overlap. If three different branches all check "is a paying customer" plus one other thing, you can probably collapse them into one branch with three OR'd conditions.

---

## Step 10 — Watch the History for Two Weeks

For the first two weeks the workflow is live, check the **History** tab at the end of each day. You're looking for:

- Did real leads actually fire it? (If not, something's wrong with the trigger or the form connection.)
- Did each step complete successfully, or did some fail silently?
- Are the test emails arriving as designed in real inboxes (check the spam folder too)?
- Do the merge fields resolve correctly for *every* contact, or just the test ones?
- Are leads appearing on the pipeline board on time?
- For the advanced version: are contacts ending up in the correct branch?

Workflows fail quietly in VibeReach — they don't ring an alarm or send you a panicked email. The history tab is your only window into whether the automation is doing its job. After two weeks of looking at it daily, you'll trust it and can drop the habit. Before two weeks, don't.

---

## Closing Thought — Four Tutorials, One System

You now have all four pieces:

- **Funnel Part 1** captures attention and converts visitors into contacts via well-designed pages, a custom domain, and SEO that gets found by both Google and AI search.
- **Funnel Part 2** collects clean, named, mappable data through forms and surveys with custom fields that make every downstream tool work.
- **Pipeline** organizes those leads into a Kanban board you can see, measure, and improve over time.
- **Workflow** automates the routine work that connects all three — tagging, opportunity creation, immediate follow-up, scheduled follow-up, and (with If/Else) personalized branching based on what each lead does.

These four systems, properly wired, replace the work of a full-time virtual assistant. Not as a metaphor — literally. Every email that goes out on time, every lead that lands on the pipeline before you've finished your coffee, every appointment-booked contact who *doesn't* get the wrong follow-up email — those are tasks a human used to do. Now they don't.

The rewards compound. The first lead through the full system feels like magic. The hundredth feels like infrastructure. By the thousandth, you've forgotten anyone used to do this manually.

The catch, restated one more time because it's that important: the automation is only as smart as the foundation underneath it. Bad form fields produce broken merge fields produce embarrassing emails. Bad tag naming produces reports nobody can read. Bad If/Else conditions silently route the wrong leads to the wrong place for months before anyone notices. Build the foundation deliberately, test every workflow before you trust it, watch the history for two weeks, and the system you just built will quietly compound value for as long as your business exists.

Go submit your own form. Watch the contact appear with all four custom fields populated. Watch the opportunity card land on the pipeline. Open your inbox and see the welcome email arrive. Wait until tomorrow morning and see the follow-up. The first time you watch it run for a real lead — not a test — is the moment you understand why people use VibeReach.

That's the system. The hard part is now behind you.

---

*Sources: HighLevel Support Portal — "Form Submitted Workflow Trigger," "Workflow Action: Send Email," "Workflow Action: Wait," "Workflow Action: If/Else Condition," "Getting Started: Setup Pipelines and Opportunities," and "Overview of Merge Fields & Custom Variables." Verified May 2026.*
