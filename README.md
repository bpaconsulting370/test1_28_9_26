# Business Process Automation — website

A free, multi-page website for GitHub Pages, built with Jekyll (which GitHub Pages runs for you — nothing to install).
Design: your Win95-style theme. Structure: your sitemap, page for page (127 pages) plus a 404 page.

```
index.html                     Home
services/                      Hub + 9 category folders, 55 service pages (the 4 ★ Phase 1 pages have full content)
packages/                      Hub + 10 package pages
products/                      Hub + 8 category folders, 26 product pages (all "Coming soon")
case-studies/  about/  free-audit/  contact/  resources/  legal/  thank-you/
_config.yml                    The 4 settings you'll edit
_layouts/  _includes/          Page templates — header, nav and footer are written once here
assets/                        css, js, images, documents
tools/generate_pages.py        OPTIONAL — rebuilds the services/products/packages pages (overwrites edits!)
```

## 1. Put it on GitHub Pages (free)

1. Create a GitHub repository. Name it `yourusername.github.io` for a root URL, or anything else
   (the site then lives at `yourusername.github.io/repo-name/`).
2. Upload the **contents** of this folder so that `index.html` and `_config.yml` sit at the top level of the repo
   (drag-and-drop in the web UI works, or use git).
3. Repo → **Settings → Pages → Build and deployment → Source: "Deploy from a branch"** → branch `main`, folder `/ (root)` → Save.
4. Wait a minute or two (progress shows in the **Actions** tab), then open the URL shown at the top of the Pages settings.
5. Open `_config.yml` and set `url` and `baseurl`:
   - Repo named `yourusername.github.io` → `url: "https://yourusername.github.io"`, `baseurl: ""`
   - Any other repo name → `url: "https://yourusername.github.io"`, `baseurl: "/repo-name"`
   
   (This makes `sitemap.xml`, canonical URLs and the "thank you" redirect work.)

**Do not add a `.nojekyll` file** — it switches off the templating this site relies on.
If a build fails, the error is shown in the Actions tab.

## 2. GoatCounter analytics

1. Sign up at [goatcounter.com](https://www.goatcounter.com) and choose a site code, e.g. `mybiz` (your dashboard is then `mybiz.goatcounter.com`).
2. In `_config.yml` set `goatcounter_code: "mybiz"`. That's it — the tracking script is added to every page from one place.
   Until you change it from `YOUR-CODE`, no tracking script is loaded.
3. Optional real hit counter: in GoatCounter → Settings, tick **"Allow adding visitor counts on your website"**.
   The retro counter at the bottom of the homepage stays hidden until it can load a real number (it shows homepage page views).
4. Check GoatCounter's own documentation for what it records, and describe it accurately in your Privacy Policy.

## 3. Contact and audit forms (Formspree)

GitHub Pages can't process forms itself, so the forms post to [Formspree](https://formspree.io).

1. Create a Formspree form and copy the ID from its endpoint (`https://formspree.io/f/THIS-PART`).
2. In `_config.yml` set `formspree_id: "THIS-PART"`.
3. Submit each form once to test (Formspree will ask you to confirm your email first). Check Formspree's current plan limits.

Until it's set, the forms show the visitor a "not connected yet" message instead of failing.

## 4. Before you go live — checklist

- [ ] `_config.yml`: `url`, `baseurl`, `goatcounter_code`, `formspree_id`
- [ ] `contact/index.html`: replace the Calendly link (`YOUR-HANDLE`) and email (`hello@YOURDOMAIN.co.uk`)
- [ ] **Legal pages are DRAFT templates, not legal advice.** Fill in the [BRACKETS], have them reviewed, then delete the
      banner and the `noindex` / `sitemap: false` lines at the top of each file. If you collect personal data in the UK,
      also check whether you need to pay the ICO data protection fee (ico.org.uk).
- [ ] **Case studies are illustrative scenarios**, labelled as such — replace them with real client stories (with permission) when you have them.
- [ ] `about/index.html` and the tutoring pages: add your own story, background and (for tutoring) qualifications and safeguarding details.
- [ ] Prices: only four services carry a price (from your original sample); the rest say POA. A price appears in two places — the item
      page and its category page's `items` list — so edit both (or edit `tools/generate_pages.py` and re-run it).
- [ ] Marquee notices (`notice:` in each hub page's front matter) — edit or delete.

**Wording I assumed — please check it's true for you:** "free discovery call" and "5–10 working days" (both from your original page);
"we reply within one working day"; the free audit format (20-minute call, written summary, three quick wins);
"Built for UK small businesses"; "handover documentation"; "Now booking Q4 automation projects".
I did not invent testimonials, client results or statistics; the numbers in the invoice-cost guide are labelled as made-up examples.

**Not created** (I don't have your files): `assets/images/profile.jpg` and `assets/documents/your-cv.pdf`. The folders exist; nothing links to them.

## 5. Editing the site

- Header / nav / footer → `_includes/`. Colours → the variables at the top of `assets/css/style.css`.
- Add a page: copy a similar file, change the front matter and body, and add it to its category page's `items` list.
- The four ★ pages show the pattern for fuller content (HTML below the front matter). Other pages show a short shared paragraph — replace as you write real copy.
- Both templates and pages are plain HTML; there is no Markdown.

## 6. Preview on your own computer (optional)

Install Ruby, run `bundle install` then `bundle exec jekyll serve`, and open http://localhost:4000
(add `/repo-name/` if you set a `baseurl`). The `Gemfile` is only used for this; GitHub Pages ignores it.
