#!/usr/bin/env node
const { execSync } = require('child_process');
const https = require('https');

const CUTOFF = "2026-07-06";
const ALLOWED_ECOSYSTEMS = new Set(["npm", "pip", "go", "crates.io", "github actions", "rubygems", "maven", "nuget"]);
const SEEN = new Set([
  "GHSA-vjc7-jrh9-9j86", "CVE-2026-54769", "GHSA-q9p7-wqxg-mrhc", "CVE-2026-55500",
  "GHSA-qvfm-67h2-2qfx", "CVE-2026-49445", "GHSA-3fcv-jvfp-m4q9", "CVE-2026-53486",
  "GHSA-mp2f-45pm-3cg9", "CVE-2026-55786", "GHSA-h9f9-h6gm-wc85", "GHSA-9rjw-3gwp-f59v",
  "CVE-2026-54496", "GHSA-ww9q-8r59-xv46", "CVE-2026-54771", "GHSA-gjgq-w2m6-wr5q",
  "CVE-2026-55615", "GHSA-2pq5-3q89-j7cc"
]);

function fetchAdvisories(severity) {
  try {
    const out = execSync(
      `gh api "/advisories?type=reviewed&severity=${severity}&per_page=100" -H "Accept: application/vnd.github+json"`,
      { maxBuffer: 10 * 1024 * 1024 }
    );
    return JSON.parse(out.toString());
  } catch (e) {
    process.stderr.write(`Error fetching ${severity}: ${e.message}\n`);
    return [];
  }
}

function isRecent(publishedAt) {
  if (!publishedAt) return false;
  return publishedAt.substring(0, 10) >= CUTOFF;
}

function hasAllowedEcosystem(adv) {
  const vulns = adv.vulnerabilities || [];
  return vulns.some(v => {
    const eco = ((v.package || {}).ecosystem || "").toLowerCase();
    return ALLOWED_ECOSYSTEMS.has(eco);
  });
}

function isSeen(adv) {
  return SEEN.has(adv.ghsa_id) || SEEN.has(adv.cve_id);
}

function extract(adv) {
  const vulns = adv.vulnerabilities || [];
  const ecosystems = [...new Set(vulns.map(v => ((v.package || {}).ecosystem || "").toLowerCase()).filter(Boolean))];
  const packageNames = [...new Set(vulns.map(v => ((v.package || {}).name || "")).filter(Boolean))];
  const patchedVersions = vulns.map(v => v.patched_versions).filter(Boolean);
  const cvss = adv.cvss || {};
  return {
    ghsa_id: adv.ghsa_id || null,
    cve_id: adv.cve_id || null,
    severity: adv.severity || null,
    cvss_score: cvss.score != null ? cvss.score : null,
    summary: adv.summary || null,
    ecosystems,
    package_names: packageNames,
    patched_versions: patchedVersions,
    html_url: adv.html_url || null,
    published_at: adv.published_at || null,
    epss_score: null
  };
}

async function fetchEpss(cveIds) {
  return new Promise((resolve) => {
    if (!cveIds.length) return resolve(null);
    const param = cveIds.join(',');
    const url = `https://api.first.org/data/v1/epss?cve=${encodeURIComponent(param)}`;

    // Try curl first
    try {
      const out = execSync(`curl -sf --max-time 20 "${url}"`, { maxBuffer: 2 * 1024 * 1024 });
      const data = JSON.parse(out.toString());
      return resolve(data);
    } catch (e) {
      process.stderr.write(`curl failed for EPSS, trying https module: ${e.message}\n`);
    }

    // Fallback: node https
    https.get(url, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(body)); } catch { resolve(null); }
      });
    }).on('error', (err) => {
      process.stderr.write(`https fallback failed: ${err.message}\n`);
      resolve(null);
    });
  });
}

(async () => {
  const critical = fetchAdvisories('critical');
  const high = fetchAdvisories('high');
  const all = [...critical, ...high];

  const seenGhsa = new Set();
  const filtered = [];
  for (const adv of all) {
    const ghsa = adv.ghsa_id || '';
    if (seenGhsa.has(ghsa)) continue;
    seenGhsa.add(ghsa);
    if (!isRecent(adv.published_at)) continue;
    if (!hasAllowedEcosystem(adv)) continue;
    if (isSeen(adv)) continue;
    filtered.push(extract(adv));
  }

  const cveIds = filtered.map(a => a.cve_id).filter(Boolean);
  const epssRaw = await fetchEpss(cveIds);

  if (epssRaw && Array.isArray(epssRaw.data)) {
    const epssMap = {};
    for (const item of epssRaw.data) {
      epssMap[(item.cve || '').toUpperCase()] = parseFloat(item.epss);
    }
    for (const adv of filtered) {
      if (adv.cve_id && epssMap[adv.cve_id.toUpperCase()] != null) {
        adv.epss_score = epssMap[adv.cve_id.toUpperCase()];
      }
    }
  }

  console.log(JSON.stringify({ advisories: filtered, epss_raw: epssRaw }, null, 2));
})();
