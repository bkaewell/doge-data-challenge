#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
from doge_data_challenge.helpers.print_helpers import print_dir_status


def validate_snapshot_date(snapshot_date: str) -> None:
    try:
        datetime.strptime(snapshot_date, "%Y-%m-%d")
    except ValueError:
        print(f"❌ Invalid SNAPSHOT_DATE in .env: '{snapshot_date}'")
        print("Must be YYYY-MM-DD and a real date")
        exit(1)

def bootstrap():
    """Set up DOGE data workspace"""
    from doge_data_challenge.helpers.env_setup import setup_env

    paths, config = setup_env()
    print(paths)
    print(config)

    # Validate configuration
    snapshot_date = config["SNAPSHOT_DATE"]
    validate_snapshot_date(snapshot_date)

    # Print setup status
    print("\nSetting up DOGE data workspace...")
    print(f"Snapshot Date:       {snapshot_date}")
    print(f"Word Count Strategy: {config['WORDCOUNT_METHOD']}")
    print_dir_status("Agency Metadata Directory:", paths["AGENCY_METADATA_PATH"])
    print_dir_status("Regulation Text Directory:", paths["REGULATION_TEXT_PATH"])
    print("\n🎉 Bootstrap complete! You can now run the notebooks\n")
    print("Note: Modify .env to process additional SNAPSHOT_DATE values or customize directories\n")


if __name__ == "__main__":
    bootstrap()
