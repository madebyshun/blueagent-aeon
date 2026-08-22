## Summary

`memory/on-chain-watches.yml` does not exist — no DeFi positions are configured. Per the skill's instructions, the skill was skipped and `DEFI_MONITOR_OK` was logged to `memory/logs/2026-08-22.md`.

**Follow-up:** To activate this skill, create `memory/on-chain-watches.yml` with at least one `type: pool` or `type: position` entry (wallet address, RPC URL, chain). The skill will then query on-chain state and send alerts on notable changes.
