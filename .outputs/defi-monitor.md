No DeFi positions are configured — `memory/on-chain-watches.yml` doesn't exist. Logged `DEFI_MONITOR_OK` to today's log and exited cleanly.

## Summary

- **Checked:** `memory/on-chain-watches.yml` — file not found, no positions to monitor.
- **Action:** Logged `DEFI_MONITOR_OK` to `memory/logs/2026-08-11.md`.
- **Follow-up:** Create `memory/on-chain-watches.yml` with wallet/pool/position entries to activate monitoring.
