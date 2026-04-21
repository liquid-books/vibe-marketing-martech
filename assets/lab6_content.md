## 6.12 Lab 6: Connect Every Channel and Build Your Snippet Library

Your Conversations inbox is the nerve center of all two-way communication with your contacts. But it only works if all your channels — email, SMS, Facebook, Instagram, Google Business Messages, live chat — are actually connected to it. In this lab, you connect every relevant channel to your VibeReach.io account and build a reusable snippet library of your most frequently sent responses. By the end, every inbound message from any channel lands in one inbox, and your most common replies are available with a single keystroke — ending the copy-paste chaos permanently.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- A Facebook Business Page (required for Facebook Messenger + Instagram DM connections)
- An Instagram Business or Creator account connected to your Facebook Page
- A Google Business Profile listing (for Google Business Messages)
- Your provisioned GHL phone number from Chapter 5 (for SMS — must have A2P 10DLC approved)
- Approximately 45–60 minutes

**A2P Note:** If A2P 10DLC registration is not yet approved, SMS will be read-only (inbound messages appear but outbound is blocked). Complete this lab's non-SMS channels now and return for SMS once A2P is approved.
:::

---

### Step 1: Connect Your Facebook Page and Instagram DMs

1. In the left sidebar, click ⚙️ **Settings** → **Integrations**.
2. Find **Facebook** in the integrations list → click **Connect**.
3. Click **Connect with Facebook** — a Facebook authorization window opens.
4. Log in with the Facebook account that manages your Business Page.
5. Grant all requested permissions (required for Messenger access).
6. In the "Select Pages" step, check the box next to your Business Page → click **Continue** → **Done**.
7. Back in GHL Integrations, your Facebook Page should appear as "Connected."

**To connect Instagram:**

After connecting Facebook, Instagram connection is available in the same Integrations panel:

1. Find **Instagram** in the integrations list → click **Connect**.
2. Select the Instagram Business account linked to your Facebook Page.
3. Grant messaging permissions.
4. Confirm the Instagram account shows "Connected."

:::{admonition} Why This Matters
:class: tip
Facebook Messenger is where a significant portion of inbound inquiries from your ad campaigns land. Instagram DMs capture followers who saw a post or story and clicked through. Without these connections, those messages sit in native Facebook/Instagram inboxes where team members need separate logins, conversation history is fragmented, and automation cannot touch them. Connected to GHL, they become first-class contacts in your CRM.
:::

**You'll know you did this right when:** In Settings → Integrations, both Facebook (with your Page name listed) and Instagram (with your account listed) show green "Connected" status.

---

### Step 2: Connect Google Business Messages

1. ⚙️ **Settings** → **Integrations** → find **Google Business Profile** (or Google My Business) → **Connect**.
2. Authorize with the Google account that owns your Google Business Profile.
3. Select your business location from the list → confirm.
4. Back in Integrations, your GBP listing should show "Connected."

**You'll know you did this right when:** Your Google Business Profile listing appears with "Connected" status. Messages sent to your GBP via Google Maps / Google Search will now route to your GHL Conversations inbox.

---

### Step 3: Add the Live Chat Widget to Your Website

1. ⚙️ **Settings** → **Chat Widget** (or look for **Website Chat** in the Integrations panel).
2. Click **Configure Chat Widget**.
3. Customize:
   - **Widget Headline:** "How can we help?" or your brand message
   - **Widget Color:** Match your brand primary color (hex code)
   - **Agent Name and Photo:** Add your name and a professional headshot
   - **Auto-Greeting:** "Hi! We typically respond in under 5 minutes. What can we help you with?"
4. Click **Save**.
5. Click **Get Code** → copy the JavaScript embed code.
6. Paste the code in the `<head>` section of your website (or add it via your website platform's header scripts: WordPress → header.php or a plugin like Insert Headers and Footers; Squarespace → Settings → Advanced → Code Injection).

:::{admonition} Why This Matters
:class: tip
Website chat converts passive visitors into conversations. The GHL chat widget is not a third-party tool that syncs data later — it creates a GHL contact immediately when someone chats, giving you the visitor's name and email before the conversation even starts. The auto-greeting sets the expectation for response time and makes the widget feel like a real person is present, not a bot.
:::

**You'll know you did this right when:** The chat widget appears on your website (open it in a browser after adding the code). Send a test message — it should appear in your GHL Conversations inbox within seconds.

---

### Step 4: Verify Your Phone/SMS Channel

If your A2P 10DLC registration from Chapter 5 is approved:

1. ⚙️ **Settings** → **Phone System** → confirm your provisioned number shows "Active."
2. Navigate to **Conversations** and confirm the SMS channel icon is available in the message compose area.
3. Send a test SMS to yourself: click **+ New Conversation**, select your own number, choose SMS channel, type "Test" → send.
4. Reply from your personal phone — confirm the reply lands in GHL Conversations.

**You'll know you did this right when:** Your provisioned number can send and receive SMS, and the conversation thread appears in GHL Conversations with both outbound and inbound messages shown.

---

### Step 5: Build Your Snippet Library

Snippets are pre-written text blocks you insert into any message with `/` shortcut. You are going to create 8 core snippets that handle your most common reply scenarios.

1. In the left sidebar, click **Conversations** → look for the **Snippets** option (usually in the Conversations settings or under the compose toolbar → three-dot menu → "Snippets").
   
   **Alternative path:** ⚙️ **Settings** → **Conversations** → **Snippets** tab.

2. Click **+ New Snippet** for each of the following:

**Snippet 1 — Initial Response (Fast Reply)**
- Shortcut: `/hi`
- Content: "Hi {{contact.first_name}}! Thanks for reaching out to [Business Name]. I'm [Your Name] — how can I help you today?"

**Snippet 2 — Appointment Booking**
- Shortcut: `/book`
- Content: "I'd love to set up a time to connect! Here's my calendar link so you can grab a spot that works for you: [Calendar URL]. It's a [X]-minute call — completely free, no obligation."

**Snippet 3 — Pricing Inquiry**
- Shortcut: `/price`
- Content: "Great question! Our pricing depends on a few factors specific to your situation. The best way to get an accurate number is a quick 15-minute call where I can learn more about what you need. Want to grab a time? [Calendar URL]"

**Snippet 4 — Not Ready Yet (Nurture)**
- Shortcut: `/nurture`
- Content: "Totally understand — timing is everything. I'll make a note to follow up with you in [timeframe]. In the meantime, feel free to reply to this message anytime with questions. We're always here."

**Snippet 5 — Documents Needed**
- Shortcut: `/docs`
- Content: "To move forward, I'll need the following: [list your required documents]. The easiest way to send them is [method]. Once I have those, we can typically [next step] within [timeframe]."

**Snippet 6 — Closed Won — Handoff to Onboarding**
- Shortcut: `/won`
- Content: "Welcome aboard, {{contact.first_name}}! I'm so excited to get started. Your onboarding coordinator will reach out within 24 hours with next steps. If you have any questions before then, I'm always reachable here."

**Snippet 7 — Review Request (Manual)**
- Shortcut: `/review`
- Content: "{{contact.first_name}}, it was such a pleasure working with you on this! If you have 60 seconds, a Google review would mean the world to us and help other clients find us: [Google Review Link]. Thank you!"

**Snippet 8 — Out of Office / After Hours**
- Shortcut: `/ooo`
- Content: "Thanks for your message! Our team is currently unavailable but will respond by [next business day/time]. For urgent matters, call [phone number] and leave a voicemail — we'll return your call as soon as possible."

3. Click **Save** after each snippet.

:::{admonition} Why This Matters
:class: tip
Snippets are not shortcuts for lazy replies — they are quality control. Every contact who sends a message gets the same professional, thoughtful, correctly-spelled response regardless of which team member is on duty. They also dramatically reduce the response time lag caused by composing from scratch for common inquiries.
:::

**You'll know you did this right when:** In a Conversations compose window, type `/` and see your snippet shortcuts appear in a dropdown. Click one and confirm it populates the message field with the correct text and merge fields.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 7:

- ☐ Facebook Page connected — shows green "Connected" in Settings → Integrations
- ☐ Instagram connected — Business account linked through Facebook Page
- ☐ Google Business Profile connected — messages routing to Conversations inbox
- ☐ Live chat widget installed on your website — test message appears in GHL inbox
- ☐ SMS channel verified — test SMS sent and reply received (if A2P approved)
- ☐ At least 8 snippets created with shortcut keys
- ☐ `/` trigger tested in compose window — snippets appear in dropdown

You now have a true unified inbox. Every inbound message from every channel lands in one place, and your team can respond consistently with your pre-built snippet library.
:::

::::{dropdown} Troubleshooting Common Issues

**Facebook "Connect" redirects to an error page:**
Clear your browser cache and disable any pop-up blockers. GHL opens the Facebook OAuth flow in a new window — if pop-ups are blocked, the connection fails silently. Allow pop-ups for your GHL domain and try again.

**Instagram shows connected but DMs aren't appearing:**
Instagram DM routing requires that your Instagram account be a Business or Creator account (not Personal) and that it is linked to your Facebook Business Page. Check this in Instagram → Settings → Account → Switch to Professional Account (if needed), then re-link to your Facebook Page.

**Google Business Profile connection succeeds but no messages come through:**
Google Business Messages must be enabled for your GBP listing. In your Google Business Profile Manager, check that messaging is turned on (Profile → Messaging → Enable). Messages typically take 24 hours to start routing after connection.

**Chat widget code was added but the widget doesn't appear on the website:**
Confirm the code is in the `<head>` section (not the `<body>` or `<footer>`). Test in an incognito window (some browser extensions block chat widgets). If using WordPress, confirm the plugin that injects header code is active and not cached — clear your CDN cache.

**Snippets `/` shortcut doesn't trigger in Conversations:**
The shortcut only works in the message compose box within the Conversations module, not in campaign email composers. Type `/` and wait — there may be a brief delay before the popup appears. If no popup appears, check that snippets are created and saved correctly in Settings → Conversations → Snippets.
::::

