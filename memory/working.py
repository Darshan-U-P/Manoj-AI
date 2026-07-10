"""
==========================================================
Manoj AI
working.py

Working memory.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from collections import deque

from memory.models import MemoryEntry


class WorkingMemory:
    """
    Working memory.

    Temporary memory used during the current
    conversation or task.

    Responsibilities
    ----------------
    - Store active memories
    - Maintain limited capacity
    - Clear temporary context

    Does NOT
    --------
    - Save to disk
    - Retrieve long-term memories
    """

    def __init__(
        self,
        capacity: int = 20,
    ) -> None:

        self._capacity = capacity

        self._memories: deque[MemoryEntry] = deque(
            maxlen=capacity
        )

    # ==================================================
    # Add
    # ==================================================

    def add(
        self,
        memory: MemoryEntry,
    ) -> None:

        self._memories.append(memory)

    # ==================================================
    # Extend
    # ==================================================

    def extend(
        self,
        memories: list[MemoryEntry],
    ) -> None:

        self._memories.extend(memories)

    # ==================================================
    # Remove
    # ==================================================

    def remove(
        self,
        memory_id: str,
    ) -> bool:

        for memory in list(self._memories):

            if memory.id == memory_id:

                self._memories.remove(memory)

                return True

        return False

    # ==================================================
    # Clear
    # ==================================================

    def clear(self) -> None:

        self._memories.clear()

    # ==================================================
    # Get All
    # ==================================================

    @property
    def memories(
        self,
    ) -> list[MemoryEntry]:

        return list(self._memories)

    # ==================================================
    # Latest
    # ==================================================

    @property
    def latest(
        self,
    ) -> MemoryEntry | None:

        if not self._memories:

            return None

        return self._memories[-1]

    # ==================================================
    # Size
    # ==================================================

    @property
    def size(self) -> int:

        return len(self._memories)

    # ==================================================
    # Empty
    # ==================================================

    @property
    def is_empty(self) -> bool:

        return len(self._memories) == 0

    # ==================================================
    # Capacity
    # ==================================================

    @property
    def capacity(self) -> int:

        return self._capacity