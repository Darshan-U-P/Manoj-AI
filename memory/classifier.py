"""
==========================================================
Manoj AI
classifier.py

Memory classifier.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from enum import Enum

from memory.models import (
    MemoryCategory,
    MemoryPriority,
)


# ==========================================================
# Memory Decision
# ==========================================================

class MemoryDecision(Enum):
    """
    What should happen with the information.
    """

    IGNORE = "ignore"

    STORE = "store"


# ==========================================================
# Classification Result
# ==========================================================

class ClassificationResult:

    def __init__(
        self,
        decision: MemoryDecision,
        category: MemoryCategory,
        priority: MemoryPriority,
    ) -> None:

        self.decision = decision

        self.category = category

        self.priority = priority


# ==========================================================
# Memory Classifier
# ==========================================================

class MemoryClassifier:
    """
    Decides whether information should be remembered.
    """

    def classify(
        self,
        text: str,
    ) -> ClassificationResult:

        sentence = text.lower()

        # --------------------------------------------------
        # Name
        # --------------------------------------------------

        if (
            "my name is" in sentence
            or "i am " in sentence
        ):

            return ClassificationResult(
                MemoryDecision.STORE,
                MemoryCategory.FACT,
                MemoryPriority.CRITICAL,
            )

        # --------------------------------------------------
        # Preference
        # --------------------------------------------------

        if (
            "i like" in sentence
            or "i love" in sentence
            or "my favorite" in sentence
        ):

            return ClassificationResult(
                MemoryDecision.STORE,
                MemoryCategory.PREFERENCE,
                MemoryPriority.HIGH,
            )

        # --------------------------------------------------
        # Project
        # --------------------------------------------------

        if (
            "i am building" in sentence
            or "i'm building" in sentence
            or "my project" in sentence
            or "working on" in sentence
        ):

            return ClassificationResult(
                MemoryDecision.STORE,
                MemoryCategory.PROJECT,
                MemoryPriority.HIGH,
            )

        # --------------------------------------------------
        # Goal
        # --------------------------------------------------

        if (
            "my goal" in sentence
            or "i want to" in sentence
            or "i plan to" in sentence
        ):

            return ClassificationResult(
                MemoryDecision.STORE,
                MemoryCategory.GOAL,
                MemoryPriority.HIGH,
            )

        # --------------------------------------------------
        # Skill
        # --------------------------------------------------

        if (
            "i know" in sentence
            or "i can" in sentence
        ):

            return ClassificationResult(
                MemoryDecision.STORE,
                MemoryCategory.SKILL,
                MemoryPriority.MEDIUM,
            )

        # --------------------------------------------------
        # Ignore
        # --------------------------------------------------

        return ClassificationResult(
            MemoryDecision.IGNORE,
            MemoryCategory.OTHER,
            MemoryPriority.LOW,
        )