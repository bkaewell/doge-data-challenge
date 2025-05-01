#!/usr/bin/env python3

import os
from pathlib import Path
from dotenv import load_dotenv


def load_paths() -> dict[str, Path | str]:
    """
    Load project paths from .env configuration, creating directories if needed.

    Returns:
        Dictionary with project paths and configuration values.
    """
    # Resolve project root (helpers/ -> doge_data_challenge/ -> root)
    root = Path(__file__).resolve().parents[2]
    env_path = root / ".env"

    if not env_path.exists():
        raise FileNotFoundError(
            f".env file not found at {env_path}. Run bootstrap.py to create it."
        )

    load_dotenv(dotenv_path=env_path)
    snapshot_date = os.getenv("SNAPSHOT_DATE")
    archive_dir = os.getenv("ARCHIVE_DIR", "archive")
    data_dir = os.getenv("DATA_DIR", "data")
    wordcount_method = os.getenv("WORDCOUNT_METHOD", "regex")

    # Validate SNAPSHOT_DATE (basic check, since bootstrap.py validates format)
    if not snapshot_date:
        raise ValueError("SNAPSHOT_DATE must be set in .env")

    paths = {
        "ROOT": root,
        "SNAPSHOT_DATE": snapshot_date,
        "ARCHIVE_PATH": root / archive_dir,
        "DATA_PATH": root / data_dir,
        "XML_SNAPSHOT_PATH": root / data_dir / "regulations_xml" / snapshot_date,
        "WORDCOUNT_METHOD": wordcount_method,
    }

    # Create directories
    for path_name, path in paths.items():
        if isinstance(path, Path) and "PATH" in path_name:
            path.mkdir(parents=True, exist_ok=True)

    return paths




# import os

# from pathlib import Path
# from dotenv import load_dotenv


# """
# Utility for loading project paths and .env config cleanly across notebooks

# This helps keep notebooks simple and lets users configure behavior through the .env file
# """
# def load_paths():
#     # helpers/ dir is at project root
#     ROOT = Path(__file__).resolve().parents[1]  # go up one directory to the project root
#     env_path = ROOT / ".env"

#     if not env_path.exists():
#         raise FileNotFoundError(f".env file not found at expected location: {env_path}")

#     load_dotenv(dotenv_path=env_path)
#     snapshot_date = os.getenv("SNAPSHOT_DATE")
#     archive_dir = os.getenv("ARCHIVE_DIR", "archive")
#     data_dir = os.getenv("DATA_DIR", "data")
    
#     return {
#         "ROOT": ROOT,
#         "SNAPSHOT_DATE": snapshot_date,
#         "ARCHIVE_PATH": ROOT / archive_dir,
#         "DATA_PATH": ROOT / data_dir,
#         "XML_SNAPSHOT_PATH": ROOT / data_dir / "regulations_xml" / snapshot_date,
#     }
