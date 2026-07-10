"""
==========================================================
Manoj AI
types.py

Common type aliases used throughout the project.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, TypeAlias


# ==========================================================
# Basic Types
# ==========================================================

JSONValue: TypeAlias = (
    dict[str, Any]
    | list[Any]
    | str
    | int
    | float
    | bool
    | None
)

JSONDict: TypeAlias = dict[str, Any]

JSONString: TypeAlias = str


# ==========================================================
# File System
# ==========================================================

FilePath: TypeAlias = str | Path


# ==========================================================
# Chat
# ==========================================================

Role: TypeAlias = str

MessageContent: TypeAlias = str

ChatMessage: TypeAlias = dict[str, str]

ChatMessages: TypeAlias = list[ChatMessage]


# ==========================================================
# Configuration
# ==========================================================

ConfigKey: TypeAlias = str

ConfigValue: TypeAlias = Any


# ==========================================================
# Model
# ==========================================================

TokenCount: TypeAlias = int

ContextSize: TypeAlias = int

Temperature: TypeAlias = float

TopP: TypeAlias = float

TopK: TypeAlias = int


# ==========================================================
# Application
# ==========================================================

Milliseconds: TypeAlias = float

Seconds: TypeAlias = float