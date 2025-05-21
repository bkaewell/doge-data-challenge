#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv


def load_paths() -> tuple[dict[str, Path], dict[str, str]]:
    """
    Load project paths and configuration from .env, creating directories if needed

    Returns:
        Tuple of two dictionaries:
        - paths: Dictionary of project directory paths (Path objects)
        - config: Dictionary of non-path configuration values (strings)
    """
    # Resolve project root (helpers/ -> doge_data_challenge/ -> root)
    root = Path(__file__).resolve().parents[2]
    env_path = root / ".env"

    if not env_path.exists():
        raise FileNotFoundError(
            f".env file not found at {env_path}. Restore it from the repository."
        )

    load_dotenv(dotenv_path=env_path)
    today = datetime.today().strftime("%Y-%m-%d")
    snapshot_date = os.getenv("SNAPSHOT_DATE", today)
    agency_metadata_dir = os.getenv("AGENCY_METADATA_DIR", "agency_metadata")
    regulation_text_dir = os.getenv("REGULATION_TEXT_DIR", "regulation_text")
    wordcount_method = os.getenv("WORDCOUNT_METHOD", "regex")

    # Define paths and create directories
    paths = {
        "ROOT": root,
        "AGENCY_METADATA_PATH": root / agency_metadata_dir / snapshot_date,
        "REGULATION_TEXT_PATH": root / regulation_text_dir / snapshot_date,
    }

    # Create directories
    paths["AGENCY_METADATA_PATH"].mkdir(parents=True, exist_ok=True)
    paths["REGULATION_TEXT_PATH"].mkdir(parents=True, exist_ok=True)

    # Define non-path configuration
    config = {
        "SNAPSHOT_DATE": snapshot_date,
        "WORDCOUNT_METHOD": wordcount_method,
    }

    return paths, config
