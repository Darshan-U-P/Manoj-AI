"""
==========================================================
Manoj AI
long_term.py

Long-term memory.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from memory.models import (
    MemoryEntry,
    MemoryType,
)

from memory.storage import MemoryStorage


class LongTermMemory:
    """
    Long-term memory.

    Stores important information permanently.

    Responsibilities
    ----------------
    - Store important memories
    - Retrieve memories
    - Update memories
    - Remove memories

    Does NOT
    --------
    - Perform semantic search
    - Classify memories
    """

    def __init__(
        self,
        storage: MemoryStorage,
    ) -> None:

        self._storage = storage

        self._memories = self._storage.load()

    # ==================================================
    # Add
    # ==================================================

    def add(
        self,
        memory: MemoryEntry,
    ) -> None:

        memory.memory_type = MemoryType.LONG_TERM

        self._memories.append(memory)

        self._storage.save(self._memories)

    # ==================================================
    # Update
    # ==================================================

    def update(
        self,
        memory: MemoryEntry,
    ) -> bool:

        for index, item in enumerate(self._memories):

            if item.id == memory.id:

                self._memories[index] = memory

                self._storage.save(self._memories)

                return True

        return False

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
    # Find
    # ==================================================

    def find(
        self,
        keyword: str,
    ) -> list[MemoryEntry]:

        keyword = keyword.lower()

        results = []

        for memory in self._memories:

            if keyword in memory.content.lower():

                memory.touch()

                results.append(memory)

        return results

    # ==================================================
    # Exists
    # ==================================================

    def exists(
        self,
        keyword: str,
    ) -> bool:

        keyword = keyword.lower()

        return any(
            keyword in memory.content.lower()
            for memory in self._memories
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

        self._storage.save(self._memories)