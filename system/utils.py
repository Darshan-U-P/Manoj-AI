"""
==========================================================
Manoj AI
utils.py

General utility functions.

Author: Darshan
==========================================================
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


# ==========================================================
# Directory Utilities
# ==========================================================

def ensure_directory(directory: Path) -> None:
    """
    Create directory if it does not exist.
    """
    directory.mkdir(parents=True, exist_ok=True)


# ==========================================================
# File Utilities
# ==========================================================

def file_exists(path: Path) -> bool:
    """
    Check whether a file exists.
    """
    return path.exists() and path.is_file()


def directory_exists(path: Path) -> bool:
    """
    Check whether a directory exists.
    """
    return path.exists() and path.is_dir()


# ==========================================================
# JSON Utilities
# ==========================================================

def load_json(path: Path) -> dict[str, Any]:
    """
    Load a JSON file.
    """

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(
    path: Path,
    data: dict[str, Any]
) -> None:
    """
    Save data as JSON.
    """

    with open(path, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================================
# Time Utilities
# ==========================================================

def current_time() -> str:
    """
    Current local time.
    """

    return datetime.now().strftime("%H:%M:%S")


def current_date() -> str:
    """
    Current local date.
    """

    return datetime.now().strftime("%Y-%m-%d")


def timestamp() -> str:
    """
    Current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================================================
# String Utilities
# ==========================================================

def separator(length: int = 70) -> str:
    """
    Create a separator line.
    """

    return "=" * length


def is_blank(text: str) -> bool:
    """
    Check if text is empty or whitespace.
    """

    return len(text.strip()) == 0


# ==========================================================
# Path Utilities
# ==========================================================

def normalize_path(path: str | Path) -> Path:
    """
    Convert to absolute Path.
    """

    return Path(path).expanduser().resolve()


# ==========================================================
# Validation
# ==========================================================

def require(
    condition: bool,
    message: str
) -> None:
    """
    Raise ValueError if condition is False.
    """

    if not condition:
        raise ValueError(message)