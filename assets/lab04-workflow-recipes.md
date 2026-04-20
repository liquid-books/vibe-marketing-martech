# Workflow Recipe Library — Lab 4 Reference
## The 12 Workflows Every Business Should Have Running

Use these recipes as blueprints when building your workflows in VibeReach. Each recipe lists the trigger, conditions, and actions in order.

---

### 🔵 Recipe 1 — New Lead Welcome Sequence
**Purpose:** Instantly engage every new lead the moment they enter your system.

| Step | Type | Details |
|------|------|---------|
| Trigger | Form Submitted | Any opt-in form |
| Action 1 | Add Tag | `new-lead` |
| Action 2 | Send SMS | "Hi {{contact.first_name}}! Thanks for reaching out to {{location.name}}. We'll be in touch within the hour. Reply STOP to opt out." |
| Action 3 | Send Email | Welcome email with lead magnet delivery or next step |
| Action 4 | Create Task | Assign to sales rep: "Call {{contact.first_name}} within 1 hour" |
| Action 5 | Wait | 1 hour |
| Action 6 | If/Else | IF Task completed → End. IF not → Send internal Slack/email alert |

---

### 🔵 Recipe 2 — Missed Call Text-Back
**Purpose:** Recover every missed call with an instant SMS — the highest-ROI automation ever built.

| Step | Type | Details |
|------|------|---------|
| Trigger | Missed Call | Any inbound call not answered |
| Action 1 | Send SMS | "Hi! Sorry we missed your call at {{location.name}}. We'd love to help — reply here or call us back at {{location.phone}}." |
| Action 2 | Add Tag | `missed-call` |
| Action 3 | Create Opportunity | Pipeline: Sales | Stage: New Lead |

---

### 🔵 Recipe 3 — Appointment Reminder Sequence
**Purpose:** Eliminate no-shows with a 3-touch reminder sequence.

| Step | Type | Details |
|------|------|---------|
| Trigger | Appointment Booked | Calendar event created |
| Action 1 | Send Email | Confirmation email with date/time/location/prep instructions |
| Action 2 | Wait | Until 24 hours before appointment |
| Action 3 | Send SMS | "Reminder: You have an appointment tomorrow at {{appointment.time}} with {{location.name}}. Reply C to confirm or R to reschedule." |
| Action 4 | Wait | Until 2 hours before appointment |
| Action 5 | Send SMS | "See you in 2 hours! {{location.address}}. Questions? Just reply here." |

---

### 🔵 Recipe 4 — No-Show Recovery
**Purpose:** Re-engage prospects who booked but didn't show.

| Step | Type | Details |
|------|------|---------|
| Trigger | Appointment Status Changed | Status = No Show |
| Action 1 | Add Tag | `no-show` |
| Action 2 | Wait | 30 minutes |
| Action 3 | Send SMS | "We missed you today, {{contact.first_name}}. Life happens — let's find another time that works. Here's my calendar: [link]" |
| Action 4 | Wait | 2 days |
| Action 5 | Send Email | "Still interested?" email with rebooking link |
| Action 6 | Create Task | "Follow up call — no-show recovery" |

---

### 🔵 Recipe 5 — Review Request (Post-Service)
**Purpose:** Systematically collect Google reviews after every completed job.

| Step | Type | Details |
|------|------|---------|
| Trigger | Tag Applied | `job-complete` OR Opportunity Stage = Closed Won |
| Action 1 | Wait | 2 hours (let the warm feeling set in) |
| Action 2 | Send SMS | "Thank you for choosing {{location.name}}! If we did a great job, would you mind leaving us a quick Google review? It means the world to us: [review link]" |
| Action 3 | Wait | 3 days |
| Action 4 | If/Else | IF review received (tag `reviewed`) → End. IF not → Send Email follow-up |

---

### 🔵 Recipe 6 — Lead Nurture Drip (14-Day)
**Purpose:** Stay top of mind for leads who aren't ready to buy yet.

| Step | Type | Details |
|------|------|---------|
| Trigger | Tag Applied | `not-ready` OR Stage = Qualified (no activity 3 days) |
| Action 1 | Send Email | Day 1: Value email — tip, insight, or case study |
| Action 2 | Wait | 3 days |
| Action 3 | Send Email | Day 4: Social proof — testimonial or result story |
| Action 4 | Wait | 3 days |
| Action 5 | Send SMS | Day 7: "Quick check-in" — one question, conversational |
| Action 6 | Wait | 4 days |
| Action 7 | Send Email | Day 11: Objection-handling email ("You might be wondering...") |
| Action 8 | Wait | 3 days |
| Action 9 | Send Email | Day 14: Soft CTA — "Ready when you are" with booking link |
| Action 10 | Add Tag | `nurture-complete` |

---

### 🔵 Recipe 7 — Pipeline Stage Notification
**Purpose:** Alert the right person the moment an opportunity advances.

| Step | Type | Details |
|------|------|---------|
| Trigger | Pipeline Stage Changed | Stage = Verbal Commit |
| Action 1 | Send Internal Email | Notify sales manager: "{{contact.full_name}} just hit Verbal Commit — send the contract NOW." |
| Action 2 | Create Task | "Send contract to {{contact.full_name}} — do not delay" (Due: today) |
| Action 3 | Add Tag | `verbal-commit` |

---

### 🔵 Recipe 8 — Reactivation Campaign (Cold Leads)
**Purpose:** Re-engage contacts who went cold 30+ days ago.

| Step | Type | Details |
|------|------|---------|
| Trigger | Smart List Membership | "Cold Leads — No Activity 30 Days" |
| Action 1 | Send SMS | "{{contact.first_name}}, it's been a while! We've added [new offer/update] since we last spoke. Worth a quick conversation? Reply YES and I'll reach out." |
| Action 2 | Wait | 5 days |
| Action 3 | If/Else | IF replied → Create task "Hot reactivation — call now". IF not → Send Email |
| Action 4 | Wait | 7 days |
| Action 5 | If/Else | IF still no response → Add tag `long-term-nurture` → Exit |

---

### 🔵 Recipe 9 — Document Sent / Awaiting Signature
**Purpose:** Follow up on unsigned contracts automatically.

| Step | Type | Details |
|------|------|---------|
| Trigger | Document Status | Sent (not yet signed) |
| Action 1 | Wait | 24 hours |
| Action 2 | Send SMS | "Hi {{contact.first_name}} — just checking that you received the agreement we sent. Any questions before you sign?" |
| Action 3 | Wait | 48 hours |
| Action 4 | If/Else | IF signed → Tag `signed` + trigger onboarding. IF not → Create task "Call about unsigned contract" |

---

### 🔵 Recipe 10 — Onboarding Kickoff
**Purpose:** Deliver a structured, automated first week for new clients.

| Step | Type | Details |
|------|------|---------|
| Trigger | Tag Applied | `client-new` |
| Action 1 | Send Email | Welcome email + portal access + what to expect |
| Action 2 | Create Task | "Book kickoff call with {{contact.first_name}}" |
| Action 3 | Wait | 1 day |
| Action 4 | Send SMS | "Welcome to the family, {{contact.first_name}}! Your kickoff call is the first step — has someone reached out to schedule?" |
| Action 5 | Wait | 3 days |
| Action 6 | Send Email | "Getting started" resource email with top 3 things to do first |

---

### 🔵 Recipe 11 — Birthday / Anniversary Message
**Purpose:** Build loyalty with a personal touch on key dates.

| Step | Type | Details |
|------|------|---------|
| Trigger | Date/Time | Contact's birthday field (annually recurring) |
| Action 1 | Send SMS | "Happy Birthday, {{contact.first_name}}! 🎉 From all of us at {{location.name}} — hope it's a great one." |

---

### 🔵 Recipe 12 — Referral Request (Post-Win)
**Purpose:** Turn happy clients into your best lead source.

| Step | Type | Details |
|------|------|---------|
| Trigger | Opportunity Stage | Closed Won |
| Action 1 | Wait | 7 days |
| Action 2 | Send Email | "You're exactly the kind of client we love working with — do you know anyone else who could use [service]? We'll make sure they're taken care of." |
| Action 3 | Add Tag | `referral-ask-sent` |
| Action 4 | Create Task | "Follow up on referral ask" (5 days) |

---

## 📋 Lab 4 Build Assignment

Using these recipes as your reference, build the following in VibeReach:

**Required Build:**
1. **Recipe 1** — New Lead Welcome Sequence (with SMS, email, task, and Slack notification)
2. **Recipe 2** — Missed Call Text-Back
3. **One additional recipe** of your choice

Each workflow must be tested using a test contact before submission.
