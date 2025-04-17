#!/usr/bin/env python3

import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

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

    return snapshot_date, data_dir, archive_dir

def bootstrap(snapshot_date, data_dir, archive_dir):
    xml_path = PROJECT_ROOT / data_dir / "regulations_xml" / snapshot_date
    archive_path = PROJECT_ROOT / archive_dir

    print("📦 Setting up DOGE data workspace...")
    print(f"📅 Snapshot Date:     {snapshot_date}")
    print(f"📂 XML Directory:     {xml_path}")
    print(f"📂 Archive Directory: {archive_path}")

    for path in [xml_path, archive_path]:
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Ensured directory: {path}")

    print("\n🎉 Bootstrap complete! You can now run the notebooks.")

if __name__ == "__main__":
    snapshot_date, data_dir, archive_dir = get_env_config()
    bootstrap(snapshot_date, data_dir, archive_dir)


