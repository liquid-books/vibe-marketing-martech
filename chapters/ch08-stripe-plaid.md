---
title: "Stripe & Plaid: Making Money Move at the Speed of Trust"
subtitle: "The distance between 'yes' and 'paid' is where most businesses leak revenue."
short_title: "Ch 8: Stripe & Plaid"
description: >
  Master the financial layer inside your CRM. Learn how Stripe processes cards and ACH, how Plaid verifies bank accounts without manual statement uploads, and how to build products, subscriptions, invoices, order forms, and dunning sequences that recover revenue automatically — all from inside VibeReach.io.
label: ch-08-stripe-plaid
tags: [stripe, plaid, payments, invoices, subscriptions, dunning, order forms, ACH, VibeReach, financial automation]
---

# Stripe & Plaid: Making Money Move at the Speed of Trust

:::{figure} ../images/ch08-infographic.png
:label: fig-ch08-infographic
:alt: Chapter 8 comprehensive infographic showing the full payment flow from CRM contact through invoice creation, Stripe checkout, payment confirmation, and automated workflow trigger, with Plaid bank verification and dunning sequences
:width: 100%
:align: center
Chapter 8 overview: from CRM contact to collected funds — the complete financial layer inside VibeReach, powered by Stripe for card and ACH payments and Plaid for instant bank verification.
:::

---

The handshake happened — figuratively, digitally, emotionally — and the client said yes. Then what? You emailed a payment link. They forgot. You followed up three days later. They said they would get to it. A week passed. By the time money actually moved, the emotional high of "yes" had evaporated, replaced by friction, delay, and doubt.

The distance between "yes" and "paid" is where most businesses hemorrhage revenue. Not because customers change their minds. But because the payment infrastructure was not built to move at the speed of the agreement. Your close moved at the speed of a handshake. Your collection moved at the speed of a fax machine.

This chapter eliminates that gap.

---

## 8.1 The Financial Layer: Why Payments Belong Inside Your CRM

For most of the history of small business software, payments lived in a separate tool. You closed a deal in your CRM, then pivoted to QuickBooks to send an invoice, or logged into PayPal, or emailed a bank transfer request. Each pivot was a friction point — not just for you, but for your contact. Every app they had to visit, every password they had to remember, every checkout that looked different from your brand was a moment where the deal could die.

The insight behind embedded payments is deceptively simple: **the fastest path from commitment to cash is the one with the fewest steps.** When payment infrastructure lives inside your CRM, every trigger, every contact record, every pipeline stage can generate financial events. A deal moves to "Proposal Sent" and an invoice fires automatically. A subscription lapses and a dunning workflow starts without anyone touching a keyboard. A new client books a call and a payment link is included in the confirmation email — before anyone has asked for a credit card.

:::{admonition} The Revenue Leakage Principle
:class: important
Every manual step between "yes" and "paid" reduces your collection rate. Research by McKinsey & Company found that B2B companies that digitize and automate payment collection reduce their average days-sales-outstanding (DSO) by 30% to 50%. The reduction is not primarily from faster payment processing — it is from eliminating the human delays that precede the payment request.
:::

In VibeReach.io (the white-labeled GoHighLevel platform you are working in), the financial layer is not an add-on. It is built into the same environment as your contacts, pipelines, funnels, and workflows. Stripe handles card and ACH payment processing. Plaid handles bank account verification for high-trust, high-volume transactions. Together, they form a payment infrastructure that rivals what enterprise finance teams spend months building — available to any business with a Stripe account and an afternoon.

:::{figure} ../images/ch08-stripe-architecture.png
:label: fig-ch08-stripe-architecture
:alt: Stripe payment architecture diagram showing the data flow from customer through Stripe API to merchant bank
:width: 80%
:align: center
Stripe payment architecture: customer card data is tokenized at the browser level, travels through Stripe's API for authorization, and settles to the merchant's bank account — your platform never stores raw card numbers.
:::

The shift from "payments as a separate tool" to "payments as a CRM feature" changes how you think about revenue operations. Instead of asking "how do I collect payment?" you start asking "at what trigger point should payment happen, and what should occur the moment it does?" That is a fundamentally more powerful question.

---

## 8.2 Stripe Explained in Ten Minutes — Cards, ACH, Fees, Payouts

Stripe is a payment processing platform. At its core, it does one thing: moves money from your customer's account to yours. But the way it does that — securely, compliantly, across dozens of payment methods and currencies — is sophisticated enough that understanding it at a conceptual level will save you hours of troubleshooting and thousands of dollars in avoidable fees.

**Cards:** When a customer enters a credit or debit card number into a Stripe-powered checkout, the card number never touches your servers. Stripe.js captures card data client-side, tokenizes it, and sends only the token to Stripe's servers. Your system never stores raw card numbers — this is the foundation of PCI compliance.

Stripe then sends an authorization request to the card network (Visa, Mastercard, Amex), which routes it to the issuing bank. The bank approves or declines. Stripe returns the result to your platform in milliseconds — customer clicks "Pay" to "Payment confirmed" in under two seconds.

**ACH:** Electronic bank-to-bank transfers. ACH is slower than cards (one to three business days for settlement) but significantly cheaper — 0.8% capped at $5.00, versus 2.9% + $0.30 for cards. For invoices over $1,000, ACH saves meaningful money. The tradeoff: ACH requires bank account verification — this is where Plaid enters (covered in section 8.3).

**Fees:** Stripe's standard pricing is transparent and published:
- Card processing: 2.9% + $0.30 per successful charge (domestic cards)
- ACH Direct Debit: 0.8%, capped at $5.00
- Invoices sent via Stripe Invoicing: included in card/ACH rates
- International cards: additional 1.5% cross-border fee
- Currency conversion: 1% above Stripe's exchange rate

When you collect $1,000 via credit card, Stripe keeps $29.30 and sends you $970.70. These numbers do not change based on your card processor negotiation skill — they are fixed for standard accounts. If you process over $1 million annually, Stripe will negotiate custom rates.

**Payouts:** Stripe holds your collected funds and pays them out to your connected bank account on a schedule. For new Stripe accounts, the default payout schedule is two business days after each charge. Standard accounts settle daily (funds collected Monday arrive Wednesday). You can accelerate this to same-day payouts (for an additional 1% fee) or set custom schedules if you prefer weekly lump-sum deposits.

:::{prf:definition} Payment Gateway
:label: def-payment-gateway
A **payment gateway** is the technology that securely captures, encrypts, and transmits payment information from the customer to the payment processor and back. Stripe serves as both payment gateway and payment processor — it captures the card data, handles the authorization request to the card network, and manages settlement. Most legacy systems separated gateway and processor into two vendors (with two fee schedules). Stripe unifies both.
:::

:::{prf:definition} ACH (Automated Clearing House)
:label: def-ach
**ACH** is a U.S. electronic network for bank-to-bank fund transfers operated by NACHA. ACH transactions are batched, not real-time — they are processed in cycles throughout the business day. ACH is the mechanism behind direct deposit payroll, bill pay, and bank-to-bank transfers. In a payment context, ACH allows you to pull funds directly from a customer's bank account (with authorization) at a fraction of card processing rates.
:::

---

## 8.3 Plaid Explained in Ten Minutes — Bank Verification Without the Statement Chase

Before ACH payments became practical for small businesses, collecting bank account information looked like this: you emailed the client, asked for a voided check or a bank statement, waited two days for them to locate and scan it, received a blurry PDF, manually keyed the routing and account numbers into your system, and hoped you had not made a typo. If you had, the ACH debit would fail three days later and you would start over.

Plaid replaced that entire process with a flow that takes under ninety seconds.

:::{prf:definition} Plaid
:label: def-plaid
**Plaid** is a financial data network that connects applications to bank accounts via a secure API. Rather than asking users to submit paper documents or manually enter bank details, Plaid launches a guided UI (called Plaid Link) where users log in to their bank directly. Plaid verifies account ownership and extracts routing/account numbers, balance data, and identity information — returning a verified token to the requesting application. The user's bank credentials never leave Plaid's encrypted environment.
:::

Here is how the Plaid verification flow works in practice:

```{mermaid}
sequenceDiagram
    participant B as Business App
    participant P as Plaid Link UI
    participant U as User/Customer
    participant K as Customer's Bank

    B->>U: "Please verify your bank account"
    B->>P: Launch Plaid Link (with client token)
    P->>U: Select your bank (search interface)
    U->>K: Log in with bank credentials
    K->>P: Authenticate & return account list
    U->>P: Select checking account
    P->>B: Return verified account token
    B->>B: Store token (not credentials)
    B->>K: Initiate ACH pull via Stripe + Plaid
```

The customer never pastes a routing number. They never upload a document. They log in to the same portal they use every day to check their balance, select the account, and Plaid hands the verified token back to the platform — all without the business ever touching the raw credentials.

:::{figure} ../images/ch08-plaid-flow.png
:label: fig-ch08-plaid-flow
:alt: Plaid bank verification flow showing six steps from launching Plaid Link to receiving a verified account token
:width: 80%
:align: center
The Plaid Link verification flow: customers authenticate directly with their bank, and the platform receives a verified token — never raw credentials or account numbers.
:::

**What Plaid verifies instantly:**
- Account ownership (name on the account matches the authorized signer)
- Account existence and active status
- Current balance (to assess whether an ACH pull will succeed)
- Routing and account numbers (without the user having to type them)

**What Plaid is not:** It is not universally available to all VibeReach accounts. Plaid integration requires additional business verification from GoHighLevel — your business must have completed KYC (Know Your Customer) review, and Plaid access is granted on an account-by-account basis. If your account does not yet have Plaid enabled, you will see Stripe-only options in your Payments settings. Reach out to VibeReach support to begin the verification process.

:::{admonition} Plaid Use Cases in VibeReach
:class: tip
Plaid is most valuable for: (1) high-ticket B2B invoices where ACH saves significant processing fees, (2) mortgage or MCA brokers who need to verify client income and cash flow before extending credit, (3) subscription businesses with average transaction values above $500, where the 0.8% ACH rate versus 2.9% card rate represents substantial savings at scale.
:::

---

## 8.4 Products, Prices, and Subscriptions in the Platform

Every payment starts with a product. Before you can send an invoice, build an order form, or create a subscription, you need to define what you are selling — and at what price. VibeReach organizes its financial layer using a three-tier hierarchy borrowed directly from Stripe's data model.

:::{figure} ../images/ch08-product-hierarchy.png
:label: fig-ch08-product-hierarchy
:alt: Three-tier product hierarchy diagram showing Product at top, multiple Price objects below it, and Subscription records at the base
:width: 80%
:align: center
The product-price-subscription hierarchy: each product can have multiple prices (one-time or recurring), and each subscription ties a contact to a recurring price on a billing schedule.
:::

**Tier 1 — Product:** The product is the thing you sell. "Business Funding Consultation." "Monthly Marketing Retainer." "SEO Audit Package." A product has a name, a description, and optionally an image. It is the catalog entry. By itself, it has no price — that lives at the next tier.

**Tier 2 — Price:** A price is a specific offering of a product at a specific amount and billing frequency. One product can have multiple prices: "Business Funding Consultation — $97 one-time" and "Business Funding Consultation — $147 with 60-minute extension" could both be prices under the same product. Prices are either one-time (a single charge) or recurring (charged on a schedule: weekly, monthly, quarterly, or annually).

**Tier 3 — Subscription:** A subscription ties a contact to a recurring price. When you create a subscription for a client, VibeReach automatically charges the client on the billing schedule and creates a new invoice for each cycle. Subscriptions can include trial periods (a set number of days before the first charge), setup fees (a one-time charge at subscription start), and cancellation policies.

:::{prf:definition} Subscription
:label: def-subscription
A **subscription** in VibeReach is an active billing agreement between your business and a contact, linked to a recurring price. The platform automatically generates and attempts payment for each billing period without manual intervention. Subscriptions can be paused, modified, or cancelled from the contact record or the Payments dashboard.
:::

To create a product in VibeReach, navigate to **Payments > Products > + Add Product**. You will define the name, add optional description and image, and then create one or more prices. For recurring prices, select the billing interval and whether to include a trial period. Save the product — it is now available to attach to invoices, order forms, and subscription workflows.

---

## 8.5 One-Time Payments, Installments, and the Psychology of Price Framing

Not every transaction is a subscription. Many of the most significant revenue events in a service business are one-time: a strategy day, a setup fee, a done-for-you deliverable, a course. Understanding how to structure and present one-time payments — and when to offer installments — is as important as the mechanics of processing them.

:::{figure} ../images/ch08-price-framing.png
:label: fig-ch08-price-framing
:alt: Price framing psychology infographic showing three tactics: price anchoring, installment reframing, and decoy pricing with a three-tier structure
:width: 80%
:align: center
Three evidence-based price framing tactics: anchoring (present the higher reference price first), installment reframing (break annual cost into per-day or per-month language), and decoy pricing (make the target option look like the obvious middle choice).
:::

**Price Anchoring:** The first number a buyer sees sets their reference point. Present a $2,400 annual package before revealing a $249 monthly option and the $249 feels like a deal — even though twelve payments of $249 totals $2,988. The anchor does not need to be dishonest; it simply needs to be presented first. Always open with your highest-value option.

**Installment Reframing:** "$100 per month for twelve months" feels like an operating expense. "$1,200" feels like a major decision. The total is identical; the psychological weight is not. In VibeReach, offer installment plans by creating a recurring price and building a workflow that cancels the subscription after N payments — a five-minute setup that can dramatically lift conversion on high-ticket offers.

**Decoy Pricing:** When presenting three tiers, the middle option almost always wins highest volume. Structure tiers so the option you want to sell most is the obvious middle choice — not manipulation, but removing the cognitive burden of choosing between extremes.

:::{admonition} The Per-Day Reframe
:class: tip
For services priced below $1,000 per year, the per-day reframe is powerful: "$2.74 per day" for a $997 annual subscription makes the cost feel trivially small relative to the value delivered. Use this language in your order form copy, not in your pricing table — the table should show the actual charge amount for clarity.
:::

VibeReach handles one-time payments through invoices or order forms (covered in sections 8.6 and 8.7). For installment plans, create a recurring monthly price and build a workflow that cancels the subscription after N payments. For large one-time transactions where the customer prefers ACH (to avoid card fees on their end), ensure your Plaid integration is active and offer the bank-debit option explicitly — many B2B buyers prefer it.

---

## 8.6 Invoices That Get Paid: Schedules, Reminders, and the Overdue Workflow

An invoice is a request for payment. Most businesses treat it as a formality — a document that states the amount owed and hopes the client eventually gets around to paying it. The businesses that collect faster treat the invoice as the beginning of an automated follow-up campaign, not the end of their involvement.

:::{figure} ../images/ch08-invoice-lifecycle.png
:label: fig-ch08-invoice-lifecycle
:alt: Invoice lifecycle diagram showing six stages with automation trigger points at each transition
:width: 80%
:align: center
The invoice lifecycle: each stage transition can trigger an automation — from delivery confirmation when sent to escalation workflows when overdue.
:::

```{mermaid}
flowchart LR
    A[Draft] --> B[Sent]
    B --> C[Viewed]
    C --> D{Payment?}
    D -->|Yes| E[Paid ✓]
    D -->|No| F[Overdue]
    F --> G[Reminder Sent]
    G --> H{Responds?}
    H -->|Pays| E
    H -->|Ignores| I[Escalation]
```

In VibeReach, invoices live at **Payments > Invoices**. Creating an invoice takes under two minutes: select or create a contact, add one or more products from your catalog, set a due date, add any notes, and send. The platform generates a branded payment page with a Stripe checkout — the recipient clicks the link in their email and pays by card or ACH without creating an account.

**Payment Schedules:** For large projects, split a total into multiple scheduled invoices — deposit at signing, progress at midpoint, final at delivery. VibeReach handles each as a separate invoice with its own due date and independent follow-up automation.

**Reminder Automation:** The step most businesses skip: build a workflow triggered by invoice overdue status. A simple sequence:

1. **Day 0 (due date passed):** Polite email reminder with payment link
2. **Day 3:** SMS reminder ("Your invoice for [amount] is still open: [link]")
3. **Day 7:** Final notice email, firmer tone
4. **Day 14:** Task assigned to human team member for personal outreach

Escalate tone only slightly. The goal is reducing cognitive friction — they forgot, they lost the link — not embarrassing anyone.

:::{admonition} The "Viewed But Not Paid" Trigger
:class: note
VibeReach can detect when an invoice payment link has been viewed but not completed. This is a high-signal event — the client opened the link but did not pay. Trigger a follow-up workflow specifically for this scenario: "I noticed you opened the invoice but may have run into an issue — here is the link again, and I am happy to take a card over the phone if that is easier." This converts significantly better than a generic reminder.
:::

---

## 8.7 Order Forms and Upsells — Turning One Sale Into Three

An invoice is reactive — you send it after the client has already agreed to pay. An order form is proactive — it is the checkout page embedded in your funnel, where the buyer decides to purchase without any back-and-forth. Order forms are the difference between a service business and a productized business.

:::{prf:definition} Order Form
:label: def-order-form
An **order form** in VibeReach is a Stripe-powered checkout page embedded in a funnel or linked directly from a campaign. It collects the buyer's contact information and payment simultaneously, creating a new contact record (or updating an existing one) and processing the charge in a single step. Successful order form completions can trigger any VibeReach workflow — delivering the product, assigning a team member, sending a welcome sequence, or updating a pipeline stage.
:::

:::{figure} ../images/ch08-upsell-funnel.png
:label: fig-ch08-upsell-funnel
:alt: Order form upsell funnel showing conversion flow from main offer through order bump, one-time offer, and downsell with revenue totals at each stage
:width: 80%
:align: center
The order form upsell funnel: the main offer converts buyers, the order bump adds incremental revenue at checkout, and the one-time offer (OTO) on the thank-you page converts a portion of buyers into higher-value customers — without a second sales conversation.
:::

**Order Bumps:** A checkbox add-on below the main offer — "Add a 30-minute strategy call for $47" — captures buyers already in purchasing mode. Because card details are already entered, bump conversions run 20–40%. Building an order bump into every order form is one of the highest-ROI five-minute decisions in your marketing stack.

**One-Time Offers (OTOs):** After purchase, redirect to a thank-you page with a complementary offer available only at that moment. The psychology: commitment consistency (they already said yes), scarcity (this page only), and obvious complementarity. Well-structured OTOs convert 10–25% of buyers at 2–5x the original purchase price.

**Downsells:** If the buyer declines the OTO, present a smaller, lower-commitment version. "If the full program is not right, would you like the starter kit at $97?" Downsells convert 5–15% of OTO declines.

In VibeReach, order forms are built in the Funnels builder (Chapter 2), and upsell/downsell flows connect page-by-page. Each step links to a Stripe product/price, and payment is captured automatically at each stage.

---

## 8.8 Failed Payments, Dunning, and How to Recover Revenue Without Being Rude

Subscriptions fail. It is not personal; it is probabilistic. Credit cards expire. Banks flag unfamiliar recurring charges. Accounts go temporarily negative. Industry data from Stripe suggests that approximately **9% of subscription payments fail on the first attempt** — a number that climbs to 15–20% for businesses with older card data on file. For a business with 200 active subscriptions at $297 per month, a 10% failure rate represents nearly $6,000 per month in revenue at risk.

:::{prf:definition} Dunning
:label: def-dunning
**Dunning** is the systematic process of communicating with customers to collect past-due payments. In a subscription context, dunning refers to the automated sequence of messages and payment retry attempts that follow a failed charge — from the initial failure notification to the final account suspension warning. Modern dunning systems combine smart retry logic (retrying at statistically optimal times), personalized messaging, and self-service payment update links to maximize recovery without human intervention.
:::

:::{figure} ../images/ch08-dunning-sequence.png
:label: fig-ch08-dunning-sequence
:alt: Dunning automation sequence timeline showing payment failure through recovery or account pause with recovery rates at each step
:width: 80%
:align: center
The dunning sequence: smart retry logic combined with graduated messaging recovers 60–80% of initially failed payments without manual intervention.
:::

**Smart Retry Logic:** Rather than retrying a failed card immediately (which almost never works — if the card failed at 2 PM on Tuesday, it will fail again at 2 PM on Tuesday), VibeReach and Stripe use intelligent retry scheduling. Stripe's research on optimal retry timing suggests:
- First retry: 3 days after initial failure (catches most temporary declines)
- Second retry: 5 days after first retry
- Third retry: 7 days after second retry

**The Dunning Sequence:** Communicate at each stage — not to scold, but to help:

- **Day 0:** "Your payment of [amount] did not process. Update your payment method here: [link]"
- **Day 3 (first retry):** "We tried again and had trouble — could you check your card details?"
- **Day 7 (second retry):** "We want to keep your account active. Update billing info in 30 seconds: [link]"
- **Day 14 (final notice):** "Your account will be paused on [date] if we cannot process payment."
- **Day 15:** Account restricted. Reactivation requires payment update.

Language matters. "Your payment failed" is accusatory. "We had trouble processing" is neutral. "Here is a link to update billing info" is action-oriented. Most failed payments resolve when updating a payment method is trivially easy.

:::{admonition} The Payment Update Link
:class: tip
VibeReach can generate a self-service payment update link from any subscription record. Include this link in every dunning message. Customers who receive a direct link to update their card convert at 3–4x the rate of customers directed to log in to a portal.
:::

---

## 8.9 Tax, Compliance, and the Boring Stuff That Keeps You in Business

Tax and compliance are not exciting topics. They are also not optional. The businesses that grow past seven figures do so in part because they built compliance infrastructure early — before a state tax authority sent a notice, before a bank flagged a suspicious transaction, before a customer demanded a proper receipt for their accountant.

:::{figure} ../images/ch08-tax-compliance.png
:label: fig-ch08-tax-compliance
:alt: Tax and compliance checklist infographic covering sales tax nexus, Stripe Tax automation, KYC, PCI compliance, and 1099-K reporting
:width: 80%
:align: center
The compliance checklist: five domains every business with digital payments must address — and how Stripe and VibeReach handle each one.
:::

**Sales Tax Nexus:** In the United States, you are required to collect sales tax in any state where you have "nexus" — a sufficient economic or physical presence. Since the Supreme Court's 2018 *South Dakota v. Wayfair* decision, economic nexus (based on sales volume, not physical location) applies in most states. If you make more than $100,000 in sales or more than 200 transactions in a state, you may have nexus there. **Stripe Tax** automates sales tax calculation and collection, applying the correct rate based on the buyer's location. Enable it in your Stripe dashboard, and it handles multi-state compliance automatically.

**PCI DSS Compliance:** Payment Card Industry Data Security Standard (PCI DSS) governs how businesses handle cardholder data. Stripe's architecture (tokenization at the browser, no card data on your servers) means most businesses using Stripe qualify for SAQ A — the simplest compliance level, requiring minimal documentation. Never store raw card numbers in any database or spreadsheet, ever.

**KYC and Identity Verification:** Stripe requires Know Your Customer (KYC) verification for all accounts. This means providing your business entity details, EIN or Social Security Number, and identity documents for beneficial owners. Stripe's onboarding walks you through this process. Incomplete KYC results in payout holds — set this up completely before you process your first transaction.

**1099-K Reporting:** Starting with the 2024 tax year, Stripe is required to issue 1099-K forms to any account that processes more than $5,000 in gross payments in a calendar year. Stripe handles the form generation; you are responsible for accurate reporting on your tax return. Keep your Stripe tax information current to avoid 1099-K mismatch notices.

**Refunds and Disputes:** Stripe charges the processing fee even on refunds (you get principal back, not the fee). Chargebacks incur a $15 dispute fee. Build a clear refund policy into every order form and invoice, and respond to disputes within Stripe's window (7–21 days) with documentation: order confirmation, delivery evidence, and terms acceptance.

---

## 8.10 Case Study: How an MCA Broker Replaced a Three-Day Manual Underwriting Process with Plaid Verification and Collected Funds in 14 Minutes

**The Problem:**

Capital Access Partners, a South Florida merchant cash advance brokerage, operated on a model that had not changed in a decade. When a merchant applied for funding, the underwriting process required: a phone call to collect business details, an email request for three months of bank statements, waiting two to three days for the merchant to locate and scan the statements, manual review of the PDFs to verify average daily balance and cash flow consistency, data entry of the reviewed figures into the underwriting spreadsheet, a follow-up call to the funder with the verified numbers, and finally — if approved — a funding wire that arrived the following business day.

Total elapsed time from "yes, I want funding" to funded: **three to five business days**.

Merchant attrition during this window was significant. Competing brokers who could move faster won the deal. Merchants who needed urgent capital abandoned the process midway through the statement collection step. The brokerage's conversion rate from application to funded was 34%.

:::{figure} ../images/ch08-mca-case-study.png
:label: fig-ch08-mca-case-study
:alt: MCA broker case study timeline comparing three-day manual process versus fourteen-minute Plaid-automated process
:width: 80%
:align: center
Before and after: the Plaid integration compressed a three-day manual underwriting process — with its multi-step statement chase — into a fourteen-minute digital flow from application to verified financial data.
:::

**The Solution:**

Capital Access Partners integrated VibeReach with Stripe and Plaid and rebuilt their intake process as a digital workflow:

1. **VibeReach Funnel:** A two-page funnel captures business information (name, monthly revenue range, time in business, funding need) and creates a contact record automatically.

2. **Plaid Link Trigger:** Immediately after form submission, a workflow sends a personalized SMS with a Plaid Link URL. The message reads: "Thanks, [First Name] — to complete your funding application, click here to securely connect your business bank account. This takes about 60 seconds and does not affect your credit: [Plaid Link]"

3. **Instant Verification:** The merchant selects their bank, logs in, and selects their primary business checking account. Plaid returns: verified routing and account numbers, last 90 days of transaction data, average daily balance, and account holder name — all in under 90 seconds.

4. **Automated Underwriting Pre-Screen:** A webhook from Plaid delivers the verified data to a VibeReach custom field set. A workflow evaluates: average daily balance above $5,000 AND monthly deposits above $15,000 AND account age above 6 months → moves the contact to "Pre-Approved" stage in the pipeline and sends an automated approval text within seconds.

5. **Stripe Invoice for Processing Fee:** Pre-approved merchants receive an automated invoice for the application processing fee ($250) via Stripe. The invoice includes a direct payment link. Payment is made by card or ACH in under two minutes.

6. **Funded:** With verified bank data and application fee collected, the broker submits the pre-screened package to the funder. Most funders in this workflow fund within four hours of receiving a Plaid-verified package with clean financials.

**The Results:**

- Application-to-funded time: reduced from 3–5 days to **14 minutes** (Plaid Link completion) + same-day funding
- Merchant conversion rate: from 34% to **61%** (fewer dropoffs during statement collection)
- Broker team capacity: the same three-person team handles 4x the application volume with no additional headcount
- Average revenue per funded deal: up 18% (faster funding allows brokers to work with larger merchants who previously went elsewhere for speed)

**What This Means for You:**

The MCA example is extreme in its time compression — 3 days to 14 minutes. But the principle applies to any business where verification, documentation, or payment collection creates a gap between customer commitment and revenue realization. Every step you eliminate from that process is not just a convenience — it is a conversion rate. It is a deal that does not die in the gap.

---

## 8.11 Lab 8: Connect Stripe, Create a Product, and Send Your First Payable Invoice

In this lab, you will connect Stripe to your VibeReach account, create a product in the payments catalog, and send a real payable invoice that generates a live Stripe checkout experience. By the end, you will have a working payment infrastructure you can use immediately.

**Prerequisites:**
- A VibeReach (GoHighLevel) account with admin access
- A Stripe account (free to create at stripe.com — you can start in test mode)
- A contact in your CRM to send the test invoice to (use your own email)

---

**Step 1: Connect Stripe**

Navigate to **Settings** (gear icon, bottom-left) **> Integrations > Stripe**.

Click **Connect with Stripe**. You will be redirected to Stripe's OAuth authorization screen. Log in to your Stripe account (or create one if you do not have one). Authorize VibeReach to connect to your Stripe account.

You will be redirected back to VibeReach. If the connection succeeded, you will see your Stripe account name displayed with a green "Connected" status indicator.

:::{admonition} Test Mode vs. Live Mode
:class: warning
Stripe has two modes: **Test Mode** (no real money moves, use test card numbers) and **Live Mode** (real transactions). For this lab, connect in Live Mode if you have a real Stripe account, but you can test using Stripe's test card number: **4242 4242 4242 4242**, any future expiry date, any CVV, any zip code. In Test Mode, no actual charges occur.
:::

---

**Step 2: Create a Product**

Navigate to **Payments > Products** (in the left sidebar). Click **+ Add Product** (top-right button).

Fill in the product details:
- **Name:** Business Funding Consultation
- **Description:** One-hour business funding strategy session — we review your options, qualify your business, and identify the best funding path for your goals.
- **Price:** $97.00
- **Payment Type:** One-Time

Click **Save**. Your product now appears in the Products catalog and is available to attach to invoices and order forms.

---

**Step 3: Send a Payable Invoice**

Navigate to **Payments > Invoices**. Click **+ New Invoice** (top-right).

In the invoice creation screen:
1. **Contact:** Search for and select a contact (use your own contact record for this test)
2. **Add Item:** Click "Add Item" and select the "Business Funding Consultation" product you just created
3. **Due Date:** Set to 7 days from today
4. **Notes (optional):** "Thank you for scheduling your consultation. Payment secures your appointment time."
5. **Send:** Click **Send Invoice**

Select delivery method **Email** and click **Send**. VibeReach generates a branded invoice and sends the payment link to the contact's email address.

---

**Step 4: View the Invoice from the Recipient's Perspective**

Check the email inbox for the contact you selected (your own email for this test). Open the invoice email. Click the **Pay Now** button or payment link.

You will see a Stripe-powered checkout page branded with your business name. The checkout accepts card payments and, if your Stripe account has ACH enabled, bank account payments. Enter a test card (4242 4242 4242 4242, any future date, any CVV) or your own card to confirm the experience.

---

**Step 5: Confirm in the Payments Dashboard**

Navigate back to **Payments > Invoices** in VibeReach. Locate the invoice you just sent. Confirm its status shows **Sent** (and **Paid** if you completed the test payment). Click the invoice to view full details: amount, due date, payment status, and the contact it was sent to.

---

**Expected Outcome**

After completing this lab, you have:
- ✅ Stripe connected and authorized in VibeReach
- ✅ A product in your payments catalog
- ✅ An invoice sent and visible to a contact
- ✅ A working Stripe checkout experience

::::{dropdown} Troubleshooting Common Issues
:open:

**"Connect with Stripe" button does nothing or redirects to an error:**
Clear your browser cache and try again. If using a pop-up blocker, allow pop-ups for VibeReach. Ensure your VibeReach account has admin-level permissions (sub-account users may not have Integrations access).

**Stripe shows "Connected" but invoices fail to send:**
Verify that your Stripe account has completed KYC verification. Stripe requires business details, a linked bank account, and identity verification before processing live transactions. Navigate to stripe.com > Settings > Business details to check status.

**Invoice email does not arrive:**
Check the contact's email address for typos. Check your spam folder. Ensure your VibeReach email sending domain (SMTP) is configured — invoices send from your platform email, not Stripe's. If email delivery is failing broadly, revisit Chapter 0's DNS and SMTP configuration.

**Test card is declined:**
Use exactly: **4242 4242 4242 4242** with any future expiration date and any three-digit CVV. If you are in Live Mode and testing with a real card, ensure your Stripe account is active (not restricted) and your bank has not flagged the charge.

**Plaid is not visible in my Integrations:**
Plaid requires additional business verification and is not available on all VibeReach accounts. Contact VibeReach support to request Plaid access. The lab is Stripe-only and is fully completable without Plaid.
::::

---

## 8.12 Chapter Takeaways & Reflection Questions

### Key Takeaways

- **Payments belong inside your CRM.** Every manual step between "yes" and "paid" reduces your collection rate. Embedded payment infrastructure eliminates context-switching and accelerates the revenue cycle.

- **Stripe processes cards and ACH.** Cards are instant and convenient; ACH is slower but significantly cheaper (0.8% capped at $5 vs. 2.9% + $0.30). For high-ticket B2B transactions, ACH saves real money.

- **Plaid removes the bank statement chase.** In under 90 seconds, customers authenticate with their bank directly, and your platform receives verified account data and routing numbers without ever touching credentials.

- **The product-price-subscription hierarchy gives you flexibility.** One product can have multiple prices. Recurring prices power subscriptions. Subscriptions automate billing without manual intervention.

- **Price framing is strategy, not manipulation.** Anchoring, installment reframing, and decoy pricing are evidence-based tactics that help buyers make decisions — and they help you close more at higher values.

- **Invoices need automation, not hope.** Build overdue workflows, viewed-but-not-paid triggers, and reminder sequences from day one. The platform will follow up so you do not have to feel awkward about it.

- **Order forms with upsells multiply revenue per customer.** A 20–40% order bump conversion and a 10–25% OTO conversion can increase your average transaction value by 40–100% without acquiring a single new customer.

- **Dunning is revenue recovery, not customer punishment.** Smart retry logic plus graduated, helpful messaging recovers 60–80% of initially failed payments without human intervention.

- **Compliance is not optional.** Stripe Tax handles multi-state sales tax. KYC protects your payout access. PCI tokenization protects your customers. Set these up before your first transaction.

### Reflection Questions

1. Where in your current business does the gap between "yes" and "paid" most commonly appear? What is the average number of days between a client commitment and actual payment receipt?

2. Consider your highest-ticket service or product. Which payment method would be most appropriate for your typical client — card or ACH — and what does that imply about your Plaid integration priority?

3. You currently have 150 active subscriptions at $197/month. Industry data suggests a 10% monthly payment failure rate. Walk through the math: what is your monthly revenue at risk, and what would a 70% dunning recovery rate mean for your annual revenue?

4. Review your last ten invoices. How many had a structured follow-up sequence? How many were paid within the due date? What is the correlation?

---

## Exercises

::::{exercise}
:label: ex-ch08-01

**Exercise 8.1 — Payment Method Optimization**

Your client, a digital marketing agency, currently processes all client invoices via credit card at an average invoice value of $4,500. Monthly invoice volume is 25 invoices.

Calculate: (a) total monthly Stripe fees at the standard 2.9% + $0.30 card rate; (b) total monthly fees if all invoices were paid via ACH at 0.8% capped at $5; (c) the annual fee savings from switching to ACH. What barriers to ACH adoption would you need to address, and how might Plaid help overcome them?
::::

::::{exercise}
:label: ex-ch08-02

**Exercise 8.2 — Upsell Funnel Design**

Design a three-step upsell funnel for a $497 business coaching intensive. Your funnel should include: (a) the main offer page with order form; (b) an order bump (describe it, price it, and explain why it belongs here); (c) a one-time offer on the thank-you page (describe it, price it, and apply at least one of the three price framing tactics from section 8.5). Calculate the expected revenue per 100 buyers assuming industry-average conversion rates at each step.
::::

::::{exercise}
:label: ex-ch08-03

**Exercise 8.3 — Dunning Sequence Planning**

A SaaS business has 300 active subscriptions at $149/month. In month one, 27 payments fail on the first attempt. Design a complete dunning sequence: the retry schedule, the message copy for each touchpoint (Day 0, 3, 7, 14), and the final escalation action. Using an assumed 65% recovery rate, calculate how many subscriptions are recovered and the monthly revenue saved by the dunning system versus taking no recovery action.
::::

::::{exercise}
:label: ex-ch08-04

**Exercise 8.4 — Invoice Overdue Workflow**

Build the logical flow for an invoice overdue automation in VibeReach. The invoice is due on Day 0. Map out: (a) trigger conditions; (b) three communication touchpoints with channel (email vs. SMS), timing, and tone; (c) branch logic for "viewed but not paid" vs. "not viewed at all"; (d) escalation to human task after Day 14. Draw the workflow as a flowchart or describe it step by step.

::::{dropdown} Solution Guide
:open:
**Trigger:** Invoice status changes to "Overdue" (past due date with no payment recorded)

**Branch Check (Day 1):** Has the invoice payment link been viewed?

- **Yes — Viewed, Not Paid Branch:**
  - Day 1 Email: "We noticed you opened your invoice — did you run into any issues at checkout? Here is the direct payment link: [link]. I am happy to help."
  - Day 5 SMS: "Quick follow-up on invoice #[number] for $[amount]. Link: [url]"
  - Day 10 Email: Final notice with firm tone, include phone number for direct payment by phone

- **No — Not Viewed Branch:**
  - Day 1 Email: Standard friendly reminder with payment link, subject line: "Friendly reminder: Invoice #[number] is now past due"
  - Day 4 SMS: "Hi [Name], your invoice of $[amount] was due on [date]. Here is the payment link: [url]"
  - Day 8 Email: Second reminder, mention potential service impact

**Day 14 (All Branches):** Create internal task: "Contact [Name] personally about overdue invoice — call or personalized video message." Assign to account owner.

**Key Design Principle:** The viewed-but-not-paid branch indicates purchase intent but execution friction. Lead with problem-solving language, not payment pressure.
::::
::::

---

## Discussion

**Discussion Prompt:** The integration of payment infrastructure directly into a CRM platform raises interesting questions about the nature of customer relationships and business ethics. When a business can trigger an automatic invoice the moment a deal is marked "closed," send dunning sequences without human review, and collect ACH payments from a verified bank account — all within seconds of customer consent — where does automation end and responsibility begin?

Consider: A subscription customer's payment fails because they lost their job and their bank account was overdrawn. An automated dunning sequence sends four messages over fourteen days and ultimately pauses their account. Is this the right outcome? What design choices in the dunning workflow could make the system more humane without sacrificing revenue recovery effectiveness? Use at least one scholarly or industry source to support your position.

> **Discussion Guidelines:** Write a substantive response of at least 200 words addressing the prompt above. Include at least one scholarly or credible citation (journal article, textbook, or authoritative industry report) to support your argument. Then respond to at least TWO peers with substantive feedback — go beyond "I agree" and explain why their perspective adds to or challenges your thinking.

---

## Glossary

**ACH (Automated Clearing House):** Electronic bank-to-bank transfer network operated by NACHA; cheaper than card processing but settles in 1–3 business days.

**Authorization:** The process by which a card network confirms that a card is valid and has sufficient funds or credit available before a charge is captured.

**Capture:** The step that actually moves money from a customer's account to the merchant; authorization reserves funds, capture collects them.

**Chargeback:** A forced payment reversal initiated by a cardholder through their bank; costs the merchant the transaction amount plus a dispute fee.

**Dunning:** The systematic process of communicating with customers and retrying payments to recover failed subscription charges.

**Economic Nexus:** The legal threshold (usually $100K in sales or 200 transactions per year) that creates a sales tax collection obligation in a state, even without physical presence.

**KYC (Know Your Customer):** Identity and business verification requirements imposed by financial regulators; Stripe requires KYC before allowing payouts.

**Order Bump:** A complementary add-on offer presented within the main order form, checked by the buyer before completing checkout.

**Order Form:** A Stripe-powered checkout page embedded in a funnel that simultaneously captures contact information and processes payment.

**PCI DSS:** Payment Card Industry Data Security Standard; the security framework governing how businesses handle cardholder data.

**Payment Gateway:** Technology that securely captures and transmits payment data between the customer, the processor, and the card network.

**Plaid:** A financial data network that connects applications to bank accounts for instant verification and ACH payment setup.

**Price Anchoring:** A cognitive bias technique where the first price presented creates a reference point that makes subsequent prices feel higher or lower by comparison.

**Stripe Tax:** Stripe's automated sales tax calculation and collection feature that applies correct rates based on buyer location.

**Subscription:** An active recurring billing agreement between a business and a customer, auto-charging on a defined schedule.

**Tokenization:** The process of replacing sensitive card data with a randomly generated token that represents the card without exposing its actual number.

**1099-K:** IRS tax form issued by payment processors to merchants who exceed reporting thresholds; required for accurate tax reporting.
