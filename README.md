# tmux-ses

CLI tool that provisions a standardized 3-window tmux session for a project directory.

## Install

```bash
uv tool install -e .
```

## Usage

```bash
tmux-ses ~/Code/my-project
```

Creates a tmux session named after the directory with:

| Window | Name | Command |
|--------|------|---------|
| 1 | — | shell |
| 2 | AI | `claude` |
| 3 | vim | `nvim .` |

Starts focused on window 2. Creates the directory if it doesn't exist. Errors if the session already exists.
