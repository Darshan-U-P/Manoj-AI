"""
==========================================================
Manoj AI
conversation.py

Conversation history manager.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from typing import Dict, List

from config.config import config


class Conversation:
    """
    Manages conversation history.

    Responsibilities
    ----------------
    - Store messages
    - Clear history
    - Return conversation
    - Enforce history limit

    Does NOT
    --------
    - Perform inference
    - Build prompts
    - Print output
    """

    def __init__(self) -> None:

        self._messages: List[Dict[str, str]] = []

        self._history_limit = config.get(
            "chat",
            "history_limit"
        )

    # ==================================================
    # Add User Message
    # ==================================================

    def add_user(self, message: str) -> None:

        self._messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        self._trim()

    # ==================================================
    # Add Assistant Message
    # ==================================================

    def add_assistant(self, message: str) -> None:

        self._messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

        self._trim()

    # ==================================================
    # Get Conversation
    # ==================================================

    def get_messages(self) -> List[Dict[str, str]]:

        return self._messages.copy()

    # ==================================================
    # Clear Conversation
    # ==================================================

    def clear(self) -> None:

        self._messages.clear()

    # ==================================================
    # Conversation Length
    # ==================================================

    @property
    def size(self) -> int:

        return len(self._messages)

    # ==================================================
    # Empty?
    # ==================================================

    @property
    def is_empty(self) -> bool:

        return len(self._messages) == 0

    # ==================================================
    # Trim History
    # ==================================================

    def _trim(self) -> None:
        """
        Keep only the newest messages.
        """

        if len(self._messages) <= self._history_limit:
            return

        self._messages = self._messages[
            -self._history_limit:
        ]