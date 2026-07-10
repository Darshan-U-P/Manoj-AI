"""
==========================================================
Manoj AI
chat_manager.py

Coordinates the complete chat pipeline.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from chat.conversation import Conversation
from chat.formatter import Formatter

from core.models import (
    ChatRequest,
    ChatResponse,
    Message,
)

from llm.prompt_builder import PromptBuilder
from llm.inference import InferenceEngine
from llm.tokenizer import Tokenizer

from system.logger import logger
from system.exceptions import ChatError


class ChatManager:
    """
    Coordinates the chat system.

    Responsibilities
    ----------------
    - Accept user input
    - Maintain conversation
    - Build requests
    - Run inference
    - Display output

    Does NOT
    --------
    - Generate text
    - Load models
    - Store memory
    """

    def __init__(
        self,
        inference: InferenceEngine,
        tokenizer: Tokenizer,
    ) -> None:

        self._conversation = Conversation()

        self._formatter = Formatter()

        self._builder = PromptBuilder()

        self._inference = inference

        self._tokenizer = tokenizer

    # ==================================================
    # Start
    # ==================================================

    def start(self) -> None:

        self._formatter.banner()

        self._formatter.message(
            Message(
                role="system",
                content="Type 'exit' to quit."
            )
        )

    # ==================================================
    # Process
    # ==================================================

    def process(
        self,
        user_text: str,
    ) -> ChatResponse:

        try:

            logger.info(
                "Processing user message."
            )

            request: ChatRequest = (
                self._builder.build(
                    self._conversation.messages,
                    user_text,
                )
            )

            remaining = (
                self._tokenizer.remaining_context(
                    request.messages
                )
            )

            if remaining <= 0:

                self._formatter.message(
                    Message(
                        role="system",
                        content=(
                            "Conversation context is full."
                        )
                    )
                )

            response = (
                self._inference.generate(
                    request
                )
            )

            self._conversation.add_user(
                user_text
            )

            self._conversation.add(
                response.message
            )

            logger.info(
                "Assistant response generated."
            )

            return response

        except Exception as error:

            logger.exception(
                "Chat processing failed."
            )

            raise ChatError(
                str(error)
            ) from error

    # ==================================================
    # Clear
    # ==================================================

    def clear(self) -> None:

        self._conversation.clear()

        logger.info(
            "Conversation cleared."
        )

    # ==================================================
    # Run
    # ==================================================

    def run(self) -> None:

        self.start()

        while True:

            user = input(
                "\nYou: "
            ).strip()

            if user.lower() in (
                "exit",
                "quit",
                "bye",
            ):
                break

            if not user:
                continue

            try:

                response = self.process(
                    user
                )

                self._formatter.message(
                    response.message
                )

            except ChatError as error:

                self._formatter.error(
                    str(error)
                )