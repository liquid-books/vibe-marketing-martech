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
- [ ] You have **15–30 minutes** of focused time
- [ ] You've decided which subdomains you'll use (write them down now)

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

1. Click **+ Add Domain** (top right of the Domains page).
2. A side panel opens. You'll be asked to choose what you want to connect — Funnel, Website, Store, Blog, or Webinar — and then enter your domain. For now, choose **Funnel** or **Website** (it doesn't lock you in — the domain becomes available to all funnels/websites in that sub-account once verified).
3. In the **Domain URL** field, type your root domain — for example: `martechprimer.com` (no `https://`, no `www.`, just the root).
4. You'll see a checkbox or toggle that says something like **"Add www subdomain too"** — leave this **ON**. By default, the system enables adding the www subdomain in addition to the root domain, and sets up a 301 redirect so all www traffic flows to the root. This is what you want for SEO and consistency.
5. Click **Continue**.

### Step 4: Authorize GoDaddy via Domain Connect

VIBE will detect that your domain is at GoDaddy. You'll see an "Authorize" button. Click it to allow the connection (the OAuth screen will say "**LeadConnector**" — that's the underlying service name and is expected).

1. Click **Authorize**.
2. A new browser tab opens to **GoDaddy's login page** (or auto-detects you if you're already signed in).
3. Sign into GoDaddy if prompted.
4. GoDaddy shows a consent screen: "**LeadConnector wants to update DNS records for [your domain]**." Review what records will be added (you'll see CNAME and A records targeting VIBE's backend infrastructure).
5. Click **Connect** (or **Authorize**).
6. **IMPORTANT:** Once GoDaddy says "Authorization Successful," **close that GoDaddy tab** and return to your VIBE tab. Closing it is what tells VIBE to proceed to the verification step.

### Step 5: Wait for Verification

Back in VIBE, the domain status will change from "Pending" to "Verified" — usually within 5–10 minutes, sometimes up to 24 hours.

✅ **Done.** Skip Path B and jump to **Part 2** (email setup).

---

## Path B: Manual DNS Connection (Fallback)

Use this if Path A fails, if you don't trust auto-authorization, or if your GoDaddy account is on a less-common region/setup.

### Step 1: Get the DNS Records from VIBE

In VIBE Settings → Domains:

1. Click **+ Add Domain**.
2. Enter your root domain (e.g., `martechprimer.com`).
3. Click **Continue**, then click **"Add records manually"** (a small link, usually under or next to the Authorize button).
4. VIBE shows you a screen with the records you need to add. **Keep this tab open** — you'll copy values from here.

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
2. Click **Email Services** (sometimes labeled **Email Service**).
3. Click the **Dedicated Domain & IP** tab (sometimes called **Dedicated Sending Domain**).
4. Click **+ Add Domain** in the top right.

## Step 3: Enter Your Sending Subdomain

1. In the field, type your full sending subdomain — for example: `mail.martechprimer.com`.
2. Click **Add & Verify**. Using a subdomain like `mail.martechprimer.com` is the recommended pattern for better deliverability.

VIBE now generates **5 DNS records** you need to add to GoDaddy. They typically include:

| Type | Purpose |
|------|---------|
| **TXT** (×1) | SPF — tells the world which servers are allowed to send for you |
| **TXT** (×1) | DKIM — cryptographic signature so receivers can verify the email wasn't tampered with |
| **CNAME** (×2) | Used by Mailgun (the underlying email infrastructure) for tracking and verification |
| **MX** (×1) | Tells servers where bounces and replies for the subdomain go |
| **TXT** (×1, optional but strongly recommended) | DMARC — tells receivers what to do with emails that fail SPF/DKIM |

**Keep this VIBE tab open.** You'll need to copy each value exactly.

## Step 4: Add the Records to GoDaddy

Open GoDaddy DNS in another tab (same path as before: **Domain Portfolio → your domain → DNS**).

For each record VIBE shows you:

### Adding a TXT Record (SPF, DKIM, DMARC)
1. Click **Add New Record**.
2. **Type:** TXT.
3. **Name (Host):** This is the trickiest part. When entering the host for a subdomain record in GoDaddy, copy everything from the beginning of the host value VIBE gives you up until — but **NOT INCLUDING** — the root domain part.
   - If VIBE says the host is `mail.martechprimer.com`, you enter just `mail` in GoDaddy.
   - If VIBE says `_dmarc.mail.martechprimer.com`, you enter `_dmarc.mail`.
   - If VIBE says just `martechprimer.com` (the root), you enter `@`.
4. **Value:** paste exactly what VIBE shows. **Watch for hidden spaces** — paste into a plain text editor first if you're unsure. Hidden characters or stray spaces will silently break the record.
5. **TTL:** 1 hour (or 600 seconds for faster propagation).
6. **Save.**

### Adding a CNAME Record
- Same process, but **Type: CNAME**, and the **Value** is a hostname like `mailgun.org` (no `https://`).

### Adding an MX Record
- **Type: MX**.
- **Host:** typically just `mail` (the subdomain part).
- **Value/Points to:** typically `mxa.mailgun.org` or whatever VIBE provides.
- **Priority:** VIBE specifies this — usually `10`. Enter exactly what they say.

> **CRITICAL — only ONE SPF record per domain.** If you have multiple SPF records on the same host, receiving servers (Gmail in particular) will ignore them ALL. If you already have an SPF record on your sending subdomain (you probably don't, since it's new), don't add a second one — merge them. For a brand-new subdomain this won't be an issue.

> **CRITICAL — only ONE DMARC record per domain.** Multiple DKIM records for the same selector are also not supported.

## Step 5: Verify and Wait

1. Back in VIBE, click **Verify Records**.
2. VIBE checks each record. Green checkmarks = good. Red X = something's off.
3. Verification typically completes within 1–10 minutes, but in rare cases propagation can take up to 24–48 hours.
4. If verification fails:
   - Re-check the **Host/Name** field — it's almost always the issue.
   - Re-check for trailing spaces in the value.
   - Run your domain through **https://mxtoolbox.com/SuperTool.aspx** to see what's actually published.

✅ Once all 5 records show green, you have a verified dedicated sending domain. SSL provisions automatically.

---

# Part 3 — Assign Your Domain to a Funnel or Website

Connecting the domain (Part 1) makes it **available** to your sub-account. You still have to **assign** it to a specific funnel or website.

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

Before you blast a campaign:

1. In VIBE, go to **Conversations** and send a test email to a Gmail account you own.
2. Open the email in Gmail → click the **three dots** in the top right → select **Show Original**.
3. Look at the top of the next page for these lines:
   - `SPF: PASS`
   - `DKIM: PASS`
   - `DMARC: PASS`

If all three show PASS, you're authenticated correctly.

If any show NONE or FAIL, give DNS more time to propagate — sometimes another 10–30 minutes is all it takes. If it still fails after a few hours, recheck your records.

You can also run a free deliverability test at **https://www.mail-tester.com** — aim for 9/10 or higher.

---

# Quick-Reference Cheat Sheet

| Task | VIBE Path | What You Add to GoDaddy |
|------|-----------|--------------------------|
| **Funnels/Websites** | Settings → Domains → + Add Domain | A record (`@`) + CNAME (`www`) |
| **Email Sending** | Settings → Email Services → Dedicated Domain & IP → + Add Domain | 2 TXT (SPF, DKIM) + 2 CNAME + 1 MX + 1 TXT (DMARC) on a subdomain |
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
