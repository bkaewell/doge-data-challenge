#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
from doge_data_challenge.helpers.print_helpers import print_dir_status

# Constants
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"
#DEFAULT_WORDCOUNT_METHOD = "regex"
#DEFAULT_ARCHIVE_DIR = "archive"
#DEFAULT_DATA_DIR = "data"


#def ensure_env_exists():
#    """Create .env file with default values if it doesn't exist."""
#    if not ENV_PATH.exists():
#        today = datetime.today().strftime("%Y-%m-%d")
#        default_env = f"""# Auto-generated .env
#SNAPSHOT_DATE={today}
#WORDCOUNT_METHOD={DEFAULT_WORDCOUNT_METHOD}
#ARCHIVE_DIR={DEFAULT_ARCHIVE_DIR}
#DATA_DIR={DEFAULT_DATA_DIR}
#"""
#        ENV_PATH.write_text(default_env)
#        print(f"\nCreated '.env' file with default values:\n{default_env}")


def validate_snapshot_date(snapshot_date: str) -> None:
    """Validate SNAPSHOT_DATE format."""
    try:
        datetime.strptime(snapshot_date, "%Y-%m-%d")
    except ValueError:
        print(f"❌ Invalid SNAPSHOT_DATE in .env: '{snapshot_date}'")
        print("Must be YYYY-MM-DD and a real date")
        exit(1)


def bootstrap():
    """Set up DOGE data workspace."""
    from doge_data_challenge.helpers.env_paths import load_paths

    # Ensure .env exists and load paths
    ensure_env_exists()
    paths = load_paths()

    # Validate configuration
    snapshot_date = paths["SNAPSHOT_DATE"]
    validate_snapshot_date(snapshot_date)

    # Print setup status
    print("\nSetting up DOGE data workspace...")
    print(f"Snapshot Date:       {snapshot_date}")
    print(f"Word Count Strategy: {paths['WORDCOUNT_METHOD']}")
    print_dir_status("Agency Metadata Directory:", paths["AGENCY_METADATA_PATH"])
    print_dir_status("Regulation Text Directory:", paths["REGULATION_TEXT_PATH"])
    print("\n🎉 Bootstrap complete! You can now run the notebooks.\n")


if __name__ == "__main__":
    bootstrap()




# import os

# from pathlib import Path
# from datetime import datetime
# from dotenv import load_dotenv
# from helpers.print_helpers import shorten_path, print_dir_status

# # Constants
# PROJECT_ROOT = Path(__file__).resolve().parent
# ENV_PATH = PROJECT_ROOT / ".env"
# DEFAULT_WORDCOUNT_METHOD = "regex"
# DEFAULT_ARCHIVE_DIR = "archive"
# DEFAULT_DATA_DIR = "data"

# def ensure_env_exists():
#     if not ENV_PATH.exists():
#         today = datetime.today().strftime("%Y-%m-%d")
#         default_env = f"""# Auto-generated .env
# PYTHONPATH=.
# SNAPSHOT_DATE={today}
# WORDCOUNT_METHOD={DEFAULT_WORDCOUNT_METHOD}
# ARCHIVE_DIR={DEFAULT_ARCHIVE_DIR}
# DATA_DIR={DEFAULT_DATA_DIR}"""
#         ENV_PATH.write_text(default_env)
#         print(f"\nCreated '.env' file with default values:\n{default_env}")

# def get_env_config():
#     ensure_env_exists()
#     load_dotenv(dotenv_path=ENV_PATH)

#     snapshot_date = os.getenv("SNAPSHOT_DATE")
#     wordcount_method = os.getenv("WORDCOUNT_METHOD", DEFAULT_WORDCOUNT_METHOD)
#     archive_dir = os.getenv("ARCHIVE_DIR", DEFAULT_ARCHIVE_DIR)
#     data_dir = os.getenv("DATA_DIR", DEFAULT_DATA_DIR)

#     # Validate date format
#     try:
#         datetime.strptime(snapshot_date, "%Y-%m-%d")
#     except ValueError:
#         print(f"❌ Invalid SNAPSHOT_DATE in .env: '{snapshot_date}'")
#         print("Must be YYYY-MM-DD and a real date")
#         exit(1)

#     return snapshot_date, wordcount_method, archive_dir, data_dir

# def bootstrap(snapshot_date, wordcount_method, archive_dir, data_dir):
#     archive_path = PROJECT_ROOT / archive_dir
#     xml_path = PROJECT_ROOT / data_dir / "regulations_xml" / snapshot_date

#     print("\nSetting up DOGE data workspace...")
#     print(f"Snapshot Date:       {snapshot_date}")
#     print(f"Word Count Strategy: {wordcount_method}")
#     print_dir_status("Archive Directory:", archive_path)
#     print_dir_status("XML Directory:", xml_path)
#     print("\n🎉 Bootstrap complete! You can now run the notebooks.\n")

# if __name__ == "__main__":
#     snapshot_date, wordcount_method, archive_dir, data_dir = get_env_config()
#     bootstrap(snapshot_date, wordcount_method, archive_dir, data_dir)
