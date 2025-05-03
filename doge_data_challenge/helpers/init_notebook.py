#!/usr/bin/env python3

import sys
from pathlib import Path
from .env_paths import load_paths

def init_notebook() -> dict[str, Path | str]:
    """
    Initialize notebook by setting up sys.path and loading project paths

    Returns:
        Dictionary of project paths from env_paths.load_paths()
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

