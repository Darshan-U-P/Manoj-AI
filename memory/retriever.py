"""
==========================================================
Manoj AI
retriever.py

Memory retrieval engine.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from memory.models import (
    MemoryEntry,
    MemorySearchResult,
)

from memory.working import WorkingMemory
from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from memory.semantic import SemanticMemory
from memory.episodic import EpisodicMemory


class MemoryRetriever:
    """
    Retrieves relevant memories.

    Responsibilities
    ----------------
    - Search every memory system
    - Rank memories
    - Return the best memories

    Does NOT
    --------
    - Store memories
    - Extract memories
    """

    def __init__(
        self,
        working: WorkingMemory,
        short_term: ShortTermMemory,
        long_term: LongTermMemory,
        semantic: SemanticMemory,
        episodic: EpisodicMemory,
    ) -> None:

        self._working = working
        self._short = short_term
        self._long = long_term
        self._semantic = semantic
        self._episodic = episodic

    # ==================================================
    # Retrieve
    # ==================================================

    def retrieve(
        self,
        query: str,
        limit: int = 10,
    ) -> list[MemoryEntry]:

        results: list[MemorySearchResult] = []

        # ----------------------------------------------
        # Working Memory
        # ----------------------------------------------

        for memory in self._working.memories:

            score = self._score(
                query,
                memory.content,
            )

            if score > 0:

                results.append(
                    MemorySearchResult(
                        memory=memory,
                        score=score + 5.0,
                    )
                )

        # ----------------------------------------------
        # Short-Term Memory
        # ----------------------------------------------

        for memory in self._short.memories:

            score = self._score(
                query,
                memory.content,
            )

            if score > 0:

                results.append(
                    MemorySearchResult(
                        memory=memory,
                        score=score + 3.0,
                    )
                )

        # ----------------------------------------------
        # Long-Term Memory
        # ----------------------------------------------

        for memory in self._long.memories:

            score = self._score(
                query,
                memory.content,
            )

            if score > 0:

                results.append(
                    MemorySearchResult(
                        memory=memory,
                        score=score + 2.0,
                    )
                )

        # ----------------------------------------------
        # Semantic Memory
        # ----------------------------------------------

        for memory in self._semantic.memories:

            score = self._score(
                query,
                memory.content,
            )

            if score > 0:

                results.append(
                    MemorySearchResult(
                        memory=memory,
                        score=score + 4.0,
                    )
                )

        # ----------------------------------------------
        # Episodic Memory
        # ----------------------------------------------

        for memory in self._episodic.memories:

            score = self._score(
                query,
                memory.content,
            )

            if score > 0:

                results.append(
                    MemorySearchResult(
                        memory=memory,
                        score=score + 1.0,
                    )
                )

        # ----------------------------------------------
        # Sort
        # ----------------------------------------------

        results.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        memories: list[MemoryEntry] = []

        seen: set[str] = set()

        for result in results:

            if result.memory.id in seen:
                continue

            result.memory.touch()

            seen.add(result.memory.id)

            memories.append(result.memory)

            if len(memories) >= limit:
                break

        return memories

    # ==================================================
    # Score
    # ==================================================

    def _score(
        self,
        query: str,
        text: str,
    ) -> float:

        score = 0.0

        query_words = set(
            query.lower().split()
        )

        text_words = set(
            text.lower().split()
        )

        for word in query_words:

            if word in text_words:

                score += 1.0

        return score