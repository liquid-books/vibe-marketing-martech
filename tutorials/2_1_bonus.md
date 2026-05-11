# Bonus: Deliver the Free Chapter Automatically

The main guide gets your funnel live: it captures the lead, tags them in your CRM, and redirects to a Thanks Page that promises *"Chapter 1 delivered to your inbox in under 60 seconds."*

Right now, that promise is a lie. The Thanks Page says the email is on the way, but nothing is actually sending it. This bonus fixes that.

You're going to extend the existing `MarTech Primer — Lead Capture Tagging` workflow with one more action: a **Send Email** step that fires immediately after the contact is tagged. The email delivers this link to the lead's inbox:

```
https://liquid-books.github.io/vibe-marketing-martech/
```

The whole bonus takes ~10 minutes.

---

## Before You Begin

- [ ] You've completed Part 5 of the main guide (form built, workflow built, tagging working)
- [ ] Your sender domain is verified in **Settings → Email Services** (otherwise the email won't send, or it'll land in spam). If you haven't done this yet, set up DKIM/SPF/DMARC records for `martechprimer.com` first — VIBE walks you through the DNS records under Email Services → Dedicated Domain.
- [ ] You have a sender email address (e.g., `book@martechprimer.com`) on that verified domain

---

## Part A — Extend the Existing Workflow

### Step 1: Open the workflow

1. Left sidebar → **Automation** → **Workflows**.
2. Click `MarTech Primer — Lead Capture Tagging` (the one you built in Part 5.4 of the main guide).

You should see:
- **Trigger:** Form Submitted → `MarTechPrimerForm`
- **Action 1:** Add Contact Tag → `martech-primer-lead`

### Step 2: Add the Send Email action

1. Click the **+** below the "Add Contact Tag" action.
2. Search the action menu for **Send Email** → click it.
3. The action config panel opens on the right.

### Step 3: Configure the sender

| Field | Value |
|-------|-------|
| **From Name** | `Ernesto from MarTech Primer` |
| **From Email** | `book@martechprimer.com` *(must be on your verified domain)* |
| **Reply-to Email** | `book@martechprimer.com` *(same address — replies go to you)* |
| **Subject** | `Your free chapter of MarTech Primer is here 📘` |
| **Preview Text** | `Chapter 1 — The MarTech Landscape. Read it in your browser, no download needed.` |

> **Why a real name in the From field?** "Ernesto from MarTech Primer" outperforms "MarTech Primer Team" or "noreply@…" on open rates by a wide margin. Inboxes are crowded; humans open emails from humans.

### Step 4: Paste the email body

Toggle the email editor to **HTML mode** (look for a `</>` icon or a "Code" toggle in the editor toolbar).

Paste the template from the next section. The merge tags (`{{contact.first_name}}` etc.) auto-fill from the form submission at send time.

### Step 5: Save and republish

1. Click **Save Action** in the right panel.
2. Top of the workflow editor → make sure the toggle is set to **Publish** (not Draft).
3. Save the workflow.

Your workflow now looks like:

```
Trigger:  Form Submitted → MarTechPrimerForm
Action 1: Add Contact Tag → martech-primer-lead
Action 2: Send Email      → Free Chapter Delivery
```

That's the entire automation. The next form submission will trigger it.

---

## Part B — The Email HTML Template

Paste this exactly into the HTML editor. It's a table-based email (the only thing that renders reliably across Gmail, Outlook, Apple Mail, and Yahoo) styled with your funnel's brand colors.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your free chapter of MarTech Primer</title>
</head>
<body style="margin:0; padding:0; background-color:#f5f1e8; font-family: -apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; color:#0a1628;">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color:#f5f1e8;">
    <tr>
      <td align="center" style="padding: 40px 16px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width:600px; background-color:#ffffff; border-radius:8px; overflow:hidden;">

          <!-- Header -->
          <tr>
            <td style="background-color:#0a1628; padding: 36px 40px; text-align: center;">
              <p style="margin:0; color:#c69009; font-size: 12px; letter-spacing: 2.5px; text-transform: uppercase; font-weight: 600;">MarTech Primer · 2026</p>
              <h1 style="margin: 14px 0 0; color:#f5f1e8; font-size: 30px; font-weight: 700; font-family: Georgia, 'Times New Roman', serif; line-height: 1.2;">Your free chapter is here.</h1>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding: 40px;">
              <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.65;">Hi {{contact.first_name}},</p>

              <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.65;">Welcome to the MarTech Primer community. As promised, here's your free copy of <strong>Chapter 1 — The MarTech Landscape</strong>.</p>

              <p style="margin: 0 0 32px; font-size: 16px; line-height: 1.65;">Click below to read it now. No download, no PDF — it opens right in your browser, beautifully formatted on any device:</p>

              <!-- CTA Button -->
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin: 0 auto 28px;">
                <tr>
                  <td align="center" style="background-color:#c69009; border-radius: 6px;">
                    <a href="https://liquid-books.github.io/vibe-marketing-martech/" target="_blank" style="display: inline-block; padding: 16px 36px; color:#0a1628; font-size: 16px; font-weight: 700; text-decoration: none; letter-spacing: 0.3px;">Read Chapter 1 Now →</a>
                  </td>
                </tr>
              </table>

              <p style="margin: 0 0 8px; font-size: 13px; line-height: 1.6; color: #5a6677; text-align: center;">Button not working? Copy and paste this link:</p>
              <p style="margin: 0 0 8px; font-size: 13px; line-height: 1.6; text-align: center;"><a href="https://liquid-books.github.io/vibe-marketing-martech/" style="color:#c69009; word-break: break-all;">https://liquid-books.github.io/vibe-marketing-martech/</a></p>

              <hr style="border: none; border-top: 1px solid #e5e0d5; margin: 36px 0;">

              <h2 style="margin: 0 0 16px; font-size: 20px; color: #0a1628; font-family: Georgia, 'Times New Roman', serif; font-weight: 700;">What happens next</h2>

              <p style="margin: 0 0 14px; font-size: 15px; line-height: 1.65;"><strong style="color:#c69009;">This week —</strong> I'll send you a short note with the most underrated idea from Chapter 1. The kind of thing readers highlight, then forget.</p>

              <p style="margin: 0 0 14px; font-size: 15px; line-height: 1.65;"><strong style="color:#c69009;">Monthly —</strong> One email with the MarTech insights I'm actually using right now. No roundups, no fluff, just signal.</p>

              <p style="margin: 0 0 14px; font-size: 15px; line-height: 1.65;"><strong style="color:#c69009;">At launch —</strong> Early-access pricing for the full book, weeks before public release.</p>

              <hr style="border: none; border-top: 1px solid #e5e0d5; margin: 36px 0;">

              <p style="margin: 0; font-size: 15px; line-height: 1.65;">Reply to this email if you have a question, want to push back on something in the chapter, or just want to say hi. I read every reply.</p>

              <p style="margin: 24px 0 0; font-size: 15px; line-height: 1.65;">— Ernesto<br>
              <span style="color:#5a6677; font-size: 13px;">Author, MarTech Primer</span></p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#f5f1e8; padding: 24px 40px; text-align: center;">
              <p style="margin: 0 0 8px; font-size: 12px; color: #5a6677; line-height: 1.5;">MarTech Primer · {{location.address}}</p>
              <p style="margin: 0; font-size: 12px; color: #5a6677; line-height: 1.5;"><a href="{{unsubscribe_url}}" style="color:#5a6677; text-decoration: underline;">Unsubscribe</a> &nbsp;·&nbsp; You're receiving this because you requested a free chapter at <a href="https://book.martechprimer.com" style="color:#5a6677; text-decoration: underline;">book.martechprimer.com</a></p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

### Merge tag notes

- `{{contact.first_name}}` — auto-fills from the form's First Name field
- `{{location.address}}` — auto-fills from your sub-account business address (required by CAN-SPAM and GDPR)
- `{{unsubscribe_url}}` — VIBE auto-generates this per-recipient. If your editor shows it as plain text instead of a working link, check the email action settings for a "Show Unsubscribe Link" toggle and turn it ON — or use the **Insert Custom Value** menu in the editor to pick "Unsubscribe Link" directly.

---

## Part C — Test It End-to-End

Don't trust it until you've seen it land. Run this exact test before you call it done.

1. Open `https://book.martechprimer.com` in an **incognito window** (so VIBE doesn't recognize you as an existing contact).
2. Submit the inline form using:
   - First Name: `Test`
   - Email: a real inbox you can check (Gmail is fine — bonus points for testing in two inboxes, e.g., Gmail + Outlook, since they render emails very differently)
   - Phone: leave blank
3. You should be redirected to the Thanks Page.
4. Within 30–60 seconds, check the test inbox.

**You should see:**

- [ ] Email arrives in **inbox**, not spam (if it lands in spam: your domain auth isn't fully set up — see Troubleshooting)
- [ ] From name shows as `Ernesto from MarTech Primer`
- [ ] Subject line displays correctly with the 📘 emoji
- [ ] Preview text in the inbox shows the preview line, not random body text
- [ ] `{{contact.first_name}}` rendered as "Test" (not as literal `{{contact.first_name}}`)
- [ ] The gold "Read Chapter 1 Now" button is clickable and goes to `https://liquid-books.github.io/vibe-marketing-martech/`
- [ ] The fallback text link also works
- [ ] Unsubscribe link at the bottom is clickable
- [ ] Email renders correctly on mobile (open it on your phone, not just desktop)

Back in VIBE:

- [ ] **Contacts** → the "Test" contact exists with the `martech-primer-lead` tag
- [ ] **Conversations** → there's a new conversation thread for "Test"
- [ ] **Automation → Workflows → [your workflow] → Enrollment History** → you can see the test contact entered the workflow and both actions (tag + email) show as **Completed**

If all 11 checkboxes pass, ship it. Delete the test contact from Contacts so it doesn't pollute your analytics.

---

## Part D — Optional Enhancements

### D.1 — A/B test the subject line

VIBE's email action has a **Subject Line** field; some versions of the UI allow multiple subjects with an A/B split. If yours supports it, test these two against each other:

- **Variant A:** `Your free chapter of MarTech Primer is here 📘`
- **Variant B:** `Ernesto, the chapter you requested (open me first)` *(uses personalization in the subject — these typically outperform generic subjects by 15–25%)*

Wait until at least 200 sends before declaring a winner. Smaller samples will tell you noise, not signal.

### D.2 — Add a delivery-confirmation tag

Sometimes emails fail silently (recipient marked as bounced, SMTP error, etc.). Add another action *after* the Send Email action:

- **Action 3:** Add Contact Tag → `chapter-delivered`

Then, if a contact has `martech-primer-lead` but not `chapter-delivered`, you know the email failed for them and you can manually resend or troubleshoot.

### D.3 — Build a 5-email nurture sequence

After the delivery email, add **Wait → 2 days → Send Email** actions in sequence. A simple post-delivery nurture:

| # | Send | Subject (suggestion) | Goal |
|---|------|----------------------|------|
| 1 | Immediately *(this bonus)* | Your free chapter is here 📘 | Deliver |
| 2 | +2 days | The one MarTech mistake I see every week | Reinforce expertise |
| 3 | +5 days | Did Chapter 1 land? (one question) | Engagement / reply-bait |
| 4 | +9 days | The chapter people DM me about most | Curiosity for full book |
| 5 | +14 days | Early-access list closes Friday | Soft pre-launch CTA |

Build each as a `Send Email` action with a `Wait` action between them. Same workflow, same trigger — just longer.

### D.4 — Internal notification when a lead comes in

Add a parallel branch (or another action) → **Send Internal Notification** → email yourself at every form submission. Useful in the early days when volume is low and you want to know the moment someone's interested. Turn this off once you're getting more than ~20 submissions per day or your own inbox becomes the bottleneck.

---

## Troubleshooting

**Email goes to spam**
Your domain authentication isn't fully set up. Open **Settings → Email Services → Dedicated Domain** and verify all three records show ✓ Verified: SPF, DKIM, DMARC. Spam folder placement is almost always a DNS/auth issue, not an email-content issue. Test deliverability at [mail-tester.com](https://www.mail-tester.com/) — you want a score of 9/10 or higher.

**`{{contact.first_name}}` shows up as literal text**
You typed the merge tag instead of inserting it from VIBE's **Insert Custom Value** menu. Some versions of the editor are strict about this. Delete the typed version and re-insert from the menu.

**Email doesn't send at all**
Check the **Workflow Enrollment History** for the test contact. If the Send Email action shows "Skipped" or "Failed," hover over it for the error. Most common causes: (1) sender email isn't on a verified domain, (2) the workflow is in Draft mode instead of Published, (3) the contact already received this same email recently and VIBE deduped it (rare but possible).

**The CTA button looks broken in Outlook**
Outlook 2016/2019 desktop versions are notoriously bad at rendering CSS-styled buttons. The table-based button in this template *should* render correctly in Outlook, but if it doesn't, replace the button code with VLO (Vector Markup Language for Outlook) using a [bulletproof button generator](https://buttons.cm/) — paste the generated code in place of the existing button table.

**Mobile rendering breaks**
The template uses `max-width:600px` and inline styles — should be solid. If it breaks, the most common cause is a copy-paste error stripping a `style` attribute. Re-paste the full template into the HTML editor, replacing whatever's there.

**Workflow fires but no email arrives, and no error in Enrollment History**
Check whether the test email address is already in your CRM as a contact with `DND (Do Not Disturb)` enabled. Open the contact → DND tab → confirm "All Channels" is OFF. DND-enabled contacts are silently skipped by Send Email actions.

**I want to send a real PDF attachment instead of a link**
Switch the link to a hosted PDF URL (upload the PDF to **Media Library**, copy the public URL, replace the link in the email). VIBE doesn't support file attachments in workflow emails — only linked downloads. Linked downloads are actually better anyway: you can track clicks, swap the file later without re-sending, and avoid attachment-based spam filters.

---

## Final Sanity Check

- [ ] Workflow shows three steps: Trigger → Add Tag → Send Email
- [ ] Workflow is Published, not Draft
- [ ] Sender domain authenticated (SPF/DKIM/DMARC all ✓)
- [ ] Test submission landed in inbox (not spam) within 60 seconds
- [ ] Merge tags rendered correctly (no `{{ }}` visible to the reader)
- [ ] CTA link goes to `https://liquid-books.github.io/vibe-marketing-martech/`
- [ ] Email renders correctly on both desktop and mobile
- [ ] Test contact + tag both appear in Contacts
- [ ] Test contact deleted from Contacts after QA

✅ The Thanks Page promise is now true. Your funnel actually delivers what it says it does.
