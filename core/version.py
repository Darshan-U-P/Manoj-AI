"""
==========================================================
Manoj AI
version.py

Application version information.

This file is the single source of truth for
application metadata.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """
    Represents application version information.
    """

    name: str
    version: str
    stage: str
    build: int
    author: str


# ==========================================================
# Application Metadata
# ==========================================================

APP = Version(
    name="Manoj AI",
    version="0.5.0",
    stage="Development",
    build=1,
    author="Darshan",
)