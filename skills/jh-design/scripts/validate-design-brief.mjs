import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const target = resolve(process.argv[2] ?? "DESIGN_BRIEF.md");
let source;

try {
  source = readFileSync(target, "utf8");
} catch {
  console.error(`[jh-design] DESIGN_BRIEF not found: ${target}`);
  process.exit(1);
}

const requiredSections = [
  "Product job",
  "Direction",
  "Brand reading",
  "Reference evidence",
  "Reference synthesis",
  "Reference implementation map",
  "Signature composition and component",
  "Motion storyboard",
  "Tokens",
  "Behavior that must remain unchanged",
  "Anti-template decisions",
  "Responsive and motion contract",
  "Verification captures",
];

const missing = requiredSections.filter((section) => !new RegExp(`^## ${section}\\s*$`, "mi").test(source));
const checks = [
  ["implementation map table", /Reference evidence\s*\|\s*Extracted principle\s*\|\s*Local component/i],
  ["motion storyboard table", /Beat\s*\|\s*Trigger\s*\|\s*Elements\s*\|\s*From/i],
  ["reduced-motion decision", /reduced[- ]motion|prefers-reduced-motion/i],
  ["mobile viewport evidence", /320|360|390|430/],
  ["signature component decision", /signature|시그니처/i],
];
const failedChecks = checks.filter(([, pattern]) => !pattern.test(source)).map(([label]) => label);

function hasCompletedTable(sectionName, minimumCells) {
  const section = source.match(new RegExp(`^## ${sectionName}\\s*$([\\s\\S]*?)(?=^## |(?![\\s\\S]))`, "mi"))?.[1] ?? "";
  const dataRows = section
    .split(/\r?\n/)
    .filter((line) => /^\|/.test(line))
    .filter((line) => !/^\|[-: |]+\|?$/.test(line))
    .slice(1)
    .map((line) => line.split("|").slice(1, -1).map((cell) => cell.trim()))
    .filter((cells) => cells.length >= minimumCells && cells.every((cell) => cell && !/^\[.*\]$/.test(cell)));
  return dataRows.length > 0;
}

if (!hasCompletedTable("Reference implementation map", 6)) failedChecks.push("completed implementation-map row");
if (!hasCompletedTable("Motion storyboard", 7)) failedChecks.push("completed motion-storyboard row");

if (missing.length || failedChecks.length) {
  if (missing.length) console.error(`[jh-design] Missing sections: ${missing.join(", ")}`);
  if (failedChecks.length) console.error(`[jh-design] Missing evidence: ${failedChecks.join(", ")}`);
  process.exit(1);
}

console.log(`[jh-design] Design brief contract passed: ${target}`);
