*Security Digest — 2026-08-10*
Verdict: nothing urgent today. 0 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*MONITOR*
- [GHSA-9rj7-rf2p-w77r](https://github.com/advisories/GHSA-9rj7-rf2p-w77r) — GitPython (pip) · CVSS 7.5 · EPSS n/a · fix: ≥3.1.58
  5th in the GitPython cluster (all vuln ≤3.1.57): unguarded --template arg in Repo.init lets attacker-controlled hooks execute at process privilege. Basic PoC in advisory. Same 3.1.58 patch as the 4 advisories from Aug 9.
  → upgrade GitPython to ≥3.1.58 if not yet done.

_Note: 6 KEV additions this week (all reported Aug 3–7, deduped). 3 non-tracked critical advisories (CodeIgniter 9.8/9.4, CraftCMS unscored) filtered — composer ecosystem, not in stack._
