## 8.11 Lab 8: Connect Stripe, Create a Product, and Send Your First Payable Invoice

A business that manually sends PayPal invoices and waits for bank transfers is leaving 20–30% of its revenue on the table from collection delays, forgetting to follow up, and uncomfortable "did you pay yet?" conversations. This lab wires Stripe directly into your VibeReach.io account, creates a real product in your payments catalog, and sends a live invoice that generates a professional Stripe checkout experience — all within a single platform. By the end, you can collect payment from any client in under 60 seconds without leaving GHL.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- A Stripe account (free to create at [stripe.com](https://stripe.com) — start in Test Mode to complete this lab without real charges)
- At least one contact in your CRM to send the test invoice to (your own email works perfectly for testing)
- Approximately 30–45 minutes

**Test Mode vs. Live Mode:** Stripe operates in two modes. For this lab, you can complete every step in Test Mode — no real money moves. Use Stripe's test card: **4242 4242 4242 4242**, any future expiry date, any 3-digit CVV, any ZIP code. When you're ready to accept real payments, switch your Stripe account to Live Mode in Stripe's dashboard (stripe.com → Settings → Activate Account).
:::

---

### Step 1: Connect Stripe to VibeReach.io

1. In the left sidebar, click ⚙️ **Settings** → **Integrations**.
2. Scroll to find **Stripe** in the integrations list → click **Connect Stripe**.
3. A new browser window opens showing Stripe's OAuth authorization screen.
4. Log in to your Stripe account (or click "Create Account" if you don't have one yet and complete basic Stripe setup).
5. Review the permissions GHL is requesting → click **Connect my Stripe account**.
6. You are redirected back to VibeReach.io.

**You'll know you did this right when:** In Settings → Integrations, the Stripe section shows your Stripe account name (or email) and a green **"Connected"** status indicator.

:::{admonition} Why This Matters
:class: tip
This OAuth connection authorizes VibeReach.io to create payment records, generate checkout sessions, and receive webhook notifications when payments are made or fail — all on your behalf. Without this connection, the payment features in GHL (invoices, order forms, subscriptions) are greyed out and non-functional.
:::

---

### Step 2: Create a Product in Your Catalog

1. In the left sidebar, click **Payments** → **Products**.
2. Click **+ Add Product** in the upper right.
3. Configure the product:
   - **Name:** `Business Funding Consultation`
   - **Description:** `One-hour business funding strategy session — we review your options, qualify your business, and identify the best funding path forward.`
   - **Price:** `97.00`
   - **Currency:** USD
   - **Payment Type:** One-Time
4. Click **Save**.

Your product now appears in the Products catalog.

:::{admonition} Why This Matters
:class: tip
Creating a product in the catalog before building invoices or order forms means you never have to type the price manually again. Every invoice or payment form referencing this product automatically pulls the current price. If you ever change your pricing, update the product once — every future invoice updates automatically.
:::

**You'll know you did this right when:** "Business Funding Consultation" appears in your Products list with the $97.00 price displayed.

---

### Step 3: Create and Send a Payable Invoice

1. In the left sidebar, click **Payments** → **Invoices**.
2. Click **+ New Invoice** in the upper right.
3. In the invoice creation screen, fill in:
   - **Contact:** Click the contact search field → type your name or test email → select the contact
   - **Invoice Title:** `Business Funding Consultation` (optional — auto-fills from product)
   - **Add Item:** Click **+ Add Item** → select `Business Funding Consultation` from your catalog → verify price shows $97.00
   - **Due Date:** Set to 7 days from today (click the calendar and select)
   - **Notes (optional):** "Thank you for scheduling your consultation. Payment secures your appointment time and includes your personalized funding readiness report."
4. Click **Send Invoice**.
5. In the delivery dialog, select **Email** → confirm the contact's email address is correct → click **Send**.

**You'll know you did this right when:** The invoice appears in your Invoices list with status **"Sent"** and the send timestamp displayed.

:::{admonition} Why This Matters
:class: tip
The invoice you just sent generates a Stripe-hosted checkout page — a professional, mobile-optimized payment experience branded with your business name. The contact clicks one link in their email, sees a secure checkout, and pays in 30 seconds. Compare that to "here's my Venmo" or "can you do a bank transfer?" and the professionalism gap is obvious. Payment friction is revenue friction.
:::

---

### Step 4: View the Invoice From the Recipient's Perspective

1. Check the inbox of the email address you used for the test contact.
2. Open the invoice email — it arrives from your verified sending domain, branded with your business name.
3. Click the **View Invoice** or **Pay Now** button.
4. You see the Stripe-hosted checkout page with:
   - Your business name at the top
   - Invoice line items (Business Funding Consultation — $97.00)
   - Payment form accepting credit/debit card
5. Enter the test card: **4242 4242 4242 4242** · Expiry: any future month/year · CVV: any 3 digits · ZIP: any 5 digits.
6. Click **Pay**.

**You'll know you did this right when:** The payment processes without errors and you see a "Payment Successful" confirmation screen.

---

### Step 5: Confirm Payment in the GHL Dashboard

1. Return to VibeReach.io → **Payments → Invoices**.
2. Find the invoice you sent → confirm its status has changed from **"Sent"** to **"Paid"**.
3. Click the invoice to view the full record — it shows: amount paid, payment timestamp, payment method used (card), and the Stripe transaction ID.
4. Navigate to the contact record → scroll to the **Payments** or **Transactions** section → confirm the payment is visible on the contact's record.

:::{admonition} Why This Matters
:class: tip
Every payment recorded on a contact's record becomes a data point for your business intelligence. You can filter contacts by payment history, build Smart Lists of paying clients, and trigger post-payment workflows automatically. This is only possible when payments flow through your CRM — not when they live in a separate PayPal account with no CRM integration.
:::

**You'll know you did this right when:** The invoice shows "Paid" status with a Stripe transaction reference, and the payment appears in the contact's record.

---

### Step 6: Create a Payment Automation Workflow (Bonus)

Wire a workflow that fires automatically when an invoice is paid:

1. **Automation → Workflows → + New Workflow → Start from Scratch**
2. Name: `Invoice Paid — Onboarding Trigger`
3. **Trigger:** Search for "Invoice" or "Payment" → select **Invoice Paid** (or "Order Submitted / Payment Received" — the exact name varies by GHL version).
4. Add actions:
   - **Add Tag:** `paying-client`
   - **Remove Tag:** `consultation-applicant` (cleanup)
   - **Create Pipeline Opportunity** → move to your Onboarding pipeline, stage "Contract Signed"
   - **Send Email:** "Welcome aboard! Your onboarding coordinator will reach out within 24 hours..."
5. Toggle **Active** → **Publish**.

**You'll know you did this right when:** The workflow is Active and the trigger shows "Invoice Paid" as the trigger type.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 9:

- ☐ Stripe account connected — green "Connected" status in Settings → Integrations
- ☐ Product created in Payments → Products with correct name and price
- ☐ Invoice created, sent, and visible in Invoices list with "Sent" status
- ☐ Invoice email received — Pay Now link opens Stripe checkout
- ☐ Test payment completed with test card (4242 4242 4242 4242)
- ☐ Invoice status updated to "Paid" in GHL dashboard
- ☐ Payment visible on contact's record
- ☐ Bonus: Payment automation workflow created and Active

You have a live payment infrastructure. Every invoice you send from this point forward generates a professional Stripe checkout experience and records the payment automatically on the contact's CRM record.
:::

::::{dropdown} Troubleshooting Common Issues

**"Connect Stripe" button does nothing or opens a blank page:**
Pop-up blockers prevent the Stripe OAuth window from opening. Disable your pop-up blocker for the GHL domain (or allow pop-ups from gohighlevel.com / your VibeReach.io subdomain) and try again. Also try in an incognito browser window.

**Stripe shows "Connected" but invoices fail to send:**
Your Stripe account may not have completed KYC (Know Your Customer) verification. Stripe requires business details, a linked bank account, and sometimes identity documents before processing live payments. Go to stripe.com → Settings → Business → check for any incomplete verification steps. For Test Mode, full KYC is not required.

**The invoice email arrived but the Pay Now link shows an error:**
This usually means your Stripe connection lost authorization. Return to Settings → Integrations → Stripe → click "Reconnect" and re-authorize. This can happen if you changed your Stripe password or revoked API access.

**Test card declined:**
Use exactly: **4242 4242 4242 4242** with any future expiry and any 3-digit CVV. For intentional declines in testing, use Stripe's decline test card: **4000 0000 0000 0002**. If neither works, check that your Stripe account is in Test Mode (stripe.com dashboard should show "Test Mode" in the upper right).

**Payment successful but invoice still shows "Sent" not "Paid":**
GHL receives payment confirmation via Stripe webhooks. Webhook delivery can take 1–2 minutes. Wait, then refresh the Invoices page. If it still shows "Sent" after 5 minutes, check your Stripe webhook configuration: stripe.com → Developers → Webhooks → confirm the GHL webhook endpoint is active and the last delivery shows 200 status.

**I don't see the Payments section in my sidebar:**
The Payments module requires a GHL plan that includes payment features. Some lower-tier plans do not include full Payments access. Check your VibeReach.io plan under Settings → Account → Billing. Contact support if Payments should be included in your plan but isn't visible.
::::

