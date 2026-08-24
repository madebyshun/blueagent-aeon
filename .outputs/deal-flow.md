The `.pending-notify/` staging is the correct path — the same pattern used by narrative-tracker and token-movers. The postprocess-notify.sh workflow step will pick it up after this skill run completes.

## Summary

**Skill executed:** `skills/deal-flow/SKILL.md` — 2026-08-24

**What I did:**
- Built dedup set from Aug 10 and Aug 17 deal-flow logs (14 company names excluded)
- Gathered ~27 candidates from Tier 1/2/3 sources (Crunchbase, TechCrunch, crypto-fundraising.info, cryptorank, aifundingtracker, WebSearch)
- Dropped 20 candidates via quality gates: >14 days old (Firmus Grid Aug 6, Hadrian, Fireworks AI, Baseten, Together AI, Sail Research, Grace), token sale (ZeroStack), M&A (TradeZero), unverifiable amount/lead (Prometheus, Kite, Concrete Protocol, Velaura AI, LeapXpert), conflicting data (Beldex), score <12 without Tier-3 (Relativity Networks, Alloy Robotics)
- Scored and ranked 7 deals clearing all gates

**Final digest — 7 deals:**
1. Etched $700M @ $21B (UP >2×) — Jane Street + Sequoia/a16z/Kleiner/Tiger — score 24/25
2. Databricks $5B @ $190B (UP) — Coatue + Blackstone/MGX — score 21/25
3. Form Energy $750M Series G @ $1.75B (DOWN from ~$3B) — T. Rowe Price — score 20/25
4. Fasset $68M Series C — SBI Holdings — score 16/25
5. Skan.ai $63M — Dell Technologies Capital + Bloomberg Beta — score 14/25
6. Castelion $1B Series C @ $13B — JPMorgan SIG + a16z + Carlyle — score 13/25
7. NeoSoul $11M Series A — MH Ventures — score 11/25 (Tier-3: prediction markets + oracle infra)

**Files written:**
- `.pending-notify/deal-flow-2026-08-24.md` — digest staged for fan-out (multi-line sandbox pattern)
- `memory/logs/2026-08-24.md` — appended `### deal-flow` log entry
