"""
==========================================================
Manoj AI
semantic.py

Semantic memory.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from memory.models import (
    MemoryEntry,
    MemoryType,
)

from memory.storage import MemoryStorage


class SemanticMemory:
    """
    Semantic memory.

    Stores concepts, preferences, skills,
    relationships, and knowledge.

    Responsibilities
    ----------------
    - Store semantic memories
    - Search by meaning (currently keyword)
    - Update memory usage

    Future
    ------
    Will support embeddings and vector search.
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

        memory.memory_type = MemoryType.SEMANTIC

        self._memories.append(memory)

        self._storage.save(
            self._memories
        )

    # ==================================================
    # Search
    # ==================================================

    def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[MemoryEntry]:

        query = query.lower()

        results: list[MemoryEntry] = []

        for memory in self._memories:

            score = 0

            content = memory.content.lower()

            for word in query.split():

                if word in content:

                    score += 1

            if score > 0:

                memory.touch()

                results.append(memory)

        results.sort(

            key=lambda memory: (
                memory.priority.value,
                memory.access_count,
            ),

            reverse=True,

        )

        return results[:limit]

    # ==================================================
    # Update
    # ==================================================

    def update(
        self,
        memory: MemoryEntry,
    ) -> bool:

        for index, item in enumerate(
            self._memories
        ):

            if item.id == memory.id:

                self._memories[index] = memory

                self._storage.save(
                    self._memories
                )

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

                self._memories.remove(
                    memory
                )

                self._storage.save(
                    self._memories
                )

                return True

        return False

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
    # Clear
    # ==================================================

    def clear(
        self,
    ) -> None:

        self._memories.clear()

        self._storage.save(
            self._memories
        )