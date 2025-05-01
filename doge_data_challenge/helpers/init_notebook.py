#!/usr/bin/env python3

import sys
from pathlib import Path
from .env_paths import load_paths

def init_notebook() -> dict[str, Path | str]:
    """
    Initialize notebook by setting up sys.path and loading project paths.

    Returns:
        Dictionary of project paths from env_paths.load_paths().
    """
    # Resolve project root (assuming notebook is in notebooks/)
    project_root = Path().resolve().parents[1]  # notebooks/ -> project root
    package_path = project_root / "doge_data_challenge"

    # Add project root and package to sys.path if not already present
    for path in [str(project_root), str(package_path)]:
        if path not in sys.path:
            sys.path.insert(0, path)

    # Load paths from env_paths
    return load_paths()


# import os
# import sys
# from pathlib import Path
# from dotenv import load_dotenv

# def init_notebook():

#     project_root = Path(__file__).resolve().parent
#     sys.path.insert(0, str(project_root))



#     notebook_dir = Path(__file__).resolve().parent
#     repo_root = notebook_dir.parent

#     # Add repo root to sys.path if not already present
#     if str(repo_root) not in sys.path:
#         sys.path.insert(0, str(repo_root))

#     # Load .env file from root
#     load_dotenv(repo_root / ".env")

#     from helpers.env_paths import load_paths
#     return load_paths()

