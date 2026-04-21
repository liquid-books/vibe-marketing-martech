## 4.13 Lab 4: Build a New-Lead Welcome Workflow

Every new lead who submits your funnel deserves the same excellent first impression — whether they arrive at 9 AM on a Tuesday or 2 AM on a Sunday. A welcome workflow delivers that consistency automatically. In this lab, you build a published, tested workflow that fires the moment a contact submits your Lab 2 funnel form, tags them as a new lead, delivers a warm welcome email, and creates a follow-up task for your team. This is the first real automation in your system — and it runs forever without anyone having to remember to send it.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with your verified sending domain (Lab 0)
- Lab 2 completed — your lead-magnet funnel and opt-in form must exist
- Your lead magnet file (PDF or link) ready to include in the welcome email
- Approximately 20–30 minutes

**Note on SMS:** SMS is the highest-engagement follow-up channel and GHL workflows support it fully. However, sending business SMS requires A2P 10DLC carrier registration (covered in Chapter 5). For this lab, your welcome sequence uses email. Once your A2P registration is approved after Chapter 5, return here and add an SMS action as Step 3B in the sequence.
:::

---

### Step 1: Navigate to the Workflow Builder

1. In the left sidebar, click **Automation** → **Workflows**.
2. Click **+ New Workflow** in the upper right.
3. When prompted, select **Start from Scratch**.
4. In the "Workflow Name" field, type: `New Lead Welcome Sequence`
5. Click **Create Workflow**.

The builder canvas opens with an empty trigger slot at the top of the canvas.

**You'll know you did this right when:** The workflow canvas appears with an empty trigger node labeled "Add Trigger" and a blank canvas below it.

---

### Step 2: Add the Trigger — Form Submitted

1. Click the **+ Add New Trigger** button in the trigger node (or the grey trigger block at the top of the canvas).
2. In the trigger search panel on the right side, type: `Form` → select **Form Submitted** from the results.
3. In the trigger configuration:
   - Click **+ Add Filter**
   - Select **Form Name** → **is** → choose your Lab 2 opt-in form from the dropdown
4. Click **Save Trigger**.

:::{admonition} Why This Matters
:class: tip
The form filter ensures this workflow fires *only* for submissions from your specific Lab 2 form — not from any other form you create later. Without the filter, every form submission on your entire account would trigger this workflow, sending your lead magnet to people who filled out your contact form, your consultation form, or anything else. Always scope your triggers.
:::

**You'll know you did this right when:** The trigger node shows "Form Submitted" with the filter displaying your form's name below it.

---

### Step 3: Action 1 — Add Tag

1. Click **+ Add Action** (the blue + button below the trigger node).
2. In the action search panel, type: `Tag` → select **Add Tag**.
3. In the tag field, type: `new-lead`

   If `new-lead` doesn't exist yet, GHL creates it automatically when the workflow first fires.
4. Click **Save Action**.

:::{admonition} Why This Matters
:class: tip
The `new-lead` tag does two things simultaneously: it marks this contact's lifecycle stage in your CRM (so Smart Lists can filter for new leads), and it serves as a trigger condition for future workflows. If you ever build a re-engagement workflow, you'll want to exclude contacts who already went through onboarding — and the tag history is how you know.
:::

**You'll know you did this right when:** An "Add Tag" node appears on the canvas connected below the trigger, showing `new-lead` as the tag value.

---

### Step 4: Action 2 — Send Email (Welcome + Lead Magnet Delivery)

1. Click **+ Add Action** below the Add Tag node.
2. Search for and select **Send Email**.
3. Configure the email:
   - **Subject:** `Your [Lead Magnet Name] is here, {{contact.first_name}}!`
   - **From Name:** Your name or business name
   - **From Email:** Your verified sending domain address
   - **Reply-To:** Your monitored business email
   - **Body:** Write a short, warm welcome. Example:

> Hi {{contact.first_name}},
>
> Your [Lead Magnet Name] is attached — it's the same checklist we walk through with every client before starting a funding application.
>
> [Attach PDF or link to lead magnet here]
>
> I'll be reaching out personally within the next business hour. If you'd rather connect now, you can grab a time on my calendar here: [calendar link]
>
> Talk soon,
> [Your Name]

4. Attach your lead magnet PDF (or include a link if it's hosted online).
5. Click **Save Action**.

:::{admonition} Why This Matters
:class: tip
The first email a new lead receives sets the tone for the entire relationship. Keep it short — 4–6 sentences maximum. A wall of marketing copy at first contact signals "list blast," not personal attention. The calendar link embedded in the welcome email is how 10–20% of your best leads will self-schedule before you ever reach out. Don't leave it out.
:::

**You'll know you did this right when:** The Send Email node shows your subject line and the email preview renders correctly with the {{contact.first_name}} merge field visible.

---

### Step 5: Action 3 — Create Task (Human Follow-Up Reminder)

1. Click **+ Add Action** below the Send Email node.
2. Search for and select **Create Task**.
3. Configure:
   - **Task Name:** `Follow up with {{contact.first_name}} — new lead`
   - **Due Date:** `1 hour` from workflow execution (use the relative time option)
   - **Assigned To:** Your user account
   - **Notes:** `Lead submitted [Form Name]. Welcome email sent. Next: personal outreach call or text.`
4. Click **Save Action**.

:::{admonition} Why This Matters
:class: tip
Automation handles the immediate response, but the first human contact is still yours to make. The task ensures you don't rely on memory to follow up. It appears in your Tasks list with a 1-hour due date — it's waiting for you when you open GHL, not buried in a spreadsheet or forgotten in a mental note.
:::

**You'll know you did this right when:** A "Create Task" node appears on the canvas, showing the task name with the {{contact.first_name}} merge field and the 1-hour relative due date.

---

### Step 6: Add a Wait Step and Second Email (Optional but Recommended)

For a complete welcome sequence, add a 24-hour follow-up:

1. Click **+ Add Action** below the Create Task node.
2. Select **Wait** → set duration to **1 Day** → toggle "Send during business hours" ON.
3. Click **Save**.
4. Add another **Send Email** action below the Wait:
   - **Subject:** `Quick question for you, {{contact.first_name}}`
   - **Body:** One paragraph, one question about their specific situation. Example: "I wanted to check in — did the checklist I sent answer your questions about funding readiness? What's the biggest challenge you're running into right now?"
5. Save.

**You'll know you did this right when:** The canvas shows: Trigger → Add Tag → Send Email → Create Task → Wait (1 Day) → Send Email. The workflow reads as a linear sequence from top to bottom.

---

### Step 7: Test the Workflow

Before publishing, run a live test:

1. In the workflow builder, click the **Test Workflow** button (or use the "Add Test Contact" option).
2. Select a contact from your database (use yourself or a test contact) → **Run Test**.
3. Verify in the contact's record:
   - The `new-lead` tag was applied
   - The welcome email appears in the contact's email timeline
   - A task was created and appears in the contact's Tasks tab
4. Check your own email inbox to confirm the welcome email arrived.

**You'll know you did this right when:** All three actions show as executed in the contact's activity timeline.

---

### Step 8: Publish the Workflow

1. In the top right of the workflow builder, toggle the workflow status from **Draft** to **Active** (or click the **Publish** button, depending on your GHL version).
2. Confirm the status shows "Published" or "Active" in the workflow list.

**You'll know you did this right when:** The workflow appears in the Workflows list with a green "Active" status indicator. From this point on, every new form submission triggers the entire sequence automatically.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 5:

- ☐ Workflow created: "New Lead Welcome Sequence"
- ☐ Trigger: Form Submitted, filtered to your specific Lab 2 form
- ☐ Action 1: Add Tag → `new-lead` applied immediately on form submission
- ☐ Action 2: Send Email — welcome message with lead magnet delivery
- ☐ Action 3: Create Task — 1-hour follow-up reminder assigned to you
- ☐ Optional: Wait (1 Day) + second follow-up email added
- ☐ Test run executed — all actions confirmed in contact timeline
- ☐ Workflow published / Active status confirmed

You now have a live automation that delivers a consistent, professional first impression for every lead — forever. This workflow runs automatically even when you're away from your desk.
:::

::::{dropdown} Troubleshooting Common Issues

**The workflow triggered but the tag wasn't applied:**
Check the Add Tag action configuration. The tag name must exist or be typed correctly — check for extra spaces. Open the workflow execution log (click the workflow → History tab) to see if the action was attempted and any error message.

**The welcome email didn't arrive in my test:**
Verify the From Email uses your verified sending domain. If the sending domain shows "Unverified" in Settings → Email Services, the email will not send. Also check your spam folder before assuming it didn't send.

**The task was created but has the wrong due date:**
The "1 hour from now" relative time only works for relative time settings. If you accidentally set a specific date and time instead of a relative offset, edit the task action and switch from "Specific Date" to "Relative Time" → set to 1 hour.

**The workflow is Active but never fires when I submit the form:**
The most common cause: the trigger filter specifies a different form than the one you submitted. Check that the form name in the trigger filter exactly matches the name of the form in your funnel. If names contain special characters, try removing them.

**{{contact.first_name}} shows literally in the email instead of the contact's name:**
The merge field is not resolving. Verify the contact record has a First Name value. If First Name is blank on the contact, the merge field returns empty. For the test, use a contact with a populated first name, or add a fallback: {{contact.first_name | default: 'there'}} — which renders as "Hi there" if the field is empty.
::::

