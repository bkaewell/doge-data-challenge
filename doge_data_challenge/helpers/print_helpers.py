from pathlib import Path

"""
Helper functions for clean, consistent printing of directory and path statuses.
"""
def shorten_path(path: Path) -> str:
    """
    Converts an absolute home path to ~ for cleaner and safer display
    """
    try:
        home = str(Path.home())
        return str(path).replace(home, "~")
    except Exception:
        return str(path)

def print_dir_status(label: str, path: Path):
    """
    Prints a status message for a directory with an emoji indicating existence
    """
    emoji = "✅" if path.exists() else "❌"
    # Aligns label and prints directory path with emoji status
    # Example output:
    # Agency Metadata Directory: 
    # Regulation Text Directory: 
    char_width = 26
    print(f"{label:<{char_width}} {shorten_path(path)} {emoji}")
