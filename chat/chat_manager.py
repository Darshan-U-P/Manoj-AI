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
    - Receive user messages
    - Maintain conversation
    - Build prompts
    - Run inference
    - Display responses

    Does NOT
    --------
    - Load models
    - Build UI
    - Handle startup/shutdown
    """

    def __init__(
        self,
        inference: InferenceEngine,
        tokenizer: Tokenizer
    ) -> None:

        self._conversation = Conversation()

        self._formatter = Formatter()

        self._builder = PromptBuilder()

        self._inference = inference

        self._tokenizer = tokenizer

    # ==================================================
    # Banner
    # ==================================================

    def start(self) -> None:

        self._formatter.banner()

        self._formatter.system(
            "Type 'exit' to quit."
        )

    # ==================================================
    # Process Message
    # ==================================================

    def process(
        self,
        user_message: str
    ) -> str:
        """
        Process one user message.

        Returns
        -------
        Assistant response.
        """

        try:

            logger.info("Processing user message.")

            history = self._conversation.get_messages()

            messages = self._builder.build(
                history,
                user_message
            )

            if self._tokenizer.is_context_full(
                messages
            ):

                self._formatter.system(
                    "Conversation context is full."
                )

            response = self._inference.generate(
                messages
            )

            self._conversation.add_user(
                user_message
            )

            self._conversation.add_assistant(
                response
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
    # Conversation
    # ==================================================

    def clear(self) -> None:

        self._conversation.clear()

        logger.info(
            "Conversation cleared."
        )

    # ==================================================
    # Interactive Loop
    # ==================================================

    def run(self) -> None:

        self.start()

        while True:

            user = input("\nYou: ").strip()

            if user.lower() in (
                "exit",
                "quit",
                "bye"
            ):
                break

            if not user:
                continue

            try:

                reply = self.process(
                    user
                )

                self._formatter.assistant(
                    reply
                )

            except ChatError as error:

                self._formatter.error(
                    str(error)
                )