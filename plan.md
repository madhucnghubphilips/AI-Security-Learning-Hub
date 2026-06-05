# GitHub Pages Slide Deck Plan

## Goal

Publish this repository as a GitHub Pages presentation site similar to:

https://npalm.github.io/supply-chain-security-talks/geecon26/index.html

The site should present the current AI security learning content as a browser-based slide deck, using the existing `README.md` content and `Resources/` images.

## Recommended Approach

Use a Marp-based static slide deck.

The reference site is not a normal GitHub-rendered README page. It is a generated HTML presentation with slide navigation and hash-based slide URLs. Marp is a good fit because it converts Markdown into static HTML slides that can be hosted directly on GitHub Pages.

## Target URL Shape

After GitHub Pages is enabled, the expected public URLs should look like:

```text
https://<github-username>.github.io/OWASP-Top10-LLM---Workshop/
https://<github-username>.github.io/OWASP-Top10-LLM---Workshop/owasp-top10-llm/
```

The exact username or organization depends on where the repository is hosted.

## Planned Repository Structure

```text
README.md
Resources/
plan.md
package.json
decks/
  owasp-top10-llm/
    slides.md
    deck.yml
scripts/
  build-deck.js
  build-site.js
.github/
  workflows/
    pages.yml
site/
```

`site/` should be generated build output. It can either be ignored locally and built in GitHub Actions, or committed only if using branch/static-folder based publishing. The preferred approach is to build it in GitHub Actions.

## Implementation Plan

1. Add Node project tooling.
   - Create `package.json`.
   - Add Marp CLI as a development dependency.
   - Add scripts for local build, local preview, and full site generation.

2. Create the slide deck source.
   - Create `decks/owasp-top10-llm/slides.md`.
   - Convert the current `README.md` sections into individual slides.
   - Keep the existing learning flow:
     - What is AI
     - Deterministic vs probabilistic systems
     - Machine learning
     - Why GPUs matter
     - Jailbreak attacks
     - Hallucinations
     - RAG
     - MCP
     - How LLMs work
     - Responsible AI principles
   - Reuse the existing images from `Resources/`.

3. Add deck metadata.
   - Create `decks/owasp-top10-llm/deck.yml`.
   - Store slug, title, tags, and any future session metadata there.

4. Add build scripts.
   - `scripts/build-deck.js` should convert the Marp Markdown file into HTML.
   - `scripts/build-site.js` should create the final `site/` folder.
   - The generated site should include:
     - A root landing page.
     - A deck page at `owasp-top10-llm/index.html`.
     - Copied image assets from `Resources/`.

5. Add visual styling.
   - Use a dark conference-style slide theme.
   - Prefer full-slide images where the content benefits from it.
   - Keep text readable on desktop and projector screens.
   - Avoid turning the site into a marketing landing page; the first real experience should be the deck.

6. Add GitHub Pages deployment.
   - Create `.github/workflows/pages.yml`.
   - On push to `main`, install dependencies, build the site, upload the `site/` folder as a Pages artifact, and deploy it.
   - In GitHub repository settings, set Pages source to `GitHub Actions`.

## Local Verification

Before publishing:

```text
npm install
npm run build
npm run site
npx http-server site -c-1 -a 127.0.0.1
```

Then verify:

- The landing page loads.
- The slide deck loads.
- All images from `Resources/` render correctly.
- Slide navigation works.
- Hash URLs work, for example `index.html#10`.
- The deck is readable on desktop and mobile widths.

## GitHub Pages Verification

After pushing to GitHub:

1. Open the repository on GitHub.
2. Go to Settings -> Pages.
3. Set Source to `GitHub Actions`.
4. Confirm the Pages workflow completes successfully.
5. Open the published Pages URL.
6. Confirm the root page and slide deck page both load.

## Out of Scope for This Plan File

This file is only a future-use implementation plan.

Do not implement the slide deck, build tooling, or GitHub Actions workflow until explicitly requested.

## Assumptions

- The repository should become a static GitHub Pages site.
- The preferred presentation format is a slide deck, not a normal README page.
- Existing `README.md` content is the source material.
- Existing `Resources/` images should be reused as-is.
- Marp is the preferred tool because it matches the reference site's generated presentation model.
