# Building Your First Form and Survey in VibeReach — Funnel Part 2

*A continuation of the funnel tutorial. Part 1 built the pages, the domain, and the SEO. This part builds the data layer underneath them: the form that captures leads, the survey that qualifies them, and the custom fields that make every downstream tool — pipelines, workflows, emails, reports — actually work. Forms and surveys are the moment your funnel turns into a CRM.*

---

## Why This Tutorial Exists (And What Part 1 Skipped)

Part 1 walked through the funnel editor, but it told a small lie by omission: it dropped a Form element onto the landing page without ever showing how to build the form behind it. The Form element on a funnel page is just a placeholder — a slot that points at a *separate* form definition built in a different part of VibeReach. We never built that definition. So if you completed Part 1 and tried to publish, the form on your page is either an empty default or it's missing entirely.

This tutorial closes that gap, and it closes a bigger one too. The form isn't just a UI element — it's the engine that decides what data lands on every contact record in your CRM. Every workflow, every email merge field, every pipeline filter, every report you'll ever run is downstream of the choices you make right now about what fields the form collects and how those fields map to your contact records.

So we're going to take this slowly. Build the form once, build it right, and everything downstream just works. Skip this step, and you'll spend the next six months wondering why your emails say "Hi {{contact.first_name}}" instead of "Hi Ernesto."

---

## Foundation — The Concept Behind Forms, Surveys, and Custom Fields

Three things you need to understand before you click anything. Five minutes here saves an hour of head-scratching later.

### Forms vs. Surveys — When to Use Which

They share the same drag-and-drop builder. They write to the same contact records. They look almost identical in the editor. But they serve different jobs.

**Forms are single-page, short, and direct.** Name, email, phone, maybe one or two qualifying questions, then a Submit button. The visitor sees the entire form at once. Use forms for opt-ins, contact-us pages, newsletter signups, and any place where speed-to-conversion matters more than depth of information. Forms convert better when the visitor's commitment is small.

**Surveys are multi-page, progressive, and conditional.** Each slide can have its own question or two, the visitor clicks Next to advance, a progress bar shows how far they are, and — critically — surveys support **page-level branching logic.** Based on how someone answers question 1, they can be routed to question 4, skip question 2 entirely, or be disqualified before ever reaching the end. Use surveys for lead qualification, intake forms, quizzes, application processes, and anything where you need depth of information *and* want the user to feel like the experience is responding to them.

A useful rule: if you can fit the questions on one phone screen, use a form. If you can't, use a survey. And if you ever need different visitors to see different questions based on what they answered, you must use a survey — forms don't branch.

### Standard Fields vs. Custom Fields

Same distinction as the workflow tutorial mentioned, but it's worth restating because it's the single most-confused topic in VibeReach.

**Standard fields are built into every account.** First Name, Last Name, Email, Phone, Address, City, State, Country, Postal Code, Company Name, Date of Birth, Website. They can't be deleted, they can't be renamed, and they auto-map to the matching slots on the contact record without any setup. If your form collects a "First Name" field, the value writes to the contact's First Name. No mapping decisions to make.

**Custom fields are anything else.** Biggest business challenge. Annual revenue. Team size. Lead source. Timeline. Buyer or seller. Preferred contact method. These don't exist until you create them, and **you must create them at the account level *before* you can use them in a form.** This is the sequence error that trips up every new VibeReach user: they jump into the form builder, can't find their custom field in the field palette, and don't realize they need to create it elsewhere first.

Custom fields are managed at **Settings → Custom Fields.** That's where they're born, edited, organized, and (carefully) deleted. The form builder just references the ones that already exist.

### A Word About Query Keys

Each field on a form has a **query key** — a unique behind-the-scenes identifier that tells VibeReach which field is which. For standard fields, query keys are pre-set (`first_name`, `email`, `phone`). For custom fields, the query key is generated from the field name when you create it (a field called "Biggest Challenge" might get a query key like `biggest_challenge`).

**Two rules about query keys, learned the hard way:**

First, **don't change a query key once the field is in use.** If you have workflows, automations, or merge fields referencing `biggest_challenge` and you rename it to `main_challenge`, every reference downstream breaks silently. The form keeps working. The data keeps getting collected. But your workflows stop seeing the answer and you don't find out until two months later.

Second, **build automations on custom fields, not on raw query keys.** Custom fields are stable, named, reusable across forms and surveys. Query keys are tied to specific fields on specific forms. If you build a workflow rule that says "if query key X equals Y, do Z," and you later replace that form with a new version, the rule breaks. Build on custom fields and the automations survive form rebuilds.

This is the kind of warning that sounds abstract until it costs you a Saturday. Trust it.

---

## Step 1 — Create the Custom Field First (Always First)

Before we touch the form or survey builder, we're going to create the one custom field we know our funnel needs: a place to capture the lead's *biggest business challenge*. This is the question that turns a generic opt-in into a useful lead — knowing what the prospect is actually trying to solve.

1. From the left navigation, go to **Settings.**
2. Click **Custom Fields.**
3. Make sure you're on the **Contact** custom fields tab (not Opportunity — that's a different object, covered in the pipeline tutorial). Contact custom fields live on the *person*; opportunity custom fields live on the *deal*. We want this attached to the person.
4. Click **+ Add Field** in the top right.
5. Configure:
   - **Field Type:** **Long Text (Multi-line Text).** Use Long Text instead of Short Text because we want the visitor to be able to type a sentence or two, not just a few words.
   - **Field Name:** *Biggest Business Challenge.* This is the label that shows up on the contact record. Make it clear enough that anyone on your team understands what's in it.
   - **Placeholder** (optional): something the visitor sees in the empty field, like *"In one or two sentences, what's the biggest problem you're trying to solve right now?"*
   - **Group:** *Additional Info* (the default group) or create a new group like "Lead Qualification" if you want fields organized into sections on the contact record.
6. Click **Save.**

You've now created a slot on every contact record in your account where this answer can live. Confirm this by opening any existing contact — scroll down past the standard fields and you'll see the new "Biggest Business Challenge" field, currently empty. The slot exists. Now we'll build the form that fills it.

**One critical detail to remember:** the field type you chose (Long Text) is permanent. You cannot change Long Text to Dropdown to Date Picker later. If you decide three weeks from now that you actually want this to be a dropdown with preset options, you'll need to create a new field and migrate the data manually. Choose the type deliberately the first time.

---

## Step 2 — Build the Form (The Simple Opt-In)

Now we build the form that lives on the CRM funnel's landing page. We're keeping it short — short forms convert better at the top of funnel.

1. Go to **Sites → Forms → Builder.**
2. Click **+ Add Form** (or **+ New Form**).
3. Name the form descriptively. *"CRM Funnel — Main Opt-In — 2026."* The name shows up in the workflow trigger picker later, so generic names like "Form 1" become a problem when you have ten of them.
4. The form builder opens with a blank canvas on the left and a field palette on the right.

### Add the Fields

From the right-hand panel, drag these fields onto the canvas in this order:

1. **First Name** — drag from the Standard Fields section. This is a standard field, so it auto-maps to the contact's First Name slot. No setup needed.
2. **Email** — drag from Standard Fields. Same deal — auto-maps. Email is the most important field on the form because it's also the deduplication key by default.
3. **Phone** — drag from Standard Fields. Phone is optional in most opt-in scenarios, but it unlocks SMS follow-up, which is one of the highest-ROI channels in VibeReach. Include it but consider making it optional (more on that below).
4. **Biggest Business Challenge** — scroll down to **Custom Fields** in the palette. You should see the field you created in Step 1. Drag it onto the form.

That's four fields. Resist the urge to add more. Every additional field on an opt-in form reduces conversion by a measurable amount. *Name, Email, Phone, and one open-ended qualifying question* is the sweet spot — short enough to convert well, deep enough to feel personalized when you follow up.

### Configure Each Field

Click on any field to open its settings on the right panel. The settings that matter:

**Label** — what the visitor sees as the field's title. The defaults are fine, but you can soften them ("Your First Name" instead of "First Name") if your brand voice is casual.

**Placeholder** — the gray hint text inside the empty field. Use this to give an example. For the Biggest Challenge field, a placeholder like *"e.g., I'm losing leads because nobody follows up fast enough"* dramatically increases the quality of answers because visitors mirror the example.

**Required** — toggle this on for First Name, Email, and Biggest Challenge. Leave it off for Phone. Required fields show an asterisk and block submission until filled; making everything required hurts conversion. Make required only the fields you genuinely cannot follow up without.

**Query Key** — leave it alone. The auto-generated key is fine, and (per the warning above) you don't want to be changing this once the form goes live.

### Configure the Submit Button

Click the Submit button at the bottom of the form to edit it.

**Button Text** — never leave this as "Submit." Replace it with action language that describes the outcome: *"Get My Free CRM Audit"* or *"Send Me the Guide"* or *"Yes, I Want This."* Button text is the smallest piece of copy on the page and one of the most testable — small changes here move conversion rates noticeably.

**Color, padding, font** — match your brand from Part 1. The button should be the highest-contrast element on the form, screaming "click me."

### Configure What Happens on Submission

Click the **Options** (or **Settings**) tab at the top of the builder. Here you configure post-submission behavior.

**On Submit:** choose **Redirect to URL** and paste in the URL of your funnel's thank-you page (the second step in your funnel from Part 1). When the visitor submits, they immediately land on the thank-you page. Alternative is *Show a Thank-You Message* in place — fine if you don't have a dedicated thank-you page, but the redirect is usually better because it gives you a second page to work with.

**Sticky Contact** — toggle this on if you want repeat visitors to have their fields auto-filled from previous submissions. Useful in some cases, occasionally awkward on shared devices (a partner submits using a household computer that has the other partner's data sticky-cached). My default: leave it off for top-of-funnel opt-ins, turn it on for return-visitor pages like client portals.

**Notifications** — under the Notifications section, you can configure an email alert to yourself every time the form is submitted. Useful in the early days when you want to know immediately that the form is working. Once your workflows take over the follow-up, you can disable these to save your inbox.

### Style the Form

Click the **Styles** tab. Set the background color, the text color, and the form's border styling to match your brand. Toggle **Full Width** if you want the form to fill its container — usually yes inside a funnel page section.

Click **Save Form** at the top right when you're done. The form definition is now alive in your account.

---

## Step 3 — Drop the Form Into the Funnel From Part 1

Time to connect this back to the funnel you built in Part 1. The Form element you dropped onto the landing page is currently pointing at nothing — or at a generic default. We'll point it at the form we just built.

1. Go to **Sites → Funnels** and open the CRM funnel from Part 1.
2. Click into the landing page (step 1).
3. In the funnel editor, find the Form element on the page. If it doesn't exist yet, drop one in using the plus sign (Forms is under the elements menu).
4. With the Form element selected, look at the right-hand sidebar. There's a **Form** dropdown — click it.
5. From the dropdown, select *"CRM Funnel — Main Opt-In — 2026"* (or whatever you named your form).
6. The form on the page instantly updates to show the fields you built.
7. Save the page.

That's the moment Part 1 and Part 2 actually connect. The funnel page now has a real, working form that writes to real contact fields, including your custom field.

---

## Step 4 — Build the Survey (Multi-Step Qualifying Questions)

Now we build something forms can't do: a multi-step qualifying survey that branches based on the visitor's answers. We're going to use this as the *next step* after someone opts in — instead of (or in addition to) the thank-you page, we'll route engaged leads through three qualifying questions before they reach the calendar.

This is what separates an okay funnel from a great one. Every minute the prospect spends interacting with your survey is a minute they're getting more invested — and you're getting more data to follow up well.

### Plan the Survey on Paper First

Same discipline from the pipeline tutorial. Before clicking, write down the questions and the branches.

Our survey, for the CRM consulting scenario, has four slides:

- **Slide 1:** What's your current biggest sales/marketing challenge? (Radio buttons — three options)
- **Slide 2:** How big is your team? (Radio buttons — three options)
- **Slide 3:** What's your timeline for solving this? (Radio buttons — three options)
- **Slide 4:** Branching outcome — qualified leads see the calendar; unqualified see a "stay in touch" message

The first three slides write to three custom fields. The fourth slide uses **conditional logic** to route based on the timeline answer.

### Create Three More Custom Fields First

Same sequence as before — fields first, then build the survey.

Go to **Settings → Custom Fields** and create three new contact custom fields:

1. **Sales Marketing Challenge** — Field Type: *Single Options (Radio Buttons)* — Options: *"Not enough leads," "Leads don't convert," "Following up is a mess."*
2. **Team Size** — Field Type: *Single Options* — Options: *"Just me," "2-10 people," "11+ people."*
3. **CRM Timeline** — Field Type: *Single Options* — Options: *"This month," "Next 1-3 months," "Sometime later."*

Note that we're using *Single Options (Radio Buttons)* with **pre-set choices** rather than open text. This is intentional. Pre-set choices give you clean, segmentable data ("show me everyone who answered 'This month'") instead of free-text answers that all need to be normalized manually. Use radio buttons or dropdowns for any field you'll later filter or report on.

Save each field. Now we have four custom fields total (the Biggest Challenge from Step 1, plus these three new ones).

### Build the Survey

1. Go to **Sites → Surveys → Builder.**
2. Click **+ Add Survey.**
3. Name it *"CRM Funnel — Qualification Survey — 2026."*
4. The survey builder opens. It looks almost identical to the form builder, but with one critical difference at the top: a row of **slide thumbnails.** Each slide is a separate page in the survey.

**Slide 1 — Sales/Marketing Challenge.** Drag your "Sales Marketing Challenge" custom field onto the slide. Above it, drag in a **Text** element from the static elements section, and write a short heading: *"What's your biggest sales and marketing challenge right now?"* Make the heading visually prominent.

**Slide 2 — Team Size.** Click the **+** at the top to add a new slide. On Slide 2, add a heading: *"How big is your team?"* Then drag the "Team Size" custom field onto the slide.

**Slide 3 — Timeline.** Add another slide. Heading: *"When are you looking to solve this?"* Drag the "CRM Timeline" custom field onto the slide.

**Slide 4 — Outcome / Branching.** Add a fourth slide. On this one, place two pieces of static content: a heading like *"Let's talk."* and a paragraph inviting them to book a call, with a button linking to your calendar. We're going to use conditional logic to control who actually reaches this slide.

### Add Conditional Logic

This is the part forms can't do. We're going to set up logic so that visitors who select *"Sometime later"* on the timeline question are routed to a different message — a polite "we'll stay in touch" — instead of the calendar.

1. In the survey builder, click **Conditional Logic** in the top bar (sometimes labeled **Conditions**).
2. Click **+ Add New Condition.**
3. Choose action type: **Redirect** (we'll redirect "later" leads to a different URL — perhaps a blog post or a "subscribe for updates" page on your site).
4. Configure the condition using the three-step builder:
   - **Select Field:** CRM Timeline
   - **Select State:** is equal to
   - **Provide Value:** Sometime later
5. **Redirect URL:** paste in your nurture page URL (or your blog).
6. Save the condition.

Now: when a visitor reaches the end of Slide 3 and clicks Next, VibeReach evaluates the condition. If their answer matches, they're redirected. If not, they continue to Slide 4 (the calendar invite).

**Optional — add a second condition.** You can add another condition that routes hot leads (timeline = "This month") to a dedicated VIP calendar with shorter slots, while medium-urgency leads (timeline = "Next 1-3 months") go to the standard calendar on Slide 4. The pattern is the same: another **+ Add New Condition**, another Redirect action, another field/state/value combo.

A few notes on the logic builder that save time:

- Rules are evaluated **top to bottom.** The first matching rule wins. Order your conditions from most-specific to most-general.
- You can combine multiple conditions in the same rule using **AND / OR** connectors. AND = all conditions must be true. OR = any one of them being true is enough. Switching between AND and OR updates all the conditions in the rule at once.
- Calendar fields aren't supported in conditional logic — you can't branch based on whether someone has booked a meeting before. (That kind of branching goes in workflows, not surveys, and it's covered in the workflow tutorial.)
- The builder prevents you from creating loops (Slide A → Slide B → Slide A would be blocked). If you ever see a "looping logic" error, that's what it means.

### Configure Survey Settings

Click the Options/Settings tab at the top. Configure:

- **On Survey Completion:** redirect to your funnel's thank-you page, or to a calendar page, depending on what your end-state is.
- **Progress Bar:** toggle ON. Visitors are much more likely to complete a multi-step survey when they see how close they are to finishing. This single toggle measurably improves completion rates.
- **Notifications:** same as forms — set up an email alert to yourself in the early days while you confirm the survey is working.

Click **Save Survey.**

### Drop the Survey Into the Funnel

Just like the form, the survey is now a defined object you can place anywhere. The natural place is on your funnel's thank-you page (step 2 from Part 1) — visitors who just opted in are now offered the qualifying survey as the immediate next step.

1. Open your funnel from Part 1, navigate to the thank-you page.
2. Either replace the existing "thank you" content with the survey, or add a section below it that introduces the survey ("Want to skip the wait? Answer 3 quick questions and book a call.").
3. Drop a **Survey** element onto the page using the plus sign, and select your new survey from the dropdown.
4. Save the page.

You now have a two-step funnel that captures the basics on page 1, qualifies on page 2, and routes prospects appropriately based on their answers. That is a real CRM front-end.

---

## Step 5 — Test the Whole Thing End-to-End

Don't trust it until you've seen it work. Test the entire flow in an incognito browser window with a test email you own:

1. Open your funnel's landing page.
2. Fill out the form: First Name, Email, Phone, and a real-sounding "Biggest Challenge" answer.
3. Submit. You should redirect to the thank-you page.
4. Take the survey: answer all three slides.
5. Verify the routing: if you answered "Sometime later" on the timeline, you should land on your nurture URL. Otherwise, you should land on the calendar slide.

Now back to VibeReach:

1. Go to **Contacts** in the left nav.
2. Find your test contact (search by the email you used).
3. Open the contact record.
4. Verify the standard fields: First Name and Phone should be populated. The email should be the contact's primary email.
5. Scroll to the **Additional Info** section. You should see all four custom fields populated: Biggest Business Challenge (with the sentence you typed), Sales Marketing Challenge (with the radio option you picked), Team Size, and CRM Timeline.

If anything is missing — say, the custom field shows blank even though you typed an answer — go back to the form/survey builder, click the field, check that the **Query Key** matches the custom field you created at Settings → Custom Fields. The most common cause of missing data is a form field that *looks* like the right custom field but is actually a different one with a similar name.

Also verify the submission record:

1. Go to **Sites → Forms → Submissions** to see the form submissions log.
2. Go to **Sites → Surveys → Submissions** to see the survey submissions log.
3. Both should show your test submission with timestamp and all field values.

If everything is populated correctly, congratulations — every workflow you build from here on out has clean, named, mappable data to work with. The merge fields will resolve. The tags will fire on the right conditions. The pipeline filters will return the right contacts. None of that works without this foundation.

---

## Step 6 — A Few Habits That Pay Off Forever

Quick list of disciplines worth adopting now, before you have fifty forms and twenty surveys:

**Name your forms and surveys descriptively.** *"CRM Funnel — Main Opt-In — 2026"* is far better than *"Form 1"* or even *"Contact Form."* Once you have multiple funnels, multiple campaigns, and multiple years of history, the name is how you'll find what you need.

**Create custom fields with the future in mind.** Resist the temptation to create a one-off custom field for every form. Custom fields are *reusable* across forms, surveys, workflows, and reports. If "Annual Revenue" is going to come up in three different forms, create *one* "Annual Revenue" field and use it in all three. Don't create three different versions.

**Keep custom field types deliberate.** Single Options for things you'll filter on. Long Text for things you'll read. Date Picker for dates (never store dates as text). Monetary for dollar amounts. The right type up front prevents data hell later.

**Use radio buttons or dropdowns for any field you'll segment by.** Open text fields produce free-form answers that are nearly impossible to filter — "small business," "small biz," "SMB," "smol business" all mean the same thing but show up as four different values in your reports. Pre-set choices solve this at the source.

**Don't rename query keys after fields are in use.** It will silently break things downstream. If you absolutely must, search every workflow and merge field for references to the old key first.

**Test every form and survey end-to-end after every change.** It takes ninety seconds. Forms can stop writing data correctly for subtle reasons, and the only way to catch it is to actually submit one and inspect the contact record.

---

## Closing Thought — The Data Layer Beneath Everything

Most people building in VibeReach start with the visible stuff: the pages, the design, the colors. That's natural — those are the things you can see. But the work that decides whether the platform actually delivers value is the work nobody sees: which fields you collect, how they map to records, what types they are, how they're named. Every workflow you build from this point forward, every email that personalizes correctly, every pipeline filter that returns the right contacts, every report that tells you something true about your business — all of it sits on top of the choices you just made.

You can build a beautiful funnel and a clean pipeline and a sophisticated automation, but if the form underneath them collects "Name" as one undifferentiated string instead of First Name and Last Name as two fields, every personalized email you ever send for the rest of that account's life will be slightly wrong. You can rebuild the funnel. You can rebuild the pipeline. The data layer is the part that's painful to redo because every field rename cascades through every workflow that references it.

Get this right the first time and the rest of VibeReach becomes the smooth, automated machine the marketing says it is.

Submit your own form. Take your own survey. Open your contact record. Watch the fields populate exactly as you designed them. That's the moment Part 1 and Part 2 stop being separate tutorials and become one working CRM front-end.

---

*Sources: HighLevel Support Portal — "How to Create a Contact Form in HighLevel," "How to Create and Use Custom Fields," "Quick Add & Edit Custom Fields in Forms & Surveys," "Conditional Logic in Forms," "Conditional Logic in Surveys (v2)," and "Overview of Merge Fields & Custom Variables." Verified May 2026.*
