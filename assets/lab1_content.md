## 1.12 Lab 1: Import Contacts, Apply Tags, and Build Your First Three Smart Lists

Your CRM is only as useful as the data inside it and the organization applied to that data. In this lab, you import 30 real-looking South Florida business contacts, tag them by lead source, and build three dynamic Smart Lists that will power targeting decisions throughout the rest of this course. By the end, you will have a live, organized contact database — not a flat spreadsheet, but a structured, filterable marketing asset.

:::{admonition} Lab Prerequisites
:class: note
Before starting this lab, you need:
- An active VibeReach.io sub-account with admin access
- The Lab 1 contacts CSV downloaded (link below)
- Approximately 30–45 minutes

📥 **[Download lab01-contacts.csv](https://raw.githubusercontent.com/liquid-books/vibe-marketing-martech/main/assets/lab01-contacts.csv)**

The file contains 30 realistic South Florida business contacts with 13 fields: first name, last name, email, phone, business name, industry, lead source, city, state, annual revenue, employees, last contact date, and notes.
:::

---

### Step 1: Create Custom Fields Before Importing

Some of the CSV fields do not have default GHL mappings — you must create them first.

1. In the left sidebar, click ⚙️ **Settings** → **Custom Fields**.
2. Click the **Contacts** tab.
3. Click **+ Add Field** in the upper right.
4. Create three custom fields:
   - **Field Name:** `Industry` · **Field Type:** Text
   - **Field Name:** `Annual Revenue` · **Field Type:** Number
   - **Field Name:** `Employees` · **Field Type:** Number
5. Click **Save** after creating each field.

:::{admonition} Why This Matters
:class: tip
Custom fields are how GHL stores information that doesn't fit the default contact schema. If you try to import a CSV with columns that don't exist as fields, those columns are either dropped or create mapping errors. Creating the fields first ensures no data is lost during import.
:::

**You'll know you did this right when:** All three custom fields (Industry, Annual Revenue, Employees) appear in the Contacts section of Settings → Custom Fields.

---

### Step 2: Import the CSV

1. In the left sidebar, click **Contacts**.
2. In the Contacts view, click the **Smart Lists** tab at the top.
3. Click the **Import** (downward arrow) icon in the upper right of the page.
4. Select **Contacts** → click **Next**.
5. Click **Upload File** → select `lab01-contacts.csv` from your desktop → click **Open**.
6. In the "Import Type" dropdown, select **Create new contacts** → click **Next**.

**You'll know you did this right when:** The file upload completes and you see the field mapping screen with your CSV column headers on the left.

---

### Step 3: Map Your Fields

On the mapping screen, match each CSV column to the correct GHL field:

| CSV Column | Map To |
|------------|--------|
| first_name | First Name (standard) |
| last_name | Last Name (standard) |
| email | Email (standard) |
| phone | Phone (standard) |
| business_name | Company Name (standard) |
| city | City (standard) |
| state | State (standard) |
| notes | Notes (standard) |
| industry | Industry (custom field you created) |
| lead_source | Lead Source (standard — select from dropdown) |
| annual_revenue | Annual Revenue (custom field) |
| employees | Employees (custom field) |
| last_contact_date | Last Contact Date (use Date type custom field if needed) |

For any column you cannot map, check "Don't import data for unmapped columns."

Click **Next** → **Import**.

:::{admonition} Why This Matters
:class: tip
Proper field mapping is what turns a flat CSV into a queryable database. When fields are correctly mapped, you can build Smart Lists like "contacts with annual revenue over $1M" or "contacts whose last contact date was more than 30 days ago." Unmapped data is permanently lost — it cannot be recovered without re-importing.
:::

**You'll know you did this right when:** The import completes and your All Contacts count increases to reflect the 30 new records. Check that a contact record shows the Industry and Annual Revenue values populated.

---

### Step 4: Apply Tags by Lead Source

You will now tag each contact group based on their lead source. Tags let you build behavioral segments and trigger automations.

For each lead source value in the CSV (Referral, Paid Ads, Website Form, Inbound Call, Cold Outreach):

1. In **Contacts → All Contacts**, click **Advanced Filters**.
2. Add filter: **Lead Source** | **is** | `[value]` (e.g., Referral) → click **Apply**.
3. Check the header checkbox to select all filtered contacts.
4. Click **Actions** → **Add Tag** → type the tag name → **Confirm**.

Apply these tags:
- Lead Source = Referral → tag: `referral`
- Lead Source = Paid Ads → tag: `paid-ads`
- Lead Source = Website Form → tag: `website-form`
- Lead Source = Inbound Call → tag: `inbound-call`
- Lead Source = Cold Outreach → tag: `cold-outreach`

:::{admonition} Why This Matters
:class: tip
Lead Source is a standard field, but tags are behavioral markers you can layer on top. A contact tagged `referral` can be treated differently in automations than one tagged `cold-outreach` — different messaging tone, different follow-up cadence, different offers. Tags are how you personalize at scale.
:::

**You'll know you did this right when:** Open any contact from the imported list and confirm their lead-source tag appears under the Tags section of their contact record.

---

### Step 5: Build Smart List #1 — Hot Leads (Contacted Last 7 Days)

1. In **Contacts**, click the **Smart Lists** tab.
2. Click **+ Smart List** (or **+ New Smart List**).
3. **Name:** `Lab — Hot Leads: Contacted Last 7 Days`
4. Click **Advanced Filters**:
   - Filter: **Last Contact Date** | **is** | **Last 7 days**
5. Click **Apply** → **Save Smart List**.

The list updates automatically every time a contact's Last Contact Date falls within the trailing 7-day window.

**You'll know you did this right when:** The Smart List saves and shows a live contact count. If the count is zero, that's correct — the sample data's Last Contact Dates may be outside the last 7 days. The list will populate as you use the system.

---

### Step 6: Build Smart List #2 — High Revenue Prospects

1. **+ New Smart List** → Name: `Lab — High Revenue Prospects`
2. **Advanced Filters** → Filter: **Annual Revenue** | **is greater than** | `1000000`
3. **Apply** → **Save Smart List**.

Expect approximately 8–12 contacts from the sample data to qualify (businesses with annual revenue over $1M).

**You'll know you did this right when:** The Smart List shows a non-zero count and the contact records in the list all have Annual Revenue values exceeding $1,000,000.

---

### Step 7: Build Smart List #3 — Uncontacted Referrals

1. **+ New Smart List** → Name: `Lab — Uncontacted Referrals`
2. **Advanced Filters**:
   - Filter 1: **Tags** | **contains** | `referral`
   - Click **+ Add Nested Filter (AND)**
   - Filter 2: **Last Contact Date** | **is empty**
3. **Apply** → **Save Smart List**.

This list finds referral contacts who have never been contacted — your highest-priority outreach targets, since referral leads close at the highest rate and you haven't even reached out yet.

:::{admonition} Why This Matters
:class: tip
The AND logic is what makes this list powerful. A referral who's already been contacted is different from one who hasn't. The compound filter finds only the contacts at the intersection of both conditions — the specific people who need your attention most, right now.
:::

**You'll know you did this right when:** The Smart List shows contacts who have the `referral` tag AND no Last Contact Date populated.

---

:::{admonition} Expected Outcome
:class: tip
Verify each item before moving to Chapter 2:

- ☐ Custom fields created: Industry, Annual Revenue, Employees
- ☐ 30 contacts imported successfully (All Contacts count increased)
- ☐ Every imported contact has a lead-source tag (referral, paid-ads, website-form, inbound-call, or cold-outreach)
- ☐ Smart List #1 saved: Hot Leads (Last 7 Days) — live count shown
- ☐ Smart List #2 saved: High Revenue Prospects — shows contacts over $1M revenue
- ☐ Smart List #3 saved: Uncontacted Referrals — shows referral contacts with no contact date

You now have a structured, segmented contact database. The Smart Lists you built here are the foundation for every targeted campaign and automation in the chapters ahead.
:::

::::{dropdown} Troubleshooting Common Issues

**0 contacts imported — the count didn't change:**
Verify the CSV is properly formatted (comma-separated, UTF-8 encoding, header row present). Confirm at least one of Email or Phone is mapped — GHL requires a unique identifier. Try opening the CSV in a plain text editor to check for hidden characters or formatting issues.

**Custom field mapping not appearing during import:**
Custom fields must be created *before* starting the import. If you created them after beginning the import flow, cancel, return to Settings → Custom Fields → Contacts, confirm they saved, then restart the import.

**Smart List returns 0 contacts after saving:**
For the "Last 7 Days" filter: check whether the sample CSV's Last Contact Date values fall outside the trailing 7 days (the sample data uses realistic dates that may be older). The filter is correct — the list will populate as you use the system with real contacts.

For the "Annual Revenue" filter: verify the field was mapped as a Number type (not Text) during import. If it was mapped as Text, the "greater than" numeric comparison will not work. Re-import or manually update a few records to test.

**Actions menu doesn't appear after selecting contacts:**
You must check the header checkbox to select all visible contacts before the bulk Actions button appears. Clicking individual checkboxes on each row also works, but the header checkbox selects all at once.

**Tags not sticking — contacts lose their tags:**
This happens if you apply a tag and then immediately start a new filtered view before the save is confirmed. Apply tags for one lead source group, confirm the tag appears on at least one contact, then move to the next group.
::::

