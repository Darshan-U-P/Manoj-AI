"""
==========================================================
Manoj AI
prompt_builder.py

Builds chat requests for the language model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from core.models import (
    ChatRequest,
    Message,
)

from config.config import config


class PromptBuilder:
    """
    Builds structured chat requests.

    Responsibilities
    ----------------
    - Add system prompt
    - Add conversation history
    - Add current user message

    Does NOT
    --------
    - Perform inference
    - Manage conversations
    - Load models
    """

    def __init__(self) -> None:

        self._system_prompt = config.get(
            "chat",
            "system_prompt"
        )

    # ==================================================
    # Build Request
    # ==================================================

    def build(
        self,
        conversation: list[Message],
        user_message: str,
    ) -> ChatRequest:

        messages: list[Message] = []

        # --------------------------------------------
        # System Prompt
        # --------------------------------------------

        messages.append(
            Message(
                role="system",
                content=self._system_prompt,
            )
        )

        # --------------------------------------------
        # Conversation History
        # --------------------------------------------

        messages.extend(conversation)

        # --------------------------------------------
        # Current User Message
        # --------------------------------------------

        messages.append(
            Message(
                role="user",
                content=user_message,
            )
        )

        return ChatRequest(
            messages=messages
        )