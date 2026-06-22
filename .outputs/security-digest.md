*Security Digest — 2026-06-22*
Verdict: nothing urgent today. 1 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-33646](https://github.com/advisories/GHSA-fjj5-v948-whjj) — mise (crates.io) · CVSS 9.6 · EPSS n/a (new CVE) · public PoC ✓
  Tera template exec() fires silently on `cd` into any repo with a malicious .tool-versions file — full RCE, no trust prompt, no warning. Supply chain attack vector; PoC validated on mise 2026.3.9.
  → upgrade mise to ≥ 2026.3.10 and redeploy CI runners.
