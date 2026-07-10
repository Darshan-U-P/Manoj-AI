"""
==========================================================
Manoj AI
memory/models.py

Core memory models.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


# ==========================================================
# Memory Types
# ==========================================================

class MemoryType(Enum):
    """
    Categories of memory.
    """

    WORKING = "working"

    SHORT_TERM = "short_term"

    LONG_TERM = "long_term"

    SEMANTIC = "semantic"

    EPISODIC = "episodic"


# ==========================================================
# Memory Categories
# ==========================================================

class MemoryCategory(Enum):
    """
    What kind of information is stored.
    """

    FACT = "fact"

    PREFERENCE = "preference"

    PROJECT = "project"

    GOAL = "goal"

    EVENT = "event"

    SKILL = "skill"

    PERSON = "person"

    LOCATION = "location"

    OTHER = "other"


# ==========================================================
# Memory Priority
# ==========================================================

class MemoryPriority(Enum):
    """
    Importance level.
    """

    LOW = 1

    MEDIUM = 2

    HIGH = 3

    CRITICAL = 4


# ==========================================================
# Memory Entry
# ==========================================================

@dataclass(slots=True)
class MemoryEntry:
    """
    Represents one memory.
    """

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    content: str = ""

    memory_type: MemoryType = MemoryType.SHORT_TERM

    category: MemoryCategory = MemoryCategory.OTHER

    priority: MemoryPriority = MemoryPriority.MEDIUM

    created_at: datetime = field(
        default_factory=datetime.now
    )

    updated_at: datetime = field(
        default_factory=datetime.now
    )

    access_count: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # ------------------------------------------------------

    def touch(self) -> None:
        """
        Update access statistics.
        """

        self.access_count += 1

        self.updated_at = datetime.now()


# ==========================================================
# Memory Search Result
# ==========================================================

@dataclass(slots=True)
class MemorySearchResult:
    """
    Result returned by retriever.
    """

    memory: MemoryEntry

    score: float


# ==========================================================
# Memory Statistics
# ==========================================================

@dataclass(slots=True)
class MemoryStats:
    """
    Overall memory statistics.
    """

    total: int = 0

    working: int = 0

    short_term: int = 0

    long_term: int = 0

    semantic: int = 0

    episodic: int = 0