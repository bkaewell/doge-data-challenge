from dotenv import load_dotenv
from pathlib import Path
import os

"""
Utility for loading project paths and .env config cleanly across notebooks

This helps keep notebooks simple and lets users configure behavior through the .env file
"""
def load_paths():
    ROOT = Path(__file__).resolve().parents[2]  # utils/ is one deeper than notebooks/
    load_dotenv(ROOT / ".env")
    
    archive_dir = os.getenv("ARCHIVE_DIR", "archive")
    data_dir = os.getenv("DATA_DIR", "data")
    snapshot_date = os.getenv("SNAPSHOT_DATE")
    
    return {
        "ROOT": ROOT,
        "ARCHIVE_PATH": ROOT / archive_dir,
        "DATA_PATH": ROOT / data_dir,
        "XML_SNAPSHOT_PATH": ROOT / data_dir / "regulations_xml" / snapshot_date,
        "SNAPSHOT_DATE": snapshot_date,
    }
