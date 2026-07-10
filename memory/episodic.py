"""
==========================================================
Manoj AI
episodic.py

Episodic memory.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from datetime import datetime

from memory.models import (
    MemoryEntry,
    MemoryType,
)

from memory.storage import MemoryStorage


class EpisodicMemory:
    """
    Episodic memory.

    Stores chronological events.

    Responsibilities
    ----------------
    - Store events
    - Retrieve timeline
    - Retrieve recent events
    """

    def __init__(
        self,
        storage: MemoryStorage,
    ) -> None:

        self._storage = storage

        self._memories = self._storage.load()

        self._sort()

    # ==================================================
    # Add
    # ==================================================

    def add(
        self,
        memory: MemoryEntry,
    ) -> None:

        memory.memory_type = MemoryType.EPISODIC

        self._memories.append(memory)

        self._sort()

        self._storage.save(self._memories)

    # ==================================================
    # Timeline
    # ==================================================

    def timeline(
        self,
    ) -> list[MemoryEntry]:

        self._sort()

        return list(self._memories)

    # ==================================================
    # Recent
    # ==================================================

    def recent(
        self,
        limit: int = 10,
    ) -> list[MemoryEntry]:

        self._sort()

        return self._memories[-limit:]

    # ==================================================
    # Between Dates
    # ==================================================

    def between(
        self,
        start: datetime,
        end: datetime,
    ) -> list[MemoryEntry]:

        results = []

        for memory in self._memories:

            if start <= memory.created_at <= end:

                memory.touch()

                results.append(memory)

        return results

    # ==================================================
    # Remove
    # ==================================================

    def remove(
        self,
        memory_id: str,
    ) -> bool:

        for memory in self._memories:

            if memory.id == memory_id:

                self._memories.remove(memory)

                self._storage.save(self._memories)

                return True

        return False

    # ==================================================
    # Sort
    # ==================================================

    def _sort(
        self,
    ) -> None:

        self._memories.sort(
            key=lambda memory: memory.created_at
        )

    # ==================================================
    # Clear
    # ==================================================

    def clear(
        self,
    ) -> None:

        self._memories.clear()

        self._storage.save(self._memories)

    # ==================================================
    # Get All
    # ==================================================

    @property
    def memories(
        self,
    ) -> list[MemoryEntry]:

        return list(self._memories)

    # ==================================================
    # Size
    # ==================================================

    @property
    def size(
        self,
    ) -> int:

        return len(self._memories)