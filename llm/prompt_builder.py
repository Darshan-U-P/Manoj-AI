"""
==========================================================
Manoj AI
prompt_builder.py

Builds chat messages for the language model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from typing import List, Dict

from config.config import config


class PromptBuilder:
    """
    Builds structured chat prompts.

    Responsibilities
    ----------------
    - Add system prompt
    - Add conversation history
    - Add current user message

    Does NOT:
    - Perform inference
    - Manage memory
    - Load models
    """

    def __init__(self) -> None:

        self._system_prompt = config.get(
            "chat",
            "system_prompt"
        )

    # ==================================================
    # Build Prompt
    # ==================================================

    def build(
        self,
        conversation: List[Dict[str, str]],
        user_message: str
    ) -> List[Dict[str, str]]:
        """
        Build chat messages for the model.

        Parameters
        ----------
        conversation
            Previous conversation.

        user_message
            Current user input.

        Returns
        -------
        list
            Chat messages.
        """

        messages: List[Dict[str, str]] = []

        # --------------------------------------------
        # System Prompt
        # --------------------------------------------

        messages.append(
            {
                "role": "system",
                "content": self._system_prompt
            }
        )

        # --------------------------------------------
        # Conversation History
        # --------------------------------------------

        messages.extend(conversation)

        # --------------------------------------------
        # Current User Message
        # --------------------------------------------

        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        return messages