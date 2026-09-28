#!/usr/bin/env python3
"""Generates the services/, products/ and packages/ page trees for the Jekyll site.

OPTIONAL TOOL. Run from the site root:  python3 tools/generate_pages.py  (needs: pip install pyyaml)
WARNING: this OVERWRITES every generated page in services/, products/ and packages/, including any edits you
have made to them by hand. Use it to rebuild from scratch, or copy an existing page to add a single new one.
"""
import os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the site root (parent of tools/)

def write(path, front_matter, body=""):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    fm = yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    with open(full, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(fm)
        f.write("---\n")
        if body:
            f.write(body.strip() + "\n")

SERVICE_FOOTNOTE = ("<strong>Note:</strong> All automations are built around tools you already use "
    "(Gmail, Outlook, Xero, QuickBooks, HubSpot, and others). A short discovery call is required "
    "before final pricing is confirmed. Turnaround is typically 5&ndash;10 working days from "
    "project confirmation.")
PRODUCT_FOOTNOTE = ("<strong>Note:</strong> Once live, every pack in this shop is an instant digital "
    "download &mdash; no automation build or discovery call required.")

TUTORING_FOOTNOTE = ("<strong>Note:</strong> Get in touch with the subject, level and exam board (if relevant) "
    "and we'll confirm availability and pricing.")
TUTORING_BODY = ("<p>Sessions are tailored to the student's exam board, current grade and goals. When you get in "
    "touch, it helps to mention the subject, the level, and any upcoming exam dates.</p>")
TUTORING_PRICE_NOTE = "Pricing depends on subject, level and how often sessions run &mdash; get in touch and we'll confirm."

REASSURANCE = ('<p>Like everything we build, this runs on the tools you already use &mdash; nothing new '
    'to learn, and a free discovery call before anything goes live.</p>')

# ---------------------------------------------------------------------------
# STAR (Phase 1) body content — the four priority pages get real depth
# ---------------------------------------------------------------------------
STAR_BODIES = {
    "invoice-chasing-automation": """
<h3>How it works</h3>
<p>Your invoicing system (or spreadsheet) is connected once. From then on, every unpaid invoice is tracked
against its due date automatically. When an invoice runs late, a friendly reminder goes out on the
schedule you set &mdash; no one on your team has to remember to chase it.</p>
<h3>What's included</h3>
<ul>
<li>Connection to your existing invoicing tool (Xero, QuickBooks, or a spreadsheet)</li>
<li>A reminder sequence you approve before it goes live &mdash; tone, timing and number of nudges</li>
<li>A simple log of what's been sent and what's still outstanding</li>
</ul>
<h3>Good to know</h3>
<p>Because reminders go out consistently &mdash; not just when someone remembers &mdash; invoices tend to
get paid sooner, without anyone having to send an awkward chasing email themselves.</p>
""",
    "ai-invoice-receipt-processing": """
<h3>How it works</h3>
<p>Send invoices and receipts in however they arrive &mdash; email attachment, photo, or a shared folder.
AI reads each one, pulls out the supplier, amount, date and VAT, and matches it to the right category
before it lands in Xero or QuickBooks.</p>
<h3>What's included</h3>
<ul>
<li>Connection to your inbox, a shared folder, or both</li>
<li>Matching rules tuned to your chart of accounts</li>
<li>A review step for anything the AI isn't confident about, so nothing gets filed wrongly</li>
</ul>
<h3>Good to know</h3>
<p>This pairs well with Remote Bookkeeping and AI Expense Management if you want the whole finance admin
loop covered, not just data entry.</p>
""",
    "email-triage-routing": """
<h3>How it works</h3>
<p>Your inbox is connected once. Incoming email is read, classified &mdash; invoice, support query,
urgent, general &mdash; and either routed to a folder, forwarded to the right person, or flagged, based
on rules you set.</p>
<h3>What's included</h3>
<ul>
<li>Classification rules built around how your inbox actually works today</li>
<li>Routing to folders, labels, or specific team members</li>
<li>A weekly summary of what's coming in, if you want one</li>
</ul>
<h3>Good to know</h3>
<p>Most businesses start here because it's quick to set up and the effect &mdash; an inbox that's actually
manageable &mdash; is immediate.</p>
""",
    "lead-capture-crm-follow-up": """
<h3>How it works</h3>
<p>Every form submission, whether from your website, a landing page, or a lead ad, is added to your CRM
automatically. The lead gets an instant welcome email, and you get notified so a warm enquiry never sits
unanswered.</p>
<h3>What's included</h3>
<ul>
<li>Connection to your website form and your CRM (HubSpot, Pipedrive, or similar)</li>
<li>A welcome email sequence you approve before it goes live</li>
<li>Instant notification to you or your sales team</li>
</ul>
<h3>Good to know</h3>
<p>Pairs naturally with AI Lead Qualification &amp; Scoring once volume grows, so your team's time goes to
the leads most likely to convert.</p>
""",
}

# ---------------------------------------------------------------------------
# SERVICES data: category-slug -> (title, intro, [ (name, slug, badge, price, summary) ])
# price=None means POA. slug in STAR_BODIES gets the rich body + star:true.
# ---------------------------------------------------------------------------
SERVICES = {
  "finance-cash-flow": ("Finance & Cash Flow",
    "Keep cash moving without chasing it yourself &mdash; invoicing, receipts, bookkeeping and forecasting, automated.",
    [
      ("Invoice Chasing Automation", "invoice-chasing-automation", "STD", "From &pound;250", "Friendly, automatic payment reminders sent the moment an invoice runs late."),
      ("Automated Invoice Generation", "automated-invoice-generation", "STD", None, "Professional invoices created and sent the moment a job is marked complete."),
      ("Payment Reminder Sequences", "payment-reminder-sequences", "STD", None, "Multi-step reminders scheduled automatically before and after each due date."),
      ("AI Invoice & Receipt Processing", "ai-invoice-receipt-processing", "AI", "From &pound;350", "Invoices and receipts are read by AI, key data extracted, and everything filed into Xero or QuickBooks."),
      ("Intelligent Document Processing (IDP)", "intelligent-document-processing", "AI", None, "Structured data extracted automatically from any business document, not just invoices."),
      ("AI Expense Management", "ai-expense-management", "AI", None, "Receipts are scanned, categorised and matched to transactions automatically."),
      ("Remote Bookkeeping", "remote-bookkeeping", "STD", None, "Ongoing bookkeeping, reconciliation and monthly reporting, handled remotely."),
      ("AI Cash Flow Forecasting", "ai-cash-flow-forecasting", "AI", None, "See cash gaps coming before they happen, using your live accounting data."),
      ("Compliance Document Chasing", "compliance-document-chasing", "STD", None, "Automatic reminders to collect missing compliance documents from clients or suppliers."),
    ]),
  "admin-operations": ("Admin & Operations",
    "The recurring admin that quietly eats a week every month &mdash; sorted, scheduled and summarised automatically.",
    [
      ("Email Triage & Routing", "email-triage-routing", "AI", "From &pound;200", "Your inbox is sorted automatically by type &mdash; invoices, queries, urgent items &mdash; and routed to the right place."),
      ("AI Email & Calendar Management", "ai-email-calendar-management", "AI", None, "AI drafts replies, books meetings and keeps your calendar conflict-free."),
      ("AI Meeting Transcription & Summarisation", "ai-meeting-transcription", "AI", None, "Meetings recorded, transcribed and summarised into action points automatically."),
      ("Data Entry Elimination", "data-entry-elimination", "STD", None, "Stop retyping the same information between systems, automatically."),
      ("Document & File Management", "document-file-management", "STD", None, "Files are automatically named, sorted and filed into the right place."),
      ("Scheduled Report Generation", "scheduled-report-generation", "STD", None, "Recurring reports generated and delivered on a schedule, hands-free."),
      ("AI Business Performance Summaries", "ai-business-performance-summaries", "AI", None, "A plain-English summary of how your business is performing, delivered automatically."),
      ("Weekly/Monthly Dashboards", "weekly-monthly-dashboards", "STD", None, "Live dashboards showing the numbers that matter, always up to date."),
      ("Operations & Job Scheduling", "operations-job-scheduling", "AI", None, "Jobs, shifts and resources scheduled automatically to your own rules."),
      ("Supplier & Purchase Order Management", "supplier-purchase-order-management", "AI", None, "Purchase orders raised, tracked and matched to deliveries automatically."),
      ("Specialist Virtual Assistant", "specialist-virtual-assistant", "STD", None, "A dedicated remote assistant for the recurring admin that eats your week."),
    ]),
  "sales-lead-management": ("Sales & Lead Management",
    "Capture every enquiry, qualify it automatically, and never let a warm lead go cold.",
    [
      ("Lead Capture &rarr; CRM &rarr; Follow-Up", "lead-capture-crm-follow-up", "STD", "From &pound;300", "New enquiries are added to your CRM, welcomed by email and flagged to you instantly."),
      ("AI Lead Qualification & Scoring", "ai-lead-qualification-scoring", "AI", None, "Leads are scored automatically so your team calls the hottest ones first."),
      ("Quoting Agent", "quoting-agent", "AI", None, "Instant, accurate quotes generated automatically from a customer enquiry."),
      ("AI Proposal & Contract Generation", "ai-proposal-contract-generation", "AI", None, "Proposals and contracts drafted automatically from your templates and client details."),
      ("RFP & DDQ Response Agent", "rfp-ddq-response-agent", "AI", None, "First-draft answers to RFPs and due-diligence questionnaires, generated from your own knowledge base."),
      ("CRM Integration & Nurture Workflows", "crm-integration-nurture-workflows", "STD", None, "Automatic nurture sequences that keep leads warm until they're ready to buy."),
      ("Abandoned Cart & Re-engagement", "abandoned-cart-re-engagement", "STD", None, "Automatic follow-ups that win back customers who didn't check out."),
    ]),
  "marketing-content": ("Marketing & Content",
    "Keep a consistent marketing drumbeat &mdash; email, social and search content, created and scheduled automatically.",
    [
      ("Email Marketing Automation Setup", "email-marketing-automation-setup", "STD", None, "Welcome series, newsletters and campaigns, set up and automated for you."),
      ("AI Cold Email Outreach", "ai-cold-email-outreach", "AI", None, "Personalised outreach sequences generated and sent automatically, at scale."),
      ("AI Content Repurposing Studio", "ai-content-repurposing-studio", "AI", None, "One piece of content becomes a week of social posts, automatically."),
      ("AI Social Media Content Generation", "ai-social-media-content-generation", "AI", None, "On-brand social posts drafted and scheduled automatically, week after week."),
      ("SEO Content Writing (British English)", "seo-content-writing-british-english", "STD", None, "Search-optimised articles, written in clear, correct British English."),
      ("Google Review Agent", "google-review-agent", "AI", None, "Happy customers are automatically prompted to leave you a Google review."),
      ("AI Ads Agent", "ai-ads-agent", "AI", None, "Ad copy, targeting and budget managed automatically across your campaigns."),
    ]),
  "customer-support": ("Customer Support",
    "Answer more questions and miss fewer calls, without adding headcount.",
    [
      ("AI Chatbot for Website & WhatsApp", "ai-chatbot-website-whatsapp", "AI", None, "A trained AI chatbot answers customer questions on your site and WhatsApp, 24/7."),
      ("Off-Hours AI Receptionist", "off-hours-ai-receptionist", "AI", None, "Calls outside business hours are answered, logged and routed automatically."),
      ("24/7 AI Voice Agent", "24-7-ai-voice-agent", "AI", None, "A natural-sounding AI voice agent handles calls around the clock."),
      ("AI Email Triage & Classification", "ai-email-triage-classification", "AI", None, "Support emails automatically categorised and routed to the right person."),
      ("Order Processing Automation", "order-processing-automation", "STD", None, "Orders flow from checkout to fulfilment with no manual re-entry."),
    ]),
  "hr-recruitment": ("HR & Recruitment",
    "Screen, onboard and manage leave without the paperwork chase.",
    [
      ("AI Applicant Tracking & CV Screening", "ai-applicant-tracking-cv-screening", "AI", None, "CVs automatically screened and ranked against your job requirements."),
      ("AI Onboarding Automation", "ai-onboarding-automation", "AI", None, "New starters get accounts, documents and welcome tasks set up automatically."),
      ("Time-Off & Leave Management", "time-off-leave-management", "STD", None, "Leave requests, approvals and balances tracked automatically."),
    ]),
  "ecommerce-retail": ("E-commerce & Retail",
    "Keep stock, orders and tenants moving without manual chasing.",
    [
      ("AI Order Processing & Inventory", "ai-order-processing-inventory", "AI", None, "Stock levels update automatically as orders come in and go out."),
      ("AI Supplier & Purchase Order Management", "ai-supplier-purchase-order-management", "AI", None, "Reordering and supplier POs triggered automatically as stock runs low."),
      ("Abandoned Cart Recovery", "abandoned-cart-recovery", "STD", None, "Automatic emails that recover sales from carts left at checkout."),
      ("Event Registration System", "event-registration-system", "STD", None, "Registrations, tickets and confirmations, handled automatically from one form."),
      ("Real Estate / Property Management Automations", "real-estate-property-management-automations", "STD", None, "Tenant enquiries, maintenance requests and renewals, handled automatically."),
    ]),
  "consulting-advisory": ("Consulting & Advisory",
    "Not sure where to start? These sessions map out exactly what to automate, and in what order.",
    [
      ("AI Audit / Workshop", "ai-audit-workshop", "AI", None, "A hands-on session mapping where AI can save your business the most time."),
      ("AI Readiness Assessment", "ai-readiness-assessment", "AI", None, "A clear report on where you stand today, and what to automate first."),
      ("Process Mapping & Workflow Design", "process-mapping-workflow-design", "STD", None, "Your current processes mapped and redesigned for maximum efficiency."),
      ("AI Governance & Safety Consulting", "ai-governance-safety-consulting", "AI", None, "Practical guidance on using AI responsibly, safely and within regulation."),
      ("AI Automation Consulting", "ai-automation-consulting", "AI", None, "Strategic advice on the right automations for your business, in the right order."),
    ]),
  "tutoring-uk": ("Tutoring (UK)",
    "Tutoring for GCSE, A-Level and university-level study, following the UK curriculum.",
    [
      ("GCSE / A-Level Tutoring", "gcse-a-level-tutoring", None, None, "Focused tuition to build confidence and grades across GCSE and A-Level subjects."),
      ("English Tutoring", "english-tutoring", None, None, "Essay technique, comprehension and exam skills for GCSE, A-Level and beyond."),
      ("University-Level Support", "university-level-support", None, None, "Study skills, essay structure and subject support for undergraduates."),
    ]),
}

# ---------------------------------------------------------------------------
# PRODUCTS data: category-slug -> (title, intro, [ (name, slug, summary, [sub-items]) ])
# ---------------------------------------------------------------------------
PRODUCTS = {
  "spreadsheet-templates": ("Spreadsheet Templates", "Excel and Google Sheets templates you can start using the same day.", [
      ("Excel Templates", "excel-templates", "Ready-made Excel workbooks for cash flow, inventory, budgeting and project tracking.", ["Cash Flow Forecaster", "Inventory Tracker", "Budget Tracker", "Project Management"]),
      ("Google Sheets Templates", "google-sheets-templates", "The same core templates, built natively for Google Sheets.", ["Cash Flow Forecaster", "Inventory Tracker", "Budget Tracker", "Project Management"]),
  ]),
  "notion-dashboards": ("Notion Dashboards & Templates", "Drop-in Notion systems for running client work and admin in one place.", [
      ("Client Portals", "client-portals", "A branded space to share progress, files and updates with each client.", []),
      ("Project Trackers", "project-trackers", "Keep every project, task and deadline visible in one board.", []),
      ("Invoice Systems", "invoice-systems", "Track invoices sent, paid and overdue without leaving Notion.", []),
      ("CRM Templates", "crm-templates", "A lightweight CRM to track leads and follow-ups inside Notion.", []),
  ]),
  "canva-template-packs": ("Canva Template Packs", "On-brand design templates, ready to customise in Canva.", [
      ("Social Media Templates", "social-media-templates", "A set of on-brand post and story templates for your social channels.", []),
      ("Invoice Designs", "invoice-designs", "Professional invoice layouts you can customise with your own branding.", []),
      ("Proposal Decks", "proposal-decks", "A polished proposal template to send to prospective clients.", []),
  ]),
  "ai-prompt-packs": ("AI Prompt Packs", "Tested prompts for common tasks, grouped by role.", [
      ("For UK Accountants", "for-uk-accountants", "Prompts for client correspondence, report summaries and common bookkeeping queries.", []),
      ("For Customer Service", "for-customer-service", "Prompts for replying to reviews, complaints and common support questions.", []),
      ("For Content Creators", "for-content-creators", "Prompts for repurposing long-form content into social posts and newsletters.", []),
      ("For Small Business Owners", "for-small-business-owners", "General-purpose prompts for admin, marketing and planning tasks.", []),
  ]),
  "ai-agent-templates": ("AI Agent Templates", "Configurable agent templates you can adapt to your own tools.", [
      ("Email Triage Agent", "email-triage-agent", "A configurable template for sorting and routing inbound email.", []),
      ("Invoice Processing Agent", "invoice-processing-agent", "A configurable template for extracting and filing invoice data.", []),
      ("Lead Qualification Agent", "lead-qualification-agent", "A configurable template for scoring inbound leads.", []),
  ]),
  "ai-workflow-blueprints": ("AI Workflow Blueprints", "Ready-to-import automation workflows for the platform you already use.", [
      ("n8n Workflows", "n8n-workflows", "Importable n8n workflow files for common automation tasks.", []),
      ("Make Scenarios", "make-scenarios", "Ready-to-import Make (formerly Integromat) scenarios.", []),
      ("Zapier Templates", "zapier-templates", "Pre-built Zaps you can connect to your own accounts in minutes.", []),
  ]),
  "document-packages": ("Document Packages", "Templated business documents, ready to adapt to your own branding.", [
      ("Invoice Templates", "invoice-templates", "A set of clean, professional invoice templates.", []),
      ("Proposal Templates", "proposal-templates", "Proposal templates structured to help you win more of the work you quote for.", []),
      ("Contract Templates", "contract-templates", "Standard contract templates for common small business arrangements.", []),
      ("UK Compliance Checklists", "uk-compliance-checklists", "Checklists covering common UK small business compliance requirements.", []),
  ]),
  "bundles": ("Bundles", "Templates, grouped and discounted.", [
      ("Basic", "basic", "A single template of your choice.", []),
      ("Pro", "pro", "A template, plus a written guide and a walkthrough video.", []),
      ("Full", "full", "Multiple templates bundled together at a discount.", []),
  ]),
}

# ---------------------------------------------------------------------------
# PACKAGES data (flat list, cards style)
# ---------------------------------------------------------------------------
PACKAGES = [
    ("Invoice Rescue Package", "invoice-rescue-package", None, "Overdue invoices chased automatically, so late payments stop quietly piling up. Ideal if you're sitting on unpaid invoices right now."),
    ("Lead Leak Fix Package", "lead-leak-fix-package", None, "Plug the gaps where enquiries go cold. Capture, CRM and follow-up wired together in one fixed-scope project."),
    ("AI Document Processing Setup", "ai-document-processing-setup", None, "Invoices and receipts extracted and filed automatically, matched straight to your accounting software."),
    ("Email Triage Setup", "email-triage-setup", None, "Your inbox sorted automatically by priority and type, working correctly from day one."),
    ("AI Receptionist Setup", "ai-receptionist-setup", None, "Never miss another call. An AI receptionist answers, logs and routes calls whenever you can't."),
    ("AI Audit Session", "ai-audit-session", None, "A focused session mapping your best automation opportunities, with a written action plan to follow."),
    ("Admin Time Audit", "admin-time-audit", "FREE", "A free, no-obligation review of where your team's admin hours are really going, with three suggested quick wins."),
    ("Monthly Automation Retainer", "monthly-automation-retainer", None, "Ongoing automation support, maintenance and new builds, billed simply each month."),
    ("Bookkeeping Starter Package", "bookkeeping-starter-package", None, "Get your books automated and up to date, with monthly reconciliation included."),
    ("Content Retainer", "content-retainer", None, "A steady stream of on-brand content, written and scheduled for you every month."),
]

# ===========================================================================
# BUILD: services
# ===========================================================================
service_hub_items = []
for cat_slug, (cat_title, cat_intro, items) in SERVICES.items():
    cat_crumbs = [{"name": "Services", "url": "/services/"}]
    idx_items = []
    for (name, slug, badge, price, summary) in items:
        star = slug in STAR_BODIES
        fm = {
            "layout": "item",
            "title": name,
            "description": summary.replace("&mdash;", "-").replace("&rarr;", "to").replace("&amp;", "and"),
            "badge": badge,
            "price": price,
            "summary": summary,
            "crumbs": cat_crumbs + [{"name": cat_title, "url": f"/services/{cat_slug}/"}],
            "star": star,
        }
        body = STAR_BODIES.get(slug, "")
        if not body:
            body = TUTORING_BODY if cat_slug == "tutoring-uk" else REASSURANCE
        if cat_slug == "tutoring-uk":
            fm["price_note"] = TUTORING_PRICE_NOTE
        write(f"services/{cat_slug}/{slug}.html", fm, body)
        idx_items.append({"name": name, "url": f"{slug}.html", "badge": badge, "price": price, "summary": summary, "cta": "View"})

    write(f"services/{cat_slug}/index.html", {
        "layout": "category",
        "title": cat_title,
        "description": cat_intro.replace("&mdash;", "-"),
        "intro": cat_intro,
        "crumbs": cat_crumbs,
        "items": idx_items,
        "layout_style": "table",
        "footnote": TUTORING_FOOTNOTE if cat_slug == "tutoring-uk" else SERVICE_FOOTNOTE,
    })
    service_hub_items.append({"name": cat_title, "url": f"{cat_slug}/", "summary": cat_intro.split(".")[0] + ".", "cta": "View services"})

write("services/index.html", {
    "layout": "category",
    "title": "Services",
    "description": "Full catalogue of business automation and AI services across finance, admin, sales, marketing, support, HR, e-commerce, consulting and tutoring.",
    "intro": ("Everything we offer, organised by department. Prices marked <strong>POA</strong> (Price on "
              "Application) are quoted after a short, free discovery call &mdash; every business's tools and "
              "workflow are a little different. <span class=\"badge badge-ai\">AI</span> marks services powered "
              "by AI; <span class=\"badge badge-std\">STD</span> marks standard rules-based automation. Prefer a "
              "fixed-scope option instead? See <a href=\"../packages/\">Packages</a>."),
    "items": service_hub_items,
    "layout_style": "cards",
    "show_price": False,
    "notice": "Onboarding slots for Q4 automation projects are now open &nbsp;|&nbsp; All quoted prices exclude VAT",
}, "")

# ===========================================================================
# BUILD: products
# ===========================================================================
product_hub_items = []
for cat_slug, (cat_title, cat_intro, items) in PRODUCTS.items():
    cat_crumbs = [{"name": "Shop", "url": "/products/"}]
    idx_items = []
    for (name, slug, summary, sublist) in items:
        fm = {
            "layout": "item",
            "title": name,
            "description": summary,
            "summary": summary,
            "status": "coming-soon",
            "crumbs": cat_crumbs + [{"name": cat_title, "url": f"/products/{cat_slug}/"}],
        }
        body = ""
        if sublist:
            body = "<h3>What's inside</h3>\n<ul>\n" + "\n".join(f"<li>{s}</li>" for s in sublist) + "\n</ul>\n"
        write(f"products/{cat_slug}/{slug}.html", fm, body)
        idx_items.append({"name": name, "url": f"{slug}.html", "summary": summary, "status": "coming-soon", "cta": "View"})

    write(f"products/{cat_slug}/index.html", {
        "layout": "category",
        "title": cat_title,
        "description": cat_intro,
        "intro": cat_intro,
        "crumbs": cat_crumbs,
        "items": idx_items,
        "layout_style": "table",
        "footnote": PRODUCT_FOOTNOTE,
    })
    product_hub_items.append({"name": cat_title, "url": f"{cat_slug}/", "summary": cat_intro, "status": "coming-soon", "cta": "Browse"})

write("products/index.html", {
    "layout": "category",
    "title": "Shop",
    "description": "Ready-made spreadsheet templates, Notion dashboards, AI prompt packs and automation blueprints for small businesses.",
    "intro": ("Ready-made spreadsheets, dashboards, prompt packs and automation blueprints you can put to work "
              "without a bespoke build. The storefront is being wired up &mdash; every pack is <strong>coming "
              "soon</strong>. Tell us which ones you want and we'll email you the moment they're live."),
    "items": product_hub_items,
    "layout_style": "cards",
    "notice": "The template shop is launching soon &nbsp;|&nbsp; Join the notify list to get first access",
}, "")

# ===========================================================================
# BUILD: packages
# ===========================================================================
pkg_hub_items = []
for (name, slug, badge, summary) in PACKAGES:
    fm = {
        "layout": "item",
        "title": name,
        "description": summary,
        "badge": badge,
        "price": "FREE" if badge == "FREE" else None,
        "summary": summary,
        "crumbs": [{"name": "Packages", "url": "/packages/"}],
    }
    write(f"packages/{slug}.html", fm, REASSURANCE if badge != "FREE" else "")
    pkg_hub_items.append({"name": name, "url": f"{slug}.html", "badge": badge, "summary": summary,
                           "price": "FREE" if badge == "FREE" else None, "cta": "Learn more"})

write("packages/index.html", {
    "layout": "category",
    "title": "Packages",
    "description": "Fixed-scope automation packages including Invoice Rescue, AI Receptionist Setup and the free Admin Time Audit.",
    "intro": ("Fixed-scope packages with a clear deliverable and timeline &mdash; no lengthy scoping call "
              "required to get started. If your need doesn't fit neatly into one of these, browse the full "
              "<a href=\"../services/\">Service Catalogue</a> instead and we'll scope something custom."),
    "items": pkg_hub_items,
    "layout_style": "cards",
    "notice": "Free Admin Time Audit &mdash; no obligation &nbsp;|&nbsp; All quoted prices exclude VAT",
}, "")

print("Generated:")
print(" services:", sum(len(v[2]) for v in SERVICES.values()) + len(SERVICES) + 1, "pages")
print(" products:", sum(len(v[2]) for v in PRODUCTS.values()) + len(PRODUCTS) + 1, "pages")
print(" packages:", len(PACKAGES) + 1, "pages")
