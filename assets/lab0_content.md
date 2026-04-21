## 0.7 Lab 0: Point a Domain, Verify a Sending Domain, and Send Your First Authenticated Email

Your domain is the foundation of every marketing campaign you will ever run. Without a properly configured domain and authenticated sending address, your emails land in spam, your funnels break, and your brand looks unprofessional at every customer touchpoint. This lab gives you a fully authenticated, deliverability-ready domain in VibeReach.io — so every campaign you build in this course starts with the best possible infrastructure beneath it.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- A domain name you own (register one at Namecheap for approximately $10–$15 if needed; choose a `.com` using your brand or full name)
- Access to your domain registrar's DNS management panel (Namecheap, GoDaddy, Cloudflare, or similar)
- An active VibeReach.io sub-account with admin access
- Approximately 60–90 minutes of focused work (plus up to 48 hours for DNS propagation)
:::

---

### Step 1: Add Your Domain to VibeReach.io

1. Log in to your VibeReach.io sub-account.
2. In the left sidebar, click the ⚙️ **Settings** gear icon → **Domains**.
3. Click the **+ Add Domain** button in the upper right.
4. In the "Domain Name" field, type your root domain: `yourbusiness.com` (no `www`, no `https://`).
5. Click **Add Domain**.
6. The platform displays the IP address you need for your A record. **Copy this IP address** — you need it in Step 2.

:::{admonition} Why This Matters
:class: tip
Every funnel and page you build in VibeReach.io is hosted on the platform's servers. The A record you're adding tells the internet that your domain name points to those servers. Without it, your funnel links show broken pages.
:::

**You'll know you did this right when:** Your domain appears in the Domains list with a "Pending" status and the platform shows you DNS values to copy.

---

### Step 2: Add DNS Records at Your Registrar

Open your domain registrar in a new browser tab.

- **Namecheap:** Domain List → **Manage** → **Advanced DNS** tab
- **GoDaddy:** My Products → your domain → **DNS**
- **Cloudflare:** Select domain → **DNS** → **Records**

First, delete any default A record pointing to a registrar parking page (they conflict). Then add:

| Record Type | Host / Name | Value | TTL |
|-------------|-------------|-------|-----|
| A | `@` | *(IP address from Step 1)* | 3600 |
| CNAME | `www` | `yourbusiness.com` | 3600 |

Click **Save** after each record.

**You'll know you did this right when:** Both records appear in your DNS table. Propagation begins immediately but may take 2–48 hours globally.

---

### Step 3: Set Up Your Email Sending Domain

1. In VibeReach.io: ⚙️ **Settings** → **Email Services** → **Dedicated Domain & IP**.
2. Click **+ Add Domain**.
3. For best deliverability, use a subdomain like `mail.yourbusiness.com`. Type it → **Add & Verify**.
4. The platform generates two DKIM TXT records. They look like:

| Type | Host / Name | Value |
|------|-------------|-------|
| TXT | `s1._domainkey` | `v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3...` (long string) |
| TXT | `s2._domainkey` | `v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3...` (long string) |

5. **Copy both TXT record names and values exactly** — do not shorten the long key strings.

:::{admonition} Why This Matters
:class: tip
DKIM adds a cryptographic signature to every email you send. Email providers check it on every incoming message. Without valid DKIM, your campaigns score lower on spam filters and are more likely to land in junk — even for contacts who want to hear from you.
:::

---

### Step 4: Add DKIM Records at Your Registrar

Return to your registrar's DNS panel:

1. Add Record → select **TXT**
2. Host field: enter `s1._domainkey` (your registrar may auto-append the domain name)
3. Value: paste the full DKIM value from VibeReach.io
4. TTL: 3600 → Save
5. Repeat for `s2._domainkey`

**You'll know you did this right when:** Both DKIM TXT records appear in your DNS table.

---

### Step 5: Add Your SPF Record

Add this TXT record at your registrar:

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT | `@` | `v=spf1 include:_spf.gohighlevel.com ~all` | 3600 |

:::{admonition} Critical: The Two-SPF Trap
:class: warning
If a TXT record beginning with `v=spf1` already exists for your domain, do NOT add a second one. Two SPF records cause SPF authentication to fail. Instead, **edit the existing record** to add `include:_spf.gohighlevel.com` before the `~all`. Example: `v=spf1 include:_spf.google.com include:_spf.gohighlevel.com ~all`
:::

**You'll know you did this right when:** Exactly one `v=spf1` TXT record exists for your root domain, and it includes `_spf.gohighlevel.com`.

---

### Step 6: Add Your DMARC Record

| Type | Host | Value | TTL |
|------|------|-------|-----|
| TXT | `_dmarc` | `v=DMARC1; p=none; rua=mailto:dmarc@yourbusiness.com` | 3600 |

Replace `yourbusiness.com` in the `rua=` address with your actual domain. Start with `p=none` — this monitors without blocking anything. After 30 days of clean reports, upgrade to `p=quarantine`.

:::{admonition} Why This Matters
:class: tip
DMARC enforces your SPF and DKIM policies and alerts you when someone tries to impersonate your domain. Without it, phishing attacks using your domain name are easier to execute — and your reputation with receiving mail servers is lower.
:::

---

### Step 7: Verify Your Domain in VibeReach.io

1. **Settings → Email Services → Dedicated Domain & IP**
2. Find your domain → click the ⋮ three-dot menu → **Verify Domain**
3. The platform checks your records live:
   - ✅ Green checkmark — record found, correctly formatted
   - ❌ Red X — missing or incorrectly formatted
   - 🔄 Spinning — still propagating; retry in 1–4 hours

Do not proceed until all three records (DKIM ×2, SPF, DMARC) show green.

**You'll know you did this right when:** All authentication indicators show green and your domain status reads "Verified."

---

### Step 8: Score Your Email With mail-tester.com

1. Open [mail-tester.com](https://mail-tester.com) — copy the unique test address shown.
2. In VibeReach.io, create a test email → send it to the mail-tester address using your verified sending domain.
3. Return to mail-tester.com → **Check your score**.
4. Target 8/10 or higher. All three should read PASS: SPF ✅ · DKIM ✅ · DMARC ✅

**You'll know you did this right when:** Your score is 8/10 or higher with no authentication failures.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 1:

- ☐ Domain added to VibeReach.io with "Verified" status
- ☐ A record and www CNAME present in registrar DNS panel
- ☐ Both DKIM TXT records added; showing green in VibeReach.io
- ☐ Single SPF record exists with `_spf.gohighlevel.com` include
- ☐ DMARC TXT record at `_dmarc.yourbusiness.com`
- ☐ All authentication indicators green in VibeReach.io
- ☐ mail-tester.com score 8/10 or higher
- ☐ Verified sending address configured in sub-account settings

You now have a fully authenticated email infrastructure. Every campaign you send from this account has maximum deliverability.
:::

::::{dropdown} Troubleshooting Common Issues

**All records show red Xs immediately after adding them:**
DNS propagation takes time — up to 48 hours globally. Wait at least 2 hours, then click Verify again. Use [dnschecker.org](https://dnschecker.org) to check global propagation status for each record type.

**DKIM still fails after 48 hours:**
The most common cause is your registrar auto-doubling the domain name in the host field. If you entered `s1._domainkey` and your registrar stored it as `s1._domainkey.yourbusiness.com.yourbusiness.com`, delete it and re-enter with just `s1._domainkey`. Check what the registrar actually stored vs. what you typed.

**SPF shows red even though I added the record:**
You likely have two SPF records. Check your DNS panel for any other TXT record beginning with `v=spf1` at the `@` host. Delete the duplicate and merge both `include:` directives into one record.

**DMARC shows red:**
The host field must be exactly `_dmarc` (with the underscore). Some registrars store this differently — check whether `_dmarc.yourbusiness.com` resolves. Also verify the value starts exactly with `v=DMARC1;` — no extra spaces.

**Settings → Email Services is not visible:**
You're likely in the Agency view, not a sub-account. In VibeReach.io, email sending domains are sub-account level settings. Click into a sub-account from the agency dashboard first.

**Mail-tester score below 7 despite passing SPF/DKIM/DMARC:**
Review the full scorecard. Common causes: your IP is on a shared blacklist, the test email content contains spammy phrases, or the HTML is malformed. Each flagged item links to specific remediation instructions.
::::

