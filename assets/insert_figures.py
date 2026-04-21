"""Insert figure blocks into chapters 9-12 at appropriate locations."""

def insert_after(content, search_text, figure_block):
    """Insert figure block after the first occurrence of search_text."""
    pos = content.find(search_text)
    if pos == -1:
        print(f"  WARNING: Could not find '{search_text[:60]}'")
        return content
    # Find end of current paragraph/section
    insert_pos = pos + len(search_text)
    # Find next double newline
    next_para = content.find('\n\n', insert_pos)
    if next_para == -1:
        next_para = len(content)
    else:
        next_para += 2  # include the newlines
    
    return content[:next_para] + figure_block + '\n\n' + content[next_para:]

CHAPTERS = '/home/node/openclaw/books/vibe-marketing-martech/chapters/'

# CH09 figures
ch09_figures = [
    # (search text to insert AFTER, figure block)
    (
        '## 9.2 What GHL\'s AI Employee Actually Is',
        ''':::{figure} ../images/ch09-ai-employee-suite.png
:label: fig-ch09-ai-employee-suite
:alt: The five GHL AI Employee tools arranged as a workforce diagram: Voice AI, Conversation AI, Review AI, Content AI, and Workflow AI
:width: 100%
:align: center
GHL's AI Employee suite — five specialized tools each designed for a specific job function that previously required a human staff member.
:::'''
    ),
    (
        '### Accessing Voice AI in GHL',
        ''':::{figure} ../images/ch09-voice-ai-setup.png
:label: fig-ch09-voice-ai-setup
:alt: GHL Voice AI agent setup interface showing Settings path, agent configuration form, and call flow diagram
:width: 100%
:align: center
Voice AI agent configuration: the Settings navigation path, agent fields, and how calls flow from caller through the AI agent to resolution or human handoff.
:::'''
    ),
    (
        '**Layer 4 — Guardrails.**',
        ''':::{figure} ../images/ch09-knowledge-base-layers.png
:label: fig-ch09-knowledge-base-layers
:alt: Four-layer pyramid showing the AI Training Framework: Identity, Knowledge, Goals, and Guardrails from bottom to top
:width: 100%
:align: center
The Four-Layer AI Training Framework. Each layer builds on the one below it — a well-configured Guardrails layer requires solid Identity, Knowledge, and Goals foundations first.
:::'''
    ),
    (
        '### The Human Escalation Trigger',
        ''':::{figure} ../images/ch09-human-handoff.png
:label: fig-ch09-human-handoff
:alt: Decision tree showing Voice AI human handoff triggers and routing logic for business hours vs. after-hours
:width: 100%
:align: center
Human handoff decision tree: three escalation triggers route calls to live agents during business hours and to voicemail with SMS callback outside hours.
:::'''
    ),
    (
        '### Lead Qualification Sequences',
        ''':::{figure} ../images/ch09-conversation-ai-flow.png
:label: fig-ch09-conversation-ai-flow
:alt: Sequence diagram showing Conversation AI qualification flow from lead greeting through booking with CRM field updates
:width: 100%
:align: center
Conversation AI qualification sequence: the AI gathers lead information, updates CRM fields, books an appointment or escalates to a human — all without manual intervention.
:::'''
    ),
    (
        '## 9.6 AI Appointment Booking: The Full Integration',
        ''':::{figure} ../images/ch09-appointment-booking-ai.png
:label: fig-ch09-appointment-booking-ai
:alt: Diagram showing AI booking conversation flow alongside real-time calendar update and post-booking workflow trigger
:width: 100%
:align: center
AI appointment booking: the conversation thread confirms a time slot while the GHL calendar updates in real time and the post-booking reminder workflow fires automatically.
:::'''
    ),
    (
        '## 9.7 Review AI: Your Reputation on Autopilot',
        ''':::{figure} ../images/ch09-review-ai-modes.png
:label: fig-ch09-review-ai-modes
:alt: Comparison of Suggestive Mode versus Auto-Pilot Mode for Review AI responses
:width: 100%
:align: center
Review AI modes: Suggestive Mode drafts responses for human approval (maximum control, slower); Auto-Pilot Mode publishes instantly (maximum speed, lower control). Match the mode to your review volume.
:::'''
    ),
    (
        '## 9.8 Content AI: Your Built-In Copywriter',
        ''':::{figure} ../images/ch09-content-ai-uses.png
:label: fig-ch09-content-ai-uses
:alt: Content AI embedded in three GHL tools: funnel builder, email composer, and social planner
:width: 100%
:align: center
Content AI appears inside the three GHL builders where copy decisions happen — funnels, email campaigns, and social posts — so generation happens in context rather than requiring a separate tool.
:::'''
    ),
    (
        '## 9.10 Case Study:',
        ''':::{figure} ../images/ch09-med-spa-case-study.png
:label: fig-ch09-med-spa-case-study
:alt: Data visualization showing before/after metrics for med spa AI Employee deployment: 87 after-hours calls handled, 31 appointments booked
:width: 100%
:align: center
Case study results: 87 after-hours calls handled by Voice AI in the first 30 days, generating 31 new patient appointments at a 36% booking conversion rate.
:::'''
    ),
    (
        '**5. Workflow AI**',
        ''':::{figure} ../images/ch09-workflow-ai-builder.png
:label: fig-ch09-workflow-ai-builder
:alt: GHL Workflow AI builder showing a natural language prompt generating a complete automation workflow
:width: 100%
:align: center
Workflow AI converts a plain-English description into a scaffolded workflow with triggers, wait steps, and conditional branches — ready to review and activate.
:::'''
    ),
]

with open(CHAPTERS + 'ch09-ai-employees.md', 'r') as f:
    content = f.read()

for (search, figure) in ch09_figures:
    old_len = len(content)
    content = insert_after(content, search, figure)
    if len(content) > old_len:
        print(f"  ✓ ch09: inserted figure after '{search[:50]}'")

with open(CHAPTERS + 'ch09-ai-employees.md', 'w') as f:
    f.write(content)
print("ch09 figures inserted")

# CH10 figures
ch10_figures = [
    (
        '## 10.2 Why Reviews Are the New Word of Mouth',
        ''':::{figure} ../images/ch10-star-rating-revenue.png
:label: fig-ch10-star-rating-revenue
:alt: Bar chart showing correlation between star rating and revenue indexed to baseline at 4 stars
:width: 100%
:align: center
Harvard Business School research on the star rating–revenue relationship: each full star improvement correlates with a 5–9% revenue increase for local service businesses.
:::'''
    ),
    (
        '## 10.4 Connecting Your Review Platforms',
        ''':::{figure} ../images/ch10-gbp-connection.png
:label: fig-ch10-gbp-connection
:alt: Step-by-step visual guide showing four numbered steps to connect Google Business Profile to GHL
:width: 100%
:align: center
Four steps to connect Google Business Profile: navigate to Reputation → Settings, authorize with Google, select your business location, and verify the green "Connected" status appears.
:::'''
    ),
    (
        '## 10.5 Automated Review Requests:',
        ''':::{figure} ../images/ch10-review-request-flow.png
:label: fig-ch10-review-request-flow
:alt: Flowchart showing automated review request workflow from service completion through SMS request to optional follow-up
:width: 100%
:align: center
The automated review request workflow: a 48-hour wait, a complaint gate, a warm SMS request, and a single 5-day follow-up — requesting reviews from every completed client without manual intervention.
:::'''
    ),
    (
        '## 10.6 Handling Negative Reviews:',
        ''':::{figure} ../images/ch10-negative-review-response.png
:label: fig-ch10-negative-review-response
:alt: Three-step negative review response framework: Acknowledge, Empathize, Invite Private Resolution — with examples
:width: 100%
:align: center
The acknowledge-empathize-resolve framework for negative review responses. Every step is visible to future prospects reading your reviews — respond to the audience, not just the reviewer.
:::'''
    ),
    (
        '## 10.7 Review Widgets:',
        ''':::{figure} ../images/ch10-review-widget.png
:label: fig-ch10-review-widget
:alt: GHL review widget showing star rating, total reviews, and individual review cards with embed code below
:width: 100%
:align: center
The GHL Review Widget: paste one HTML code block into your website or funnel and your live Google rating, review count, and most recent reviews display automatically — updating every time a new review arrives.
:::'''
    ),
    (
        '## 10.8 Reputation Reporting:',
        ''':::{figure} ../images/ch10-reputation-metrics.png
:label: fig-ch10-reputation-metrics
:alt: Reputation management dashboard showing average star rating, total reviews, response rate, and review request conversion rate
:width: 100%
:align: center
Four reputation KPIs to monitor monthly: star rating (target 4.5+), total review volume, response rate (target 100%), and review request conversion rate (benchmark 25–35% for SMS requests).
:::'''
    ),
    (
        '## 10.14 Case Study:',
        ''':::{figure} ../images/ch10-home-services-case-study.png
:label: fig-ch10-home-services-case-study
:alt: Infographic showing home services agency review growth from 23 to 211 reviews over 180 days with monthly bar chart
:width: 100%
:align: center
180-day results: automated review requests after every completed job grew the client's review count from 23 to 211, improving their Google star rating from 3.9 to 4.8.
:::'''
    ),
]

with open(CHAPTERS + 'ch10-reputation.md', 'r') as f:
    content = f.read()

for (search, figure) in ch10_figures:
    old_len = len(content)
    content = insert_after(content, search, figure)
    if len(content) > old_len:
        print(f"  ✓ ch10: inserted figure after '{search[:50]}'")

with open(CHAPTERS + 'ch10-reputation.md', 'w') as f:
    f.write(content)
print("ch10 figures inserted")

# CH11 figures
ch11_figures = [
    (
        '## 11.2 The GHL Reporting Suite:',
        ''':::{figure} ../images/ch11-reporting-suite.png
:label: fig-ch11-reporting-suite
:alt: Infographic showing seven GHL report types with icons and descriptions
:width: 100%
:align: center
The GHL Reporting Suite: seven report types covering contacts, attribution, calls, appointments, conversations, ad performance, and custom dashboards — each answering a different operational question.
:::'''
    ),
    (
        '## 11.3 Understanding Attribution:',
        ''':::{figure} ../images/ch11-attribution-models.png
:label: fig-ch11-attribution-models
:alt: Comparison diagram showing First Attribution, Last Attribution, and Linear Attribution credit assignment across a customer journey
:width: 100%
:align: center
Attribution models: the same customer journey assigns credit differently depending on the model used. Most businesses should start with Last Attribution (what closes deals?) before adding First Attribution (what attracts leads?).
:::'''
    ),
    (
        '## 11.4 Connecting Google and Facebook Ads',
        ''':::{figure} ../images/ch11-google-ads-connection.png
:label: fig-ch11-google-ads-connection
:alt: Step diagram showing three steps to connect Google Ads to GHL with data flow showing conversions reported back
:width: 100%
:align: center
Google Ads connection: three steps to link your ad account, plus the data flow showing how GHL contact creations and pipeline events report back to Google as conversion signals.
:::'''
    ),
    (
        '## 11.4 Connecting Google and Facebook Ads',
        ''':::{figure} ../images/ch11-facebook-capi-diagram.png
:label: fig-ch11-facebook-capi
:alt: Comparison diagram showing browser pixel tracking (unreliable) versus Facebook Conversions API server-side tracking (complete)
:width: 100%
:align: center
Facebook Conversions API (CAPI) vs. browser pixel: server-side conversion tracking bypasses iOS privacy restrictions and ad blockers, delivering near-complete conversion data to Facebook's attribution model.
:::'''
    ),
    (
        '## 11.5 Call Reporting:',
        ''':::{figure} ../images/ch11-call-reporting-dashboard.png
:label: fig-ch11-call-reporting-dashboard
:alt: GHL call reporting dashboard showing total calls, answer rate, hourly call volume chart, and missed call time windows
:width: 100%
:align: center
Call Performance dashboard: four headline metrics, hour-by-hour call volume distribution, and a table of peak missed-call windows — the data needed to staff phones correctly or deploy Voice AI strategically.
:::'''
    ),
    (
        '## 11.6 Appointment Reports:',
        ''':::{figure} ../images/ch11-appointment-funnel.png
:label: fig-ch11-appointment-funnel
:alt: Funnel chart showing appointment performance from leads generated through forms submitted, consultations booked, attended, and clients converted
:width: 100%
:align: center
The appointment performance funnel: each stage has a benchmark conversion rate. A no-show rate above 15% signals a reminder sequence problem; a booked-to-submitted rate below 60% signals a calendar UX problem.
:::'''
    ),
    (
        '## 11.7 Custom Dashboards:',
        ''':::{figure} ../images/ch11-custom-dashboard-layout.png
:label: fig-ch11-custom-dashboard-layout
:alt: GHL custom dashboard mockup showing Business Command Center with six widget tiles covering contacts, pipeline, calls, appointments, reputation, and response time
:width: 100%
:align: center
The Business Command Center dashboard: six widgets, one screen, 90-second morning review. Every number has a decision attached to it.
:::'''
    ),
]

with open(CHAPTERS + 'ch11-reporting.md', 'r') as f:
    content = f.read()

for (search, figure) in ch11_figures:
    old_len = len(content)
    content = insert_after(content, search, figure)
    if len(content) > old_len:
        print(f"  ✓ ch11: inserted figure after '{search[:50]}'")

with open(CHAPTERS + 'ch11-reporting.md', 'w') as f:
    f.write(content)
print("ch11 figures inserted")

# CH12 figures
ch12_figures = [
    (
        '## 12.3 Connecting Each Platform',
        ''':::{figure} ../images/ch12-platform-connections.png
:label: fig-ch12-platform-connections
:alt: Hub-and-spoke diagram showing GHL Social Planner connected to seven social platforms with connection requirements for each
:width: 100%
:align: center
GHL Social Planner platform connections: seven platforms, all managed from one hub. Each platform has specific account type requirements before connection is possible.
:::'''
    ),
    (
        '## 12.4 Scheduling and Publishing Posts',
        ''':::{figure} ../images/ch12-social-calendar-view.png
:label: fig-ch12-social-calendar-view
:alt: GHL Social Planner calendar view showing color-coded scheduled posts by platform across a monthly grid
:width: 100%
:align: center
The Social Planner Calendar View: color-coded posts by platform, hover preview cards, and monthly distribution at a glance — the difference between "posting when you remember" and "posting on a system."
:::'''
    ),
    (
        '## 12.5 AI Content Generation:',
        ''':::{figure} ../images/ch12-content-ai-workflow.png
:label: fig-ch12-content-ai-workflow
:alt: Four-step process diagram: write brief, generate AI variations, select and humanize, schedule across platforms
:width: 100%
:align: center
Content AI workflow: four steps from blank brief to scheduled post. The AI handles the blank-page problem; you handle the authenticity. Every AI post should be edited before scheduling.
:::'''
    ),
    (
        '## 12.6 Content Queue and Best-Time Scheduling',
        ''':::{figure} ../images/ch12-posting-schedule.png
:label: fig-ch12-posting-schedule
:alt: Weekly heat map showing optimal posting times by platform with darkest orange indicating best performance windows
:width: 100%
:align: center
Platform-optimized posting windows (2025–2026 data): configure your Content Queue to match these windows for each platform and let GHL distribute your scheduled content automatically.
:::'''
    ),
    (
        '## 12.7 Managing Multiple Clients',
        ''':::{figure} ../images/ch12-agency-multiaccount.png
:label: fig-ch12-agency-multiaccount
:alt: Agency architecture diagram showing multiple client sub-accounts each with separate Social Planner vs competing tools requiring separate subscriptions
:width: 100%
:align: center
Agency Social Planner architecture: every client sub-account has its own Social Planner with isolated platform credentials, no tool subscriptions per client, and full management from the agency dashboard.
:::'''
    ),
    (
        '## 12.8 Social Media Reporting',
        ''':::{figure} ../images/ch12-gbp-posts-local-seo.png
:label: fig-ch12-gbp-posts-local-seo
:alt: Infographic showing how Google Business Profile posting frequency correlates with local search pack appearance rate
:width: 100%
:align: center
GBP posting and local SEO: weekly posting to Google Business Profile is one of the highest-ROI activities for local search visibility — and one of the least utilized by most local businesses.
:::'''
    ),
    (
        '## 12.12 Social Media Strategy Frameworks',
        ''':::{figure} ../images/ch12-441-framework.png
:label: fig-ch12-441-framework
:alt: Visual representation of the 4-1-1 content framework showing four educational posts, one soft sell, and one direct offer in sequence
:width: 100%
:align: center
The 4-1-1 content framework: for every 6 posts, four provide genuine value with no sales pitch, one soft-sells through sharing or testimonial, and one makes a direct offer. Audiences follow and trust value-first accounts.
:::'''
    ),
]

with open(CHAPTERS + 'ch12-social.md', 'r') as f:
    content = f.read()

for (search, figure) in ch12_figures:
    old_len = len(content)
    content = insert_after(content, search, figure)
    if len(content) > old_len:
        print(f"  ✓ ch12: inserted figure after '{search[:50]}'")

with open(CHAPTERS + 'ch12-social.md', 'w') as f:
    f.write(content)
print("ch12 figures inserted")

print("\nAll figures inserted!")
