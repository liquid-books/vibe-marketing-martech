# Forms and Documents — Sending Contracts for E-Signature in VibeReach

*Part six of the curriculum. Funnel Part 2 already taught Forms — Standard and Custom fields, surveys with conditional logic, the field mapping that powers everything downstream. We won't re-cover that here. What we will cover is the other half of the "Forms and Documents" pair: the Documents & Contracts module, which is how you send proposals, contracts, and service agreements for legally binding e-signature directly from inside VibeReach. This tutorial turns the Pipeline's "Proposal Sent" stage from aspirational to operational.*

---

## What This Tutorial Assumes

Same curriculum stack as before. By now you have:

- **Funnel Part 1 + Part 2** — pages, a working form with custom fields, a qualifying survey.
- **Pipeline** — Kanban stages New Lead → Call Booked → Proposal Sent → Won/Lost.
- **Workflow** — automation that tags, creates opportunities, sends emails, branches on appointment status.
- **Calendars + Conversations** — booking calendar, unified inbox, mobile app for daily ops.

Forms, as we built them, capture data at the *top* of the funnel — Name, Email, Phone, plus custom qualifying fields. That data lives on the contact record and feeds every downstream automation. Documents work at the *bottom* of the funnel — you've had the call, the prospect is interested, and now you need to send them something to sign so the deal can close. The Pipeline stage we've been calling "Proposal Sent" needs to actually have a proposal attached to it. This tutorial builds it.

A small note on what we're *not* covering: Funnel Part 2 included a section on Forms with signature fields embedded in them (people sometimes use a form-with-signature as a lightweight "agreement"). That works for low-stakes acknowledgments — a media release, a cancellation policy acceptance — but it's not appropriate for actual contracts. For real proposals, service agreements, and legally binding e-signatures with audit trails, you use Documents & Contracts. That's what this tutorial is about.

---

## Why Documents Lives Where It Lives (and Why That's Confusing)

The first thing that trips people up: Documents & Contracts isn't under its own top-level menu item. It lives under **Payments**. Which is weird, because most of what you'll do with it has nothing to do with collecting payment. The reason it's filed there is because VibeReach designed the module to bundle e-signature with optional integrated payment collection — sign the contract and pay the deposit in the same flow — so they grouped it with the payments tools.

Once you know it's there, finding it is easy: **Payments → Documents & Contracts** in the left navigation. You'll see a dashboard listing every document you've ever created or sent, with status columns showing draft, sent, viewed, completed, declined, or expired.

---

## The Three Ways to Create a Document

Click the **+ New** button in the top-right of the Documents & Contracts dashboard. You'll see three options:

**New Document** — start from scratch in VibeReach's editor. Best for proposals and agreements you want to fully brand and customize. You'll build it from text blocks, headings, images, video embeds, pricing tables, and signature fields, all dragged and dropped.

**Upload Existing PDF** — import a PDF you already have (say, a contract your lawyer wrote in Word and exported) and overlay signature, date, and text fields on top of it. Best for legal documents you don't want to rebuild from scratch and that already have your firm's exact language.

**Import from Template Library** — choose from VibeReach's prebuilt templates or your own saved templates. Best for recurring agreements where the structure is the same every time and only the contact name and pricing change.

For this tutorial we'll build a New Document from scratch, because once you know how to do that you can also handle the other two paths without trouble. The fields and signature mechanics are the same.

---

## Plan on Paper First

This is the same discipline from the pipeline and workflow tutorials, and it matters even more here because once a document is sent, it locks. If you sent it directly (not as a draft), the platform considers it legally executed in-progress and you cannot edit it. You can clone it and start over, but the version with the typo is now a permanent record. So get it right before you send.

Before you open the editor, decide on paper:

**Sections.** A typical service proposal has: cover/title, introduction, scope of work, deliverables, timeline, pricing, terms and conditions, signature block. List your sections in order.

**Pricing structure.** One-time fee? Recurring monthly? Multiple line items? Optional add-ons? Decide before you start, because the editor has a Product List element that pulls from your product catalog — knowing your structure determines whether you need to set up products first.

**Variable fields.** What changes per client? Contact name, company name, project scope, total price, start date — these will become Custom Values (merge fields) in your template so you don't manually edit each send. Make the list now.

**Signers.** Who signs? Just the client? You and the client? Multiple stakeholders on their side? Each signer needs their own signature field, assigned to them specifically.

**Sending mode.** Will this auto-send from a workflow, or do you want it to create as a draft so you can review and personalize before sending manually? For high-value contracts, draft mode is usually the right answer.

Take five minutes for this. It saves an hour of cleanup later.

---

## Step 1 — Configure Document Settings Once, Globally

Before building your first template, do the one-time settings configuration. This applies to every document you'll ever send from this sub-account.

1. Go to **Payments → Documents & Contracts**.
2. Click the **Settings** button in the upper right.
3. In the secondary nav, choose **Document Settings**.

Two things to configure here:

**Signature Type.** Scroll to Control Signature Settings. You can allow signers to **Draw** their signature (touchpad / mouse / finger), **Type** their signature (rendered in a script font), or **Both** (signer's choice). Both is the most flexible and the most common choice. If you're in a regulated industry that requires hand-drawn marks for compliance, restrict to Draw. Most consulting work is fine with Both.

**Email Templates and Team Notifications.** Set the default subject line and body for the email that goes out when a document is sent. Default is fine to start with; you can override per-document later. Also set who on your team gets notified when a document is signed — at minimum, this should be you.

Save. You won't think about these settings again unless your business changes.

---

## Step 2 — Create the Template

Now build the actual document. Templates are reusable — build it once, send it dozens of times.

1. From **Documents & Contracts**, click **Templates** tab.
2. Click **+ New Template**.
3. Give it a clear, specific name: *"CRM Setup — Service Agreement"*. Not "Contract." Not "Template 1." Same naming discipline as everything else in this curriculum — if you have to read it back to yourself in six months, will you know what it is?
4. The editor opens.

The editor is drag-and-drop, similar to the funnel page builder. Left side has a toolbar with elements you can drop onto the canvas. Right side has properties for the currently selected element.

**Elements you'll use most:**

- **Text** — paragraphs, headings, list items. The workhorse element.
- **Image** — your logo at the top, product screenshots in the scope section, signature line graphics.
- **Video** — optional. Embedding a 60-second personal video at the top of a proposal raises close rates noticeably. People sign more readily when they remember talking to a human.
- **Table** — for structured data like timeline milestones or deliverables breakdowns.
- **Product List** — pulls from your VibeReach product catalog with live pricing. Use this for line-item pricing instead of typing numbers in a text block.
- **Custom Values** — the merge fields. These insert dynamic data like contact name, company name, or any custom field you set up in Funnel Part 2.
- **Signature Box** — required. At least one. Assigned to a specific signer.
- **Date Field** — auto-fills the signing date when the signer completes the signature.
- **Text Input Field** — for signer to fill in something themselves (e.g., their title, their company's billing address).

---

## Step 3 — Build the Document Section by Section

Working top to bottom on a typical service proposal:

**Header.** Drop an Image element, upload your logo. Drop a Heading element below it with the document title: *"Service Agreement — CRM Setup and Implementation."* Below that, a Text element with the date — use the `{{current_date}}` custom value so it auto-fills.

**Introduction / Cover Letter.** A Text element with a personalized greeting using `{{contact.first_name}}` and `{{contact.company_name}}`. Two or three sentences setting the tone: *"Thanks for the conversation last week, {{contact.first_name}}. This agreement outlines the scope, timeline, and pricing for the CRM setup work we discussed for {{contact.company_name}}."*

**Scope of Work.** A Heading element followed by Text. Bullet out exactly what you're delivering. Be specific. Vague scope is where every freelance and consulting relationship goes wrong. *"Migration of existing contacts from current CRM. Setup of three custom pipelines. Configuration of two automated workflows. Training session with up to three of your team members. One round of post-launch optimization."* Specifics protect both sides.

**Timeline.** A Table element with two columns — Milestone and Date. Five rows for a typical engagement: Kickoff, Week 1 Discovery, Week 2-3 Build, Week 4 Training, Week 5 Launch. Use real dates if you know them, or relative phrasing like "Week 1 from kickoff."

**Pricing.** Drop a Product List element. In the right-side properties, add your services from your product catalog. If you haven't set up products yet, you can also build a manual table — Product, Quantity, Unit Price, Subtotal — and just type the numbers. Product List is cleaner and the math auto-totals, so it's worth setting up products first if you have time.

**Terms and Conditions.** A long Text block with the legal language. Payment terms (50% upfront, 50% on completion, or whatever your standard is). Cancellation policy. IP ownership. Confidentiality. Limitation of liability. This is the part where you want a real lawyer's eyes if you don't have a template you trust. Don't write contract terms from scratch based on what you think they should say.

**Signature Block.** This is the part that makes it a contract instead of a proposal. Drop a Heading element: "Acceptance and Signature." Below it, two Signature Box elements side by side — one for the client, one for you. Assign each signature box to its signer in the right-side properties. If you're sending from a workflow, the "you" signature is the **Sender** field (typically auto-mapped to the workflow's From User). The client signature is mapped to **Contact**. Add a Text Input Field below each for "Printed Name" and "Title." Add Date Fields next to each signature for "Date Signed."

Save the template. You can come back and edit it anytime — but keep in mind that *changes don't apply retroactively to documents already sent.* If you sent a contract yesterday and edit the template today, yesterday's contract still has yesterday's text. The template change only affects new documents created after the edit. This is a feature, not a bug — it protects the legal integrity of in-flight agreements — but it surprises people the first time.

---

## Step 4 — Test the Template Manually Before Wiring It to Automation

Don't trust automation until you've watched the document work manually first.

1. Go to **Documents & Contracts**, click **+ New** → **New Document** (not template — actual document).
2. Select your template from the list.
3. Choose a test contact (yourself, ideally — a real contact record with a real email address you can check).
4. The document generates with all the merge fields filled in. Scan it. Does the company name appear correctly? Does the pricing pull right? Are the signature boxes assigned to the right signers? Is the date current?
5. If anything's off, go back and fix the template, then regenerate the document.
6. When it looks right, click **Send**.

The contact receives an email with a secure link to the document. They click, the document opens in their browser (no login required), they review, fill in their signature box (drawing or typing), fill in any text input fields, and click to complete.

You receive a notification — both in-app and via email — that the document has been signed. The document status changes to **Completed** on the dashboard. A signed PDF copy is automatically emailed to the signer and saved on the document record.

**The audit trail.** Click into the completed document. There's a tab showing the audit log — when the email was sent, when the contact opened the link, when they viewed each page, the IP address they signed from, the timestamps. This is what makes the e-signature legally binding under ESIGN and UETA in the US (and similar laws elsewhere). Don't skip this — if a dispute ever arises, the audit trail is your evidence.

---

## Step 5 — Wire the Document to the Pipeline via Workflow

Now the part where this connects to everything else in the curriculum. Remember the pipeline has a "Proposal Sent" stage. Currently, dragging a card to that stage doesn't do anything beyond updating the visual. We're going to make it actually send the proposal.

1. Go to **Automation → Workflows**.
2. Either create a new workflow or open your existing CRM workflow from Tutorial 4.
3. We're adding a new branch to the existing workflow — *or* building a small standalone workflow whose only job is to send contracts. Either pattern works. For clarity, build it standalone first; you can always merge it later.

**Trigger:** Pipeline Stage Changed. In the filter, select your pipeline, then select the stage **Proposal Sent**. This means the workflow only runs when a card moves *into* that specific stage.

**Action 1:** Send Documents & Contracts.
- **Template:** Select your CRM Setup — Service Agreement template.
- **Sending Mode:** Choose between *Send Directly* (the contract goes immediately to the contact) or *Create as Draft* (the contract is generated but waits for you to review and send manually). For most consulting work, Create as Draft is the safer default — you want a chance to glance at the auto-generated document before it lands in the prospect's inbox.
- **From User:** Choose the user who appears as the sender on the contract. For solo work this is you. For team setups, this is whichever user is assigned to the contact's opportunity.

**Action 2:** Send Internal Notification (optional). An internal Slack-style message to yourself: *"Contract sent to {{contact.first_name}} {{contact.last_name}} at {{contact.company_name}}."* Useful so you have a record in your notification feed.

Save and publish the workflow.

---

## Step 6 — Test the Full Pipeline-to-Contract Flow

End-to-end test, the way you've done at every step of this curriculum:

1. Go to your pipeline. Pick a test opportunity (or create a new test contact and add an opportunity for them).
2. Drag the card from Call Booked to Proposal Sent.
3. Within a few seconds, the workflow fires. If you set Create as Draft, the document appears in your Documents & Contracts dashboard with status "Draft." If you set Send Directly, the contact receives the email.
4. If Draft mode: open the document, review it, personalize anything that needs personalizing, then click Send.
5. The contact's Conversations thread (from Tutorial 5) now shows the outbound document email logged there.
6. The contact opens the document, signs, completes.
7. Status flips to Completed on the dashboard. A signed PDF is saved on the contact record.
8. Now — and this is the loop closing — you can build *another* workflow that triggers on "Document Status = Completed" and automatically advances the pipeline card to **Won**, fires an onboarding email sequence, sends a payment invoice, or whatever the next step in your process is.

That's the deal cycle, end to end, fully automated. Lead lands, qualifies through the survey, books a call via the calendar, gets nurtured by the workflow, takes the call, gets dragged to Proposal Sent, signs the contract, advances to Won, kicks off onboarding. You touch the keyboard maybe three times in that whole sequence. Everything else is the system.

---

## Public Document Links — For When You Don't Have a Contact Yet

One more feature worth knowing about: **Public Document Links.** Sometimes you need a one-size-fits-all document that anyone can sign without you having to create a contact record first. Examples: a media release for podcast guests, a standard NDA for prospective partners, a webinar attendance waiver, an event terms-of-attendance agreement.

1. Go to **Documents & Contracts → Templates.**
2. Click **+ New Template → Create Public Document** (or open an existing template and click Publish).
3. Build the document the same way you'd build a regular one, but instead of contact-specific merge fields, the public version asks signers to enter their own name and email at the start of the signing flow.
4. After publishing, a unique public URL is generated. Share it anywhere — embed it in a funnel page, put it in your email signature, paste it in a calendar event description.
5. Each signature is captured and stored in the Responses section of the template, where you can download signed copies.

Public Document Links are independent of workflows and don't require a contact to exist beforehand. They're not the right tool for client contracts (those need to be tied to a real contact, real opportunity, real pipeline), but they're invaluable for the one-off agreements that don't fit a sales process.

---

## A Few Things That Will Trip You Up

**The "edit after send" lock.** Once a document is sent (not draft), it's locked. You cannot fix a typo. You can clone the document, fix the clone's underlying template, and send a new one — but the original is permanent. Always proofread *before* you click Send.

**Workflow status branching is point-in-time.** If your workflow has an If/Else after the document send checking "Document Status = Completed," remember that the workflow evaluates the status at the moment the contact reaches that branch. If the contact hasn't signed yet when the branch evaluates, they go down the "not completed" path — and the branch doesn't re-evaluate later when they do sign. To handle "what happens when they finally sign," use a separate workflow triggered on **Document Signed** as its own event. Same lesson from the workflow tutorial about If/Else not reconverging — applies here too.

**Phone numbers and country codes.** If your contract collects a phone number from the signer (e.g., a custom text field), and you plan to text that number from VibeReach later, make sure your form/field tells signers to include their country code. International number formatting is the single most common reason "the SMS isn't sending" tickets get filed.

**Templates vs. one-off documents.** Build templates for anything you'll send more than twice. Build one-off New Documents for unique agreements. If you find yourself editing the same template every time you send it, the template isn't doing its job — refactor it so the per-client variation lives in custom values, not in manual edits.

---

## Closing Thought — The Deal Cycle Is Now Closed

You've now built every link in the chain a service business needs:

- **Funnel** captures the lead
- **Forms/Surveys** qualify the lead with structured data
- **Pipeline** organizes the lead through stages
- **Workflow** automates the follow-up
- **Calendar** schedules the conversation
- **Conversations** holds every exchange in one place
- **Documents** closes the deal

That's the entire commercial lifecycle of a service offering, end-to-end, inside one platform. From a stranger arriving at your funnel page to a signed contract sitting in their inbox and a Won card on your pipeline — every step accounted for, every transition automated where it should be, every human touchpoint amplified by the system around it.

What comes next isn't more chain links. What comes next is what makes the chain *smarter and more visible*. The remaining tutorials in this series add three layers on top of what you've already built: **AI Employees** (which offload routine work the system used to require from you), **Reporting and Analytics** (so you can see what's actually happening across the system you built), and **Social Media + Social Planner** (so the system has a top of funnel that doesn't require you to be hand-feeding it traffic).

Go run a complete deal through the pipeline with a real document attached. Watch a Proposal Sent stage actually send a proposal. Sign it as your own test contact. See the whole loop work. Once you've watched it once, you'll never set up a closing process any other way.

---

*Sources: HighLevel Support Portal — "Documents & Contracts in HighLevel: Setup and Guide," "How to Create and Send Document or Contract Templates Automatically in a Workflow," "Workflow Action: Send Documents & Contracts," "Public Document Links for E-Signing," "Control Signature Type for Documents & Contracts." Verified May 2026.*
