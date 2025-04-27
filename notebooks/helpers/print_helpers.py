from pathlib import Path

"""
Helper functions for clean, consistent printing of directory and path statuses.
"""
def shorten_path(path: Path) -> str:
    """
    Converts an absolute home path to ~ for cleaner display
    """
    try:
        home = str(Path.home())
        return str(path).replace(home, "~")
    except Exception:
        return str(path)

def print_dir_status(label: str, path: Path):
    """
    Creates the directory if needed and prints a status message with emoji.
    """
    try:
        path.mkdir(parents=True, exist_ok=True)
        emoji = "✅"
    except Exception:
        emoji = "❌"
    # Aligns label and prints directory path with emoji status
    print(f"{label:<20} {shorten_path(path)} {emoji}")

