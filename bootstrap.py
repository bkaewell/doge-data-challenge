#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Import print helper
from notebooks.utils.print_helpers import shorten_path, print_dir_status


# Define project root and .env location
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"

def ensure_env_exists():
    """
    If .env is missing, create it with default values.
    """
    if not ENV_PATH.exists():
        today = datetime.today().strftime("%Y-%m-%d")
        default_env = f"""# Auto-generated .env
SNAPSHOT_DATE={today}
DATA_DIR=data
ARCHIVE_DIR=archive
"""
        ENV_PATH.write_text(default_env)
        print(f"🆕 Created .env file with default values:\n{default_env}")

def get_env_config():
    """
    Load .env config (creates it if missing) and return key paths.
    """
    ensure_env_exists()
    load_dotenv(dotenv_path=ENV_PATH)

    snapshot_date = os.getenv("SNAPSHOT_DATE", datetime.today().strftime("%Y-%m-%d"))
    data_dir = os.getenv("DATA_DIR", "data")
    archive_dir = os.getenv("ARCHIVE_DIR", "archive")

    # Validate date from .env (unless overridden later)
    try:
        datetime.strptime(snapshot_date, "%Y-%m-%d")
    except ValueError:
        print(f"❌ SNAPSHOT_DATE in .env is invalid: '{snapshot_date}'")
        print("Must be YYYY-MM-DD and a real date")
        sys.exit(1)

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
    parser = argparse.ArgumentParser(description="Bootstrap DOGE data directories and config.")
    parser.add_argument(
        "--date", type=str, help="Override SNAPSHOT_DATE (format: YYYY-MM-DD)", default=None
    )
    args = parser.parse_args()

    snapshot_date, data_dir, archive_dir = get_env_config()

    # Override date if --date was provided
    if args.date:
        try:
            # Validate format
            datetime.strptime(args.date, "%Y-%m-%d")
            snapshot_date = args.date
            print(f"\n📆 Overriding SNAPSHOT_DATE with --date {snapshot_date}")
        except ValueError:
            print(f"❌ Invalid --date '{args.date}'")
            print("Must be in YYYY-MM-DD format and a real date")
            sys.exit(1)

    bootstrap(snapshot_date, data_dir, archive_dir)
