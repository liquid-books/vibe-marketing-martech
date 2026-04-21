## 11.8 Lab 11: Build Your Business Command Center Dashboard

A business running on gut feelings and monthly PDF reports is flying blind. The businesses that grow fastest have one thing in common: they look at the same five numbers every single morning and make decisions based on what those numbers say. In this lab, you build a custom GHL reporting dashboard that shows your five most important business metrics at a glance — updated in real time — and generates a shareable link for your team or clients. By the end, you have a daily morning ritual dashboard you can check in 90 seconds and know exactly where your business stands.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with at least 30 days of activity (contacts, calls, or appointments) — some widgets will show zero if the account is brand new, which is expected
- Admin-level access (needed to create dashboards and access all report types)
- Approximately 20–30 minutes
:::

---

### Step 1: Navigate to the Reporting Dashboard Builder

1. In the left sidebar, click **Reporting**.
2. You land on the default Overview Dashboard. To create your custom dashboard:
   - Click the **Dashboards** dropdown (or tab) at the top of the Reporting section
   - Click **+ New Dashboard**
3. Enter the dashboard name: `Business Command Center — [Your Business Name]`
4. Click **Create Dashboard**.

The dashboard builder opens with an empty canvas.

**You'll know you did this right when:** A blank dashboard canvas appears with a "+ Add Widget" button in the upper right or center of the canvas.

---

### Step 2: Add Widget 1 — Contact Acquisition (Where Are My Leads Coming From?)

1. Click **+ Add Widget**.
2. Browse the widget library → select **Contact Summary** (or "Contacts" widget).
3. Configure:
   - **Metric:** New Contacts Added
   - **Date Range:** Last 30 Days
   - **Group By / Breakdown:** First Attribution Source
4. Click **Apply** or **Save Widget**.
5. On the canvas, drag the widget to the top-left position → resize to full-width by dragging its corner.

**You'll know you did this right when:** The Contact Acquisition widget shows a bar chart or list of lead sources with contact counts for the last 30 days.

:::{admonition} Why This Matters
:class: tip
This widget answers the most important marketing question: where are my leads actually coming from? Businesses that believe Facebook is their top source often discover in this widget that organic Google is generating more contacts than paid ads. Let the data challenge your assumptions — then adjust your budget accordingly.
:::

---

### Step 3: Add Widget 2 — Pipeline Revenue (How Much Money Is In Progress?)

1. **+ Add Widget** → select **Pipeline Value** or **Opportunities Summary**.
2. Configure:
   - **Pipeline:** Your primary Sales pipeline
   - **View:** Value by Stage (shows dollar amount in each stage)
   - **Date Range:** Current Period (or All Time, depending on your GHL version)
3. Save the widget → drag to the top-right position on the canvas.

**You'll know you did this right when:** The Pipeline widget shows each pipeline stage with the total dollar value of opportunities in that stage. If values show $0, verify that your opportunities have dollar values entered.

---

### Step 4: Add Widget 3 — Call Performance (Are We Capturing Every Lead?)

1. **+ Add Widget** → select **Call Summary** or **Phone / Call Performance**.
2. Configure:
   - **Metrics:** Inbound Calls Answered, Inbound Calls Missed, Answer Rate (%)
   - **Date Range:** Last 30 Days
   - **Filter:** All phone numbers (or select specific number)
3. Save → drag to the middle-left position.

:::{admonition} Why This Matters
:class: tip
Your call answer rate is a direct measure of missed revenue opportunities. If your answer rate is 70%, 30% of every inbound call — people who were ready to ask about your service — got no response from you. Each percentage point of answer rate improvement is a direct revenue increase. This widget makes the problem visible so you can solve it.
:::

**You'll know you did this right when:** The widget shows three distinct metrics: total inbound calls, answered calls, and missed calls, with an answer rate percentage.

---

### Step 5: Add Widget 4 — Appointment Funnel (Are Booked Appointments Actually Happening?)

1. **+ Add Widget** → select **Appointment Summary** or **Appointments**.
2. Configure:
   - **Metrics:** Appointments Booked, Attended, No-Show Rate (%)
   - **Date Range:** Last 30 Days
   - **Calendar:** Your primary consultation calendar
3. Save → drag to the middle-right position.

**You'll know you did this right when:** The widget shows booked appointments alongside attended appointments and a no-show rate percentage.

---

### Step 6: Add Widget 5 — Reputation (How Do We Look Today?)

1. **+ Add Widget** → select **Review Summary** or **Reputation**.
2. Configure:
   - **Metrics:** Average Star Rating, Total Reviews, Reviews This Month
   - **Platform:** Google (select from dropdown)
3. Save → drag to the bottom of the dashboard.

**You'll know you did this right when:** The widget shows your current Google star rating (e.g., 4.8 ★), total review count, and reviews added this month.

---

### Step 7: Add Widget 6 — Conversation Response Time (How Fast Is Your Team Responding?)

1. **+ Add Widget** → select **Conversation Summary** or **Inbox Activity**.
2. Configure:
   - **Metric:** Average First Response Time
   - **Date Range:** Last 30 Days
3. Save → add to the dashboard.

:::{admonition} Why This Matters
:class: tip
Speed to lead is one of the highest-impact conversion levers in sales. A lead who receives a response within 5 minutes is 21× more likely to convert than one who waits 30 minutes. This widget shows your team's actual average response time — not what you think it is, but what the data says it is. Most businesses that add this widget are surprised by the gap between their assumed and actual response times.
:::

---

### Step 8: Arrange, Save, and Generate the Share Link

1. Rearrange widgets by dragging them into your preferred layout:
   - Top row: Contact Acquisition (full width)
   - Second row: Pipeline Revenue (left) + Call Performance (right)
   - Third row: Appointment Funnel (left) + Reputation (right)
   - Bottom: Conversation Response Time
2. Click **Save Dashboard** (or it auto-saves — confirm by looking for a save confirmation).
3. Click **Share** (or the share icon, usually at the top of the dashboard) → **Get Read-Only Link**.
4. Copy the link.
5. Bookmark the link in your browser for daily use.
6. Share the link with your team members who need visibility into these metrics.

**You'll know you did this right when:** The shared link opens the dashboard in a browser without requiring a GHL login — it's read-only and can be bookmarked or shared without exposing account access.

---

### Step 9: Run the Morning Dashboard Ritual

This 90-second ritual replaces every "how are we doing?" conversation with actual data:

**Every morning, open your dashboard and check:**

1. **Contact Acquisition:** Did we add leads yesterday? Are sources performing as expected?
2. **Pipeline Revenue:** Any stuck deals (no movement in 7+ days)?
3. **Call Performance:** Was yesterday's answer rate above 80%? If below, why?
4. **Appointment Funnel:** Is the no-show rate above 15%? If yes, reminder workflow needs attention.
5. **Reputation:** Did any new reviews come in? Do any need a response?

If a number surprises you, drill down. If everything looks normal, move on. The ritual takes 90 seconds when the dashboard is built correctly.

**You'll know you did this right when:** You can describe what each widget shows and name one actionable decision each widget informs for your business.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 12:

- ☐ Custom dashboard created and named
- ☐ Contact Acquisition widget — shows last 30 days with attribution source breakdown
- ☐ Pipeline Revenue widget — shows dollar value by stage in your Sales pipeline
- ☐ Call Performance widget — shows answer rate and missed call count
- ☐ Appointment Funnel widget — shows no-show rate
- ☐ Reputation widget — shows current star rating and review count
- ☐ Conversation Response Time widget — shows average first response time
- ☐ Dashboard saved and arranged logically
- ☐ Read-only share link generated and bookmarked
- ☐ You can describe the 5-item morning dashboard ritual

You have a command center for your business. The guessing is over.
:::

::::{dropdown} Troubleshooting Common Issues

**Widgets show zero values even though I have data in my account:**
Check the date range setting on each widget. A widget set to "Today" will show zero if no activity occurred today. Change to "Last 30 Days" or "All Time" to verify data exists. Also confirm the filters match your actual data — a Pipeline widget filtered to a pipeline with no opportunities shows zero.

**"+ Add Widget" doesn't show the widget types I expect:**
The widget library varies by GHL plan tier. Some advanced widget types (Attribution breakdown, Conversation analytics) require higher-tier plans. If a specific widget type isn't available, use the closest available alternative.

**I can't find "Get Read-Only Link" or "Share Dashboard":**
The share feature may appear as a share icon (person with + symbol) in the dashboard header. If not visible, check that you're viewing the custom dashboard you created (not the default Overview Dashboard) — the default dashboard may not have sharing enabled.

**The share link requires a GHL login:**
Read-only dashboard links should work without login. If the link redirects to a login page, the dashboard may be set to "Private." Check the dashboard settings (click the three-dot menu on the dashboard) for a visibility or sharing setting.

**Pipeline Revenue shows wrong values:**
Verify that opportunities have dollar values entered (an opportunity with $0 or blank value contributes $0 to pipeline totals). Check the pipeline filter in the widget configuration — it must match the pipeline where your real opportunities live.

**Call Performance widget shows no data:**
Call reporting requires that calls flow through your GHL phone number (not a forwarded external number). Confirm your team is using the GHL app or GHL phone system for calls, not personal cell phones that aren't tracked.
::::

