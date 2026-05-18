# Reporting and Analytics — Measuring What You Built in VibeReach

*Part eight of the curriculum. You've built a complete system — funnel, forms, pipeline, workflows, calendars, conversations, documents, and AI Employees. The system is running. Now the question is: how do you actually know if it's working? Which parts are performing? Where are leads dropping off? Which marketing source is producing closed deals versus tire-kickers? This tutorial walks through VibeReach's reporting and analytics tools — the dashboards, the attribution model, the source reports, the custom widgets — and (more importantly) which metrics actually matter versus which ones just look impressive on a screen.*

---

## What This Tutorial Assumes

The same seven pieces as before, but reporting is special because it depends on data that comes from *every* prior tutorial:

- **Funnel** produces page view counts and step conversion rates.
- **Forms/Surveys** produces completion rates and field-level drop-off data.
- **Pipeline** produces opportunity counts, stage velocity, win rate, and pipeline value.
- **Workflow** produces email and SMS open/click rates, automation completion rates.
- **Calendars** produces booking rates, show rates, and no-show rates.
- **Conversations** produces response times and message volume by channel.
- **Documents** produces send-to-sign rates and average time-to-close.
- **AI Employees** produces deflection rates (how often AI resolves a conversation without human handoff) and cost-per-interaction.

If you haven't built the prior systems, the reporting will be empty. Reporting reports on reality. It's not a fix for not having a business — it's a lens for seeing the business you have.

---

## The First Important Distinction: Vanity Metrics vs. Revenue Metrics

Most people approach reporting wrong. They open the dashboard, see big numbers, feel good, close the dashboard. Those big numbers — total page views, total leads in the system, total emails sent — are vanity metrics. They look impressive. They don't pay the bills.

The metrics that actually matter are the ones that connect activity to revenue. There are roughly four of them:

**1. Lead-to-Customer Conversion Rate.** Out of every 100 leads who entered the system, how many became paying customers? This is the master KPI. A 5% rate is normal for cold traffic in many service businesses. A 15-25% rate is excellent. Below 2% means something earlier in the funnel is broken.

**2. Pipeline Velocity.** How many days, on average, does it take a lead to move from New Lead all the way to Won? Sometimes broken down by stage — *days in New Lead, days in Call Booked, days in Proposal Sent.* Slow stages are bottlenecks. Stages that have been getting slower over time are leading indicators of a problem.

**3. Pipeline Value (and Forecasted Revenue).** Total dollar value of every open opportunity weighted by stage probability. The pipeline editor lets you set a probability percentage per stage (e.g., New Lead = 10%, Call Booked = 30%, Proposal Sent = 60%). Multiply each opportunity's deal value by its stage probability and sum — that's your forecasted close revenue for the period.

**4. Source ROI.** For every marketing source (Google search, Facebook ad, LinkedIn post, referral, etc.), what's the ratio of dollars in to dollars out? Some sources produce expensive leads that convert at high rates; some produce cheap leads that never close. Knowing the difference is what separates profitable marketing from a money pit.

Everything else in the dashboards is supporting data. Useful for diagnosis when one of these four moves the wrong direction. Not the thing to stare at every day.

---

## The Main Dashboard — Your Daily Glance

Navigate to **Dashboard** in the left navigation. This is the command center — the page you should open every morning for 60 seconds before doing anything else.

The default dashboard ships with several widgets. The ones worth your attention:

**Opportunities.** Total count and total dollar value of open deals in your pipeline(s), broken down by stage. Quick gut check: is the pipeline growing or shrinking week over week? If it's shrinking, your lead generation isn't keeping pace with deal close velocity.

**Pipeline Value.** Total potential revenue currently in flight. Useful for forecasting and for the obvious psychological boost of seeing a six-figure number when your pipeline is healthy.

**Stage Distribution.** A visual breakdown of where your opportunities sit. Healthy distribution: opportunities spread across all stages, with the most volume in early stages (New Lead, Call Booked) tapering down to fewer in late stages (Proposal Sent, Won/Lost). Unhealthy distribution: most opportunities stuck in one middle stage (a bottleneck), or no opportunities in early stages (you stopped feeding the funnel).

**Funnel Conversion Rate.** Step-by-step conversion through your published funnels. This is where you spot leaks. If the survey page from Funnel Part 2 has a 60% drop-off, you have a real problem there — too many fields, too long, wrong tone, broken something.

**Recent Conversations / Recent Bookings.** Quick views into the past 24-48 hours of activity. Less for analysis, more for "did anything happen overnight I need to act on?"

### Customizing the Dashboard

Click **Add Widget** in the top right (or **Edit Dashboard** depending on UI version). You can add, remove, and rearrange widgets based on what matters to your business.

What I recommend adding for the curriculum scenario:

- **Leads by Source** — bar chart of contacts created per source over the last 30 days
- **Appointments Booked vs. Showed Up vs. No-Showed** — your calendar performance
- **Average Days in Stage** — your pipeline velocity by stage
- **Email Open & Click Rates** — workflow performance

What I recommend removing:

- Anything showing "total page views" without conversion context
- Total contact count (it only ever goes up; the number doesn't tell you anything actionable)
- "AI messages sent" volume metrics (volume isn't the win condition; deflection is)

The dashboard should answer one question fast: *what changed this week, and does anything need my attention?* If a widget doesn't help you answer that, it shouldn't be on the dashboard.

---

## The Attribution Report — The Most Important Report in VibeReach

Click **Reporting** in the left navigation, then **Attribution.** This is the report most people don't fully use, and it's arguably the single most valuable thing the platform produces.

Attribution answers the question: where did this lead come from, and what did they cost you to acquire?

### First Attribution vs. Latest Attribution

VibeReach stores two attribution records on every contact:

**First Attribution** — the first time this contact ever interacted with your system. The very first session that resulted in them becoming a contact. Source, medium, campaign, content — captured at the moment of first contact.

**Latest Attribution** — the most recent session where this contact interacted with you. Every new session updates this record. If they came in originally from Google search and later clicked a Facebook ad, the Latest Attribution shows Facebook.

Both records are always stored. Which one to focus on depends on what you're trying to optimize:

- **First Attribution** is right for measuring which channels *create* leads. If you want to know whether your Google Ads are bringing in net-new prospects, use First Attribution.
- **Latest Attribution** is right for measuring which channels *close* deals. If you want to know which final-touch channel pushes warm prospects over the line, use Latest Attribution.

Most attribution debates between marketing teams and sales teams come from people looking at different records and not realizing they're measuring different questions. Now you know which is which.

### Source Reports

Below the Attribution report there's a Source Reports section. This shows, for every source (utm_source value, referrer, direct, organic, etc.), how many contacts came from it, how many became opportunities, how many became customers, and total revenue closed. Read this as: *"For every 100 leads I got from Google Ads, X became opportunities, Y closed, generating $Z revenue."*

If you've been running paid ads without this report open, you've been guessing. Now you can actually see ROI per source.

---

## UTM Parameters — The Discipline That Makes Attribution Work

Attribution is only as good as the data you feed it. The mechanism for feeding it good data is **UTM parameters** — query strings appended to your campaign URLs that tell VibeReach where the click came from.

A standard UTM-tagged URL looks like this:

```
https://yourdomain.com/funnel-page?utm_source=linkedin&utm_medium=organic&utm_campaign=may-newsletter&utm_content=hero-cta
```

Five UTM parameters matter:

- **utm_source** — the platform (linkedin, google, facebook, mailchimp, instagram)
- **utm_medium** — the type of channel (organic, cpc, email, social, referral)
- **utm_campaign** — the specific campaign name (spring-launch, q2-webinar, weekly-newsletter)
- **utm_content** — the specific creative or placement (hero-cta, sidebar-ad, footer-link)
- **utm_term** — paid search keyword (optional, mainly for Google Ads)

### The Naming Convention Problem

Every UTM-tagging system fails the same way: inconsistent naming. Half the team writes `utm_source=facebook` and the other half writes `utm_source=Facebook` (capitalized) — and now your reports show "Facebook" and "facebook" as two separate sources, splitting the data. Or someone uses `utm_source=fb` once and never again.

Solve this on day one:

- All UTM values lowercase, always
- Use hyphens, not underscores or spaces (`spring-launch` not `Spring_Launch`)
- Maintain a small spreadsheet (or just a notes file) listing every utm_source, utm_medium, and utm_campaign you've ever used
- Before adding a new utm_campaign, check the spreadsheet to make sure it's not a near-duplicate of an existing one

This sounds obsessive. It's the difference between attribution reports you can trust and attribution reports that are 30% garbage.

### Building UTM URLs

You can build UTM URLs manually, but use a generator to avoid typos. Google's free Campaign URL Builder (search "Google campaign URL builder") generates them clean. Bookmark it.

Then: every link you put anywhere — every email link in a workflow, every social post, every paid ad, every QR code, every podcast show notes — gets UTMs. The few minutes per link is what makes attribution work.

---

## Sites and Funnel Analytics — Asset-Level Performance

Navigate to **Sites → Analytics tab** (depending on UI version, this may be at **Funnels → Stats** or under a Site Analytics menu). This is the asset-level performance view.

At the top, choose an **asset type:**

- Funnels
- Websites
- Blogs
- Webinars
- Forms
- Surveys
- QR Codes
- External Tracking (sites where you've installed the VibeReach tracking script)

The metrics shown change based on what you select. For Funnels, you see total visits, unique visitors, conversion rate per step, and the funnel chart that visually shows drop-off between steps. For Forms, you see submissions, completion rate, and field-level abandonment. For Surveys, you see completion rate, average time spent, and per-question drop-off.

Then choose a **specific asset** (or leave on "All") and a **date range** (last 7 days, last 30 days, custom range, comparison to prior period).

### The Funnel Drop-Off View

This is the most diagnostic single view in the platform. Open Sites → Analytics → select Funnels → select your specific funnel from Tutorial 1. You'll see a visual representation of each step in your funnel with conversion rates between steps.

Reading the funnel:

- **Step 1 (landing page) → Step 2 (survey).** If only 20% of visitors progress, your landing page or CTA isn't strong enough. The hook isn't landing.
- **Step 2 (survey) → Step 3 (calendar).** If only 30% of people who start the survey complete it, the survey is too long, the questions feel off, or one specific question is the dealbreaker. Drill into the per-question drop-off to find the offender.
- **Step 3 (calendar) → completed booking.** If 80% of survey completers reach the calendar but only 40% actually book, the calendar UX is broken or the available times are bad.

Each leak is a hypothesis. Each fix is something to test. *"I changed the headline on Step 1 — did the Step 1 → Step 2 conversion rate go up?"* That's data-driven optimization. You can't do it without the analytics view open.

---

## Pipeline Reporting — Where Deals Actually Move

Navigate to **Reporting → Pipeline Reports** (or Opportunities → Reports depending on UI version). Pipeline reporting is where you measure deal flow.

Key views:

**Stage Distribution Over Time.** Stacked bar chart showing how many opportunities have been in each stage on each date over a period. A healthy chart shows balanced bars growing slowly. An unhealthy chart shows the "Proposal Sent" stage ballooning (deals stalling), or the "New Lead" stage shrinking (you stopped generating leads).

**Average Days in Stage.** For each stage, how long do opportunities sit before moving forward (or being marked Lost)? If "Call Booked" averages 30 days, you have a problem — that stage should average maybe 3-5 days max. Long stage times mean leads are going cold while waiting for you to follow up.

**Win Rate by Stage.** Of all opportunities that entered each stage, what percentage eventually moved to Won? Your absolute win rate (Won / Total Opportunities) is one number. Stage-level win rates tell you where the leak is.

**Lost Reason Analysis.** Remember the workflow tutorial recommended marking Lost opportunities with a reason (price, timing, competitor, other)? Now that data pays off. Pivot Lost opportunities by reason to see the dominant cause. If 60% are Lost due to price, you have a positioning problem. If 60% are Lost due to timing, you have a follow-up cadence problem (you should be re-engaging those contacts 90 days later — that's a workflow worth building).

---

## Call and Conversation Reporting

If you're using VibeReach's phone system and Conversations module (you are, after Tutorial 5), there's reporting specific to communication volume.

**Call Reporting** at **Reporting → Calls** shows: total calls inbound, total outbound, average duration, missed calls, call source. Missed calls are particularly important — every missed call is a lead that may not call back. If your missed-call rate is over 10-15%, you need either better availability or an after-hours auto-text-back workflow.

**Conversation Reporting** shows response time analytics. Your average response time to inbound messages. Slowest threads. Which team member (if you have a team) is responding fastest or slowest. Best-in-class for B2C is under 10 minutes. Under 1 hour is acceptable for B2B. Over 4 hours is hurting your conversion rate noticeably.

---

## Integrating Google Analytics 4 — When You Need More

VibeReach's native reporting is solid for CRM-focused metrics — what's happening to leads, opportunities, and revenue. It's lighter on web behavior analytics — what people did on your site before becoming leads. For that, GA4.

### Setup

1. Create a GA4 property if you don't have one (analytics.google.com, free).
2. Copy the Measurement ID (format: `G-XXXXXXXXXX`).
3. In VibeReach, go to **Settings → Integrations → Google Analytics**.
4. Paste the Measurement ID and save.

VibeReach now fires GA4's base tag on every funnel and website page automatically. GA4 starts collecting data: page views, sessions, user demographics, traffic acquisition, engagement metrics, and conversion events.

### What GA4 Adds That VibeReach Doesn't

- Detailed page-level behavior (scroll depth, time on page, exit pages)
- Multi-channel attribution paths (the full sequence of touches, not just first and latest)
- Audience demographics and interests
- Comparison of user behavior across devices

### Configure GA4 Conversion Events

In GA4, go to **Configure → Events.** VibeReach automatically fires a `generate_lead` event when a form is submitted on a VibeReach page. Mark it as a conversion in GA4 so it shows up in conversion reports. Verify it's firing by using GA4's DebugView while you submit a test form.

For more advanced setups (call tracking, document signing as a conversion event), you can fire custom events from VibeReach workflows or via the Tracking Code Manager. That's beyond the scope of this tutorial, but worth knowing it's possible.

---

## Connecting Facebook Ads and Google Ads

If you're running paid ads, native integration is genuinely useful.

**Facebook Ads.** Go to **Settings → Integrations → Facebook.** Connect your ad account. VibeReach auto-creates a Facebook Ads reporting dashboard at **Reporting → Facebook Ads** showing spend, clicks, leads generated, cost per lead, and (if you've configured offline conversions properly) cost per closed deal. You don't have to log into Facebook Ads Manager separately for routine reporting.

**Google Ads.** Same pattern at **Settings → Integrations → Google Ads.** Connect your account. VibeReach creates a Google Ads dashboard at **Reporting → Google Ads** with the same kind of metrics.

The big win from native integration is **offline conversion tracking** — telling Facebook and Google when one of their clicks eventually became a closed deal, weeks after the original click. Without offline conversion data, the ad platforms optimize for "leads" (form fills), which is a poor proxy for "deals." With offline conversion data, they optimize for actual revenue. This often improves ad ROI by 20-50% over 90 days.

---

## Building a Custom Dashboard

The default dashboard works for general use, but if you have specific KPIs you watch every morning, build a custom dashboard.

1. Go to **Reporting → Dashboards** (or **Reporting → Add Widget** depending on UI).
2. Create a new dashboard, name it (e.g., "Weekly Review Dashboard").
3. Click **Add Widget** repeatedly to build out the views you want.

Widget types available:

- KPI cards (single number: total leads, total revenue, conversion rate)
- Line charts (trend over time)
- Bar charts (comparison across categories)
- Pie charts (distribution)
- Tables (raw data)

A solid weekly review dashboard for the curriculum scenario:

- **KPI Card:** New Contacts (last 7 days)
- **KPI Card:** Opportunities Created (last 7 days)
- **KPI Card:** Deals Won (last 7 days)
- **KPI Card:** Revenue Closed (last 7 days)
- **Bar Chart:** Leads by Source (last 30 days)
- **Line Chart:** Conversion Rate Over Time (last 90 days)
- **Table:** Top 5 Opportunities by Value (currently open)
- **Bar Chart:** Pipeline Value by Stage (current snapshot)

This is what you open every Monday morning. Fifteen minutes with this view tells you exactly how last week went and where to focus this week.

---

## Review Cadence — Daily, Weekly, Monthly

The dashboards are useless if you don't actually look at them on a rhythm. Here's the cadence that works for most service businesses:

**Daily (5 minutes).** Open the main dashboard. Check overnight activity — new conversations, new leads, new bookings, anything stuck or broken. Look at any red flags (no new leads in 48 hours, unanswered messages, missed calls). Triage if needed.

**Weekly (30 minutes — block it on the calendar).** Open the custom weekly review dashboard. Compare this week to last week. Are leads up or down? Conversion rate up or down? Pipeline value growing or shrinking? Note 1-2 things to investigate or adjust this week. Look at the source report and ask: where should we double down? Where should we cut?

**Monthly (60 minutes).** Open Attribution, Source Reports, and Lost Reason analysis. Ask deeper questions: which source has the best ROI? Which Lost reason is dominant? Which step in the funnel has the worst conversion rate? Pick 1-3 things to fix or test next month. Document them somewhere (a notes file works fine).

**Quarterly (2-3 hours).** The big strategic review. Pull data back 90 days. Look at trends. Re-evaluate goals. Decide what marketing channels to keep, double down on, or kill. Adjust pricing if the numbers say it's time. Plan next quarter's initiatives based on what the data actually showed, not what you assumed at the start.

The discipline isn't fancy. It's just *actually looking,* on a rhythm, with specific questions in mind. The plurality of businesses lose because they never look. The platform gives you the view; you have to schedule the time to use it.

---

## A Word About What Reporting Won't Tell You

Reporting tells you *what* happened. It doesn't tell you *why.* When pipeline velocity slows down, the dashboard tells you slowdown is happening. It doesn't tell you whether the cause is:

- A new competitor undercutting you
- A specific salesperson taking too long to follow up
- The market entering a slow season
- Your pricing being out of step with new market norms
- A change in lead quality from a particular source

Reporting flags the questions to ask. Conversations and customer interviews answer them. Don't get lost optimizing the dashboard while you've stopped talking to actual humans about why they did or didn't buy.

---

## Closing Thought — From Building to Operating

Five tutorials built the system. Two more (this one and Social Media) make the system observable and renewable. After the next tutorial, you'll have a complete operating manual for a service business inside VibeReach — every link in the chain from a stranger seeing a LinkedIn post to a signed contract and a Won card.

Reporting is the loop-closer. Without measurement, you're building blind. With measurement on a rhythm, you compound. Each week, you fix the worst-performing thing. Each month, you double down on the best-performing thing. After six months, you have a system that runs measurably better than it did when you launched it — not because you got lucky, but because the data told you exactly where to focus.

Open the dashboard tomorrow morning. Look at it for five minutes before opening your email. Build the habit. The system you built can only get better from here.

The next tutorial covers Social Media and the Social Planner — the part of the system that *creates* the leads everything else processes. We'll demo with LinkedIn since that's where most professional services traffic actually lives, and we'll show how to write and schedule posts that drive measurable traffic back to the funnel from Tutorial 1, closing the system's loop completely.

---

*Sources: HighLevel Support Portal — "Understanding Attribution Source," "How to Use Site and Funnel Analytics in HighLevel," "Reporting Dashboard Customization," "Google Analytics 4 Tracking," "Google Ad Reporting Setup," "Facebook Ad Reporting Setup," and HighLevel platform documentation on the Attribution Report and Source Reports. Verified May 2026.*
