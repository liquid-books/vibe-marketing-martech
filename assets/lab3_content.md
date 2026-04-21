## 3.10 Lab 3: Design a Three-Pipeline Structure for Your Own Business

A pipeline without stages is just a list of names. A pipeline with the right stages is a decision-support system — it tells you at a glance where every deal stands, what action is needed, and which opportunities are stalling. In this lab, you build three distinct pipelines for your business: a Sales pipeline (converting leads to closed clients), an Onboarding pipeline (delivering your service), and a Renewal pipeline (protecting long-term revenue). Together, they give you complete revenue visibility from first contact through retention.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- A clear understanding of your business's sales process (the steps a lead goes through from first inquiry to paying client)
- A service or product that involves an ongoing client relationship (not required, but Renewal pipeline is most relevant if you have recurring clients)
- Approximately 30–45 minutes

📥 **[Download lab03-pipeline-planning-worksheet.pdf](https://raw.githubusercontent.com/liquid-books/vibe-marketing-martech/main/assets/lab03-pipeline-planning-worksheet.pdf)**

Complete the worksheet before building. It guides you through mapping your stages before clicking a single button.
:::

---

### Step 1: Plan Your Pipelines on Paper (Before You Build)

Before touching the platform, spend 10 minutes on the worksheet:

**Sales Pipeline:** List the stages a new lead moves through from first contact to closed/won. Common stages: `New Lead → Contacted → Qualified → Proposal Sent → Negotiation → Closed Won / Closed Lost`

**Onboarding Pipeline:** List the steps after someone becomes a client. Common stages: `Contract Signed → Kickoff Scheduled → Setup In Progress → Delivered → Review Requested → Complete`

**Renewal Pipeline:** List the stages for renewing or retaining existing clients. Common stages: `Active Client → Renewal Due (60 days) → Renewal Sent → Renewal Accepted → Churned`

Identify for each stage: what action moves a contact from this stage to the next one?

:::{admonition} Why This Matters
:class: tip
Building a pipeline without planning first leads to stages that don't reflect how your business actually works — meaning your team won't use them. The 10-minute planning exercise prevents rebuilding the pipeline three times.
:::

---

### Step 2: Create Your Sales Pipeline

1. In the left sidebar, click **Opportunities** (or **CRM → Opportunities**, depending on your GHL version).
2. Click **+ Add Pipeline** or the **Pipelines** tab → **+ New Pipeline**.
3. **Pipeline Name:** `[Your Business Name] — Sales`
4. Click **Create Pipeline**.

**You'll know you did this right when:** A new pipeline appears in the Pipelines list and you are taken to the stage configuration view.

---

### Step 3: Add Stages to Your Sales Pipeline

You are now in the pipeline stage builder. Add each stage you identified in Step 1:

1. Click **+ Add Stage**.
2. Enter the stage name → click **Save**.
3. Repeat for each stage.

For the standard sales pipeline:
- `New Lead`
- `Contacted`
- `Qualified`
- `Proposal Sent`
- `Negotiation`
- `Closed Won` *(mark this as a Won stage in the dropdown)*
- `Closed Lost` *(mark this as a Lost stage in the dropdown)*

For each stage, set the **Win Probability %** — this feeds your pipeline revenue forecast. Example: New Lead = 5%, Qualified = 30%, Proposal Sent = 60%, Negotiation = 80%.

Click **Save Pipeline**.

:::{admonition} Why This Matters
:class: tip
Win probability percentages let GHL calculate your expected revenue at any moment. If you have $50,000 in opportunities at "Proposal Sent" (60% probability) and $20,000 at "New Lead" (5% probability), your expected pipeline value is $31,000. That number drives decisions about whether you need more deals in the pipeline or better closing rates.
:::

**You'll know you did this right when:** The pipeline shows all your stages in the correct order, and Closed Won / Closed Lost are marked with the appropriate outcome type.

---

### Step 4: Create Your Onboarding Pipeline

1. Click **+ New Pipeline** (or return to the Pipelines list → **+ Add Pipeline**).
2. **Pipeline Name:** `[Your Business Name] — Onboarding`
3. Add your onboarding stages:
   - `Contract Signed`
   - `Kickoff Scheduled`
   - `Setup In Progress`
   - `Delivered / Live`
   - `Review Requested`
   - `Complete`
4. Click **Save Pipeline**.

:::{admonition} Why This Matters
:class: tip
Most businesses track sales in a pipeline but abandon pipeline tracking the moment a client signs. This creates an invisible bottleneck — late deliveries, missed kickoffs, and forgotten deliverables that cause churn. An Onboarding pipeline makes every in-progress client visible. When a client is stuck in "Setup In Progress" for three weeks, you see it and can act before they send a frustrated email.
:::

**You'll know you did this right when:** A second pipeline appears in your Pipelines list with its own set of stages. It is completely separate from the Sales pipeline.

---

### Step 5: Create Your Renewal Pipeline

1. **+ New Pipeline** → **Pipeline Name:** `[Your Business Name] — Renewals`
2. Add stages:
   - `Active Client`
   - `Renewal Due — 60 Days`
   - `Renewal Sent`
   - `Renewal Accepted` *(mark as Won)*
   - `Churned` *(mark as Lost)*
3. **Save Pipeline**.

**You'll know you did this right when:** A third pipeline exists in your list. All three pipelines (Sales, Onboarding, Renewals) are visible and distinct.

---

### Step 6: Create Your First Opportunity

Now populate your Sales pipeline with a real (or practice) deal:

1. Click into your **Sales pipeline** → click **+ Add Opportunity** (or **+ New Opportunity**).
2. Configure:
   - **Opportunity Name:** `[Contact Name] — [Service]` (e.g., "Rivera Roofing — Marketing Retainer")
   - **Contact:** Search for and select a contact from your imported Lab 1 contacts
   - **Pipeline:** Sales pipeline
   - **Stage:** `New Lead`
   - **Value:** Enter the estimated deal value in dollars
   - **Assigned To:** Yourself
3. Click **Save**.

**You'll know you did this right when:** The opportunity appears in the Kanban board view under the "New Lead" column with the contact name, value, and your name as assigned.

---

### Step 7: Practice Moving Opportunities and Run the Morning Ritual

1. Click the opportunity card you just created → drag it to the **Contacted** stage.
2. Add a note: "Initial call completed — prospect is interested in retainer."
3. Create a task: "Send proposal by [date]" with a due date.
4. Click **Save**.

**The Morning Stand-Up Ritual:** Every business day, open your Opportunities board and scan for:
- Anything in "New Lead" for more than 24 hours with no activity
- Anything in "Proposal Sent" for more than 7 days with no movement
- Anything in "Negotiation" with a close date in the past

These three checks — 2 minutes total — are how you prevent deals from dying quietly in a stage with no follow-up.

:::{admonition} Why This Matters
:class: tip
The pipeline is not a trophy case — it's a task manager. The morning ritual turns the pipeline from a reporting tool into an action trigger. Every stalled deal you catch in the morning ritual is one that doesn't fall through the cracks by end of week.
:::

**You'll know you did this right when:** The opportunity has a note, a task, and shows the updated stage. The Kanban board shows at least one card in a stage beyond "New Lead."

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 4:

- ☐ Sales pipeline created with stages from New Lead through Closed Won/Lost
- ☐ Win probability % set for each stage
- ☐ Onboarding pipeline created with post-signature stages
- ☐ Renewal pipeline created with retention-focused stages
- ☐ At least one opportunity created in the Sales pipeline
- ☐ Opportunity has a note and a task with a due date
- ☐ You can describe the morning stand-up ritual (what you check, why, how often)

You now have a complete revenue operations structure. Every contact you generate through Lab 2's funnel can flow into an opportunity in this pipeline.
:::

::::{dropdown} Troubleshooting Common Issues

**"+ New Pipeline" button is not visible:**
Check that you are in the Opportunities section of the left sidebar (not Contacts or Conversations). Some GHL accounts organize this under CRM → Pipelines. If you're using the mobile app, switch to desktop browser for pipeline configuration.

**Stages are saving but showing in the wrong order:**
GHL allows you to drag and reorder stages in the pipeline builder. After adding all stages, drag them into the correct sequence before saving. If order is wrong after save, click the edit (pencil) icon next to the pipeline and drag to reorder.

**Win probability percentages aren't appearing:**
Win probability is set per stage in the stage configuration. Click the stage name to expand its settings and look for "Win Probability" or "Stage Probability." This field may be labeled differently depending on your GHL version.

**An opportunity isn't showing the pipeline value in reports:**
The opportunity must have a numeric Value entered. Opportunities with a $0 value or no value entered are excluded from pipeline revenue calculations. Edit the opportunity and enter the estimated deal value.

**The pipeline shows in "List View" but I want the Kanban board:**
In the Opportunities view, look for a View toggle (usually top-right) with icons for List, Kanban, and sometimes Calendar. Click the Kanban icon (grid of squares) to switch to the board view where deals appear as draggable cards.
::::

