## 9.9 Lab 9: Deploy Your First AI Employee — Complete Voice Agent Setup

Every missed after-hours call is a prospect who called a competitor instead. Your AI Voice Employee works 24/7 — answering every call, handling your most common questions, booking appointments directly into your calendar, and transferring to a human when the situation demands one. In this lab, you configure a complete Voice AI agent: name it, write its opening script, build its knowledge base, connect your calendar, set up human handoff, and activate it on your GHL phone number. By the end, your business line answers professionally at 2 AM on a Sunday.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with AI Employee features enabled (check Settings → AI Employee — if this section doesn't appear, contact support to enable it on your plan)
- A provisioned GHL phone number from Chapter 5
- A configured GHL calendar with at least one service type available for booking
- Your business information ready: hours, services, top 5–10 FAQ answers, address
- Approximately 30–45 minutes

**Billing note:** Voice AI charges per conversation minute. Confirm AI credit balance in Settings → AI Employee → Usage before activating.
:::

---

### Step 1: Enable Voice AI and Create Your Agent

1. In the left sidebar, click ⚙️ **Settings** → **AI Employee**.
2. Click the **Voice AI** tab.
3. Toggle **Enable Voice AI** to ON. A billing confirmation popup appears — review and confirm.
4. Click **+ Create Agent** in the upper right.
5. Configure the agent basics:
   - **Agent Name:** `Main Inbound Receptionist` *(internal label — callers won't hear this)*
   - **Persona Name:** Choose a first name — e.g., `Aria`, `Alex`, or `Jordan`. This is how the agent introduces itself to callers.
   - **Phone Number:** Click the dropdown → select your provisioned GHL number from Chapter 5
   - **Primary Language:** English (or Spanish if serving Spanish-speaking market — both are available as of 2026)
   - **Primary Goal:** `Book an Appointment`
6. Click **Save** (or **Next** if the builder uses a wizard).

**You'll know you did this right when:** Your new agent appears in the Voice AI agent list with your assigned phone number displayed.

:::{admonition} Why This Matters
:class: tip
The Primary Goal is the most important setting in the entire setup — it shapes every response the AI gives. An agent with "Book an Appointment" as its goal steers every conversation toward scheduling. An agent with "Answer FAQs" deflects callers without a booking path. Choose the goal that matches your business objective before touching anything else.
:::

---

### Step 2: Write Your Opening Script

1. In the agent settings, find the **Opening Message** field.
2. Write a greeting under 25 words that uses your real business name. Keep it warm and natural:

   > "Hi, thanks for calling [Your Business Name]! This is [Agent Name] — how can I help you today?"

3. Avoid long corporate-sounding intros. Callers decide in the first 3 seconds whether to stay on the line. Short and warm wins.
4. If relevant, add a brief availability note: "I can help you schedule an appointment or answer questions about our services."
5. Click **Save**.

**You'll know you did this right when:** The Opening Message field shows your custom greeting with the real business name. The character count is under 150 (aim for 20–30 words).

---

### Step 3: Build Your Knowledge Base

Click the **Knowledge Base** tab in your agent settings. This is the most important step in the entire lab. Spend at least 15 minutes here.

Add entries for each of the following categories:

**Business Identity:**
- Full legal business name
- Physical address (if applicable) and service area
- Hours of operation (include time zone): "We're available Monday through Friday, 9 AM to 6 PM Eastern Time. I can schedule appointments outside those hours on request."

**Services:** Write one clear sentence for each service you offer:
- Service name
- What it is and who it's for
- Approximate time required
- Price range (or "pricing depends on your specific situation — I can schedule a free consultation to discuss")

**Top FAQ Answers (minimum 5, target 10):** Think of the 10 questions your front desk fields most often. Write them as Q&A pairs:
- "What is your pricing for [service]?" → your honest answer
- "Do you accept insurance / [payment method]?" → yes/no with details
- "How long does [service] take?" → specific answer
- "Where are you located / do you travel to [area]?" → specific answer
- "What should I bring / prepare for my appointment?" → specific instructions

**Booking Details:**
- What information you need to book: name, phone, email, service type
- What appointment types are available
- How far in advance you book
- Your cancellation/rescheduling policy

:::{admonition} Why This Matters
:class: tip
The knowledge base is the agent's brain. Every gap in the knowledge base becomes a moment where the AI says "I'm not sure about that" — which sounds professional (it's better than guessing), but it's a missed opportunity. The agents that generate 36% booking rates from after-hours calls have comprehensive knowledge bases. The agents that frustrate callers have five FAQ entries.
:::

**You'll know you did this right when:** Your knowledge base has at least 5 FAQ entries, full business hours, all services listed, and booking details configured.

---

### Step 4: Connect Your Calendar for AI Booking

1. In your agent settings, click the **Integrations** tab (or **Calendar** tab).
2. Click **Connect Calendar** (or select from the dropdown).
3. Select your primary GHL calendar — the one used for consultations or appointments.
4. Configure booking settings:
   - **Minimum Advance Notice:** 2 hours (prevents same-hour surprises for your team)
   - **Maximum Days in Advance:** 14 or 30 days (your preference)
   - **Confirmation Delivery:** Enable SMS confirmation (if A2P approved) and/or Email confirmation
5. Click **Save**.

**You'll know you did this right when:** The Integrations tab shows your calendar name with a green connected indicator, and minimum advance notice is configured.

---

### Step 5: Configure Human Handoff

1. In your agent settings, click the **Handoff** or **Transfer** tab.
2. Configure:
   - **Transfer Phone Number:** Your direct line or your team's main line (the number a caller reaches when they ask for a human)
   - **Trigger: Caller Requests Human** — toggle ON
   - **Trigger: Repeated Misunderstandings** — set to 3 consecutive unrecognized inputs → toggle ON
   - **Trigger: Escalation Keywords** — add: `complaint`, `cancel`, `legal`, `angry`, `refund`, `manager`
   - **Handoff Message:** "Let me connect you with one of our team members who can help you with that. One moment, please."
3. **After-Hours Handoff:** Under "Outside Business Hours":
   - Route to voicemail instead of live transfer
   - Voicemail greeting: "Our team isn't available right now, but [Agent Name] has noted your inquiry and our team will call you back during business hours. Please leave your name and number."
4. Click **Save**.

:::{admonition} Why This Matters
:class: tip
Human handoff is not failure — it's the system working as designed. Configure handoff rules that protect the two situations where AI should never handle the call alone: when the caller is upset (keyword triggers), and when the AI genuinely can't help (repeated misunderstandings). The callers the AI can't help well need a human; everyone else is served efficiently by the AI.
:::

**You'll know you did this right when:** The Handoff tab shows your transfer number, at least 3 escalation keywords, and an after-hours routing rule.

---

### Step 6: Test Your Agent (Five Scenarios)

Click **Test Agent** — this initiates a real call to your mobile phone from the agent. Run five scenarios and document any gaps:

1. **Common FAQ:** Ask your most frequently asked question. Does the agent answer accurately and completely?
2. **Service pricing:** Ask about cost. Does it handle "it depends" answers gracefully, or does it give a wrong number?
3. **Book an appointment:** Say "I'd like to schedule an appointment for [your service] this Thursday." Does it offer available times and complete the booking?
4. **Off-topic question:** Ask something completely unrelated to your business (what's the weather, who is the president, etc.). Does it redirect gracefully without making up answers?
5. **Request a human:** Say "I need to speak with someone." Does it trigger the handoff message and transfer correctly?

For any scenario that doesn't go well: return to the Knowledge Base and add or refine the relevant entries. Retest after each improvement.

**You'll know you did this right when:** All five test scenarios produce responses you would be comfortable having a real prospect hear.

---

### Step 7: Activate Your Agent

1. After successful testing, return to the agent settings.
2. Click **Activate Agent** (or toggle the agent status from **Draft** to **Active**).
3. Confirm the activation — your phone number now answers with your AI Employee.

**You'll know you did this right when:** The agent shows "Active" status in your Voice AI agent list. Call your provisioned number from any phone — your AI Employee answers.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 10:

- ☐ Voice AI enabled in Settings → AI Employee
- ☐ Agent created with Persona Name, Phone Number, and Primary Goal configured
- ☐ Opening script written — 20–30 words, real business name used
- ☐ Knowledge base contains: business hours, all services, minimum 5 FAQ Q&A pairs, booking details
- ☐ Calendar connected with 2-hour minimum advance notice
- ☐ Human handoff configured: transfer number, 3+ escalation keywords, after-hours routing
- ☐ All five test scenarios completed — knowledge gaps addressed
- ☐ Agent activated on your GHL phone number

Your business line now answers 24/7. Every call outside business hours — every 11 PM inquiry, every Saturday morning question — is handled professionally and given a path to book.
:::

::::{dropdown} Troubleshooting Common Issues

**"Settings → AI Employee" is not visible in my account:**
AI Employee features require a GHL plan tier that includes AI capabilities. Contact your VibeReach.io/GHL support to confirm AI Employee is included in your subscription. If you recently upgraded, try logging out and back in to refresh your feature flags.

**Agent created but the phone number dropdown shows no numbers:**
Your phone number must be provisioned first (Chapter 5). If Chapter 5 is not yet complete, go to Settings → Phone System → Phone Numbers → + Add Number to provision a number, then return to Voice AI setup.

**Test call connects but agent sounds stilted or gives wrong answers:**
Return to the Knowledge Base. The most common cause: FAQ answers are too vague (e.g., "pricing varies" without explaining what to do instead). Replace vague entries with specific ones: "For pricing information, I recommend scheduling a free consultation — I can book that for you right now. Does that sound good?"

**Appointment booking test fails — agent says it can't book:**
Verify the calendar is connected in the Integrations tab of your agent settings. Confirm the calendar has available time slots (check Settings → Calendars → your calendar → view the schedule). The agent cannot book into times that are blocked or outside your availability windows.

**Agent activates but doesn't answer calls — callers hear ringing then voicemail:**
The agent must be assigned to the phone number's call flow. Go to Settings → Phone Numbers → click your number → confirm the incoming call flow routes through Voice AI (not directly to voicemail). Check the call flow settings and assign the AI agent as the first action.
::::

