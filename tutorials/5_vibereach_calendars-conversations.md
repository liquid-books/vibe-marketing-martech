# Building Your First Calendar and Mastering Conversations in VibeReach

*Part five of the funnel → forms → pipeline → workflow → calendar/conversations series. Your workflow already references "did they book a call?" as an If/Else condition. This tutorial builds the calendar that question evaluates against, wires its notifications to the Conversations inbox, and walks through how to actually live inside Conversations day-to-day on both desktop and mobile. This is the tutorial that turns the system you've built into something you can run from your phone.*

---

## What This Tutorial Assumes

Same curriculum context as before. The earlier tutorials produced:

- **Funnel Part 1 + Part 2** — pages with a working form and qualifying survey, all wired to custom fields on the contact record.
- **Pipeline** — a Kanban board with stages New Lead → Call Booked → Proposal Sent → Won/Lost.
- **Workflow** — automation that tags, creates opportunities, sends emails, waits a day, and branches on whether a call has been booked.

That workflow's If/Else condition (`Has Appointment = TRUE`) is currently waiting for a calendar to evaluate against. We're about to give it one. We're also building the daily-use side of the system — Conversations — so the work that comes *out* of all this automation actually has a place to live where you can read, reply, and act.

This tutorial has two halves:

1. **Calendars** — build a Personal Booking Calendar, wire it into the funnel, configure notifications.
2. **Conversations** — tour the unified inbox, learn the four-panel layout, master daily use on desktop and mobile.

The two halves connect because every calendar booking generates conversations (confirmation, reminders, follow-ups, the actual back-and-forth with the prospect) and every reply flows into the same inbox. Calendars are the input. Conversations are where you live.

---

## Part One: Calendars

### Why the Calendar Matters More Than It Looks

Most people treat a booking calendar as a utility — a way for someone to pick a time. That framing undersells it. The calendar is the single highest-friction transition in your entire funnel. A prospect went from "I'm curious" all the way to "I'm willing to spend twenty minutes of my actual day with this person." If anything goes wrong in those last few clicks — the available times look terrible, the form is too long, the confirmation never arrives, the reminder lands in spam, the meeting link is broken — the deal dies.

A well-built calendar prevents all of those failures by default. A poorly built one creates them. Same underlying tool, opposite outcomes. The difference is fifteen minutes of setup.

There's also a bigger framing point: the calendar isn't just a scheduling form. It's a *conversion event* in your CRM. Every booking creates an appointment record attached to the contact, which can trigger workflows, move pipeline stages, fire confirmation messages across multiple channels, sync to your personal Google or Outlook calendar, and put a real meeting on your real day. The booking is the moment a lead becomes a meeting. Treat it accordingly.

### Calendar Types — Which One to Pick

VibeReach offers several calendar types. You need to know which one fits before you create anything.

- **Personal Booking** — one person, one calendar, 1-to-1 meetings. Best for solo operators, consultants, and anyone running their own discovery calls. *This is what we're building.*
- **Round Robin** — multiple team members share one booking link, appointments distribute across the team based on availability or fair rotation. Best for sales teams of 2+ people. (Personal Booking is essentially Round Robin with one user — same features, single-user limit.)
- **Class / Event** — multiple attendees can book the same time slot. Best for webinars, group sessions, classes. Note: this type doesn't support Zoom or Google Meet auto-generation, so don't use it for one-to-many video calls unless you handle the link separately.
- **Collective** — all assigned users must be available for a slot to appear bookable. Best for joint calls and co-hosted sessions.
- **Service** — service + staff selection, like "pick a haircut, then pick which stylist." Best for service businesses with multiple appointment types.

For our scenario — a solo consultant running 1:1 CRM discovery calls — Personal Booking is the right pick. Round Robin becomes the right pick the day you hire your first sales rep.

### Step 1 — Create the Calendar

1. Go to **Calendars** in the left navigation (sometimes labeled **Calendars & Appointments**).
2. Click **Calendar Settings** (the gear/configuration tab — exact label varies by UI version).
3. Click **+ Create Calendar** or **+ New Calendar.**
4. From the calendar-type picker, choose **Personal Booking.**
5. The setup wizard opens.

### Step 2 — Configure the Basics

The setup screen walks you through several fields. Take a minute on each — the defaults are usually wrong for you specifically.

**Calendar Name** — visible to bookers when they're choosing a time. Make it specific: *"CRM Setup Discovery Call — 20 min."* Not "Calendar 1." Not "Book a Call." The name doubles as part of the page title and as the entry in workflow pickers later. Be precise.

**Calendar Owner / Assigned User** — this is the user whose availability the calendar reflects. For Personal Booking it's just one person — most likely you. The calendar will pull this user's connected Google or Outlook calendar (if connected) for conflict-checking, and any Zoom integration uses this user's Zoom account.

**Custom URL Slug** — the part of the booking URL after your domain. VibeReach generates one automatically from the calendar name; you can edit it to something cleaner like `book-call` or `crm-setup`. Keep it short. Lowercase. Hyphens, not spaces. The slug is what shows up in the public booking URL, so make it something you'd be happy to read out loud on a podcast.

**Meeting Duration** — for a discovery call, 20 to 30 minutes is the sweet spot. Long enough to actually qualify and connect, short enough that you can take five of them in a day without burning out. Don't default to 60 — most consultative conversations only need 20-30 if you've done qualification work upstream (which you have, because Part 2 built the survey).

**Meeting Location** — choose Zoom, Google Meet, phone call, or a custom location. Zoom and Google Meet auto-generate a unique meeting link per booking and inject it into the confirmation email. Phone means the meeting link slot in the email shows your number. Custom is for in-person ("our office at...") with a static text value. For a remote consulting call, pick Zoom or Google Meet.

**Linked / Conflict Calendars** — this is the toggle that prevents double-booking. Connect your personal Google or Outlook calendar at **Settings → Integrations** if you haven't already, then in the calendar settings make sure that connected calendar is set as a *conflict calendar*. Now if you have a 3pm dentist appointment blocked on your personal Google calendar, VibeReach will hide the 3pm slot on the booking page automatically. This is the single most important toggle on the entire setup screen. Without it, you will end up double-booked the first week.

### Step 3 — Configure Availability

Click into the **Availability** tab inside the calendar settings. This is where you tell the booker which days and hours appointments can be scheduled.

**Working Hours** — toggle on the days you accept bookings. For a typical service business that's Monday through Friday. For each active day, set start and end times. The instinct is to maximize availability (9 AM - 7 PM, Mon-Sat) — resist it. A wider availability window doesn't get you more bookings; it just means more late-night and weekend calls. Pick the hours you actually want to be working and stick to them. 10 AM to 4 PM, Tuesday through Thursday, is a fine answer if that's the reality. Bookers will work around your schedule, not the other way around.

**Time Zone** — set to your local time zone. VibeReach will automatically convert and display times in the *booker's* local time zone on the public page, so a Florida visitor and a California visitor each see times in their own zone. This works perfectly as long as your owning user's time zone is correct.

**Buffer Time** — how long between back-to-back meetings. Set 10-15 minutes. Without buffer, you finish one call and immediately start another with no time to take notes, drink water, or recover. Your meeting quality collapses by mid-afternoon. Buffer is non-negotiable.

**Minimum Scheduling Notice** — how far in advance someone can book. Set 4-24 hours depending on how prepared you need to be. A 4-hour minimum prevents the "they booked you for an hour from now and you're not in front of a computer" disaster.

**Maximum Booking Window** — how far into the future bookings can be made. 14 to 30 days is typical. Too short and motivated leads can't grab the slot they want; too long and you have a calendar full of cold leads who forgot they booked.

**Maximum Bookings Per Day** — cap this. Even if you have 10 slots available, set a daily max of 3-5 calls. Past that point your performance drops and the system is doing you no favors by stuffing the day.

### Step 4 — Configure the Form on the Calendar

Click the **Forms** or **Booking Form** tab. By default, the calendar uses a generic form that collects Name and Email. You can replace it with a custom form — including the qualifying survey you built in Funnel Part 2.

There are two paths here:

**Path A (simple):** keep the default form, which collects Name, Email, and Phone. This works fine if you've already qualified the lead through the funnel survey before they reached the booking page. The booking is the conversion event; you don't need to re-qualify.

**Path B (advanced):** attach a custom form with additional fields right at the booking step — a one-line "What do you want to focus on in our call?" question, or a checkbox for "I have an existing CRM I want to migrate from." Use this when the booking page is the *only* place the prospect interacts with you (no funnel survey upstream) and you need qualifying data before the call.

For the curriculum scenario where the survey already lives upstream, Path A is correct. Don't make people fill out the same information twice.

### Step 5 — Configure Notifications (The Bridge to Conversations)

Click the **Notifications** tab. This is where the calendar half of the tutorial meets the conversations half. Every appointment event — booked, confirmed, rescheduled, cancelled, reminded, followed up — can fire a notification across one or more channels (email, SMS, WhatsApp, in-app). All of those notifications land in Conversations, attached to the contact's thread.

The six notification types you can configure:

- **Appointment Booked (Unconfirmed)** — sent immediately when someone books, before any approval step.
- **Appointment Booked (Confirmed)** — sent when an appointment is auto-confirmed (or manually approved).
- **Reschedule** — sent when the appointment time changes.
- **Cancellation** — sent when the appointment is cancelled.
- **Reminder** — sent before the appointment based on a time you set (e.g., 24 hours before, 1 hour before).
- **Follow-Up** — sent after the appointment based on a time you set.

For each type, you can configure recipients separately: the **Contact** (the booker), **Guests** (if they invited others), **Assigned User** (you), and any **Additional Emails / Phone Numbers** you specify.

Here's the configuration I recommend for a discovery call:

1. **Appointment Booked (Confirmed)** — Email to Contact AND Assigned User. Customize the contact email to include the meeting link, what to prepare, and a one-line "if you need to reschedule, here's the link." The user notification ensures *you* get an internal alert.
2. **Reminder** — Email to Contact 24 hours before, SMS to Contact 1 hour before. The 24-hour email gives them time to prep; the 1-hour SMS is the "this is happening" nudge that prevents no-shows.
3. **Cancellation** — Email to Contact AND Assigned User. So both sides have a record.
4. **Follow-Up** — Email to Contact 2 hours after. Brief thank-you, summary of next steps, and the calendar link in case they want to book a second call.

Use the variables VibeReach makes available — `{{contact.first_name}}`, `{{appointment.start_time}}`, `{{appointment.time_zone}}`, `{{appointment.meeting_location}}` — so each message is personalized without you writing anything custom per booking.

**One important note about workflow conflicts.** If you also have a workflow (from the workflow tutorial) using the **Customer Booked Appointment** trigger to send confirmations, you'll end up with *two* confirmation messages — one from the calendar settings, one from the workflow. Pick one or the other. The cleaner pattern is: handle confirmations and reminders in the calendar notification settings (because it's faster to configure and stays local to the calendar), and handle deeper follow-up sequences and pipeline movements in workflows (because those need branching logic the calendar settings can't provide).

### Step 6 — Save, Get the Link, and Plug It Into the Funnel

Click **Save Calendar.** The calendar is now live. VibeReach generates a hosted booking URL — something like `yourdomain.com/widget/booking/crm-setup` — that you can share anywhere.

Now back to the funnel from Funnel Part 2. The survey's final slide had a placeholder calendar invite. Replace it with this real calendar:

1. Open your funnel, navigate to the survey's final slide (or the thank-you page, depending on where you placed the booking step).
2. Drop a **Calendar** element onto the page using the plus sign.
3. In the right-hand settings, select your new "CRM Setup Discovery Call — 20 min" calendar from the dropdown.
4. Save the page.

The embedded calendar widget now loads inline on the page. Bookers can pick a time without leaving your funnel. The widget is mobile-responsive by default, which matters because most opt-ins these days happen on a phone.

### Step 7 — Test Booking a Real Appointment

Same drill as every other tutorial — don't trust it until you've watched it work end-to-end. Open the funnel in an incognito window, fill out the form, take the survey, get routed to the calendar (if your survey logic from Part 2 was set up that way), pick a time, complete the booking.

Watch what happens:

1. Within a few seconds, the appointment appears on the contact's record in VibeReach.
2. The contact's pipeline opportunity moves from *New Lead* to *Call Booked* (if you configured the calendar to update the pipeline stage on booking — there's a Pipeline + Stage selector on the Confirmation tab of the calendar settings worth checking).
3. The confirmation email arrives in the test inbox within a minute.
4. The appointment shows up on your personal Google or Outlook calendar via the two-way sync.
5. A new entry appears in your **Conversations** inbox under that contact's thread — the outbound confirmation email is logged there.
6. If you have the LeadConnector mobile app installed, you get a push notification.

If any of those don't happen, troubleshoot the specific failure point. The Conversations thread is the easiest place to see what fired and what didn't — every outbound message and every inbound reply is logged there in order.

---

## Part Two: Conversations

### Why Conversations Is the Tool You'll Use Every Day

Of all the modules in VibeReach, Conversations is the one you'll have open more than any other. The funnel builder, the pipeline editor, the workflow builder — those are setup tools. You build something, you launch it, you check on it occasionally. Conversations is the operations tool. It's where the actual back-and-forth with prospects and customers lives. It's where you'll spend the morning. It's where you'll respond between meetings. It's where the mobile app will buzz at you.

Get fluent in Conversations and the whole platform feels fast. Stay clumsy in Conversations and the whole platform feels heavy, no matter how well-built the rest is.

### The Concept: One Thread Per Person, All Channels Combined

Most CRMs separate communication by channel — emails over here, texts over there, social DMs in a third place. VibeReach doesn't. Every message to or from a contact, regardless of channel, lives in a single chronological thread attached to that contact. SMS replies, email exchanges, Facebook Messenger DMs, Instagram DMs, WhatsApp messages, internal notes, even call logs — all in one timeline, top to bottom.

This is more useful than it sounds. Imagine: a prospect emails you on Monday, you reply, they text you Tuesday, you SMS back, they DM you on LinkedIn Friday. In every other CRM you'd have to piece those exchanges together from three apps and your own memory. In Conversations, that's one thread, scroll up to see Monday's email, scroll down to see Friday's DM, full context in five seconds.

Every workflow message and every calendar notification also lands in this thread. So when you open a contact, you see *everything* — your automation history, your personal messages, their replies, your notes about them — in chronological order. That's the unified inbox.

### Step 1 — Open Conversations and Get Oriented

Click **Conversations** in the left navigation. The redesigned Conversations experience uses a four-panel layout. Spend a minute on what each panel does — once you understand the geography, the rest is fast.

**Far Left — Inbox Panel.** Top-level navigation between inboxes and folders. "All" shows every conversation. "Mine" shows ones assigned to you. "Unread" shows ones you haven't read. There are also folders for starred, archived, and any custom Saved Views you've created.

**Second Column — Chat List Panel.** A scrollable list of every conversation matching your current inbox or filter. Each row shows the contact name, a preview of the most recent message, an icon for the channel (SMS, email, Facebook, Instagram, etc.), and an unread indicator if there are messages you haven't seen. At the top of this panel: a select-all checkbox for bulk actions (mark read/unread, star/unstar, delete), a sort toggle (newest/oldest activity), and a filter icon.

**Middle — Message History Panel.** The active conversation thread, top-to-bottom in chronological order. Every message regardless of channel shows here with timestamp, channel icon, and direction (inbound or outbound). You can filter the timeline at the top to show only specific channels (only emails, only SMS, only internal notes) when you need to scan a long history quickly.

**Right — Contact Context Panel.** The contact's full record alongside the conversation — name, email, phone, tags, pipeline stage, custom fields, opportunity history, and a small action menu for adding notes, creating tasks, or moving the contact in the pipeline without leaving the thread. The right panel updates live: if you edit the contact's email here, the composer at the bottom updates immediately to use the new address.

That's the layout. Inbox → list → thread → context, left to right.

### Step 2 — Read a Thread and Reply

Click any conversation in the chat list. The message history opens in the middle panel. Scroll up to read the history if you want context, or just start typing in the composer at the bottom.

**The composer is multi-channel.** At the top of the composer there's a channel selector — click it to switch between SMS, Email, WhatsApp, Facebook (if connected), Instagram (if connected), and **Internal Comment** (a private note that only your team sees, never the customer). This is the part most beginners miss: you don't need to leave the conversation to switch how you reply. Got an SMS but the answer needs to be a long email? Switch the composer to Email, type the email, send, and the email appears in the same thread alongside the SMS.

**Internal Comments are gold.** When you select Internal Comment as the channel, you can type a private note that the customer never sees. Use @mention to tag a teammate who should know about this lead. The note stays in the thread forever as part of the contact's history. Use internal comments for things like *"Spoke on the phone, mentioned they had budget concerns about the $5k tier — push the $2,500 option next time"* — context that the next person looking at this thread (or future-you) desperately needs.

**Quick replies and snippets.** If you find yourself typing the same answer ten times a day (your address, your hours, a standard pricing summary), save it as a snippet. The composer supports snippets/canned responses that you can insert with a click.

**Attachments and pasted images.** Drag-and-drop files into the composer, or paste an image directly from your clipboard (Cmd+V on Mac, Ctrl+V on Windows). The attachment sends with the message.

### Step 3 — Use Filters to Cut Through Volume

The chat list can get long fast. The filter icon at the top of the chat list opens a multi-criteria filter panel:

- **Channel** — show only SMS, only email, only Facebook, etc. Or exclude specific channels.
- **Tags** — show conversations with contacts tagged a certain way (e.g., `crm-funnel-lead` from your workflow).
- **Owner** — show only conversations assigned to a specific user.
- **Date range** — show only conversations active in a window.

Critically, filters support **AND / OR logic.** *"Show me conversations from contacts tagged `crm-funnel-lead` AND with unanswered SMS messages from the last 7 days."* That kind of multi-criteria filter is how you find the leads that need attention now versus the ones that don't.

Once you've built a useful filter combination, save it as a **Saved View.** Your custom views appear in the inbox panel on the far left for one-click access. Build a view for "Hot Leads — Last 24 Hours" or "Unanswered Replies" or "Customers — VIP Tag" and you'll never lose another high-priority message.

### Step 4 — Master the Daily Habit

Conversations is at its most useful when you treat it like an inbox you process to zero, not a feed you scroll. Here's the rhythm that works:

**Morning (15-20 minutes):**
1. Open Conversations, filter to "Unread."
2. Read every unread thread. For each one, decide: reply now, reply later (snooze with a star), or done (mark read).
3. For threads that need a reply later in the day, star them and move on.
4. By the end of this session, Unread is at zero.

**Throughout the day:**
- Push notifications from the mobile app handle the rest. Each new message buzzes; you reply from the app or note "deal with it on desktop."
- Internal notes for context as you go. Future-you will thank present-you.

**Evening (10 minutes):**
- Open the starred view. Knock out any starred threads that haven't been resolved.
- Process any remaining unread.
- Inbox to zero.

This pattern keeps you responsive without keeping you tethered. Most messages get answered within hours; nothing gets lost in a feed you scroll past.

---

## Part Three: The Mobile App

### Why the Mobile App Is the Whole Point

Here's the thing nobody tells you when you sign up for VibeReach: the mobile app is what makes the platform genuinely useful. The desktop interface is where you *build* things; the mobile app is where you *run* the business on the days when you're not at your desk. Which is most days.

The mobile app is called **LeadConnector** in the App Store and Google Play. It's a "graylabel" app — neutrally branded so it works for any VibeReach-style platform without revealing the underlying tech to your end users. Some businesses commission their own fully white-labeled mobile apps under their own brand name, but for our purposes LeadConnector is the app you download, and it works seamlessly with everything you've built in VibeReach.

### Step 1 — Install and Connect

1. On your phone, search for **LeadConnector** in the App Store (iOS) or Google Play (Android).
2. Install. Open the app.
3. Sign in using the same email and password you use for the desktop platform. If you're a user in multiple sub-accounts, the app shows all of them in a switcher at the top — incoming calls and messages from any sub-account will surface in the unified inbox.

If you don't see the install link, you can also find it inside VibeReach under **Mobile App** in your sub-account, which gives you a direct App Store / Play Store deep link.

### Step 2 — Configure Push Notifications

Push notifications are the difference between the mobile app being useful and being useless. Out of the box, they may not be fully on. Walk through this:

1. On your phone, open Settings → LeadConnector → Notifications. Enable all notification types (alerts, banners, sounds, badges).
2. Inside the LeadConnector app, open the settings/profile area and confirm push notifications are enabled for the categories you care about — messages, missed calls, new bookings, new leads.
3. If you use Do Not Disturb, add LeadConnector to your allowed apps so business notifications come through.
4. **Disable battery optimization for LeadConnector** on Android. Otherwise the OS will throttle the app in the background and notifications get delayed by hours. iOS has its own background refresh setting to check.

A common gotcha: in VibeReach, the user account assigned to your sub-account needs to be the *same* user that's signed into the mobile app. If the wrong user is assigned to a phone number or calendar, push notifications for calls to that number or bookings on that calendar won't reach you.

### Step 3 — Daily Mobile Workflow

The bottom navigation bar in the LeadConnector app gives you quick access to the modules you'll actually use on the go:

- **Notifications** — your real-time alert feed
- **Conversations** — the same unified inbox as desktop, fully usable on mobile
- **Calendar / Appointments** — see today's schedule, see upcoming bookings, manually book or reschedule appointments
- **Contacts** — search any contact, view their full record, send a message, log a note
- **Plus icon** — quick actions to create a new SMS, email, contact, opportunity, or appointment from anywhere in the app
- **Lightning bolt icon** — quick actions for sending a review request, creating an invoice, making a call

What the mobile app is genuinely great for:

**Receiving inbound calls** through your VibeReach phone number directly on the app — the prospect calls your business number, the app rings on your phone, you answer in-app, the call is logged in Conversations automatically.

**Responding to SMS from your business number** without ever exposing your personal cell. The customer texts your business number; the text shows up as a push notification; you tap it, reply in the app, and the entire exchange is logged in Conversations.

**Booking-related management** — quickly checking what's coming up, rescheduling a call from the parking lot when traffic is bad, marking someone as a no-show after they don't appear.

**Quick contact lookup** — between meetings, search a name, see their full record including the survey answers they gave you in Funnel Part 2, prep for the next call in 30 seconds.

**On-the-go sales** — a prospect texts asking for an invoice, you tap into the conversation, generate an invoice, send it from the same thread, and the platform logs it as a sent invoice attached to the contact. All while waiting in line for coffee.

The mobile app is what lets you not be at your desk and still be in business.

---

## Closing Thought — Five Tutorials, One Daily Workflow

You now have five connected systems:

1. **Funnel Part 1** — pages that capture attention
2. **Funnel Part 2** — forms and surveys that collect mapped data
3. **Pipeline** — Kanban board for tracking deals
4. **Workflow** — automation that runs follow-up
5. **Calendars + Conversations** — booking and the unified inbox that holds every exchange

Here's how a single day actually flows once all five are in place:

You wake up. Your phone has three push notifications: two new opt-ins from overnight, one booked call for this afternoon. You open Conversations on your phone, scan the new leads, send a quick personal SMS to one who looks high-intent ("Saw your form — looking forward to chatting"). The other already got the welcome email from your workflow, which you can see in their thread.

You commute to your office or co-working space. On the train, you open the LeadConnector app, look at your booked call's contact record, scroll through the survey answers from Funnel Part 2 to prep, and add an internal note: *"This person mentioned they've been burned by Salesforce — lead with the simplicity angle."*

You arrive at your desk. Open Conversations on desktop. The wider four-panel layout makes it easy to reply to the threads from this morning that needed longer responses. Then you take the booked call — at the end, you drag their pipeline card from Call Booked to Proposal Sent.

That evening, the workflow you built three months ago fires the proposal follow-up email automatically. The contact opens it, replies, and you see the reply in Conversations on your phone while making dinner. You write back: "Yes, let's set up next week — here's my calendar link." They book a second call from your phone screen.

That's the system. Not five separate tools, not a stack of products to learn. One integrated daily workflow where every part feeds the next. Build it well, run it deliberately, watch what compounds over months.

You've built the front end (funnel), the data layer (forms), the organization (pipeline), the automation (workflow), and now the daily operating system (calendars + conversations). Everything that follows — Memberships, Reputation Management, Reporting, Voice AI, Payments — bolts onto this foundation. You can learn them one at a time as you need them. The hard part — the part that holds the whole system together — is done.

Go run a real lead through the entire flow end-to-end. Watch each step do its job. The first time you take a booked call where the prospect was captured by the funnel, qualified by the survey, dropped onto the pipeline, nurtured by the workflow, scheduled by the calendar, and reminded by SMS — all without you doing anything except show up to the meeting — is the moment VibeReach stops being software you're learning and starts being how you run your business.

---

*Sources: HighLevel Support Portal — "How to Set Up a Personal Booking Calendar," "Round Robin Calendars: The Setup Guide," "Calendars & Services: SMS, Email & In-App Notifications," "Workflow Trigger: Customer Booked Appointment," "Getting Started with the New Conversations Experience," "Mobile Apps Overview," "Using Conversation AI on Mobile," and HighLevel platform documentation on the LeadConnector mobile app. Verified May 2026.*
