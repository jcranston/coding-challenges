"""
Pytest configuration for the workspace root.
This file helps pytest discover tests and handle relative imports properly.
"""
import sys
import os
from pathlib import Path

# Add the workspace root and challenges directory to sys.path for test imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Define workspace root and challenges directory
workspace_root = Path(__file__).parent
challenges_dir = workspace_root / "challenges"
sys.path.insert(0, str(challenges_dir))

# Ensure we can import from challenges subdirectories
for item in challenges_dir.iterdir():
    if item.is_dir() and (item / "__init__.py").exists():
        sys.path.insert(0, str(item))
