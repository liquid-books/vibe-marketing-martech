## 2.12 Lab 2: Build a Lead-Magnet Funnel End to End — Page, Form, Offer, Confirmation

A lead-magnet funnel is the engine that converts cold traffic into named, tagged contacts in your CRM. In this lab, you build a complete two-page funnel — a landing page with an opt-in form, and a thank-you page — then wire it to a workflow trigger so every submission automatically creates a contact, delivers the lead magnet, and starts the follow-up sequence. By the end, you will have a live, working funnel URL you can send traffic to today.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with your sending domain verified (Lab 0)
- Your Lab 0 domain configured and pointing to VibeReach.io (for custom subdomain on funnel URL)
- A lead magnet asset — this can be a simple PDF checklist (a one-page Google Doc saved as PDF works perfectly)
- Approximately 45–60 minutes

📥 **[Download lab02-funnel-template.json](https://raw.githubusercontent.com/liquid-books/vibe-marketing-martech/main/assets/lab02-funnel-template.json)**

The template file is a VibeReach.io funnel import — it gives you a pre-built two-page structure to customize rather than building from scratch.
:::

---

### Step 1: Create the Funnel

1. In the left sidebar, click **Marketing** → **Funnels**.
2. Click **+ New Funnel** in the upper right.
3. When prompted "Start from Scratch or Import?", click **Import from File**.
4. Upload `lab02-funnel-template.json` → click **Import**.

If you prefer to build from scratch:
1. Click **+ New Funnel** → **Start from Scratch**.
2. **Funnel Name:** `Lab 2 — Lead Magnet Funnel` → click **Create Funnel**.
3. You are taken to the funnel steps view. Click **+ Add Step**.

:::{admonition} Why This Matters
:class: tip
A funnel in VibeReach.io is a container that holds multiple pages, tracks visitor flow between them, and connects to your CRM. Unlike a standalone page, a funnel has built-in conversion tracking — you can see how many visitors saw the landing page, what percentage submitted the form, and what percentage reached the thank-you page. This conversion rate data is how you improve the funnel over time.
:::

**You'll know you did this right when:** A funnel appears in your Funnels list with the name you entered and shows "0 Steps" (before you add pages) or the imported template structure.

---

### Step 2: Build (or Customize) the Landing Page

1. In your funnel, click **+ Add Step** (or click the existing first step if you imported the template).
2. Name this step: `Opt-In Page` → select **Funnel Page** type → click **Create Step**.
3. Click **Edit Page** to open the page builder.
4. In the builder, configure:
   - **Headline:** Clear benefit statement — e.g., "The 5-Step Checklist to Get Your Business Funding-Ready in 7 Days"
   - **Sub-headline:** One sentence expanding on the benefit — e.g., "Download the exact checklist our consultants use before every funding application"
   - **Body text:** 2–3 bullet points listing specific things the lead magnet helps with
5. Click **Save** in the builder.

:::{admonition} Why This Matters
:class: tip
The headline is the most important element on the page — it determines whether a visitor stays or leaves in the first 3 seconds. A good headline names a specific benefit for a specific person. "Marketing Tips" is bad. "The 5-Step Checklist to Get Business Funding-Ready in 7 Days" is good. Be specific.
:::

**You'll know you did this right when:** The landing page preview shows your headline and bullet points. The page is readable on both desktop (preview button, desktop icon) and mobile (preview button, mobile icon).

---

### Step 3: Add the Opt-In Form

1. In the page builder, locate the form element (it will already exist if you imported the template, or click the **Form** element from the left elements panel and drag it to the page).
2. Click the form element to select it → click **Edit Form Fields**.
3. Configure form fields:
   - **First Name** — required
   - **Email** — required
   - **Phone** (optional — collect if your follow-up includes SMS)
4. Set the submit button text to something action-oriented: "Send Me the Checklist" or "Get Instant Access"
5. Click **Save**.

:::{admonition} Why This Matters
:class: tip
Every field you add to a form reduces conversion rate. For a top-of-funnel lead magnet, First Name and Email is the standard minimum. Adding Phone is valuable if you intend to follow up by SMS or call, but expect a 10–20% reduction in form completion rate for each additional required field. Start minimal and add fields later once you've validated the funnel works.
:::

**You'll know you did this right when:** The form shows First Name, Email (and Phone if added), and a clearly labeled submit button. The form is linked to the funnel — not a standalone form.

---

### Step 4: Configure Form Submission Action

1. Click the form in the builder → click **Edit Form Settings**.
2. Under **On Submit**, select **Redirect to URL** or **Redirect to Funnel Step**.
3. Select **Redirect to Funnel Step** → choose **Thank You Page** (the next step you will add in Step 5).
4. Under **Notifications**, enable email notification to yourself so you know when leads come in.
5. Click **Save**.

**You'll know you did this right when:** The form's submission action shows "Redirect to Thank You Page" (or whatever you name the second step).

---

### Step 5: Build the Thank-You Page

1. Back in the funnel steps view, click **+ Add Step**.
2. Name: `Thank You Page` → type: **Funnel Page** → **Create Step**.
3. Click **Edit Page**.
4. Configure:
   - **Headline:** "You're in! Check Your Email." or "Your checklist is on its way!"
   - **Body:** Tell the lead exactly what happens next: "Your [Lead Magnet Name] is headed to your inbox right now. While you wait, here's your next step: [one clear CTA — book a call, watch a video, etc.]"
   - Optional: embed a Calendly or GHL calendar widget for immediate appointment booking
5. Click **Save**.

:::{admonition} Why This Matters
:class: tip
The thank-you page is the most underused conversion opportunity in most funnels. A warm lead who just gave you their email is at peak interest — they just asked for something from you. A well-crafted thank-you page with one clear next step (book a call) converts 15–25% of opt-ins into booked appointments. An empty "thanks, check your email" page converts essentially zero.
:::

---

### Step 6: Connect a Workflow Trigger

1. In the left sidebar, click **Automation → Workflows**.
2. Click **+ New Workflow → Start from Scratch**.
3. Name: `Lab 2 — New Lead Magnet Opt-In` → **Create Workflow**.
4. Click **+ Add New Trigger** → search for **Form Submitted** → select it.
5. In the trigger configuration: **Filters → Form Name → is → [your Lab 2 opt-in form name]**.
6. Click **Save Trigger**.
7. Add Action → **Add Tag** → tag: `lead-magnet-download`.
8. Add Action → **Send Email** → configure a delivery email with your lead magnet PDF attached.
9. Click **Save Action** → toggle the workflow to **Active** → click **Publish**.

**You'll know you did this right when:** The workflow shows "Active" status and the trigger is linked to your specific funnel form.

---

### Step 7: Get the Funnel URL and Test End to End

1. Back in the funnel, click the ⚙️ settings icon for the Opt-In Page step.
2. Set a custom path (URL slug) — e.g., `free-checklist` or `get-started`.
3. If your domain is connected: the full URL becomes `yourdomain.com/free-checklist`.
4. Copy the funnel URL.
5. Open the URL in a new incognito browser window.
6. Complete the form with a test email address (use your own).
7. Verify: you are redirected to the Thank-You page, you receive the delivery email, and a new contact appears in GHL with the `lead-magnet-download` tag applied.

**You'll know you did this right when:** A test submission creates a new contact in your CRM with the tag applied, the delivery email arrives with the lead magnet, and you're redirected to the thank-you page.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 3:

- ☐ Funnel created with two steps: Opt-In Page and Thank-You Page
- ☐ Landing page headline is specific, benefit-focused, and readable on mobile
- ☐ Opt-in form collects First Name and Email (minimum), submit button is clearly labeled
- ☐ Form submission redirects to Thank-You page
- ☐ Thank-You page has a clear next step CTA
- ☐ Workflow created, triggered by form submission, tags new contacts and sends delivery email
- ☐ Workflow is Active/Published
- ☐ Funnel URL is live — test submission creates a contact in GHL with tag applied

You have a live lead generation machine. This funnel will generate contacts and start nurture sequences automatically for every piece of traffic you send to it.
:::

::::{dropdown} Troubleshooting Common Issues

**Form submission doesn't redirect to the thank-you page:**
Verify the form's "On Submit" action is set to "Redirect to Funnel Step" and the thank-you page step is selected. If the form redirects to a blank page or the same page, check the submission action setting in the form builder.

**Test contact was created but the tag wasn't applied:**
The workflow may not have fired. Check that the workflow is Active (not Draft). Verify the trigger filter specifies the correct form name. Open the workflow execution log to see if it triggered and any errors that occurred.

**The delivery email didn't arrive:**
Check your spam folder. Verify the Send Email action in the workflow uses your verified sending domain. If the email sending domain shows "Unverified," return to Lab 0 and complete the email authentication setup.

**The funnel URL shows a 404 error:**
Verify your domain is connected to VibeReach.io (Settings → Domains → should show "Verified"). Check that the funnel step's URL slug doesn't contain spaces or special characters. A fresh domain may need up to 48 hours for DNS propagation.

**The form import template doesn't load:**
If the JSON import fails, build the funnel from scratch using the step-by-step instructions. The template is a convenience — all the same elements are available manually in the builder.

**Mobile preview looks broken:**
All GHL page builder elements are responsive by default, but custom font sizes and manual spacing adjustments can break mobile layout. Use the Mobile Preview button (phone icon in the page builder toolbar) to check after each major edit. Reduce font sizes and column widths for elements that look oversized on mobile.
::::

