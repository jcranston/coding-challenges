"""Pytest configuration for the challenges directory.

This file helps pytest discover tests and handle relative imports properly.
"""

import os
import sys
from pathlib import Path

# Add the workspace root and challenges directory to sys.path for test imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Define challenges directory
challenges_dir = Path(__file__).parent

# Ensure we can import from challenges subdirectories
for item in challenges_dir.iterdir():
    if item.is_dir() and (item / "__init__.py").exists():
        sys.path.insert(0, str(item))
