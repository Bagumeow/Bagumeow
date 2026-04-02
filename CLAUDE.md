# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a GitHub profile repository (Bagumeow/Bagumeow) that serves as the special profile README for the GitHub user @Bagumeow. It also contains a personal CV and a custom MCP server for commit message generation.

## Structure

- `README.MD` — GitHub profile page (rendered on github.com/Bagumeow)
- `CV/` — Resume PDFs
- `mcp/` — MCP (Model Context Protocol) server for generating commit messages from git diffs
- `profile_webpage/` — Static HTML/CSS/JS personal profile page
- `.github/workflows/generate.yml` — Daily cron + push-triggered workflow that generates contribution snake SVGs using `Platane/snk` for both personal (@Bagumeow) and work (@NghiaLe-LF) accounts, pushed to the `generate-contribution-snake` branch

## MCP Server

Located at `mcp/mcp_server.py`. Uses `FastMCP` from `mcp[cli]` package.

Setup:
```bash
cd mcp
python -m venv .mcp
source .mcp/bin/activate
pip install "mcp[cli]"
```

The server exposes a `get_change_code_profile` tool that returns `git diff HEAD` output. Requires commit key "Bagumeow" to authenticate.

## Git Remote

Uses SSH with a custom host alias: `git@github.com-bagumeow:Bagumeow/Bagumeow.git`. This requires an SSH config entry mapping `github.com-bagumeow` to `github.com` with the correct identity file (multi-account SSH setup).

## CI/CD

The `generate.yml` workflow runs daily at midnight UTC and on pushes to `master`. It uses the `WORK_GITHUB_USERNAME` secret for the work account snake generation.
