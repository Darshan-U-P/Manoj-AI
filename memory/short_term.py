"""
==========================================================
Manoj AI
short_term.py

Short-term memory.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta

from memory.models import (
    MemoryEntry,
    MemoryType,
)

from memory.storage import MemoryStorage


class ShortTermMemory:
    """
    Short-term memory.

    Stores memories for a limited time.

    Responsibilities
    ----------------
    - Store temporary memories
    - Load memories
    - Remove expired memories

    Does NOT
    --------
    - Perform semantic search
    - Extract memories
    """

    def __init__(
        self,
        storage: MemoryStorage,
        lifetime_hours: int = 24,
    ) -> None:

        self._storage = storage

        self._lifetime = timedelta(
            hours=lifetime_hours
        )

        self._memories = self._storage.load()

        self.cleanup()

    # ==================================================
    # Add
    # ==================================================

    def add(
        self,
        memory: MemoryEntry,
    ) -> None:

        memory.memory_type = MemoryType.SHORT_TERM

        self._memories.append(memory)

        self._storage.save(self._memories)

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

                self._storage.save(
                    self._memories
                )

                return True

        return False

    # ==================================================
    # Cleanup
    # ==================================================

    def cleanup(
        self,
    ) -> None:

        now = datetime.now()

        self._memories = [

            memory

            for memory in self._memories

            if (
                now - memory.updated_at
            ) < self._lifetime

        ]

        self._storage.save(
            self._memories
        )

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

    # ==================================================
    # Empty
    # ==================================================

    @property
    def is_empty(
        self,
    ) -> bool:

        return len(self._memories) == 0

    # ==================================================
    # Clear
    # ==================================================

    def clear(
        self,
    ) -> None:

        self._memories.clear()

        self._storage.save(
            self._memories
        )