"""
==========================================================
Manoj AI
tokenizer.py

Token counting and context management.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from core.models import Message

from llm.model_loader import ModelLoader
from config.config import config


class Tokenizer:
    """
    Token utility class.

    Responsibilities
    ----------------
    - Count tokens
    - Count conversation tokens
    - Check remaining context

    Does NOT
    --------
    - Build prompts
    - Perform inference
    """

    def __init__(
        self,
        model_loader: ModelLoader
    ) -> None:

        self._loader = model_loader

        self._max_context = config.get(
            "model",
            "context_size"
        )

    # ==================================================
    # Count Tokens
    # ==================================================

    def count(
        self,
        text: str
    ) -> int:
        """
        Count tokens in a piece of text.
        """

        tokens = self._loader.model.tokenize(
            text.encode("utf-8")
        )

        return len(tokens)

    # ==================================================
    # Conversation Tokens
    # ==================================================

    def conversation_tokens(
        self,
        messages: list[Message]
    ) -> int:
        """
        Count tokens used by an entire conversation.
        """

        total = 0

        for message in messages:

            total += self.count(
                message.content
            )

        return total

    # ==================================================
    # Remaining Context
    # ==================================================

    def remaining_context(
        self,
        messages: list[Message]
    ) -> int:
        """
        Return remaining context window.
        """

        used = self.conversation_tokens(
            messages
        )

        return max(
            self._max_context - used,
            0
        )

    # ==================================================
    # Context Full
    # ==================================================

    def is_context_full(
        self,
        messages: list[Message]
    ) -> bool:
        """
        Check whether the context window is full.
        """

        return (
            self.conversation_tokens(
                messages
            )
            >= self._max_context
        )

    # ==================================================
    # Max Context
    # ==================================================

    @property
    def max_context(self) -> int:
        """
        Maximum supported context size.
        """

        return self._max_context