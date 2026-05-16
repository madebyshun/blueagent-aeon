*Aeon Onboarding — 2026-05-16*
Setup incomplete — 2 required item(s) need attention before Aeon can run.

✅ Passing (6)
• workflow .github/workflows/aeon.yml — present
• workflow .github/workflows/messages.yml — present
• workflow .github/workflows/chain-runner.yml — present
• aeon.yml — 7 skill(s) enabled
• memory/ — writable, MEMORY.md present
• skill activity log — 1 daily log file(s) under memory/logs/

⚠ Warnings (2)
• GitHub Actions — no runs yet for messages.yml
    fix: Enable Actions: gh workflow enable messages.yml -R madebyshun/blueagent-aeon  (or visit Settings → Actions → General and allow workflows).
• GH_GLOBAL (cross-repo PAT) — not configured (optional)
    fix: Only needed if you want skills like github-monitor / pr-review / external-feature to read repos outside this one. Create a fine-grained PAT and: gh secret set GH_GLOBAL -R madebyshun/blueagent-aeon

❌ Failing (2)
• auth secret — neither ANTHROPIC_API_KEY nor CLAUDE_CODE_OAUTH_TOKEN configured
    fix: gh secret set ANTHROPIC_API_KEY --body 'sk-ant-...' -R madebyshun/blueagent-aeon  (or run 'claude setup-token' and set CLAUDE_CODE_OAUTH_TOKEN)
• notification channel — no channel configured
    fix: Pick one — Telegram is fastest. See README → Notifications for the @BotFather + chat_id walk-through, then: gh secret set TELEGRAM_BOT_TOKEN -R madebyshun/blueagent-aeon && gh secret set TELEGRAM_CHAT_ID -R madebyshun/blueagent-aeon

Note: auth/channel checks show FAIL because gh secret list returns HTTP 403 in GitHub Actions (the default GITHUB_TOKEN cannot read secrets via API). If ANTHROPIC_API_KEY and notification secrets are set in repo Settings → Secrets, Aeon will run correctly — rerun ./onboard locally with `gh auth login` to confirm.

Next: Fix the ❌ items above, then rerun ./onboard --remote.
