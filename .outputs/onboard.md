*Aeon Onboarding — 2026-05-16*
Aeon will run, but 3 optional piece(s) need attention.

✅ Passing (7)
• workflow .github/workflows/aeon.yml — present
• workflow .github/workflows/messages.yml — present
• workflow .github/workflows/chain-runner.yml — present
• aeon.yml — 7 skill(s) enabled
• memory/ — writable, MEMORY.md present
• notification channel — Telegram configured (TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID set)
• skill activity log — 2 daily log file(s) under memory/logs/

⚠ Warnings (3)
• auth secret — ANTHROPIC_API_KEY/CLAUDE_CODE_OAUTH_TOKEN not set; agent authenticated via BANKR_LLM_KEY (Bankr LLM Gateway). gh secret list returns 403 in Actions so direct verification is unavailable.
    fix: No action needed if using Bankr LLM Gateway. To switch to direct Anthropic: gh secret set ANTHROPIC_API_KEY --body 'sk-ant-...' -R madebyshun/blueagent-aeon
• GitHub Actions — no runs yet for messages.yml
    fix: Enable Actions: gh workflow enable messages.yml -R madebyshun/blueagent-aeon  (or visit Settings → Actions → General and allow workflows).
• GH_GLOBAL (cross-repo PAT) — not configured (optional)
    fix: Only needed for cross-repo skills (github-monitor, pr-review, external-feature). Create a fine-grained PAT and: gh secret set GH_GLOBAL -R madebyshun/blueagent-aeon

Next: Optional improvements — Aeon will run regardless. Rerun ./onboard once addressed.

