"""
==========================================================
Manoj AI
extractor.py

Memory extractor.

Author: Darshan
==========================================================
"""

from __future__ import annotations

import re

from memory.models import (
    MemoryCategory,
    MemoryEntry,
    MemoryPriority,
    MemoryType,
)


class MemoryExtractor:
    """
    Extracts structured memories from user input.

    Responsibilities
    ----------------
    - Extract facts
    - Extract projects
    - Extract goals
    - Create MemoryEntry objects

    Does NOT
    --------
    - Store memories
    - Search memories
    - Decide whether something should be remembered
    """

    # ==================================================
    # Extract
    # ==================================================

    def extract(
        self,
        text: str,
        category: MemoryCategory,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        match category:

            case MemoryCategory.FACT:
                return self._extract_fact(
                    text,
                    priority,
                )

            case MemoryCategory.PROJECT:
                return self._extract_project(
                    text,
                    priority,
                )

            case MemoryCategory.GOAL:
                return self._extract_goal(
                    text,
                    priority,
                )

            case MemoryCategory.PREFERENCE:
                return self._extract_preference(
                    text,
                    priority,
                )

            case MemoryCategory.SKILL:
                return self._extract_skill(
                    text,
                    priority,
                )

            case _:

                return []

    # ==================================================
    # Fact
    # ==================================================

    def _extract_fact(
        self,
        text: str,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        lower = text.lower()

        match = re.search(
            r"my name is\s+(.+)",
            lower,
        )

        if match:

            name = match.group(1).strip().title()

            return [

                MemoryEntry(

                    content=f"User name is {name}",

                    memory_type=MemoryType.LONG_TERM,

                    category=MemoryCategory.FACT,

                    priority=priority,

                )

            ]

        return []

    # ==================================================
    # Project
    # ==================================================

    def _extract_project(
        self,
        text: str,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        return [

            MemoryEntry(

                content=text,

                memory_type=MemoryType.LONG_TERM,

                category=MemoryCategory.PROJECT,

                priority=priority,

            )

        ]

    # ==================================================
    # Goal
    # ==================================================

    def _extract_goal(
        self,
        text: str,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        return [

            MemoryEntry(

                content=text,

                memory_type=MemoryType.LONG_TERM,

                category=MemoryCategory.GOAL,

                priority=priority,

            )

        ]

    # ==================================================
    # Preference
    # ==================================================

    def _extract_preference(
        self,
        text: str,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        return [

            MemoryEntry(

                content=text,

                memory_type=MemoryType.SEMANTIC,

                category=MemoryCategory.PREFERENCE,

                priority=priority,

            )

        ]

    # ==================================================
    # Skill
    # ==================================================

    def _extract_skill(
        self,
        text: str,
        priority: MemoryPriority,
    ) -> list[MemoryEntry]:

        return [

            MemoryEntry(

                content=text,

                memory_type=MemoryType.SEMANTIC,

                category=MemoryCategory.SKILL,

                priority=priority,

            )

        ]