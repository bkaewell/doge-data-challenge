#!/usr/bin/env python3

import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from notebooks.utils.print_helpers import shorten_path, print_dir_status

# Constants
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"
DEFAULT_DATA_DIR = "data"
DEFAULT_ARCHIVE_DIR = "archive"

def ensure_env_exists():
    if not ENV_PATH.exists():
        today = datetime.today().strftime("%Y-%m-%d")
        default_env = f"""# Auto-generated .env
SNAPSHOT_DATE={today}
DATA_DIR={DEFAULT_DATA_DIR}
ARCHIVE_DIR={DEFAULT_ARCHIVE_DIR}
WORDCOUNT_METHOD=regex  # Options: split, regex, legal, nlp
"""
        ENV_PATH.write_text(default_env)
        print(f"🆕 Created .env file with default values:\n{default_env}")

def get_env_config():
    ensure_env_exists()
    load_dotenv(dotenv_path=ENV_PATH)

    snapshot_date = os.getenv("SNAPSHOT_DATE")
    data_dir = os.getenv("DATA_DIR", DEFAULT_DATA_DIR)
    archive_dir = os.getenv("ARCHIVE_DIR", DEFAULT_ARCHIVE_DIR)

    # Validate date format
    try:
        datetime.strptime(snapshot_date, "%Y-%m-%d")
    except ValueError:
        print(f"❌ Invalid SNAPSHOT_DATE in .env: '{snapshot_date}'")
        print("Must be YYYY-MM-DD and a real date")
        exit(1)

    return snapshot_date, data_dir, archive_dir

def bootstrap(snapshot_date, data_dir, archive_dir):
    xml_path = PROJECT_ROOT / data_dir / "regulations_xml" / snapshot_date
    archive_path = PROJECT_ROOT / archive_dir

    print("\nSetting up DOGE data workspace...")
    print(f"Snapshot Date:       {snapshot_date}")

    print_dir_status("XML Directory:", xml_path)
    print_dir_status("Archive Directory:", archive_path)

    print("\n🎉 Bootstrap complete! You can now run the notebooks.\n")

if __name__ == "__main__":
    snapshot_date, data_dir, archive_dir = get_env_config()
    bootstrap(snapshot_date, data_dir, archive_dir)

