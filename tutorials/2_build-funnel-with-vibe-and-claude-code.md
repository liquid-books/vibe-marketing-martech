# Build a Lead-Capture Funnel from Scratch in VIBE with AI Vibe Coding

You're going to build a 2-step lead-capture funnel **from scratch** — no template, no extraction step, no fighting against pre-built designs. Every section of every page is a **Custom HTML/Javascript** block you generate in your AI tool (Claude Code, Claude.ai, Gemini, ChatGPT, Cursor — pick one and stick with it for the whole build) and paste into VIBE.

Two capture points: an **inline form** mid-page for ready-to-convert visitors, and an **exit-intent popup** for visitors about to leave. Both pipe submissions straight into VIBE Contacts.

---

## ⚠️ About the example used throughout this guide

This guide uses a **concrete worked example** so you have something tangible to follow:

- **Product:** the MarTech Primer book
- **Domain:** `martechprimer.com`
- **Subdomain:** `book.martechprimer.com`
- **Lead magnet:** a free chapter (delivered via email after form submission)
- **Brand colors:** navy `#0a1628`, gold `#c69009`, cream `#f5f1e8`
- **Brand fonts:** Fraunces (serif headlines), Inter (sans body) — both via Google Fonts

**Substitute your own values everywhere you see them.** When you see `martechprimer.com`, replace it with your domain. When you see "MarTech Primer book," replace it with your product. When you see `#0a1628`, replace it with your brand color. The structure stays the same — only the values change.

---

## What You'll End Up With

- A live lead-capture funnel at `book.martechprimer.com`
- 2 funnel steps: **Sales Page** (7 stacked Custom HTML blocks + a popup) → **Thanks Page** (1 block)
- An **inline form** mid-page that captures Name, Email, Phone (optional)
- An **exit-intent popup** that captures the same fields when someone tries to leave
- Every form submission auto-creates a contact in VIBE Contacts

---

## The Build Order (read this once)

You'll build in this order — no jumping around:

1. **Subdomain** — connect `book.martechprimer.com` to VIBE
2. **Blank funnel** — create the funnel shell with two empty steps
3. **Editor tour** — learn the toolbar before you start dropping blocks
4. **Vibe coding workflow** — the 5-step procedure used for every block
5. **Sales Page blocks 1–7** — vibe code each block in order. **Block 5 pauses to build the form, get its embed code, and set up the tagging workflow** — that's the only context-switch in the build.
6. **Popup** — exit-intent capture using the same form
7. **Thanks Page** — single block, vibe coded
8. **Connect & publish** — domain, tracking, SEO, cookie consent, go live

---

## Before You Begin

- [ ] Your domain (`martechprimer.com`) is connected to VIBE (per the domain-connection guide)
- [ ] Pick **one** AI tool: Claude Code, Claude.ai, Gemini, ChatGPT, Cursor
- [ ] Brand assets ready: brand colors, brand fonts, logo, hero visual, copy

---

# Part 1 — Add the Subdomain

1. Log into VIBE → select your sub-account.
2. Left sidebar → **Settings** → **Domains**.
3. Click **Connect a domain** at the bottom of the card.
4. Click **Connect** next to **Funnel/Website/Store/Blog/Webinar**.
5. Type `book.martechprimer.com` → **Continue**.
6. **Uncheck** the "Also add www..." checkbox → **Continue**.
7. Click **Authorize domain**.
8. Wait ~5 minutes for status to flip to **Verified**. SSL provisions automatically.

✅ Subdomain ready.

---

# Part 2 — Create the Blank Funnel

1. Left sidebar → **Sites** → **Funnels** tab.
2. Click **+ New Funnel** (top-right).
3. Click **Create New Funnel** (the blank option — *not* Funnel AI, *not* Template Library).
4. **Funnel Name:** `MarTech Primer Book — Lead Capture Funnel`
5. Click **Create**.

You land on the funnel overview with **one blank step** by default.

## Add the two pages

1. Click the default first step → set **Step Name** to `Sales Page` and leave **URL Path** blank (so it lives at the root of `book.martechprimer.com`).
2. In the Funnel Steps panel, click **+ Add New Step or Import**.
3. **Step Name:** `Thanks Page`
4. **URL Path:** `thanks` (so it lives at `book.martechprimer.com/thanks`)
5. Leave it as a **blank page** — don't import anything.
6. Click **Create Funnel Step**.

You should now have two blank steps:

1. **Sales Page**
2. **Thanks Page**

Both completely empty. Good.

## Connect the funnel to your subdomain

Do this now so the preview URL matches the live URL throughout the build.

1. In the Funnel Steps panel, click **Edit** on the **Sales Page** step. The editor opens.
2. At the top of the editor, near the preview URL display, look for **Connect Domain** (a link/button).
3. Click it → a domain dropdown appears.
4. Select **`book.martechprimer.com`** from the dropdown.
5. Save.

The preview URL at the top should now show `https://book.martechprimer.com` instead of a temporary preview URL.

Stay in the editor — Part 3 picks up here.

---

# Part 3 — Editor Tour

Click **Edit** on the Sales Page step to open the editor. Before you start dropping blocks, learn the toolbar.

## 3.1 Layers

Hierarchical structure of the page (Sections → Rows → Columns → Elements) as a tree.

- **Where:** Left side rail → Layers icon
- **When:** to find/select nested elements; to reorder blocks without dragging on the canvas

## 3.2 Pages (Funnel Steps)

Lists steps in the funnel. Switch between Sales Page and Thanks Page.

- **Where:** Left side rail → Pages icon, OR top bar **Sales Page** dropdown
- **When:** every time you switch pages

## 3.3 Add Element (+)

The element library — text, image, button, video, **Custom HTML/Javascript**, form, etc.

- **Where:** Top-left of the editor → **Add Element (+)** icon
- **When:** every block — you'll drop a Custom HTML/Javascript element 7 times on the Sales Page and 1 time on the Thanks Page

## 3.4 Tracking Code

Inject scripts that run on the page — GA4, Meta Pixel, TikTok Pixel, Microsoft Clarity, Hotjar.

- **Where:** Top bar → **Settings** (gear) → **Tracking Code** tab
- **When:** before publishing. Two text areas: **Header** (most analytics) and **Body footer** (chat widgets)
- **Add to both steps** (Sales Page AND Thanks Page) so tracking is consistent

## 3.5 Custom CSS

Page-level CSS that applies to all elements, including your Custom HTML blocks.

- **Where:** Top bar → **Settings** (gear) → **Custom CSS** tab
- **When:** at the start of the build. Define brand variables once.

**Paste this starter CSS** for the MarTech Primer build:

```css
:root {
  --brand-navy: #0a1628;
  --brand-gold: #c69009;
  --brand-cream: #f5f1e8;
}
html { scroll-behavior: smooth; }
body { margin: 0; padding: 0; }
```

## 3.6 Typography

Default fonts for headings and body text. Affects native VIBE elements (popup form, etc.) so they match your custom sections.

- **Where:** Top bar → **Settings** (gear) → **Typography** tab
- **When:** once at the start. For the MarTech Primer build:
  - Headings: **Fraunces** (Google Fonts)
  - Body, links, buttons: **Inter** (Google Fonts)
  - VIBE auto-injects the Google Fonts link.

## 3.7 Background

Page-level background color/gradient/image.

- **Where:** Top bar → **Settings** (gear) → **Background** tab
- **When:** set to brand navy `#0a1628` so any gaps between blocks still feel branded

## 3.8 Popup Settings

Where you'll build the exit-intent popup (covered in Part 6).

- **Where:** Top bar → **Settings** (gear) → **Pop-up** tab
- **When:** Part 6. The popup is page-level (lives outside the stacked blocks).

## 3.9 SEO Meta Data

Page title, description, favicon, social sharing image.

- **Where:** Top bar → **Settings** (gear) → **SEO Meta Data** tab
- **When:** before publishing. Title <60 chars, description 120–160 chars.

## 3.10 Preview Custom Codes

Toggle for whether tracking codes/Custom HTML actually run during preview.

- **Where:** Top bar → **Preview** (eye icon) → toggle
- **When:** keep **off** during build (avoid polluting analytics). Turn **on** for final QA.

## 3.11 Cookie Consent

GDPR/CCPA banner. Required if you collect data from EU/California visitors — and you do.

- **Where:** Sub-account **Settings** → **Cookie Consent**
- **When:** before going live. Configure once at sub-account level.

## 3.12 Versions

Auto-saved snapshots; manual checkpoints.

- **Where:** Top bar → **Versions** (history icon)
- **When:** save a manual checkpoint after every block. Saves your ass when something breaks.

---

# Part 4 — The Vibe Coding Workflow

Every block on every page uses these **5 steps**. Memorize them.

## Step 1: Set context with your AI tool (once)

The first time you open your AI tool for this build, paste this context message:

```
I'm building a lead-capture funnel for the MarTech Primer book at
book.martechprimer.com, using GoHighLevel/VIBE. I'll be generating
sections one at a time from scratch. Each section gets pasted into a
Custom HTML/Javascript element on a blank funnel page.

CONSTRAINTS for every section you generate:
- Self-contained HTML in one block
- All CSS inline in a <style> tag at the top
- All JavaScript inline in <script> tags AT THE BOTTOM and NEVER inside divs
  (VIBE strips scripts that are nested inside divs)
- NO <link> tags anywhere in the output — VIBE's Custom HTML container
  strips them and the entire block fails to render. Google Fonts are
  loaded at the page level via Tracking Code, so just USE the font names
  in your CSS (font-family: 'Fraunces', serif; etc.) without importing them.
- No external CSS files, no frameworks (no Tailwind, React, Vue) — vanilla only
- Mobile-first responsive (works at 360px and up)
- Brand colors: --brand-navy #0a1628, --brand-gold #c69009,
  --brand-cream #f5f1e8
- Brand fonts: Fraunces (serif, for headings), Inter (sans, for body)
- Each section is a standalone block — no dependency on other sections

I'll send section specs one at a time. Acknowledge when ready.
```

Wait for the AI to acknowledge.

> **Important — set up Google Fonts at the page level BEFORE you start vibe coding:**
>
> 1. Funnel editor → top bar → **Settings** (gear) → **Tracking Code** tab.
> 2. In the **Header** field, paste:
>
> ```html
> <link rel="preconnect" href="https://fonts.googleapis.com">
> <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
> <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
> ```
>
> 3. Save. Do the same on the Thanks Page step.
>
> Now Fraunces and Inter are available everywhere on the page. Custom HTML blocks just reference them by name (`font-family: 'Fraunces', serif;`) without any imports or link tags inside the block.

## Step 2: Send the section's prompt

Send the section-specific prompt (provided in Part 5). The AI returns the full HTML/CSS/JS for that block.

## Step 3: Drop a Custom HTML/Javascript element on the page

In VIBE editor:
- Top-left → **Add Element (+)** → search **Custom**
- Drag **Custom HTML/Javascript** to the next empty spot on the page

## Step 4: Paste the code

- Click the new Custom HTML/Javascript element
- Right panel → click **Open Code Editor**
- Paste the AI's output → click **Save** in the popup

## Step 5: Preview, iterate, save version

- Top bar → **Save** → **Preview**
- If it looks right: top bar → **Versions** → **Save Version** → name it (e.g., "Hero added")
- If something's off: copy the current code out of the Code Editor, paste it back into your AI with "Change [specific thing]," paste the new version back

That's one block. Move to the next.

---

# Part 5 — Vibe Code the Sales Page (7 Blocks)

Open the **Sales Page** step in the editor. It's currently blank. We'll fill it with 7 stacked Custom HTML/Javascript blocks.

For each block: send the prompt → get code → drop element → paste code → save version. Just run Part 4 each time.

**Block 5 is special** — you'll pause the editor, build the form in Sites → Forms, set up the tagging workflow, then come back. Everything else is straight vibe coding.

---

## Block 1 — Hero

```
Generate Block 1: Hero section for the MarTech Primer book.

LAYOUT:
- Two columns on desktop (left: text; right: book visual). Single column on mobile.
- Min-height: 90vh

LEFT COLUMN:
- Eyebrow text in --brand-gold: "FREE CHAPTER • 2026"
- Big serif (Fraunces) headline: "The Marketing Technology Book Every Modern
  Marketer Needs"
- Subheadline (Inter): "From the AI revolution to the modern stack — your
  essential guide to navigating MarTech in 2026 and beyond."
- Primary CTA button: "Get the Free Chapter"
  - On click: smooth-scroll to #lead-form (the inline form block we'll add later)
- Trust badge below the button: "★★★★★  Join 500+ marketers on the
  early-access list"

RIGHT COLUMN:
- A book cover mockup (use a 400x600 picsum.photos placeholder for now)
- Subtle 3D tilt or hover effect

BACKGROUND:
- Gradient from --brand-navy to a darker navy/purple

TYPOGRAPHY:
- Headline: Fraunces, 700 weight
- Body: Inter, 400/500
- Eyebrow: uppercase, generous letter-spacing
```

Run Part 4 → Save Version → "Hero added."

---

## Block 2 — Social Proof / Logo Bar

```
Generate Block 2: Social proof / logo bar for the MarTech Primer landing page.

LAYOUT:
- Compact section (not full viewport height)
- Centered tagline: "As featured in"
- Below: a horizontal row of 5 publication-logo placeholders (use grayscale
  text logos like "Logoipsum" — I'll replace with real logos later)
- On mobile: logos wrap to 2-3 per row

STYLE:
- Background: --brand-navy
- Logos in muted gray with hover brighten
- Tagline: Inter, smaller, uppercase letter-spacing
```

Run Part 4 → Save Version → "Social proof added."

---

## Block 3 — Benefits Grid

```
Generate Block 3: "What You'll Master" benefits grid for MarTech Primer.

LAYOUT:
- Section title centered (Fraunces): "What You'll Master"
- Subtitle (Inter): "Six capabilities that separate top marketers from the
  rest in 2026"
- 3-column grid on desktop, 1-column on mobile, with these 6 cards:

  1. "AI-Native Workflows" — How to architect marketing operations around
     AI agents, not bolted onto them.
  2. "The Modern Stack" — A clear-eyed map of which MarTech tools matter
     and which are noise.
  3. "Data Without the BS" — Practical analytics that drive decisions, not
     vanity dashboards.
  4. "Attribution That Works" — Multi-touch attribution in a privacy-first
     world.
  5. "Automation at Scale" — Building workflows that compound, not collapse,
     as you grow.
  6. "The Human Layer" — Where strategy, creativity, and judgment still beat
     any tool.

EACH CARD:
- Inline SVG icon at top in --brand-gold (unique geometric icon per card)
- Title: Fraunces, 600 weight
- Description: Inter, 2 lines max
- Subtle hover: lift + shadow
- Background: --brand-cream with --brand-navy text
```

Run Part 4 → Save Version → "Benefits added."

---

## Block 4 — Inside the Book Showcase

```
Generate Block 4: "Inside the Book" showcase for MarTech Primer.

LAYOUT:
- Section title (Fraunces): "Inside the Book"
- Subtitle (Inter): "300 pages. 12 chapters. Zero fluff."
- Centered: a large book mockup using CSS 3D transforms with subtle depth.
  Slow auto-rotate animation (12 seconds for full 360°), pausing on hover.
  Use a 400x600 picsum.photos placeholder for the cover.
- Below the book: 4 chapter teasers as a horizontal scrolling marquee
  (auto-scroll on desktop, swipeable on mobile):
  - "Chapter 1: The MarTech Landscape"
  - "Chapter 4: AI Workflow Architecture"
  - "Chapter 7: Attribution in a Cookieless World"
  - "Chapter 11: Building the Compound Stack"

STYLE:
- Background: --brand-navy with subtle radial gradient highlights
- Pure CSS for the rotation and marquee animations, no external libraries
```

Run Part 4 → Save Version → "Showcase added."

---

## Block 5 — Inline Form Section ⭐

This is the lead-capture block. Before you generate the HTML, you need an actual form to embed inside it. We'll pause the editor, build the form, get its embed code, set up tagging, then come back.

### 5.1 — Build the form in Sites → Forms

Open a **new browser tab** (don't close the funnel editor — you'll come back to it).

1. In the new tab, go to VIBE → Left sidebar → **Sites** → **Forms** tab.
2. Click **+ New Form** → **Form Builder**.
3. Drag these fields onto the canvas in this order:
   - **First Name** — required
   - **Email** — required
   - **Phone** — *not* required (toggle off the Required setting in the right panel when the field is selected)
4. Add a **Submit Button** at the bottom. Edit its label to: `Send Me the Free Chapter`.
5. Click the pencil icon next to the form name at the top → rename to `MarTechPrimerForm`.

### 5.2 — Configure form behavior (Settings tab)

Click the **Settings** tab at the top of the form builder.

**On Submit:**
- **Action:** **Redirect to URL**
- **URL:** `https://book.martechprimer.com/thanks`

**Form Settings (scroll down):** Leave all four toggles **ON** (they're on by default for good reasons):

| Toggle | Why keep it ON |
|--------|----------------|
| **Sticky Contact** | Auto-fills the form on return visits |
| **Create Conversation on Submission** | Creates a thread in Conversations so you can reply to leads |
| **Enable Timezone** | Captures submitter's timezone for follow-up timing |
| **Use GDPR Compliant Font** | Privacy-safe Google Fonts loading (required for EU compliance) |

Save the form.

### 5.3 — Get the iFrame embed code

1. Click the **Integrate** button (top of the form builder).
2. Dialog opens titled **"Embed or Share Form"**. You'll see three tabs on the left: **Embed Code** | **Share** | **Email**.
3. Click the **Embed Code** tab.
4. Confirm these settings (defaults are correct for inline use):
   - **Embed Layout Type:** Inline
   - **Trigger type:** Always show
   - **Activation options:** Always activated
   - **Deactivation options:** Never deactivate
5. Click the blue **Copy embed code** button (bottom-right).
6. **Paste the embed code into a notes file** somewhere on your Mac — you'll paste it into the AI prompt below. Don't lose it.

> **Bonus:** the Share tab has a public hosted link to the form (`https://link.vibereach.io/widget/form/[id]`) — handy for testing in incognito or sharing as a direct opt-in URL in emails/SMS.

### 5.4 — Set up the tagging workflow

Tags aren't set in form settings — they're added through Workflows. Set this up now so every submission auto-tags the new contact.

1. Left sidebar → **Automation** → **Workflows**.
2. Click **+ Create Workflow** → **Start from Scratch**.
3. **Workflow Name:** `MarTech Primer — Lead Capture Tagging`
4. **Trigger:** Click **+ Add New Workflow Trigger** → select **Form Submitted**.
5. In the trigger config: **Form is** → select `MarTechPrimerForm`. Save.
6. Add an **Action** → search **Add Contact Tag** → **Tags:** `martech-primer-lead` → Save.
7. Toggle the workflow to **Publish** at the top of the editor.

Now every form submission auto-creates a contact, applies the `martech-primer-lead` tag, creates a conversation thread, and redirects to the Thanks Page.

### 5.5 — Generate the Block 5 HTML in your AI tool

Now go back to your AI tool. Send this prompt — pasting your embed code where indicated:

```
Generate Block 5: Inline lead-capture form section for MarTech Primer.

CRITICAL: This section contains a VIBE form embed code that MUST be kept
exactly intact in the output. Do not modify it, do not add classes to it,
do not wrap it in additional containers beyond the section structure I'm
asking for. Just place the embed code where the form should go.

THE EMBED CODE TO PRESERVE EXACTLY:

[PASTE YOUR iFRAME EMBED CODE FROM STEP 5.3 HERE]

LAYOUT:
- Wrap the entire section in: <section id="lead-form">...</section>
  (this is critical — the hero CTA scrolls to #lead-form)
- Two-column on desktop (left: pitch; right: form). Stacked on mobile.

LEFT COLUMN:
- Eyebrow in --brand-gold: "GET STARTED"
- Headline (Fraunces): "Read the First Chapter Free"
- 3 bullet points of what they'll get when they submit:
  - "Chapter 1 PDF delivered to your inbox in under 60 seconds"
  - "Early-access pricing when the book launches"
  - "Monthly MarTech insights newsletter (unsubscribe anytime)"
- "No spam. Unsubscribe anytime." disclaimer text below the bullets

RIGHT COLUMN:
- The iFrame embed code I pasted above goes here, untouched

STYLE:
- Background: gradient from --brand-cream to white
- Form right column: white background card with subtle shadow,
  generous padding so the embedded form has room to breathe
- The form's iframe should be set to width: 100% and a min-height of
  500px so it doesn't get clipped
- Headline and bullet text in --brand-navy
```

### 5.6 — Drop the block into the funnel and paste

Switch back to your funnel editor tab.

- Add Element (+) → search **Custom** → drag **Custom HTML/Javascript** below Block 4
- Click the new element → **Open Code Editor** → paste the AI's output → Save
- Top bar → **Save** → **Preview**

Test: scroll to the new block, fill out the form, submit. You should be redirected to the (still-blank) Thanks Page. Back in VIBE → **Contacts** → confirm the test entry appears with the `martech-primer-lead` tag.

Save Version → "Form section added."

> **The section wrapper must have `id="lead-form"`** because the hero CTA's `href="#lead-form"` smooth-scrolls to this exact id. If your AI's output dropped that id, fix it manually before the next block.

---

## Block 6 — Final CTA

Back to straight vibe coding. No more pauses.

```
Generate Block 6: Final CTA / closing section for MarTech Primer.

LAYOUT:
- Centered, generous padding
- Big serif (Fraunces) headline: "Don't Build Your 2026 Stack Without It"
- Subheadline (Inter): "Get Chapter 1 free, get on the early-access list,
  and start thinking differently about MarTech in the next 60 seconds."
- Primary CTA button: "Get the Free Chapter"
  - On click: smooth-scroll to #lead-form
- Below button: small trust line, "No spam. Unsubscribe anytime."

STYLE:
- Background: gradient from --brand-gold to --brand-navy
- Big bold headline (use clamp() for responsive font-size)
- Button: --brand-cream background with --brand-navy text, hover lift
```

Run Part 4 → Save Version → "Final CTA added."

---

## Block 7 — Footer

```
Generate Block 7: Footer for the MarTech Primer landing page.

LAYOUT:
- Compact section
- Centered: small wordmark "MarTech Primer"
- Below: a row of links — Privacy Policy, Terms, Contact
- Below: copyright line "© 2026 MarTech Primer. All rights reserved."

STYLE:
- Background: --brand-navy, slightly darker than the page
- Text: muted cream, smaller
- Links: subtle hover underline
- Wordmark: Fraunces, 600 weight
```

Run Part 4 → Save Version → "Footer added."

---

## Sales Page status check

You should now have 7 stacked Custom HTML/Javascript blocks:

1. Hero
2. Social Proof
3. Benefits Grid
4. Book Showcase
5. Form Section (with the iFrame embed inside)
6. Final CTA
7. Footer

Click **Preview** to see the whole page. Test the hero CTA → it should smooth-scroll to the form. Submit a test entry → it should redirect to the Thanks Page (which is still blank — fix that in Part 7).

---

# Part 6 — Build the Exit-Intent Popup

The popup is page-level, not a stacked block. It lives in the popup editor.

## Step 1: Open popup settings

1. Make sure you're on the **Sales Page** step in the editor.
2. Top bar → **Settings** (gear) → **Pop-up** tab.

## Step 2: Enable the popup

Toggle **Enable Popup** to **ON**.

## Step 3: Configure the trigger

- **Trigger Type:** **Exit Intent**
- **Show on:** Desktop only (mobile doesn't have exit intent — there's no mouse to detect leaving)

## Step 4: Build the popup content

Click **Edit Popup** (or similar — opens the popup design surface).

Inside the popup builder:

1. Add an element → **Custom HTML/Javascript**
2. Paste the **same iFrame embed code from Block 5.3**
3. Add a headline element above the form: "Wait — Don't Leave Empty-Handed"
4. Add a subheadline element: "Get a free chapter of MarTech Primer before you go."
5. Style with brand colors (cream background, navy text, gold accents)

Why use the same form? It keeps your single MarTechPrimerForm as the source of truth — same redirect, same tag, same workflow. Two capture points, one form.

## Step 5: Set redirect

In popup settings:

- **On Submit Action:** **Open URL** (Redirect URL)
- **Redirect URL:** `https://book.martechprimer.com/thanks`

## Step 6: Save

Save the popup. Save Version → "Popup configured."

---

# Part 7 — Vibe Code the Thanks Page

Switch to the **Thanks Page** step in the editor (top bar **Sales Page** dropdown → **Thanks Page**). It's blank.

## Single block — Thanks Page content

```
Generate the Thanks Page content for the MarTech Primer funnel.

LAYOUT:
- Centered, full viewport height
- Top: animated SVG checkmark drawing in via stroke-dasharray (1 second)
- Headline (Fraunces): "Your free chapter is on the way!"
- Subheadline (Inter): "Welcome to the MarTech Primer family. Here's what
  happens next:"
- Below: 3 next-step cards (3-column on desktop, stacked on mobile):
  1. "📧 Check Your Email" — Chapter 1 of MarTech Primer is on its way to
     your inbox. Look for a message from book@martechprimer.com.
  2. "⭐ Add to Calendar" — The book launches in Q2 2026. Save the date and
     get early-access pricing.
  3. "💬 Join the Community" — Get exclusive access to the private Slack
     for early readers, including monthly Q&A with the author.
- Confetti animation on page load using vanilla JS canvas (no external library)

STYLE:
- Background: gradient from --brand-cream to white
- Brand colors throughout
- Friendly, celebratory tone
```

Run Part 4 → Save Version → "Thanks Page added."

---

# Part 8 — Final Setup and Publish

## Step 1: Set the default page

The funnel is already connected to `book.martechprimer.com` (from Part 2). Now make sure the Sales Page loads as the root.

1. Sub-account left sidebar → **Settings** → **Domains**.
2. Find `book.martechprimer.com` → **Manage Domain** → **Edit Domain**.
3. **Default Page:** select your funnel's first step (Sales Page).
4. Save.

## Step 2: Add Cookie Consent (sub-account level)

1. Sub-account **Settings** → **Cookie Consent**.
2. Toggle **Enable**. Configure banner text. Save.

## Step 3: Add tracking codes (each step)

For Sales Page AND Thanks Page:

1. Open the step in the editor.
2. Top bar → **Settings** (gear) → **Tracking Code**.
3. Paste your GA4, Meta Pixel, etc. into the **Header** field. Save.

## Step 4: SEO Meta Data (each step)

For Sales Page:

- **Page Title:** `MarTech Primer — The Marketing Technology Book for 2026`
- **Description:** `From AI workflows to the modern stack — your essential guide to navigating MarTech in 2026 and beyond. Get a free chapter.`
- **Favicon:** 32×32 PNG of book cover or wordmark
- **OG Image:** 1200×630 promo image of the book

For Thanks Page:
- **Page Title:** `Thanks — Your Free Chapter Is On the Way | MarTech Primer`
- **Description:** Brief confirmation copy.

## Step 5: Publish

Funnel editor → top bar → **Publish**.

## Step 6: Test in incognito

Open an **incognito window** → visit `https://book.martechprimer.com`.

- Sales page renders ✓
- Hero CTA scrolls to inline form ✓
- Submitting the inline form redirects to Thanks Page ✓
- Move mouse toward browser tab edge on desktop → exit-intent popup fires ✓
- Submitting popup form redirects to Thanks Page ✓
- Back in VIBE → **Contacts** → both test entries appear with the `martech-primer-lead` tag ✓

✅ Live.

---

# Final Sanity Check

- [ ] `https://book.martechprimer.com` loads in incognito with HTTPS padlock
- [ ] All 7 Sales Page blocks render correctly on desktop and mobile
- [ ] Hero CTA smooth-scrolls to inline form
- [ ] Inline form submit creates a contact → redirects to Thanks Page
- [ ] Exit-intent popup fires on desktop when mouse approaches tab edge
- [ ] Popup form submit creates a contact → redirects to Thanks Page
- [ ] Thanks Page renders with confetti
- [ ] Tracking codes added to both steps
- [ ] Cookie Consent enabled at sub-account level
- [ ] SEO Meta Data filled in for both steps
- [ ] Final Version saved as a checkpoint

---

# Troubleshooting

**Custom HTML block renders blank**
A `<script>` tag is nested inside a `<div>`. VIBE strips these. Tell your AI: "Move all `<script>` tags to be siblings of divs, not children." Regenerate, paste back.

**The whole page is blank on Preview — nothing renders at all**
Usually one of two things:
1. **`<link>` tags in your Custom HTML.** VIBE's Custom HTML container strips `<link>` tags and the block fails to render. Move Google Fonts to **Settings → Tracking Code → Header** at the page level, then tell your AI to stop emitting `<link>` tags in Custom HTML blocks (the page-level fonts are still available).
2. **Syntax error in the pasted code.** Right-click the blank page → **Inspect** → check the **Elements tab** for your block's outermost class (e.g., `.mtp-hero`). If the section is missing from the DOM entirely, VIBE rejected it. Re-generate the code without `<link>` tags and with all scripts at the root.

**I see a bunch of console errors when I open the preview**
If they all say *"The policy is report-only, so the violation has been logged but no further action has been taken"* — those are **CSP report-only warnings**. They look scary but they don't block anything; VIBE is in monitoring mode, not enforcement mode. If your page renders visually, you're fine. Ignore them. Similarly, scripts from browser extensions ("SynthReader," "injectedMethodUS," etc.) and 400 errors from `backend.leadconnectorhq.com/stats/event` are not your problem — they're either your installed browser extensions or VIBE's internal stats endpoint hiccupping. Page still works.

**Embedded form doesn't show up in Block 5**
The iFrame may have been modified by the AI despite your instructions. Open the Code Editor for Block 5 → confirm the iFrame `src` and attributes are *exactly* what Sites → Forms gave you. Worst case, replace the iFrame portion of the AI's output with the original embed code by hand.

**Form submits but no contact appears**
Open the form in Sites → Forms → verify the field mappings. Submit a test → check in Contacts.

**Tag isn't being applied**
Check that the workflow is **Published** (Automation → Workflows → your workflow → toggle at the top). Draft workflows don't fire.

**Hero CTA doesn't scroll to form**
The form section's wrapper must have `id="lead-form"`. Open Block 5 in the Code Editor → confirm the outermost element is `<section id="lead-form">`. Fix if missing.

**Exit-intent popup never fires**
Exit intent only works on desktop (no mouse on mobile). Make sure trigger is set to **Exit Intent** in **Settings → Pop-up** and that it's enabled.

**Layout breaks on mobile**
Each Custom HTML block should include `<meta name="viewport" content="width=device-width, initial-scale=1.0">` if it isn't inheriting one. Use mobile-first CSS.

**`book.martechprimer.com` shows 404**
DNS hasn't propagated. Wait 10 minutes. Check at https://dnschecker.org. Then re-verify in Settings → Domains.

**I broke something**
Funnel editor → top bar → **Versions** → pick a previous version → Restore.
