import os
import subprocess
import sys
from pathlib import Path


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    if len(sys.argv) < 2:
        print("Usage: tmux-ses <directory>", file=sys.stderr)
        sys.exit(1)

    directory = Path(sys.argv[1]).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    session_name = directory.name
    directory = str(directory)

    result = subprocess.run(
        ["tmux", "has-session", "-t", session_name], capture_output=True
    )
    if result.returncode == 0:
        print(f"Session '{session_name}' already exists.", file=sys.stderr)
        sys.exit(1)

    run(["tmux", "new-session", "-d", "-s", session_name, "-c", directory])

    run(["tmux", "new-window", "-t", session_name, "-c", directory, "-n", "AI"])
    run(["tmux", "send-keys", "-t", f"{session_name}:AI", "claude", "Enter"])

    run(["tmux", "new-window", "-t", session_name, "-c", directory, "-n", "vim"])
    run(["tmux", "send-keys", "-t", f"{session_name}:vim", "nvim .", "Enter"])

    run(["tmux", "select-window", "-t", f"{session_name}:1"])

    subprocess.run(
        ["tmux", "run-shell", "~/.tmux/plugins/tmux-resurrect/scripts/save.sh"],
        capture_output=True,
    )

    if os.environ.get("TMUX"):
        run(["tmux", "switch-client", "-t", session_name])
    else:
        os.execvp("tmux", ["tmux", "attach-session", "-t", session_name])
