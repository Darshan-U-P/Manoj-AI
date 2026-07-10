"""
==========================================================
Manoj AI
memory_manager.py

Central memory manager.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from memory.classifier import (
    MemoryClassifier,
    MemoryDecision,
)

from memory.extractor import MemoryExtractor

from memory.models import (
    MemoryEntry,
    MemoryType,
)

from memory.retriever import MemoryRetriever

from memory.working import WorkingMemory
from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from memory.semantic import SemanticMemory
from memory.episodic import EpisodicMemory


class MemoryManager:
    """
    Central memory manager.

    Responsibilities
    ----------------
    - Remember new information
    - Retrieve relevant memories
    - Manage all memory systems

    This is the ONLY class the rest of
    Manoj AI should communicate with.
    """

    def __init__(
        self,
        working: WorkingMemory,
        short_term: ShortTermMemory,
        long_term: LongTermMemory,
        semantic: SemanticMemory,
        episodic: EpisodicMemory,
        classifier: MemoryClassifier,
        extractor: MemoryExtractor,
        retriever: MemoryRetriever,
    ) -> None:

        self._working = working

        self._short = short_term

        self._long = long_term

        self._semantic = semantic

        self._episodic = episodic

        self._classifier = classifier

        self._extractor = extractor

        self._retriever = retriever

    # ==================================================
    # Remember
    # ==================================================

    def remember(
        self,
        text: str,
    ) -> None:

        result = self._classifier.classify(
            text
        )

        if result.decision == MemoryDecision.IGNORE:

            return

        memories = self._extractor.extract(

            text=text,

            category=result.category,

            priority=result.priority,

        )

        for memory in memories:

            self._working.add(
                memory
            )

            match memory.memory_type:

                case MemoryType.SHORT_TERM:

                    self._short.add(memory)

                case MemoryType.LONG_TERM:

                    self._long.add(memory)

                case MemoryType.SEMANTIC:

                    self._semantic.add(memory)

                case MemoryType.EPISODIC:

                    self._episodic.add(memory)

    # ==================================================
    # Recall
    # ==================================================

    def recall(
        self,
        query: str,
        limit: int = 10,
    ) -> list[MemoryEntry]:

        return self._retriever.retrieve(
            query=query,
            limit=limit,
        )

    # ==================================================
    # Working Memory
    # ==================================================

    @property
    def working(self) -> WorkingMemory:

        return self._working

    # ==================================================
    # Clear Working Memory
    # ==================================================

    def clear_working(self) -> None:

        self._working.clear()

    # ==================================================
    # Clear All Memory
    # ==================================================

    def clear_all(self) -> None:

        self._working.clear()

        self._short.clear()

        self._long.clear()

        self._semantic.clear()

        self._episodic.clear()