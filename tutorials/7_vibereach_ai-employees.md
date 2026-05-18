# Putting AI Employees to Work in VibeReach

*Part seven of the curriculum. By now you have the entire deal cycle running — funnel to forms to pipeline to workflows to calendars to conversations to documents. Everything works. But everything also still requires you to actually do the work that flows through the system. AI Employees are the layer that takes routine work off your plate: answering common questions in the inbox, replying to reviews, picking up inbound calls after hours, helping you write copy faster. This tutorial walks through what AI Employees actually do, how to configure them well, and — importantly — how to keep them from embarrassing you in front of customers.*

---

## What This Tutorial Assumes

The same six pieces as before: funnel, forms/surveys, pipeline, workflows, calendars/conversations, documents. The AI Employees bolt onto all of them. Specifically:

- **Conversation AI** plugs into the Conversations inbox from Tutorial 5. Inbound SMS, web chat, Facebook DM, Instagram DM, and WhatsApp messages can be answered automatically.
- **Voice AI** plugs into your inbound phone number. Inbound calls get answered by an AI receptionist that can qualify, answer FAQs, and book appointments onto the calendar from Tutorial 5.
- **Reviews AI** plugs into your Google Business Profile and Facebook reviews. It generates personalized review responses automatically.
- **Content AI** is the writing assistant scattered throughout the platform — in email composers, SMS composers, funnel builders, and the social planner you'll build in Tutorial 9.
- **Funnel & Website AI** generates landing pages and websites from a prompt. Useful for first drafts; we're not relying on it for production pages.
- **Ask AI** is the in-platform assistant that helps you navigate VibeReach itself — like a help-desk co-pilot.

Six tools. One unified configuration story. Same underlying philosophy: AI does the high-volume routine work, you do the high-judgment specific work, and you keep watching what AI does for at least the first month so you can intervene when it gets weird.

---

## The First Big Decision: Unlimited vs. Pay-Per-Use

AI Employee pricing has two models, and you need to pick one before you start activating anything.

**Unlimited Plan** — $97/month per sub-account. Covers unlimited usage of Conversation AI, Reviews AI, Content AI, Ask AI, and Voice AI (inbound calls only). Does *not* cover Agent Studio, outbound Voice AI calls, Voice AI through the website chat widget, or Voice AI Prompt Optimizer — those remain pay-per-use even on Unlimited. And phone system charges (per-minute call costs through LC Phone or Twilio) still apply on top of Unlimited, because those are infrastructure costs separate from the AI itself.

**Pay-Per-Use** — token-based billing for each AI feature individually. Conversation AI charges per message-token exchange. Voice AI charges per minute of call time, with the cost depending on duration and complexity. Reviews AI and Content AI have their own per-use rates.

The break-even math: if you're going to handle more than roughly 50-100 AI conversations per month *or* receive more than roughly 5-10 hours of inbound Voice AI calls per month, Unlimited usually wins. For a solo consultant just starting with AI features, pay-per-use is often cheaper for the first few months while you're still calibrating. For an active service business with real inbound volume, Unlimited becomes a no-brainer fast.

**My recommendation for the curriculum scenario:** start on pay-per-use for the first 30 days while you're learning what each tool actually does. Then look at your usage report and switch to Unlimited the moment the per-use bill starts approaching $97.

To enable the AI Employee features at all, your agency admin needs to grant access to the sub-account. Once it's enabled, you'll see new menu items appear in the left navigation: AI Employee, Conversation AI, Voice AI, Reviews AI, etc.

---

## The Knowledge Base — Setup This Right or Nothing Else Works

This is the single most important point in this entire tutorial. Most failed AI Employee deployments fail because the knowledge base was set up poorly. The AI is only as good as what you tell it. A vague knowledge base produces vague, generic, off-brand answers. A specific, current, well-organized knowledge base produces answers that sound like a competent staff member.

Every AI tool that interacts with customers — Conversation AI, Voice AI, Reviews AI — pulls from a knowledge base you configure. Treat the knowledge base as your AI's training. You wouldn't hire a human receptionist and not tell them what your business does. Don't do the equivalent to the AI.

### What Goes Into the Knowledge Base

At minimum:

**Business identity.** Business name, what you do in two sentences, the markets you serve, the markets you specifically don't serve.

**Services offered.** Specific list of services with one-line descriptions. *"CRM Setup ($2,500–$5,000): Migration of contacts, configuration of pipelines and workflows, training session."* Be concrete about pricing ranges. If you refuse to discuss pricing publicly, tell the AI that explicitly so it stops trying to answer pricing questions and instead routes to a discovery call.

**Services NOT offered.** This is critical and most people skip it. If you don't do website design, tell the AI: *"We do not offer website design services. If a prospect asks, politely redirect to our CRM and automation focus."* Without explicit exclusions, the AI will helpfully agree to do things you can't actually do, and you'll find out about it when a confused prospect shows up at a discovery call expecting something different.

**Hours.** Your business hours, your time zone, what happens when someone reaches out outside hours.

**Booking flow.** Your calendar link (literal full URL). The exact phrasing you want the AI to use when offering to book: *"I'd love to set up a 20-minute discovery call so we can talk through your specific situation. You can grab a time here: [link]."* If you don't paste your full calendar URL into the prompt, the AI may invent a generic VibeReach booking link that doesn't go anywhere useful.

**FAQ pairs.** 10 to 15 question/answer pairs covering the most common things prospects ask. *"How long does CRM setup usually take?"* — *"Typical engagements run 3-5 weeks from kickoff to launch, depending on data complexity and team training needs."* Write the answers in the voice you want the AI to use. If you write FAQs in stiff corporate language, the AI will sound like a corporate manual. If you write them in your actual voice, the AI will (mostly) sound like you.

**Escalation rules.** When should the AI stop trying to handle the conversation and route to a human? Common triggers: the prospect mentions a specific dollar figure over a threshold, asks about a custom integration, expresses frustration, asks for a refund, asks about something legal or compliance-related, or uses specific keywords like "emergency" or "complaint."

### Where the Knowledge Base Lives

Navigate to **AI Employee → Conversation AI → Bot Settings → Bot Prompt** (the exact path can vary slightly by UI version, but the term "Bot Prompt" is consistent). This is the master prompt field. Paste your knowledge base content here, structured with clear headings. Format example:

```
BUSINESS IDENTITY
[Your business name] is a consulting practice that...

SERVICES OFFERED
- CRM Setup: ...
- Workflow Automation: ...
- AI Implementation: ...

SERVICES NOT OFFERED
- We do not offer: website design, paid ad management, ...

HOURS
Monday-Friday 9am-5pm Eastern. After-hours messages...

BOOKING
For discovery calls, use this link: https://yourdomain.com/widget/booking/crm-setup
Phrasing: "I'd love to set up a 20-minute call. Grab a time here: [link]"

FAQ
Q: How long does setup take?
A: Typical engagements run 3-5 weeks...

[continue for 10-15 FAQs]

ESCALATION
Route to human if the message contains: "emergency," "complaint," "refund," "lawsuit"
Route to human if the prospect mentions dollar figures over $20,000
```

Save. The AI now has context. Test it before turning it loose.

---

## Conversation AI — The Most Useful Starting Point

Conversation AI is the entry point for most users because it touches the daily-life tool from Tutorial 5 — the Conversations inbox. Inbound messages on supported channels (SMS, web chat, Facebook Messenger, Instagram DM, WhatsApp) can be handled by the AI either in **Suggestive mode** (AI drafts a reply, you review and send) or **Autopilot mode** (AI sends the reply automatically after a configurable delay).

### Step 1 — Always Start in Suggestive Mode

This is non-negotiable. *Always* start in Suggestive mode for the first two weeks. Autopilot mode looks tempting because it promises hands-off, but if you turn it on before you've verified that the AI actually handles your specific business correctly, the AI will absolutely send something embarrassing within a week. And once it's sent, it's sent — the prospect read it, your reputation took the hit.

In Suggestive mode, every time a message comes in:

1. The message appears in Conversations as usual.
2. When you open the thread, the AI displays a suggested reply at the bottom of the composer.
3. You read the suggestion, decide whether it's right.
4. If yes: one click sends it. If no: you write your own reply, or edit the suggestion before sending.

This gives you a feedback loop. After 50-100 suggestions, you'll have a clear sense of where the AI nails it (FAQ-type questions, generic greetings, booking link offers) and where it misses (anything emotional, anything specific to a deal in progress, anything requiring real judgment). That information feeds back into your knowledge base — the misses tell you what context you forgot to provide.

### Step 2 — When to Graduate to Autopilot

After two weeks of Suggestive use, look at your record. If the AI's suggestions have been correct 90%+ of the time on routine inbound messages, you can graduate Autopilot mode — but only for specific channels and specific scenarios.

**Where Autopilot makes sense:**
- After-hours auto-responses ("Thanks for reaching out — we're closed for the evening but here's our calendar link to book a call tomorrow")
- Standard FAQ replies on web chat where the prospect is clearly browsing
- Initial reply to inbound SMS while you're not at your desk

**Where Autopilot still doesn't make sense:**
- Active deal conversations where pricing or scope is being discussed
- Anything involving a complaint or refund
- B2B prospects asking specific implementation questions
- Any conversation where the customer is visibly frustrated

The pattern: AI handles the start of conversations, humans handle the meat. AI can be the receptionist; it shouldn't be the salesperson and definitely shouldn't be the closer.

### Step 3 — Configure Channel-by-Channel

Conversation AI settings let you enable or disable AI per channel:

- **SMS** — Yes, but be careful. SMS is high-trust; people read SMS messages closely. Mistakes here cost more than mistakes on web chat.
- **Web Chat (live chat widget)** — Yes. This is the most appropriate channel for AI handling because expectations are lower.
- **Facebook Messenger** — Yes for FAQs, no for complex sales conversations.
- **Instagram DM** — Same as Facebook.
- **WhatsApp** — Depends on your audience. Some regions treat WhatsApp like SMS (high-trust); others treat it like Facebook DM (casual). Match your local norm.

### Step 4 — Handoff Triggers

In the Conversation AI settings, configure handoff triggers — conditions under which the AI hands the conversation back to a human and pauses itself. Standard triggers:

- Specific keywords appear ("emergency," "complaint," "refund," "lawsuit," "manager")
- The AI's confidence score drops below 80% (i.e., it's not sure it has the right answer)
- The conversation reaches a configurable message count without resolution (e.g., after 5 back-and-forths, hand to human)
- The user explicitly asks for a human ("Can I talk to a real person?")

When a handoff fires, you get a notification in Conversations *and* on mobile. You can step into the thread and take over. The AI stops sending until you re-enable it for that conversation.

---

## Voice AI — The 24/7 Receptionist

Voice AI answers inbound calls to your VibeReach phone number with an AI agent that speaks naturally, asks qualifying questions, can answer FAQs from the same knowledge base as Conversation AI, and — most usefully — can book appointments directly onto your calendar from Tutorial 5.

### What Voice AI Is Actually Good At

- Answering the basics: hours, address, services offered
- Qualifying inbound interest (which service, urgency, budget range)
- Booking appointments by capturing name, email, preferred time, and writing to your calendar
- Routing complex calls to a real person via voicemail or call forwarding
- Handling missed-call scenarios after hours

### What Voice AI Is Not Good At

- Closing sales over the phone (it'll try; don't let it)
- Handling pricing negotiations
- Anything with emotional content (cancellations, complaints, refund discussions)
- Highly technical product questions outside the knowledge base

### Step 1 — Configure the Voice AI Agent

Navigate to **AI Employee → Voice AI → Agents** (path varies slightly). Create a new agent.

**Agent name and voice.** Choose a voice from the available options. Test several — voice quality varies, and the difference between a voice that sounds natural and one that sounds robotic is the difference between callers staying on the line and hanging up. Match the voice gender and accent to your audience expectations.

**Greeting.** First sentence the AI says when the call connects. Keep it natural: *"Hi, thanks for calling [Your Business]. I'm an AI assistant — I can answer your questions, book an appointment, or get a message to the team. How can I help?"* The disclosure that it's AI matters for trust. Don't pretend.

**Prompt.** Same content as the Conversation AI knowledge base — paste it in here, adapted slightly for voice (shorter sentences, less reliance on links since callers can't click). Make sure the calendar booking URL is included, plus your business hours and what to do when callers ask for someone specific by name.

**Booking integration.** Link Voice AI to your calendar from Tutorial 5. The AI can now actually book appointments mid-call — caller says "I'd like a discovery call," AI says "Sure, I have Wednesday at 2pm or Thursday at 10am — which works?" — and writes the appointment to your calendar in real time.

### Step 2 — Test, Then Test Again

Voice AI fails in unique ways. Real call audio is messier than text chat — background noise, accents, mumbling, interruptions. The AI can mis-hear, mis-transcribe, and respond to something the caller didn't say. You must test before going live.

1. Call your own business number from your personal phone.
2. Run through five scenarios: "What are your hours?" / "How much does CRM setup cost?" / "I want to book a call" / "Can I talk to someone?" / "I have a complaint about..." (test the escalation path).
3. Listen carefully. Did the AI hear you right? Did it answer correctly? Did it book the appointment to the right date? Did the escalation route to a real path (voicemail, forwarded call) instead of just hanging up?
4. Fix anything that broke. Re-test.
5. After live launch, listen to recordings of the first 20 real calls — Voice AI logs every call with full transcription and audio. Find the failure modes. Update the prompt.

### Step 3 — Phone System Cost Is Separate

Even on the Unlimited AI Employee plan, *phone system charges still apply.* Every minute of Voice AI call time costs you per-minute LC Phone or Twilio rates on top of the AI usage. A 5-minute Voice AI call doesn't cost just AI tokens; it also costs 5 minutes of phone airtime. Budget accordingly.

---

## Reviews AI — Automated Reply to Reviews

Reviews AI watches your Google Business Profile and Facebook reviews and generates personalized response drafts (or auto-publishes them, if you want).

### Why This Matters

Responding to reviews is a known SEO signal for local businesses and a known trust signal for prospects researching you. But responding to every review manually is tedious, especially across multiple platforms, and most businesses stop doing it consistently within a few months. Reviews AI keeps the cadence going.

### Setup

1. Connect your Google Business Profile and Facebook accounts at **Settings → Integrations.**
2. Navigate to **Reputation → Reviews AI** (or AI Employee → Reviews AI depending on UI version).
3. Configure response style: tone (professional, warm, casual), length (short, medium, long), whether to mention specific details from the review.
4. Choose mode: Auto-Reply (the AI publishes responses without your review) or Suggestive (the AI drafts responses you approve before publishing).

Same advice as Conversation AI: start in Suggestive. Auto-Reply seems efficient, but the first time the AI thanks a one-star review for "your kind feedback" because it didn't parse the sentiment correctly, you'll understand why human review matters. Two weeks of Suggestive, watch the patterns, then graduate appropriate categories to Auto.

### Tuning the Tone

Reviews AI lets you provide example responses that match your brand voice. Give it 3-5 sample responses you've written manually for different review types (5-star praise, 4-star with a small criticism, 3-star mixed, 2-star negative, 1-star angry). The AI uses these as voice references. The more specific your examples, the more your AI-generated responses will sound like you actually wrote them.

---

## Content AI — The Writing Assistant Everywhere

Content AI isn't one feature — it's a writing assistant embedded in every text composer across the platform. Email composer, SMS composer, funnel page text editor, blog post editor, social planner caption field, document template builder, and so on.

You'll see a small AI icon in any text field that supports Content AI. Click it and you get options like:

- Generate from prompt ("Write a follow-up email for someone who didn't show up to their booked call")
- Rewrite (paste text, ask AI to rewrite shorter / longer / more formal / more casual)
- Continue (you start the message, AI suggests the next paragraph)
- Translate (translate text into another language)

### Where Content AI Is Genuinely Useful

- First drafts of email sequences when you have writer's block
- Subject line variations for A/B testing
- Shortening copy that's gotten too long
- Translating standard messages into Spanish / Portuguese / French
- Rewriting your draft "with more warmth" or "with more urgency"

### Where Content AI Falls Down

- Anything requiring brand-specific voice without you giving examples
- Anything requiring current information about your business (AI doesn't know what's happening at your company today)
- Anything emotional or sensitive

The right relationship with Content AI: it's a fast first draft. You always edit. The AI gets you from blank page to 80% in 30 seconds. You take 5 minutes to get from 80% to 100% by editing in your own voice, fixing the generic phrasing, and adding the specific details only you know. That's the workflow that actually saves time and produces good copy. The workflow of "Content AI writes it, I publish it" produces copy that sounds like every other VibeReach-generated email on the internet — which is to say, slightly off, in a way prospects can usually sense.

---

## Funnel & Website AI — Useful for First Drafts Only

Funnel & Website AI generates landing pages, websites, and funnel layouts from a text prompt. You describe what you want ("A landing page for CRM consulting targeting small business owners, with a hero, three feature blocks, social proof, and a discovery call CTA"), and the AI generates the page.

Use this for: getting unblocked on a first draft when you don't know where to start, exploring layout options, generating quick variations for testing.

Don't use this for: production pages you're driving traffic to. The output is usually generic — same general layout, same generic stock images, same not-quite-right copy. It's fine as a starting point, but every single time I've seen someone publish an AI-generated funnel as-is, the conversion rate has been worse than a hand-built equivalent.

Same workflow as Content AI: generate, then heavily edit. The AI gets you the skeleton in 60 seconds. You spend 30 minutes making it actually yours.

---

## Ask AI — Your In-Platform Co-pilot

Ask AI is the assistant that lives inside VibeReach itself. It's not for customer-facing work — it's for *you* navigating the platform. Ask it questions like "How do I set up a Round Robin calendar?" or "Where's the audit log for documents?" and it gives you a directed answer with links to the right settings.

You'll see Ask AI in the top toolbar of VibeReach (the icon may be a small star or sparkle). It's covered under the Unlimited plan; per-use pricing depends on query complexity.

Use this whenever you're stuck. It's significantly faster than searching the support portal manually for most procedural questions.

---

## A Realistic AI Employee Rollout Plan

Don't turn on all five tools at once. You'll get overwhelmed, you won't notice when things break, and you'll get billed for usage you didn't watch.

**Week 1:** Activate Conversation AI in **Suggestive mode** for web chat only. Watch every suggestion before sending. Update your knowledge base prompt based on what you learn.

**Week 2:** Extend Suggestive to SMS and FB/IG DMs. Same review-every-suggestion discipline. Start using Content AI for first drafts on emails.

**Week 3:** If Suggestive mode has been 90%+ correct, graduate after-hours web chat to Autopilot. Keep humans on SMS and active conversations.

**Week 4:** Activate Reviews AI in Suggestive mode. Approve every response for two weeks before automating any of it.

**Week 5-6:** Configure and test Voice AI in a controlled way — point a test number at it before pointing your real business line. Iterate on the prompt based on real call transcripts.

**Week 7-8:** Go live on Voice AI for inbound calls during business hours; route after-hours to standard voicemail. Monitor call recordings for the first 50 calls.

**Week 9+:** Review usage and bill. Decide whether Unlimited makes sense. Continue tuning prompts based on actual customer interactions.

After 90 days of this, AI Employees have meaningfully reduced your routine workload, you have a knowledge base that actually reflects your business, and you're spending your time on the high-judgment work where humans matter and machines don't.

---

## Closing Thought — AI Amplifies the System You Built

AI Employees aren't a replacement for the rest of the curriculum. They're a multiplier on it. None of these tools work in a vacuum:

- Conversation AI is only as good as the contact data you collected in Funnel Part 2 (forms and surveys).
- Voice AI books appointments onto the calendar from Tutorial 5 — without that calendar, the booking action goes nowhere.
- Reviews AI responds to reviews about a business that needs to actually be running well; if your service delivery is bad, AI just helps you reply faster to a stream of one-star reviews.
- Content AI writes copy that goes into emails sent by workflows from Tutorial 4 — without the workflow, there's no automation to write copy for.

The pattern is: build the system first (Tutorials 1-6), then layer AI on top to make the system run faster and cover more ground without your hands on every input. Skip the system, and AI gives you garbage faster. Build the system right, and AI takes you from "I can run this business solo" to "I can run this business solo at three times the volume."

Next we'll cover Reporting and Analytics — how to measure everything you've built so you can see what's actually working, what's leaking, and where to focus next. After that, Social Media and Social Planner closes the loop by giving your funnel a source of traffic that doesn't require you to be hand-feeding it leads.

---

*Sources: HighLevel Support Portal — "AI Employee Overview," "AI Product Pricing," "Using Conversation AI on Mobile," "Voice AI Setup Guide," "Conversation AI Knowledge Base Configuration," and HighLevel platform pricing documentation. Verified May 2026.*
