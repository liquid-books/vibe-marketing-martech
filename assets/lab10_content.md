## 10.9 Lab 10: Build Your Automated Review Request System

You cannot collect five-star reviews by hoping happy clients remember to leave them. The businesses with 150+ Google reviews aren't doing anything magic — they have a system that asks every single completed customer at the right moment, every time, without anyone remembering to do it. In this lab, you build that system: a workflow that fires at the 48-hour post-service mark, sends a warm SMS review request, gates out unhappy clients, and follows up once at 5 days for non-responders. By the end, this runs in the background permanently — generating new reviews while you sleep.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- Google Business Profile connected to GHL (see Step 1 if not yet connected)
- A provisioned GHL phone number with A2P 10DLC registration approved (from Chapter 5) — SMS is required for the highest review request conversion rates
- A "Completed" or "Closed Won" stage in your primary sales pipeline
- Approximately 25–35 minutes
:::

---

### Step 1: Connect Google Business Profile

If you have not yet connected Google Business Profile to GHL:

1. In the left sidebar, click **Reputation**.
2. Click the **Settings** tab → **Integrations** → **Google Business Profile**.
3. Click **Connect Google Account** → authorize with the Google account that manages your GBP listing.
4. In the location picker, select your business location → **Connect**.
5. Click the **Reviews** tab — your existing Google reviews should load.

**You'll know you did this right when:** The Reviews tab in Reputation shows your existing Google reviews with star ratings and timestamps.

:::{admonition} Why This Matters
:class: tip
The GBP connection does two things: it pulls your existing reviews into GHL's dashboard for centralized monitoring and AI-assisted responses, and it provides the `{{review.link}}` merge field used in review request messages. Without this connection, the merge field returns empty — your SMS includes a dead link.
:::

---

### Step 2: Create Your Review Request SMS Template

1. In the left sidebar, click **Reputation** → **Requests** tab.
2. Click **+ New Request Template** (or **+ New Template** depending on your GHL version).
3. Configure:
   - **Template Name:** `Post-Service Review Request — SMS`
   - **Channel:** SMS
   - **Review Platform:** Google
4. In the message body, write your review request. Keep it warm, personal, and under 160 characters where possible:

   > Hi {{contact.first_name}}, working with you was a pleasure! If you have 60 seconds, a Google review helps others find us and means the world to our team: {{review.link}}

5. Click **Save Template**.

**You'll know you did this right when:** The template appears in your Request Templates list with the SMS icon and your message body visible.

---

### Step 3: Build the Review Request Automation Workflow

1. **Automation → Workflows → + New Workflow → Start from Scratch**
2. **Workflow Name:** `Review Request — Post-Service Automation`
3. Click **+ Add New Trigger** → search for `Opportunity` → select **Opportunity Stage Changed**.
4. In the trigger configuration:
   - **Pipeline:** Select your primary sales pipeline
   - **New Stage:** Select `Completed` (or `Closed Won`, whichever is your final successful stage)
5. Click **Save Trigger**.

**You'll know you did this right when:** The trigger node shows "Opportunity Stage Changed" with your pipeline name and final stage specified.

---

### Step 4: Add the Wait Step (48-Hour Delay)

1. Click **+ Add Action** below the trigger.
2. Select **Wait** from the action picker.
3. Configure:
   - **Duration:** 2 Days
   - **Send only during:** Toggle ON "Business Hours Only" (prevents sending at 3 AM)
   - **Business days only:** Toggle ON (optional — prevents weekend sends if your customers prefer weekdays)
4. Click **Save Action**.

:::{admonition} Why This Matters
:class: tip
The 48-hour window is the sweet spot for review requests. Immediately after service, the client is transitioning — they haven't fully processed the experience yet. At 48 hours, the experience is recent and the initial relief or satisfaction has settled into a clear opinion. Waiting a week or more drops conversion significantly because the emotional resonance fades.
:::

**You'll know you did this right when:** A Wait node showing "2 Days - Business Hours" appears on the canvas.

---

### Step 5: Add the Complaint Gate (If/Else Branch)

Before sending any review request, check that this contact doesn't have an active complaint:

1. Click **+ Add Action** → select **If/Else**.
2. Configure the condition:
   - **Condition:** Contact Tags → **does not contain** → `complaint-active`
3. Click **Save**.

This creates two branches:
- **YES (passes the gate — no complaint tag):** Continue to send the review request
- **NO (has complaint tag):** Route to **End Workflow**

4. On the "NO" branch, add an **End Workflow** action.

:::{admonition} Why This Matters
:class: tip
Sending a review request to a client who complained is the fastest way to get a public one-star review. The If/Else gate is how you protect your reputation from the inside. Your team simply applies the `complaint-active` tag to any contact who had an issue, and the automation routes around them permanently. No angry clients ever receive a review request.
:::

**You'll know you did this right when:** The canvas shows a branching path — the "YES" path continues forward, the "NO" path routes to End Workflow.

---

### Step 6: Send the Review Request (On the YES Branch)

On the YES branch after the If/Else:

1. Click **+ Add Action** → search for **Send Review Request** (may also appear as "Reputation → Review Request" in the action categories).
2. Select your `Post-Service Review Request — SMS` template.
3. Click **Save Action**.

Then add a tag:
4. Click **+ Add Action** → **Add Tag** → `review-request-sent`
5. Click **Save**.

**You'll know you did this right when:** The YES branch shows: Send Review Request → Add Tag (review-request-sent).

---

### Step 7: Add the 5-Day Follow-Up Sequence

After the Send Review Request node (still on the YES branch):

1. Add **Wait** → **5 Days** → business hours only.
2. Add another **If/Else**:
   - **Condition:** Contact Tags → **does not contain** → `review-received`
   - YES (no review yet): send follow-up
   - NO (review received): End Workflow
3. On the YES branch, add **Send SMS** (or Send Review Request again with a different template):
   - **Message:** "Hi {{contact.first_name}}, just a quick follow-up in case my message got buried! If you have a moment, here's that Google review link: {{review.link}} — Thank you so much, it means a lot to us! 🙏"
4. Add **End Workflow** at the bottom.

:::{admonition} Why This Matters
:class: tip
One follow-up doubles your review collection rate compared to a single ask. Two follow-ups does not double it again — three requests feels like harassment. One thoughtful follow-up with an apologetic tone ("in case my message got buried") comes across as human, not automated, and converts clients who missed the first message without annoying those who received it.
:::

**You'll know you did this right when:** The workflow canvas shows the complete two-request sequence with the `review-received` gate protecting against double-requesting clients who already left a review.

---

### Step 8: Test and Publish

**Test the workflow:**
1. Open a test contact in your CRM.
2. Create an opportunity for that contact in your sales pipeline.
3. Manually move the opportunity to your "Completed" stage.
4. Verify the workflow triggers (check the contact's workflow history or the Automation → Workflows → History log).
5. Since the Wait step is 2 days, use the "Skip Wait" option if available in the workflow tester, or temporarily change Wait to 1 minute for testing purposes.

**Publish:**
1. Toggle the workflow to **Active** → **Publish**.
2. Reset the Wait steps back to 2 Days and 5 Days after testing.

**You'll know you did this right when:** The workflow shows "Active" status. A test contact moving to "Completed" in the pipeline triggers the workflow execution log.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 11:

- ☐ Google Business Profile connected — Reviews tab shows existing reviews
- ☐ Review request SMS template created with {{contact.first_name}} and {{review.link}} merge fields
- ☐ Workflow trigger: Opportunity Stage Changed to "Completed" in primary pipeline
- ☐ 48-hour Wait configured with business-hours restriction
- ☐ Complaint gate If/Else — `complaint-active` tag routes to End Workflow
- ☐ Send Review Request action using your template
- ☐ `review-request-sent` tag applied after send
- ☐ 5-day follow-up with `review-received` gate
- ☐ Workflow Active/Published

Your review engine is live. Every completed client now receives a perfectly timed, warm review request automatically. You will collect more reviews in the next 30 days than most businesses collect in a year.
:::

::::{dropdown} Troubleshooting Common Issues

**{{review.link}} returns empty in the SMS:**
Your Google Business Profile is not connected. Return to Reputation → Settings → Integrations and verify the GBP connection shows green. If connected but the merge field still fails, disconnect and reconnect the GBP account, then re-save the template.

**The workflow trigger doesn't fire when I move the opportunity stage:**
The trigger requires the opportunity to have a pipeline AND the new stage to match exactly. Check that you are moving the opportunity in the same pipeline specified in the trigger filter. If the pipeline has been renamed since the workflow was built, the filter may no longer match.

**Review request SMS isn't sending even though workflow shows executed:**
A2P 10DLC registration must be approved for outbound SMS. If not yet approved, the SMS action will fail silently. Check Settings → Phone System → A2P Registration for approval status. As a temporary workaround, change the template channel to Email until A2P is approved.

**Clients are complaining they received a review request after a dispute:**
Someone on your team is not applying the `complaint-active` tag before moving the opportunity to Completed. Create a standard operating procedure: any client with a complaint gets the `complaint-active` tag applied *before* the opportunity is moved to the final stage. Consider adding a mandatory team training note in the Stage description in Settings → Pipelines.

**The 5-day follow-up fires even for clients who left a review:**
The `review-received` tag must be applied when a review is received. GHL can apply this tag automatically when a new review is detected through the Reputation module — check Reputation → Settings for automatic tag options. Alternatively, your team can manually apply the tag when a review notification arrives.
::::

