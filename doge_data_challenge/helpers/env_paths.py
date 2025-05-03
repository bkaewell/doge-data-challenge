#!/usr/bin/env python3

import os
from pathlib import Path
from dotenv import load_dotenv


def load_paths() -> dict[str, Path | str]:
    """
    Load project paths from .env configuration, creating directories if needed

    Returns:
        Dictionary with project paths and configuration values
    """
    # Resolve project root (helpers/ -> doge_data_challenge/ -> root)
    root = Path(__file__).resolve().parents[2]
    env_path = root / ".env"

    if not env_path.exists():
        raise FileNotFoundError(
#           f".env file not found at {env_path}. Run bootstrap.py to create it."
            f".env file not found at {env_path}"
        )

    load_dotenv(dotenv_path=env_path)
    snapshot_date = os.getenv("SNAPSHOT_DATE")
    agency_metadata_dir = os.getenv("AGENCY_METADATA_DIR", "agency_metadata")
    regulation_text_dir = os.getenv("REGULATION_TEXT_DIR", "regulation_text")
    wordcount_method = os.getenv("WORDCOUNT_METHOD", "regex")

    # Validate SNAPSHOT_DATE (basic check, since bootstrap.py validates format)
    if not snapshot_date:
        raise ValueError("SNAPSHOT_DATE must be set in .env")

    paths = {
        "ROOT": root,
        "SNAPSHOT_DATE": snapshot_date,
        "AGENCY_METADATA_PATH": root / agency_metadata_dir / snapshot_date,
        "REGULATION_TEXT_PATH": root / regulation_text_dir / snapshot_date,
 #       "XML_SNAPSHOT_PATH": root / data_dir / "regulations_xml" / snapshot_date,
        "WORDCOUNT_METHOD": wordcount_method,
    }

    # Create directories
    for path_name, path in paths.items():
        if isinstance(path, Path) and "PATH" in path_name:
            path.mkdir(parents=True, exist_ok=True)

    return paths