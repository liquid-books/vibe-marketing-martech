# Connecting Your GoDaddy Domain to VIBE: Complete Step-by-Step Guide

This guide walks you through **three separate connections** you'll make between your GoDaddy domain and VIBE (your VIBEreach.IO super account). Each one serves a different purpose — and you'll want all three set up properly before you start building real campaigns.

> **Heads up on naming:** VIBE is your white-labeled platform. Under the hood, some infrastructure names will still appear as you click through — specifically **LeadConnector** (when authorizing GoDaddy) and **Mailgun** (in your email DNS records). That's normal and expected; those are the underlying services VIBE rides on top of. Just don't be thrown off when you see them.

---

## What You're Actually Setting Up

Before clicking anything, understand the three connections — they're independent, and you can do them in any order:

| # | Connection | What It Does | Subdomain to Use |
|---|------------|--------------|------------------|
| 1 | **Website / Funnel domain** | Lets your funnels and websites live at `yourdomain.com` or `www.yourdomain.com` instead of VIBE's default `*.hlpages.co` URL | Root + `www` (e.g., `martechprimer.com` and `www.martechprimer.com`) |
| 2 | **Dedicated email sending domain** | Lets your emails come *from* your domain so they pass SPF/DKIM/DMARC and land in inboxes | A fresh subdomain like `mail.martechprimer.com` or `mg.martechprimer.com` |
| 3 | **(Optional) Client portal / branded links** | White-labels VIBE system URLs with your brand | Subdomain like `app.martechprimer.com` or `portal.martechprimer.com` |

> **Critical rule on email:** Never use your root domain for sending. Always use a fresh subdomain. If a deliverability problem ever happens, your root domain's reputation stays clean. This is non-negotiable.

---

## Before You Begin — Quick Checklist

- [ ] You have your **GoDaddy login** (username + password, plus 2FA device if enabled)
- [ ] You have a **VIBE sub-account** (not the agency-level account — you connect domains at the sub-account / location level)
- [ ] You know your **VIBE admin login**
- [ ] You will work in **one browser, in different tabs** — VIBE in one tab, GoDaddy in another tab of the *same* browser
- [ ] You have **15–30 minutes** of focused time
- [ ] You've decided which subdomains you'll use (write them down now)

> **⚠️ Same browser, different tabs — this matters more than it sounds.**
> A common mistake is having VIBE open in one browser (say Chrome) while GoDaddy is open in a different browser (Safari, Firefox, Edge), or in a different Chrome profile/user. When you click **Authorize** in VIBE, it opens a new tab that needs to talk to your active GoDaddy session. If GoDaddy is signed in elsewhere — different browser, different profile, incognito vs. regular — the OAuth handshake either breaks, asks you to log in again from scratch, or silently authorizes the wrong account.
>
> **Before you start, make sure:**
> - Both VIBE and GoDaddy are open in the **same browser**.
> - You're on the **same Chrome/Safari/Firefox profile** for both (check the profile avatar in the top-right corner).
> - You're not in **incognito/private mode** on one and regular mode on the other.
> - You're logged into the **correct GoDaddy account** — the one that owns `martechprimer.com`. If you have multiple GoDaddy accounts, this is exactly where things go wrong.
>
> Easiest sanity check: in your browser, open one tab to `app.vibereach.io` and another to `dcc.godaddy.com`. Confirm you can see both accounts logged in correctly *before* you start the Authorize flow.

---

## Pre-Flight: Clean Up Existing A Records in GoDaddy

**Do this before you start Part 1.** When you registered `martechprimer.com`, GoDaddy almost certainly auto-created A records pointing your root domain (`@`) to a GoDaddy parking page or forwarding service. If those records are still there when you try to connect VIBE, the auto-setup will fail with **"A record conflict. Multiple A records found."** and the Authorize button will be greyed out.

Clear them out now and the rest of the guide runs without interruption:

1. Open a new tab → go to GoDaddy → **Domain Portfolio** → click `martechprimer.com` → click **DNS**.
2. Look at the records list. You'll see multiple rows where **Type = A** and **Name = @**. *(Tip: click the **Filters** button at the top of the DNS list and filter by Type = A to see them all at once and make sure none are hidden by pagination.)*
3. **Delete all of them** (trash icon next to each). Don't worry — VIBE is about to add the correct one back.
4. Save.

### Verify the deletion actually propagated

GoDaddy's parking A records typically have a short TTL (often **600 seconds = 10 minutes**), which means DNS resolvers around the world may still serve the cached "Parked" answer for up to 10 minutes after you delete it. If you jump into VIBE too quickly, you'll hit the **"A record conflict. Multiple A records found."** error even though your GoDaddy DNS panel looks clean.

Wait ~10 minutes, then verify before continuing:

1. Go to **https://dnschecker.org**.
2. Enter `martechprimer.com` in the search field.
3. Set the record type dropdown to **A**.
4. Click **Search**.
5. Look at the global results map:
   - ✅ **Most/all servers return "No records found"** → DNS has propagated. You're clear to continue with Part 1.
   - ⏳ **Some servers still return an IP** (often a GoDaddy parking IP like `50.63.x.x` or `76.223.x.x`) → DNS hasn't fully propagated yet. Wait another 5–10 minutes and re-check.

Only proceed once the dnschecker.org result is mostly or entirely "No records found."

> **Caveat:** If `martechprimer.com` currently serves a live website (not a parking page) that you still want online, those A records are how it's reaching its host. Deleting them will take that site offline until VIBE's record replaces them — usually under a minute once you authorize, but plan accordingly. Screenshot the existing A records first so you can restore them if needed.

> **What to leave alone:** Don't touch CNAME records, MX records (these are for receiving email — deleting them breaks your inbox), TXT records you don't recognize (often Google or Microsoft verification), or NS records (deleting these breaks the entire domain).

---

# Part 1 — Connect Your Domain for Websites & Funnels

There are two paths. **Try Path A first** — it's the modern way and takes about 60 seconds. Path B is the manual fallback.

## Path A: Automatic Connection ("Domain Connect")

VIBE has a feature called **Domain Connect** that talks directly to GoDaddy via API. You authorize it once and it writes the DNS records for you. This is a domain *connection* feature, not a domain *hosting* feature — your domain still lives at GoDaddy, but VIBE is allowed to add the right records automatically.

### Step 1: Log into VIBE

1. Go to **https://app.vibereach.io** (or whichever login URL you've configured for VIBEreach.IO) and sign in.
2. If you have multiple sub-accounts, click into the **specific sub-account** where you want your funnels/websites to live. Domain connections are made at the sub-account level, not at the agency level.

### Step 2: Navigate to Domain Settings

Inside the sub-account, look at the **left-hand sidebar**:

1. Scroll to the bottom and click **Settings** (gear icon).
2. In the Settings menu (also on the left), click **Domains**. Some interfaces label this **Domains & URLs** — they're the same place.

You'll see a page titled "Domains" with a button on the top right.

### Step 3: Add Your Domain

This happens in two stages — first you tell VIBE you're connecting (vs. purchasing or transferring), then you tell VIBE what the domain is *for*.

**Stage 3a — Choose "Connect" instead of "Purchase" or "Transfer":**

On the Domains page you'll see three options — **Purchase domain**, **Transfer-In Domain**, and below them a small line that reads "Or just **Connect a domain**." Here's what each one does:

| Option | When to use it |
|--------|----------------|
| **Purchase domain** | You don't own the domain yet and want to buy it through VIBE (uses VIBE's built-in registrar). Skip this — your domain is already at GoDaddy. |
| **Transfer-In Domain** | You want to move the domain *registration itself* from GoDaddy to VIBE so VIBE manages it end-to-end. **Don't do this** unless you want to leave GoDaddy entirely. Transfers take 5–7 days and trigger a renewal charge. |
| **Connect a domain** | You're keeping the domain at GoDaddy and just want VIBE to use it. **This is the one you want.** ✅ |

Click the blue **"Connect a domain"** link at the bottom of the card (under the Purchase/Transfer buttons).

**Stage 3b — Tell VIBE what the domain is for:**

You're now on a "Connect a domain" page that lists five categories, each with a **Connect** button:

| Category | Purpose | Pick this if... |
|----------|---------|------------------|
| **Funnel/Website/Store/Blog/Webinar** | Public-facing pages | ✅ This is what you want for Part 1 |
| **Email** | Dedicated sending domain (alt path to Part 2) | Use Part 2 of this guide instead |
| **Wordpress** | VIBE's built-in WordPress hosting | Skip unless you're using that feature |
| **Client Portal** | White-label the client-facing portal URL | Optional — see Part 3 note |
| **Branded Domain** | White-label internal system links | Skip for now |

Click **Connect** next to **Funnel/Website/Store/Blog/Webinar**.

**Stage 3c — Enter the domain:**

The page is titled "Connect your domain/sub-domain with Funnels, Websites, Stores, Webinars and Blogs." It has just two things on it: a **Domain** field and a **Continue** button.

1. In the **Domain** field, type your root domain — for example: `martechprimer.com` (no `https://`, no `www.`, just the root).
2. Click **Continue**.

**Stage 3d — Confirm in the modal that pops up:**

A modal titled "**Connect your domain/subdomain**" appears. It has:

- A **Domain URL** field (already filled with `martechprimer.com`)
- A pre-checked checkbox: **"Also add www.martechprimer.com and redirect traffic to martechprimer.com"** with a blue **Recommended** tag
- An **"Add record manually"** link (bottom-left of the modal)
- A blue **Continue** button (bottom-right)

What to do:

1. **Leave the www checkbox checked** — this is the SEO-friendly default. It tells VIBE to also add the `www` subdomain and 301-redirect all `www` traffic to the root.
2. **This modal is also the branch point between Path A and Path B:**
   - Click **Continue** (blue button) → continues with **Path A** (Domain Connect / GoDaddy auto-authorization). Proceed to Step 4 below.
   - Click **"Add record manually"** (bottom-left link) → switches to **Path B** (manual DNS). Skip ahead to *Path B → Step 2: Open GoDaddy DNS Management*.
3. Since we're following Path A, click **Continue**.

### Step 4: Authorize GoDaddy via Domain Connect

VIBE will detect that your domain is at GoDaddy. You'll see an "Authorize" button. Click it to allow the connection (the OAuth screen will say "**LeadConnector**" — that's the underlying service name and is expected).

1. Click **Authorize**.
2. A new browser tab opens to **GoDaddy's login page** (or auto-detects you if you're already signed in).
3. Sign into GoDaddy if prompted.
4. GoDaddy shows a consent screen: "**LeadConnector wants to update DNS records for [your domain]**." Review what records will be added (you'll see CNAME and A records targeting VIBE's backend infrastructure).
5. Click **Connect** (or **Authorize**).
6. **IMPORTANT:** Once GoDaddy says "Authorization Successful," **close that GoDaddy tab** and return to your VIBE tab. Closing it is what tells VIBE to proceed to the verification step.

### Step 5: Confirm Connection — and Skip the "Assign" Page If You're New

Immediately after you close the GoDaddy tab, VIBE shows a **"Congratulations! You can now connect martechprimer.com with a Product"** page. This is VIBE asking which specific funnel, website, store, blog, or webinar should load when someone visits your domain.

**The connection itself is already done at this point.** This page is purely about *assigning* the domain to a piece of content — and that's optional, not required.

**What to do:**

- **If you don't have a funnel or website built yet** (typical for a fresh setup): Click **"Back to Domains"** at the top of the page. Do *not* click "Proceed to finish" — clicking it with an empty "Link domain with funnel" dropdown will either error out or create a stranded linkage you'll have to clean up. Backing out is clean. You'll come back later and assign the domain from inside whatever funnel/website you eventually build (covered in Part 3).
- **If you already have a funnel or website ready:** Pick the **product type** (Funnel/Website/Store/Blog/Webinar), select it from the **Link domain with funnel** dropdown, optionally expand **Additional options** to set a default page, then click **Proceed to finish**.

### Step 6: Wait for Verification

Back on the Domains list, your domain status will change from "Pending" to "Verified" — usually within 5–10 minutes, sometimes up to 24 hours. Once it's Verified, SSL provisions automatically.

✅ **Done.** Skip Path B and jump to **Part 2** (email setup) — you can do that now even before you've built a funnel.

---

## Path B: Manual DNS Connection (Fallback)

Use this if Path A fails, if you don't trust auto-authorization, or if your GoDaddy account is on a less-common region/setup.

### Step 1: Get the DNS Records from VIBE

In VIBE Settings → Domains:

1. Click the **"Connect a domain"** link (bottom of the card, under the Purchase/Transfer buttons — *not* the blue Purchase button).
2. On the next page, click **Connect** next to **Funnel/Website/Store/Blog/Webinar**.
3. Enter your root domain (e.g., `martechprimer.com`) in the **Domain** field and click **Continue**.
4. A modal titled **"Connect your domain/subdomain"** pops up. Leave the **"Also add www..." checkbox checked** (Recommended), then click the small **"Add record manually"** link at the bottom-left of the modal — *not* the blue Continue button.
5. VIBE shows you a screen with the records you need to add. **Keep this tab open** — you'll copy values from here.

You'll see something like this (your exact values will differ):

| Type | Host/Name | Value/Points to | TTL |
|------|-----------|-----------------|-----|
| A | `@` | `XX.XX.XX.XX` (an IP from VIBE's backend) | 1 hour |
| CNAME | `www` | `sites.leadconnectorhq.com` (or similar) | 1 hour |

> The `leadconnectorhq.com` target is the actual infrastructure DNS endpoint — keep it as-is even though it doesn't say "VIBE."

### Step 2: Open GoDaddy DNS Management

1. In a new tab, go to **https://dcc.godaddy.com/control/portfolio** (or sign in at godaddy.com and click **My Products**).
2. From your Domain Portfolio, select the individual domain you want to configure to access the Domain Settings page.
3. Click the **DNS** tab. You're now looking at every DNS record GoDaddy has on file for your domain. This is your command center for all GoDaddy DNS changes.

### Step 3: Clean Up Existing Records (Important)

Before adding new records, look at what's already there:

- If there's an existing **A record with Name `@`** pointing to a GoDaddy parking page or another service, you'll need to **edit it** (pencil icon) to point to VIBE's IP, OR delete it and create a new one. You can only have one A record per host.
- If there's an existing **CNAME with Name `www`**, same thing — edit or delete.
- **Do not touch** MX records (those are for receiving email), TXT records you don't recognize (could be Google verification, etc.), or NS records.

### Step 4: Add the A Record (for the root domain)

1. Click **Add New Record**.
2. **Type:** select **A** from the dropdown.
3. **Name:** type `@` (this means "the root domain itself").
4. **Value:** paste the IP address VIBE gave you (e.g., `XX.XX.XX.XX`).
5. **TTL:** leave default (1 hour) or set to **600 seconds** for faster propagation during setup.
6. Click **Save**.

### Step 5: Add the CNAME Record (for www)

1. Click **Add New Record** again.
2. **Type:** **CNAME**.
3. **Name:** type `www` (just the word www — **not** `www.martechprimer.com`).
4. **Value:** paste the CNAME target exactly (e.g., `sites.leadconnectorhq.com` — no `https://`, no trailing slash, no spaces).
5. **TTL:** 1 hour.
6. Click **Save**.

### Step 6: Verify in VIBE

1. Go back to the VIBE tab.
2. Click **Verify** (or **Check DNS**).
3. DNS changes take 15 minutes to a few hours to propagate globally. You can check propagation status at **https://dnschecker.org** by entering your domain and looking for the records to resolve to the right values worldwide.
4. If it doesn't verify immediately, wait 15–30 minutes and try again. Most verifications complete within an hour.

✅ Once verified, VIBE automatically issues an SSL certificate. Your domain is now ready to host funnels and websites.

---

# Part 2 — Set Up a Dedicated Email Sending Domain

This is **separate** from Part 1 and uses a **different subdomain**. This is the most-skipped step and the #1 reason emails land in spam. Email deliverability depends almost entirely on how well your sending domain is configured — not the platform itself.

## Step 1: Decide on Your Sending Subdomain

Pick a subdomain that **isn't used for anything else**. Common conventions:

- `mail.martechprimer.com`
- `mg.martechprimer.com` (mg = mailgun, the underlying email infrastructure VIBE uses)
- `send.martechprimer.com`
- `email.martechprimer.com`

> **Why a subdomain and not the root?** If something goes wrong with sending — a campaign gets flagged, a list goes cold, anything — the reputation damage is contained to the subdomain. Your root domain (where your website lives and your `you@martechprimer.com` email runs) stays untouched.

## Step 2: Navigate to the Email Domain Settings in VIBE

1. Inside your sub-account, click **Settings** (left sidebar, bottom).
2. Click **Email Services** in the Settings menu (sometimes labeled **Email Service**). You'll land on the **SMTP Service** tab by default.
3. Open the dedicated sending domain setup. You have two ways to get there:
   - **Shortcut:** When you first open Email Services, VIBE shows a popup titled **"Important Notification: Boost Your Email Deliverability!"** with a blue **"Create Dedicated Domain"** button. Click that — it's the fastest path.
   - **Manual:** If you've dismissed the popup, click the **"Dedicated Domain And IP"** button in the **top-right corner** of the page (right next to "+ Add Service"). It looks like a tab but it's actually a button.
4. On the Dedicated Domains screen, click **+ Add Domain** in the top right.

> **Note:** Earlier versions of the VIBE UI had "Dedicated Domain & IP" as a tab next to SMTP Service / Reply & Forward Settings / etc. In the current UI it has been moved to a top-right button. If you don't see a tab named that, look in the top-right corner instead.

## Step 3: Enter Your Sending Subdomain

This happens in two stages — first you enter the subdomain, then VIBE confirms how you want to add the DNS records.

**Stage 3a — Enter the subdomain on the Add new domain page:**

1. The page is titled **"Add new domain"** with the subtitle "Sending from a dedicated domain improves the likelihood of landing in the inbox."
2. In the **Enter Domain Name** field, type your full sending subdomain — for example: `mail.martechprimer.com` (lowercase only).
3. You should see a green confirmation: *"Looks good! Click 'Add & Verify' to proceed."*
4. Click the blue **Add & Verify** button (bottom-right of the card).

**Stage 3b — Confirm in the modal:**

A modal titled **"Connect your domain/subdomain"** pops up with `mail.martechprimer.com` pre-filled and two options at the bottom:

- **Continue** (blue button, bottom-right) → uses Domain Connect to auto-add the records via GoDaddy's API. **This is the recommended path.** Since GoDaddy already trusts the LeadConnector authorization from Part 1, this usually completes without a second login prompt.
- **Add record manually** (link, bottom-left) → skips Domain Connect and shows you the raw DNS records to add yourself. Use this only if Continue fails.

Click **Continue**.

> **No conflict to worry about this time:** Unlike with the root domain in Part 1, `mail.martechprimer.com` is a brand-new subdomain that has zero existing DNS records. There's nothing for VIBE's records to collide with, so the Authorize step should sail through cleanly.

After Continue (or after manual entry), VIBE shows you the records screen with **6 DNS records** for the subdomain:

| # | Type | Host (with root domain) | Purpose |
|---|------|--------------------------|---------|
| 1 | **TXT** | `mail` | **SPF** — `v=spf1 include:spf.leadconnectorhq.com include:mailgun.org ~all`. Tells receivers which servers are allowed to send for you. |
| 2 | **TXT** | `mx._domainkey.mail` | **DKIM** — `k=rsa; p=...` (long key). Cryptographic signature so receivers can verify the email wasn't tampered with. |
| 3 | **CNAME** | `email.mail` | Mailgun click/open tracking. Points to `mailgun.org`. |
| 4 | **MX** (priority 10) | `mail` | Primary bounce/reply receiver. Points to `mxa.mailgun.org`. |
| 5 | **MX** (priority 10) | `mail` | Backup bounce/reply receiver. Points to `mxb.mailgun.org`. |
| 6 | **TXT** | `_dmarc.mail` | **DMARC** — `v=DMARC1;p=none;`. Monitor-only policy, the correct starting point for a new domain. |

> **About the two MX records:** Both at priority 10 — that's intentional. They form a redundant pair: if `mxa` is down, mail still routes via `mxb`. Add both.
> **About `p=none` in DMARC:** Don't change it. Start in monitor-only mode for a few weeks, then upgrade to `p=quarantine` and eventually `p=reject` once you've confirmed SPF/DKIM are passing cleanly.

## Step 4: Add the Records to GoDaddy (Two Paths)

Same as Part 1, you have an automatic path and a manual path. **Try Auto-Configure DNS first.**

### Path A: Auto-Configure DNS (recommended)

At the bottom of the records screen, you'll see three buttons: **Previous**, **Auto-Configure DNS**, and **Verify Domain**.

1. Click **Auto-Configure DNS** (blue-outlined button, middle).
2. VIBE uses the existing GoDaddy authorization from Part 1 to push all 6 records into your DNS automatically. No tab-jumping, no copying.
3. Wait a few seconds. The "Not Verified" badges next to each record should start flipping to "Verified."
4. Once all 6 are verified (or after ~30 seconds), click the solid blue **Verify Domain** button (bottom-right) to finalize.

If Auto-Configure DNS works for all 6 records → skip Path B and move to **Step 5**.

### Path B: Manual entry (fallback)

If Auto-Configure DNS fails, partially fails, or you'd rather do it by hand, copy each record into GoDaddy yourself.

Open GoDaddy DNS in another tab (**Domain Portfolio → martechprimer.com → DNS**).

For each record VIBE shows, click the **Copy** button on the right side of the row, then add it in GoDaddy:

#### Adding a TXT Record (SPF, DKIM, DMARC)
1. In GoDaddy, click **Add New Record**.
2. **Type:** TXT.
3. **Name (Host):** This is the trickiest part. When entering the host for a subdomain record in GoDaddy, copy everything from the beginning of the host value VIBE gives you up until — but **NOT INCLUDING** — the root domain part.
   - VIBE host shown as `mail` → enter `mail` in GoDaddy.
   - VIBE host shown as `mx._domainkey.mail` → enter `mx._domainkey.mail`.
   - VIBE host shown as `_dmarc.mail` → enter `_dmarc.mail`.
4. **Value:** paste exactly what VIBE shows. **Watch for hidden spaces** — paste into a plain text editor first if you're unsure. Hidden characters or stray spaces will silently break the record. The DKIM value is especially long; copy carefully.
5. **TTL:** 1 hour (or 600 seconds for faster propagation).
6. **Save.**

#### Adding a CNAME Record
- Same process, but **Type: CNAME**.
- **Name:** `email.mail` (the host part VIBE shows).
- **Value:** `mailgun.org` (no `https://`, no trailing dot — though GoDaddy may add one).

#### Adding the Two MX Records
For each MX record (you'll do this twice — once for `mxa.mailgun.org`, once for `mxb.mailgun.org`):
- **Type: MX**.
- **Name (Host):** `mail`.
- **Value/Points to:** `mxa.mailgun.org` for the first one, `mxb.mailgun.org` for the second.
- **Priority:** `10` for both.
- **TTL:** 1 hour.

After all 6 records are added in GoDaddy, return to the VIBE tab and click **Verify Domain** (bottom-right of the records screen).

> **CRITICAL — only ONE SPF record per host.** If you have multiple SPF records on the same host, receiving servers (Gmail in particular) will ignore them ALL. For a brand-new subdomain this won't be an issue, but worth knowing.

> **CRITICAL — only ONE DMARC record per host.** Multiple DKIM records for the same selector are also not supported.

## Step 5: Verify and Wait

1. Back in VIBE, click **Verify Records**.
2. VIBE checks each record. Green checkmarks = good. Red X = something's off.
3. Verification typically completes within 1–10 minutes, but in rare cases propagation can take up to 24–48 hours.
4. If verification fails:
   - Re-check the **Host/Name** field — it's almost always the issue.
   - Re-check for trailing spaces in the value.
   - Run your domain through **https://mxtoolbox.com/SuperTool.aspx** to see what's actually published.

✅ Once all 6 records show green, you have a verified dedicated sending domain. SSL provisions automatically.

> **Heads up — 30-day auto-delete on unverified domains:** If you create a dedicated domain entry but don't finish DNS verification, VIBE will show a warning like *"Unverified domain will be auto-deleted after [date]"* (30 days from creation). It's a cleanup policy — abandoned, never-verified entries get removed. You have plenty of time, but don't let it sit indefinitely. Once verified, the warning disappears.

> **If you ever get "Domain Already Exists" while adding:** It means the domain entry already got created on a previous click and just needs to be opened, not recreated. Click **Back to Dedicated Domains**, find the existing entry, click into it, and look for **"Verify Now"** to continue from where you left off.

## Step 6: Assign Your Sending Domain to Email Types (Domain Configuration)

Verifying the domain doesn't automatically *use* it — that's a separate step. VIBE has a routing table that decides which sending domain handles which kind of email, and by default everything is routed through VIBE's shared domain (`mail.vibereach.io` or similar).

To switch your traffic over to `mail.martechprimer.com`:

1. From the Dedicated Domains screen, click the **Domain Configuration** tab (top of the page, next to **Dedicated Domain**).
2. You'll see two configuration sections.

### Section 1: Main email categories

The first section has a row for each major outbound email type:

| Row | What it controls | Recommended setting |
|-----|------------------|---------------------|
| **Calendar Domain** | Appointment confirmations, reminders, reschedules | `mail.martechprimer.com` |
| **Payments** | Invoice and payment notification emails | `mail.martechprimer.com` |
| **One – One Conversation Domain** | Replies and 1:1 messages from Conversations | `mail.martechprimer.com` |
| **Bulk Email Domain** | Broadcast campaigns — the big volume one | `mail.martechprimer.com` |
| **Campaign Domain (except test campaign)** | Marketing campaigns from the Campaigns feature | `mail.martechprimer.com` |
| **Workflow Domain** | Automation workflows — drip sequences, nurture, follow-ups, abandoned-cart, etc. **Often your highest-volume category.** Leaving this unset means automation emails fall back to the shared domain. | `mail.martechprimer.com` |
| **Default Dedicated Domain** | The catch-all fallback for any category not explicitly set | `mail.martechprimer.com` |

For each row, click the dropdown and select `mail.martechprimer.com`. The "100%" means all traffic in that category routes through that domain. You can split traffic between multiple verified domains for advanced sender rotation, but for a fresh setup, 100% to your dedicated domain is correct.

(Optional) Click **Frequency Settings** on each row to set per-category rate limits. Defaults are fine to start.

> **Don't skip Workflow Domain.** This is the easiest one to overlook because it's lower on the page, and it's typically the highest-volume sender of all. If left unset, every drip email and follow-up automation goes out via the shared domain — undermining the entire reason you built a dedicated one.

### Section 2: Notification Domain Configuration (Client Portal)

The second section, titled **Notification Domain Configuration**, applies only to VIBE's **Client Portal** feature (the branded portal where your customers log in to view invoices, messages, appointments, etc.).

| Setting | What it controls |
|---------|------------------|
| **Client portal notification domain** | "You have a new message," "Your appointment is confirmed," "Your invoice is ready" — outbound notifications |
| **Client portal OTP domain** | One-Time Password codes sent to users logging into the portal. **If these don't deliver, your customers can't log in.** |

What to set:

- **If you use or plan to use Client Portal:** Set both to `mail.martechprimer.com`. The OTP one in particular *must* deliver reliably — leaving it on the shared domain risks login failures.
- **If you don't use Client Portal at all:** You can leave both blank — they simply won't be triggered. But it's safer to set both to `mail.martechprimer.com` now anyway, so the feature is pre-configured if you ever turn it on.

> **Why split categories at all?** Some teams keep transactional emails (calendar, payments, OTP) on one domain and marketing/bulk on another, so a marketing list issue can't damage the reputation of the domain delivering critical transactional mail. For now, route everything through your one verified domain — you can split later if needed.

## Step 7: Set the Dedicated Header (default From name and email)

Back on the **Dedicated Domain** tab, the entry for `mail.martechprimer.com` has a **Dedicated Header** section that probably shows *"Name: Name not provided / Email: Email not provided."*

This is your **fallback From identity** — what recipients see when a campaign's specific From address fails DMARC alignment. Without it, those messages can be rejected outright.

1. Click the **"..." (three dots) menu** next to `mail.martechprimer.com` at the top of the domain card. A dropdown appears with options: Verify domain, Delete domain, Assign IP, **Set Headers**, Domain Settings, SMTP Settings.
2. Select **Set Headers**.
3. **Name:** what you want recipients to see — for example, `MarTech Primer` or `Dr. Lee at MarTech Primer`.
4. **Email:** an address on your verified sending subdomain — for example, `support@mail.martechprimer.com` or `hello@mail.martechprimer.com`. The address doesn't need to be a real inbox; it's just used as the From identity. Replies will route based on your Reply & Forward Settings (a separate config).
5. Save.

> **Other options in that "..." menu, for future reference:**
> - **Verify domain** — re-run DNS verification if records ever drift out of sync
> - **Delete domain** — destructive, only if starting over
> - **Assign IP** — switch to dedicated IP (typically only worth it above ~150k emails/month)
> - **Domain Settings** — advanced per-domain config
> - **SMTP Settings** — for routing this domain via external SMTP

✅ Now your domain is verified, routed, and has a default sender identity.

## Step 8: Understand Domain Warmup (and connect Google Postmaster Tools)

After verification, your dedicated domain entry will display a **Domain Warmup** card showing **"Warmup In Progress, Stage 1"** and a daily counter like *"You've sent 0 of 1000 emails today."* This isn't a bug or a limitation imposed on you — it's a feature, and it's the difference between your emails landing in inbox vs. spam over the next few months. Read this section carefully before you send your first campaign.

### Why warmup exists

Mailbox providers (Gmail, Outlook, Yahoo, Apple Mail) decide whether your emails go to inbox or spam based on **sender reputation** — a per-domain trust score they calculate from your sending history. A brand-new domain like `mail.martechprimer.com` has **zero reputation**. Gmail has never seen it before. They have no way to distinguish you from a spammer who registered a domain yesterday to run a phishing campaign.

If you blast 10,000 emails on day 1, mailbox providers see *new domain + sudden volume + no engagement history* — classic spammer signature — and route everything to spam. Once your first batch lands in spam, recovery is a months-long uphill fight.

### What VIBE's warmup actually does

VIBE caps your daily sending volume and gradually raises the cap as you demonstrate good behavior. It's a multi-stage progression:

| Stage | Daily cap (typical) | What it proves |
|-------|---------------------|----------------|
| **Stage 1** | ~1,000/day | You're a real sender with normal volume |
| Stage 2 | ~5,000/day | Your bounce rate is acceptable |
| Stage 3 | ~10,000/day | Your engagement is real (opens, clicks) |
| Stage 4+ | Higher tiers | Sustained healthy sending |
| Graduated | Unlimited | Full reputation established |

Plan to spend **4–6 weeks** in warmup. There's no shortcut.

### How to read "aim to reach your daily limit consistently"

This is the most-misread sentence on the warmup card. It looks like it's saying "send more!" — but the actual signal is:

**Send a *consistent* volume each day, not erratic spikes.**

- ❌ 1,000 today, 50 tomorrow, 800 next week → looks like a spammer or a compromised account
- ✅ 700–900 every day reliably → looks like a healthy business

The cap is a ceiling, not a goal. Reputation comes from steady, predictable patterns combined with low bounce rates and good engagement — not from hitting the cap.

### Practical warmup playbook for the first 4–6 weeks

1. **Don't import a giant list and blast it.** Even though you *could* hit 1,000/day on day one, doing it with a cold, never-engaged list means high bounces and high spam complaints — which torches the reputation you're trying to build.
2. **Start with your most-engaged segment.** Recent customers, people who've replied to your past emails, people who opted in within the last 90 days. Real engagement teaches mailbox providers your domain is trusted.
3. **Send daily or every-other-day, not weekly bursts.** Consistency > volume.
4. **Keep your bounce rate under 2%.** Run any list older than 6 months through a verifier (NeverBounce, ZeroBounce, BriteVerify) before sending. Hard bounces above 2% trigger reputation penalties immediately.
5. **Watch spam complaint rate.** Stay under 0.1%. Above that, mailbox providers throttle your sends.
6. **Send to one provider at a time when possible.** Some pros warm up Gmail-only first, then add Outlook, then Yahoo. For most people, sending to a mixed list is fine — just keep it engaged.

### ⚠️ Connect Google Postmaster Tools (do this now)

Before you send your first real email, set up **Google Postmaster Tools**. This is Google's free dashboard that shows you exactly how Gmail sees your domain — domain reputation, IP reputation, spam rate, authentication errors, and delivery errors. Without it, you're flying blind during the most important phase of your sending lifecycle.

VIBE may have shown you a yellow callout on the dedicated domain card titled **"Connect Google Postmaster"** — that's pointing to the same thing.

Setup steps:

1. Go to **https://postmaster.google.com** and sign in with the Google account you want to manage this from. (A regular Gmail account works, but a Google Workspace account at your own domain is cleaner.)
2. Click **Add a domain** (top-right or "+ Add domain" button).
3. Enter `mail.martechprimer.com` (your sending subdomain — *not* your root `martechprimer.com`).
4. Postmaster Tools will give you a single **TXT record** to add as proof of ownership. The format looks like `google-site-verification=<long-random-string>`.
5. Add that TXT record in GoDaddy DNS:
   - **Type:** TXT
   - **Name (Host):** `mail` (since you're verifying the `mail.martechprimer.com` subdomain)
   - **Value:** the full `google-site-verification=...` string Google gave you
   - **TTL:** 1 hour
6. Save in GoDaddy.
7. Back in Postmaster Tools, click **Verify**. May take a few minutes for DNS to propagate.
8. Once verified, data takes **1–3 days** to start appearing — Google needs you to actually send some email before it has anything to report.

What to monitor in Postmaster Tools (once data appears):

- **Domain Reputation:** target High or Medium. Low or Bad means deliverability problems.
- **IP Reputation:** since you're on Mailgun's shared IPs, this is mostly out of your control, but watch for sudden drops.
- **Spam Rate:** must stay under 0.1%. Above that, fix immediately.
- **Authentication:** SPF, DKIM, and DMARC should all show 100% pass. If they don't, your DNS isn't right.
- **Delivery Errors:** any sudden spike usually points to a list quality issue.

✅ Once Postmaster Tools is set up, you have full visibility into how Gmail (~30% of your audience) is treating your domain. That's the single most valuable warmup signal you can monitor.

---

# Part 3 — Assign Your Domain to a Funnel or Website *(Optional — Skip if You Haven't Built One Yet)*

> **Skip this part if you haven't created a funnel or website in VIBE yet.** Connecting the domain (Part 1) and verifying the email sending domain (Part 2) are the foundational pieces — they don't require any content to exist. Assignment is the step where you point your verified domain at a *specific* funnel or website, so it only makes sense once you have one to point at. Come back here when you build your first funnel/website.

Connecting the domain (Part 1) makes it **available** to your sub-account. You still have to **assign** it to a specific funnel or website. There are two places where this can happen — pick whichever fits your situation:

## Option A: Inline assignment (right after Domain Connect succeeds)

If you just finished Part 1 and you already have a funnel or website built, VIBE shows you the assignment screen automatically — the **"Congratulations! You can now connect martechprimer.com with a Product"** page. From there:

1. Pick the **product type** (Funnel/Website/Store/Blog/Webinar).
2. Select the specific funnel/website from the **Link domain with funnel** dropdown.
3. Optionally expand **Additional options** to set a default page.
4. Click **Proceed to finish**.

This is the fastest path *if* you have content ready when you're connecting the domain. If you don't, skip this and use Option B later.

## Option B: Assignment from inside a funnel or website (the normal path)

This is what you'll do when you build your first funnel/website *after* connecting the domain (which is most people, including you right now).

1. In your sub-account left sidebar, click **Sites** (sometimes called **Funnels & Websites**).
2. Open the funnel or website you want to publish.
3. Click **Settings** within that funnel/website.
4. Find the **Domain** field (sometimes under "URL" or "Publishing").
5. Select your verified domain from the dropdown.
6. (Optional) Set a default page — this controls what loads when someone visits the bare root domain. A default page can be selected from **Settings → Domains & URL Redirects → Manage Domain → Edit Domain**.
7. **Save** and **Publish**.
8. Visit `https://martechprimer.com` in an **incognito window** to confirm it loads (incognito avoids cached DNS).

---

# Part 4 — Test Your Email Sending

Before you blast a campaign, run two tests — one for outbound authentication, one for the full round-trip including replies.

## Test 1: Outbound authentication (SPF / DKIM / DMARC)

> **Prerequisite:** VIBE is contact-first — you can't send an email to a raw address, you can only send to a *contact*. If your sub-account is brand new with zero contacts (typical), create one for yourself before trying to send the test email. Otherwise the Conversations flow will hit "No Data" and stop you cold.
>
> **Quick contact creation:**
> 1. In the left sidebar, click **Contacts**.
> 2. Click **+ Add Contact** (top-right).
> 3. Enter your **First Name**, **Last Name** (optional), and **Email** — use your **personal Gmail address**, not your work email. You want to test what real recipients see.
> 4. Save.
> 5. Now you can return to Conversations.

1. In VIBE, go to **Conversations** (left sidebar) → click **+ New** (or the new conversation button).
2. Choose **Message Contacts** → **Single Contact Conversation**.
3. In the **Select Contact** dropdown, find the contact you just created (yourself).
4. Compose a short test email — subject line "VIBE deliverability test" and a sentence or two of body text — and click **Send**.
5. Open Gmail. You should receive the email within 30–60 seconds. (Check Spam if it's not in Inbox — and if it landed in Spam, that's information: it means warmup is needed before any real campaign.)
6. With the test email open in Gmail, click the **three dots** in the top right → select **Show Original**.
7. Look at the top of the next page for these lines:
   - `SPF: PASS`
   - `DKIM: PASS`
   - `DMARC: PASS`

If all three show PASS, your outbound authentication is configured correctly.

If any show NONE or FAIL, give DNS more time to propagate — sometimes another 10–30 minutes is all it takes. If it still fails after a few hours, recheck your records.

## Test 2: Inbound reply round-trip

This confirms that when someone replies to your VIBE-sent email, the reply actually lands back in VIBE Conversations (not lost in the void). Skip this and you'll discover broken replies the hard way — when a real customer's reply doesn't reach you.

1. From the same Gmail you used in Test 1, **click Reply** to the test email and send a short response (e.g., "testing reply"). Send it from Gmail like a normal user would.
2. Wait ~30–60 seconds for VIBE to receive and process the inbound message.
3. Back in VIBE, navigate to **Conversations** in the left sidebar.
4. Open the conversation thread you started in Test 1.
5. Confirm the reply is visible inside that thread.

If the reply doesn't appear in Conversations:

- Check **Settings → Email Services → Reply & Forward Settings** — make sure inbound replies are configured to land in Conversations (and not being forwarded somewhere else or dropped).
- Verify the **MX records** for your sending subdomain are still in place — both `mxa.mailgun.org` and `mxb.mailgun.org` at priority 10. Inbound replies route through these.
- Wait another few minutes — occasionally there's a delay during initial provisioning.

✅ When you can see the reply inside the same conversation thread in VIBE, your full email loop is working: outbound delivery, authentication, *and* inbound reply capture.

## Test 3 (optional): Deliverability score

Run a free deliverability test at **https://www.mail-tester.com** — aim for 9/10 or higher. The site gives you a unique address; send a VIBE test email to it from Conversations, then check the score. It'll flag any issues with content, authentication, blacklists, or formatting that could hurt inbox placement.

---

# Quick-Reference Cheat Sheet

| Task | VIBE Path | What You Add to GoDaddy |
|------|-----------|--------------------------|
| **Funnels/Websites** | Settings → Domains → **Connect a domain** → **Funnel/Website/Store/Blog/Webinar** | A record (`@`) + CNAME (`www`) |
| **Email Sending** | Settings → Email Services → Dedicated Domain And IP → + Add Domain → **Auto-Configure DNS** | 1 SPF + 1 DKIM + 1 CNAME + 2 MX + 1 DMARC (6 total) on a subdomain |
| **Client Portal** (optional) | Settings → Client Portal → Domain Setup | 1 CNAME on a subdomain |

---

# Troubleshooting

**"Domain not verifying after 24 hours"**
Check GoDaddy DNS one more time — make sure no old conflicting records exist. If your registrar already has conflicting records for the same host (an existing A or CNAME record on the same name), you may need to remove or edit them so only the new VIBE-pointed entry remains.

**"My website loads but shows 'Not Secure' / SSL warning"**
SSL provisions automatically *after* DNS verification succeeds. Wait 10–15 minutes after verification. If still failing after an hour, in VIBE click your domain → **Re-issue SSL**.

**"Emails verified but still landing in spam"**
DNS is only half the battle. A new domain has zero reputation with Gmail/Yahoo/Outlook. Warm it up gradually — start with 20–50 emails per day for the first week, then increase over 4–6 weeks. Also set up **Google Postmaster Tools** at **https://postmaster.google.com** to monitor your sending reputation.

**"GoDaddy says I'm exceeding the record limit"**
GoDaddy limits free DNS to ~100 records. If you hit the limit, delete unused old records (parking page records, expired services).

**"I don't see the Authorize button — only manual setup"**
This means Domain Connect isn't yet active for your specific GoDaddy region/account. Use Path B (manual). Same end result.

---

# Final Sanity Check

Before you call it done, walk through this list:

- [ ] `https://martechprimer.com` loads your funnel/website (incognito window)
- [ ] `https://www.martechprimer.com` redirects to `https://martechprimer.com`
- [ ] Padlock shows in browser (SSL is working)
- [ ] Test email sent from VIBE shows SPF, DKIM, and DMARC = PASS in Gmail's "Show Original"
- [ ] Mail-tester.com score ≥ 9/10
- [ ] Domain shows **Verified** in both Settings → Domains AND Settings → Email Services → Dedicated Domain & IP

Once all six are checked, you're fully wired up and ready to build campaigns. 🎯
