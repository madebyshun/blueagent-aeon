*Security Digest — 2026-07-14*
Verdict: nothing urgent today. 5 to schedule, 0 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [CVE-2026-61667](https://github.com/advisories/GHSA-m4m7-4cw8-62j6) — DIRAC (pip) · CVSS 9.9 · EPSS 0 · no public PoC
  RCE via SQL injection in FileCatalog DatasetManager fed into eval(). Authenticated, full server compromise.
  → schedule upgrade: DIRAC → ≥8.0.79 / ≥9.0.22 / ≥9.1.10

- [CVE-2026-45579](https://github.com/advisories/GHSA-9jpv-c7p4-997x) — DIRAC (pip) · CVSS 9.9 · EPSS 0 · no public PoC
  RCE via eval() on untrusted input in RequestManager. Same fix targets.
  → schedule upgrade: DIRAC → ≥8.0.79 / ≥9.0.22 / ≥9.1.10

- [GHSA-7xw9-549r-8jrc](https://github.com/advisories/GHSA-7xw9-549r-8jrc) — DIRAC (pip) · CVSS 8.5 · EPSS 0 · no CVE
  SQL injection + missing access control in PilotManager service.
  → schedule upgrade: DIRAC → ≥8.0.79 / ≥9.0.22 / ≥9.1.10

- [CVE-2026-61668](https://github.com/advisories/GHSA-vg99-gr89-qhw9) — DIRAC (pip) · CVSS 8.1 · EPSS 0 · no public PoC
  Pilot agent code fetched over unverified HTTPS; MITM can inject arbitrary code during download.
  → schedule upgrade: DIRAC → ≥8.0.79 / ≥9.0.22 / ≥9.1.10

- [GHSA-xf7x-x43h-rpqh](https://github.com/advisories/GHSA-xf7x-x43h-rpqh) — json-repair (pip) · CVSS 7.5 · EPSS 0 · public PoC
  Circular JSON Schema $ref infinite loop — unauthenticated CPU DoS. Docker + HTTP PoC published.
  → schedule upgrade: json-repair → ≥0.60.1
