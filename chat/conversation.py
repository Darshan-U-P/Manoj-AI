"""
==========================================================
Manoj AI
conversation.py

Conversation history manager.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from core.models import Message
from config.config import config


class Conversation:
    """
    Manages conversation history.

    Responsibilities
    ----------------
    - Store messages
    - Return messages
    - Clear history
    - Enforce history limit

    Does NOT
    --------
    - Perform inference
    - Build prompts
    - Print output
    """

    def __init__(self) -> None:

        self._messages: list[Message] = []

        self._history_limit = config.get(
            "chat",
            "history_limit"
        )

    # ==================================================
    # Add Message
    # ==================================================

    def add(
        self,
        message: Message
    ) -> None:
        """
        Add a message to the conversation.
        """

        self._messages.append(message)

        self._trim()

    # ==================================================
    # Add User
    # ==================================================

    def add_user(
        self,
        text: str
    ) -> None:

        self.add(
            Message(
                role="user",
                content=text,
            )
        )

    # ==================================================
    # Add Assistant
    # ==================================================

    def add_assistant(
        self,
        text: str
    ) -> None:

        self.add(
            Message(
                role="assistant",
                content=text,
            )
        )

    # ==================================================
    # Messages
    # ==================================================

    @property
    def messages(self) -> list[Message]:

        return self._messages.copy()

    # ==================================================
    # Clear
    # ==================================================

    def clear(self) -> None:

        self._messages.clear()

    # ==================================================
    # Size
    # ==================================================

    @property
    def size(self) -> int:

        return len(self._messages)

    # ==================================================
    # Empty
    # ==================================================

    @property
    def is_empty(self) -> bool:

        return len(self._messages) == 0

    # ==================================================
    # Last Message
    # ==================================================

    @property
    def last(self) -> Message | None:

        if self.is_empty:
            return None

        return self._messages[-1]

    # ==================================================
    # Trim
    # ==================================================

    def _trim(self) -> None:

        if len(self._messages) <= self._history_limit:
            return

        self._messages = self._messages[
            -self._history_limit:
        ]