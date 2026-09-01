*Security Digest — 2026-09-01*
Verdict: nothing urgent today. 2 to schedule, 3 to monitor. _Sources: KEV (5 this week, all prior-logged), GH Advisory, EPSS_

*PATCH THIS WEEK*
- [GHSA-gqvg-gmmx-x4hm](https://github.com/advisories/GHSA-gqvg-gmmx-x4hm) — mlflow (pip) · CVSS 8.8 · EPSS n/a
  statsmodels flavor ignores MLFLOW\_ALLOW\_PICKLE\_DESERIALIZATION=False → RCE via crafted model artifact even with the guard enabled.
  → upgrade mlflow to ≥3.15.0 and redeploy.

- [GHSA-3f6p-5ww8-9rcr](https://github.com/advisories/GHSA-3f6p-5ww8-9rcr) — mysql2 (npm) · CVSS 8.2 · EPSS n/a · PoC on request
  Rogue server/MITM forces auth plugin downgrade to mysql\_clear\_password → plaintext credentials captured; 9M weekly downloads.
  → upgrade mysql2 to ≥3.22.0 and redeploy.

*MONITOR*
- [GHSA-gr94-w7qr-f4j3](https://github.com/advisories/GHSA-gr94-w7qr-f4j3) — engine.io (npm) · CVSS 7.5 · EPSS 0.61%
  \_\_proto\_\_ SID crashes WebTransport upgrade handler → unauthenticated remote DoS. WebTransport is opt-in.
  → upgrade engine.io to ≥6.6.7; mitigate with transports: ["polling","websocket"].

- [GHSA-c83g-rgw3-j3cx](https://github.com/advisories/GHSA-c83g-rgw3-j3cx) + [GHSA-73wf-gq98-2v4g](https://github.com/advisories/GHSA-73wf-gq98-2v4g) — browserslist (npm) · CVSS 7.5 · EPSS 0.36%
  Two bugs: unbounded cache OOM (50 MB+ heap at 30k distinct queries) + prototype crash via poisoned browserslist-stats.json.
  → upgrade browserslist to ≥4.28.7; most build tools (Autoprefixer, Babel, Stylelint) pick it up transitively.
