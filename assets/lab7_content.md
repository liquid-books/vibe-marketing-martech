## 7.16 Lab 7: Build an Application Form That Routes to a Booked Consultation

A consultation booking process built from disconnected tools — a Typeform for the application, a Calendly for scheduling, a PDF for the agreement — creates friction, loses data, and produces no automatic follow-up. This lab wires all three into a single integrated flow inside VibeReach.io: a branded application form that qualifies the prospect, routes qualified applicants directly to a calendar booking page, and triggers a preparation workflow automatically. By the end, someone can go from "I'm interested" to "consultation booked with prep documents sent" in under 5 minutes — without any manual intervention from your team.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- A GHL calendar configured for your consultation service (at minimum a basic calendar from Settings → Calendars — if you haven't set one up, complete that in Settings first)
- A clear picture of what questions you need answered before a consultation (your qualification criteria)
- Approximately 45–60 minutes
:::

---

### Step 1: Create the Application Form

1. In the left sidebar, click **Sites** → **Forms** (or **Marketing → Forms** depending on your GHL version).
2. Click **+ New Form**.
3. Select **Start from Blank** → enter form name: `Consultation Application — [Your Service]`.
4. Click **Create Form**.

The form builder opens with a blank canvas.

**You'll know you did this right when:** A blank form builder canvas appears with a toolbar of form elements on the left side.

---

### Step 2: Add Your Qualification Questions

Click form elements from the left panel to add them to the form. For a business services consultation, build these fields in order:

**Section 1 — Contact Information (always first)**
1. **First Name** (text field — required)
2. **Last Name** (text field — required)
3. **Email Address** (email field — required)
4. **Phone Number** (phone field — required)
5. **Business Name** (text field — required)

**Section 2 — Qualification Questions**

Add a section divider element and label it "Tell Us About Your Business."

6. **What industry is your business in?** (dropdown — required. Pre-populate with your most common industries plus "Other")
7. **How long have you been in business?** (dropdown — required. Options: Less than 1 year / 1–3 years / 3–10 years / 10+ years)
8. **What is your approximate annual revenue?** (dropdown — required. Options: Under $100K / $100K–$500K / $500K–$1M / Over $1M)
9. **What is the primary challenge you're hoping to solve?** (textarea — required, min 50 characters)
10. **How did you hear about us?** (dropdown — optional)

:::{admonition} Why This Matters
:class: tip
These questions serve two purposes: they qualify whether this lead is a good fit for your consultation, and they brief you before the call. When someone arrives at the consultation, you already know their industry, revenue range, and stated challenge. The first 5 minutes of the call can be spent on solutions instead of discovery basics — and your close rate reflects it.
:::

**You'll know you did this right when:** The form preview shows all 10 fields organized in two logical sections, with clear labels and required field indicators.

---

### Step 3: Set the Form Submission Action — Route to Calendar

1. Click the **Form Settings** tab (gear icon) in the form builder.
2. Under **On Submit / Redirect**:
   - Select **Redirect to URL** or **Calendar Page** (if GHL shows the calendar option directly)
   - Select **Redirect to URL** → enter the URL of your GHL calendar booking page

   **To find your GHL calendar URL:**
   - Go to ⚙️ **Settings** → **Calendars**
   - Click on your consultation calendar
   - Look for "Booking Link" or "Calendar URL" — copy it
   - Paste this URL in the form's redirect field

3. Click **Save Settings**.

:::{admonition} Why This Matters
:class: tip
Routing qualified applicants directly to the calendar page eliminates the friction of a separate booking step. Without this redirect, your conversion rate at the "application to booked call" stage will be 20–40% lower because prospects have to remember to book after submitting the form. The redirect captures momentum — they're already engaged.
:::

**You'll know you did this right when:** The form settings show a redirect URL that matches your GHL calendar booking link.

---

### Step 4: Configure Field Mapping to CRM

1. In the form builder, click the **CRM Mapping** or **Field Mapping** tab.
2. Map each custom form question to the appropriate GHL contact field:
   - First Name → First Name (standard)
   - Last Name → Last Name (standard)
   - Email → Email (standard)
   - Phone → Phone (standard)
   - Business Name → Company Name (standard)
   - Industry → Industry (custom field — create if needed in Settings → Custom Fields)
   - Annual Revenue → Annual Revenue (custom field)
   - Primary Challenge → Notes (standard field, or create a "Consultation Notes" custom field)
3. Click **Save Mapping**.

**You'll know you did this right when:** All form fields are mapped to GHL fields. When you submit a test entry, the contact record in GHL is fully populated with all submitted values.

---

### Step 5: Publish the Form and Get the Embed Code

1. Click the **Publish** button in the form builder.
2. The platform generates an embed code. You have two options:
   - **Iframe embed:** A code block you paste into any web page
   - **Direct form URL:** A hosted GHL form page you can link directly

3. Copy the direct form URL for sharing, and copy the iframe code for embedding on your website.

**Embed in Your Funnel (recommended):**
In your Lab 2 funnel, add a new step for "Apply for Consultation." Add a Form element to the page and select your new application form. This keeps everything inside your funnel ecosystem.

---

### Step 6: Build the Post-Application Workflow

Now wire the automated preparation workflow that fires when someone submits the application:

1. **Automation → Workflows → + New Workflow → Start from Scratch**
2. Name: `Consultation Application — Automation`
3. **Trigger:** Form Submitted → Filter: Form Name = your application form
4. Add actions:

**Action 1 — Apply Tag:** `consultation-applicant`

**Action 2 — Create Pipeline Opportunity:**
- Search for "Create Opportunity" in the action picker
- Pipeline: Your Sales pipeline
- Stage: `Qualified` (or "Consultation Scheduled" if you have this stage)
- Value: Your average consultation-to-client value (estimate)

**Action 3 — Send Confirmation Email:**
- Subject: "Application received — here's what happens next"
- Body: Confirm their application was received, tell them what to expect, include your calendar link again as a backup, and send 1–2 preparation questions to help them get more from the call.

**Action 4 — Internal Notification to You:**
- Use "Send Internal Notification" action
- Notify your email: "[New Consultation Application] {{contact.first_name}} {{contact.last_name}} — {{contact.company_name}}"

5. Toggle workflow to **Active** → **Publish**.

:::{admonition} Why This Matters
:class: tip
The pipeline opportunity creation is the step most people skip — and it's the most valuable. Every submitted application becomes a visible card in your Sales pipeline with their name, company, and estimated value. You can see at a glance how many consultations are booked, which are pending, and what the pipeline revenue looks like. Without this step, applications disappear into contact records with no visibility.
:::

**You'll know you did this right when:** The workflow shows all four actions in sequence, the trigger is linked to your application form, and the workflow is Active.

---

### Step 7: Test the Full Flow End to End

1. Open the application form URL in an incognito browser window.
2. Complete the form with test data (use your own contact info).
3. Submit the form.
4. Verify:
   - You are redirected to the calendar booking page
   - A new contact was created in GHL with all form fields populated
   - The `consultation-applicant` tag is applied to the contact
   - A pipeline opportunity appears in your Sales pipeline under "Qualified"
   - You received the internal notification email
5. Complete a test calendar booking — verify the appointment appears in your GHL calendar.

**You'll know you did this right when:** The full flow completes — application submitted → redirected to calendar → appointment booked → contact in CRM with tag and opportunity created → confirmation email received.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 8:

- ☐ Application form created with 10 fields across two sections
- ☐ Form submit redirects to your GHL calendar booking URL
- ☐ CRM field mapping configured — all fields populate contact record on submission
- ☐ Form published with direct URL and/or iframe embed code
- ☐ Workflow Active: triggers on form submission, applies tag, creates opportunity, sends confirmation, notifies team
- ☐ End-to-end test completed: form → calendar → CRM → email confirmed

You have an automated consultation qualification and booking system. Prospects self-qualify, self-schedule, and receive preparation materials — all without manual intervention.
:::

::::{dropdown} Troubleshooting Common Issues

**Form submitted but contact wasn't created in GHL:**
Verify that Email or Phone is mapped in the CRM field mapping — GHL requires at least one unique identifier to create or match a contact. Check the form's CRM Mapping tab and confirm the mapping is saved.

**Redirect to calendar doesn't work — a blank or error page appears:**
Verify the calendar URL is correct. Go to Settings → Calendars → click your calendar → copy the exact booking link URL. Test it independently in a browser before pasting it into the form redirect setting. Make sure the calendar is set to "Public" visibility.

**The pipeline opportunity wasn't created:**
The "Create Opportunity" action requires a pipeline and stage to be selected. If either is blank, the action fails silently. Check the workflow execution log (Automation → Workflows → History tab) for the specific test contact to see what error occurred.

**Form fields appear in the wrong order in the published form:**
In the form builder, drag elements to reorder them. If order doesn't match the published form, clear your browser cache and reload. The builder may be showing a cached view.

**The confirmation email arrived but preparation questions weren't included:**
The email body is fully customizable. Edit the "Send Email" action in the workflow, click into the email body, and add your preparation questions as bullet points. Save and re-publish the workflow.

**Calendar booking isn't appearing in GHL after test booking:**
Go to Settings → Calendars → your calendar → Integrations tab. Confirm it is set to GHL internal calendar (not Google Calendar sync only). If syncing to external Google Calendar, check the sync settings and permissions.
::::

