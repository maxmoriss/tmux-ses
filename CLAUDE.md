# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Install

```bash
uv tool install -e .
```

After code changes, reinstall to pick them up (uv editable installs update automatically, but reinstall if the entry point changes).

## Architecture

Single-file tool. All logic lives in `tmux_ses/__init__.py` as `main()`, which is the entry point for the `tmux-ses` CLI command.

The tool:
1. Resolves the target directory (creates it if missing)
2. Derives the tmux session name from the directory basename
3. Exits early if a session with that name already exists
4. Creates a 3-window session: window 1 (shell), window 2 "AI" (`claude`), window 3 "vim" (`nvim .`)
5. Saves tmux-resurrect state (best-effort, ignored if plugin absent)
6. Attaches via `switch-client` if already inside tmux, or `os.execvp` into `attach-session` otherwise
