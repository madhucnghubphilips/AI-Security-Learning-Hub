const { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } = require("fs");
const { spawnSync } = require("child_process");
const path = require("path");

const rootDir = path.resolve(__dirname, "..");
const deckDir = path.join(rootDir, "decks", "owasp-top10-llm");
const sourceMarkdown = path.join(deckDir, "slides.md");
const siteDeckDir = path.join(rootDir, "site", "owasp-top10-llm");
const tempMarkdown = path.join(siteDeckDir, "slides.build.md");
const outputHtml = path.join(siteDeckDir, "index.html");

function marpBinary() {
  const binary = process.platform === "win32" ? "marp.cmd" : "marp";
  return path.join(rootDir, "node_modules", ".bin", binary);
}

function runMarp() {
  const binary = marpBinary();

  if (!existsSync(binary)) {
    throw new Error("Marp CLI is not installed. Run `npm install` first.");
  }

  const result = spawnSync(
    binary,
    [tempMarkdown, "--html", "--allow-local-files", "--output", outputHtml],
    { cwd: rootDir, stdio: "inherit", shell: process.platform === "win32" }
  );

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    throw new Error(`Marp failed with exit code ${result.status ?? "unknown"}.`);
  }
}

function buildDeck() {
  if (!existsSync(sourceMarkdown)) {
    throw new Error(`Missing slide source: ${sourceMarkdown}`);
  }

  mkdirSync(siteDeckDir, { recursive: true });
  rmSync(tempMarkdown, { force: true });

  const markdown = readFileSync(sourceMarkdown, "utf8")
    .replaceAll("../../Resources/", "../Resources/");

  writeFileSync(tempMarkdown, markdown);
  runMarp();
  rmSync(tempMarkdown, { force: true });

  return outputHtml;
}

if (require.main === module) {
  try {
    const output = buildDeck();
    console.log(`Built deck: ${path.relative(rootDir, output)}`);
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

module.exports = { buildDeck };
