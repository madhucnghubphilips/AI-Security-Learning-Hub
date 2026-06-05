const { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } = require("fs");
const path = require("path");
const { buildDeck } = require("./build-deck");

const rootDir = path.resolve(__dirname, "..");
const siteDir = path.join(rootDir, "site");
const resourcesDir = path.join(rootDir, "Resources");
const siteResourcesDir = path.join(siteDir, "Resources");
const deckMetadataPath = path.join(rootDir, "decks", "owasp-top10-llm", "deck.yml");

function copyDirectory(source, destination) {
  mkdirSync(destination, { recursive: true });

  for (const entry of readdirSync(source)) {
    const sourcePath = path.join(source, entry);
    const destinationPath = path.join(destination, entry);
    const stats = statSync(sourcePath);

    if (stats.isDirectory()) {
      copyDirectory(sourcePath, destinationPath);
    } else {
      copyFileSync(sourcePath, destinationPath);
    }
  }
}

function parseDeckMetadata() {
  const metadata = {
    slug: "owasp-top10-llm",
    title: "AI Security Learning Notes",
    subtitle: "OWASP Top 10 LLM Workshop",
    description: "Browser-based slide deck for AI security learning notes."
  };

  if (!existsSync(deckMetadataPath)) {
    return metadata;
  }

  for (const line of readFileSync(deckMetadataPath, "utf8").split(/\r?\n/)) {
    const match = line.match(/^([a-zA-Z0-9_-]+):\s*(.+)$/);
    if (match) {
      metadata[match[1]] = match[2];
    }
  }

  return metadata;
}

function htmlEscape(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function writeLandingPage(metadata) {
  const title = htmlEscape(metadata.title);
  const subtitle = htmlEscape(metadata.subtitle);
  const description = htmlEscape(metadata.description);
  const deckUrl = `${metadata.slug}/`;

  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${title}</title>
  <style>
    :root {
      color-scheme: dark;
      font-family: "Aptos", "Segoe UI", Arial, sans-serif;
      background: #0b1020;
      color: #edf2ff;
      letter-spacing: 0;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: #0b1020;
      overflow-x: hidden;
    }

    main {
      min-height: 100vh;
      display: grid;
      grid-template-columns: minmax(280px, 0.9fr) minmax(320px, 1.1fr);
      align-items: center;
      gap: 3rem;
      padding: clamp(1.25rem, 4vw, 4rem);
    }

    h1 {
      margin: 0 0 0.65rem;
      font-size: clamp(2.25rem, 7vw, 5.8rem);
      line-height: 0.95;
      letter-spacing: 0;
    }

    p {
      color: #cbd5e1;
      font-size: 1.08rem;
      line-height: 1.6;
      max-width: 52rem;
      overflow-wrap: break-word;
    }

    a {
      color: #0b1020;
      background: #7dd3fc;
      border: 0;
      border-radius: 6px;
      display: inline-block;
      font-weight: 700;
      margin-top: 1.2rem;
      padding: 0.82rem 1rem;
      text-decoration: none;
    }

    iframe {
      width: 100%;
      max-width: 100%;
      aspect-ratio: 16 / 9;
      border: 1px solid rgba(148, 163, 184, 0.35);
      border-radius: 8px;
      background: #111827;
    }

    main > * {
      min-width: 0;
    }

    .eyebrow {
      color: #7dd3fc;
      font-size: 0.92rem;
      font-weight: 700;
      margin: 0 0 1rem;
      text-transform: uppercase;
    }

    @media (max-width: 860px) {
      main {
        grid-template-columns: 1fr;
        align-items: start;
        width: 100vw;
        max-width: 100vw;
      }

      iframe {
        display: none;
      }

      section {
        width: calc(100vw - 2.5rem);
        max-width: calc(100vw - 2.5rem);
      }

      h1 {
        max-width: calc(100vw - 2.5rem);
      }

      p {
        width: calc(100vw - 2.5rem);
        max-width: 100%;
      }
    }
  </style>
</head>
<body>
  <main>
    <section>
      <p class="eyebrow">${subtitle}</p>
      <h1>${title}</h1>
      <p>${description}</p>
      <a href="${deckUrl}">Open slide deck</a>
    </section>
    <iframe title="${title} slide deck" src="${deckUrl}"></iframe>
  </main>
</body>
</html>
`;

  writeFileSync(path.join(siteDir, "index.html"), html);
}

function buildSite() {
  rmSync(siteDir, { recursive: true, force: true });
  mkdirSync(siteDir, { recursive: true });
  copyDirectory(resourcesDir, siteResourcesDir);

  const metadata = parseDeckMetadata();
  buildDeck();
  writeLandingPage(metadata);
}

if (require.main === module) {
  try {
    buildSite();
    console.log("Built site/");
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

module.exports = { buildSite };
