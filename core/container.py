"""
==========================================================
Manoj AI
container.py

Dependency Injection Container.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from typing import Any

from llm.model_loader import ModelLoader
from llm.inference import InferenceEngine
from llm.tokenizer import Tokenizer
from llm.prompt_builder import PromptBuilder

from chat.conversation import Conversation
from chat.formatter import Formatter
from chat.chat_manager import ChatManager

from app.startup import Startup
from app.shutdown import Shutdown


class Container:
    """
    Dependency Injection Container.

    Responsible for creating application services.

    Each service is created only once.
    """

    def __init__(self) -> None:

        self._services: dict[str, Any] = {}

    # ==================================================
    # Generic
    # ==================================================

    def register(
        self,
        name: str,
        instance: Any,
    ) -> None:

        self._services[name] = instance

    def resolve(
        self,
        name: str,
    ) -> Any:

        return self._services[name]

    # ==================================================
    # Model Loader
    # ==================================================

    def model_loader(self) -> ModelLoader:

        if "model_loader" not in self._services:

            self.register(
                "model_loader",
                ModelLoader()
            )

        return self.resolve("model_loader")

    # ==================================================
    # Startup
    # ==================================================

    def startup(self) -> Startup:

        if "startup" not in self._services:

            self.register(
                "startup",
                Startup(
                    self.model_loader()
                )
            )

        return self.resolve("startup")

    # ==================================================
    # Tokenizer
    # ==================================================

    def tokenizer(self) -> Tokenizer:

        if "tokenizer" not in self._services:

            self.register(
                "tokenizer",
                Tokenizer(
                    self.model_loader()
                )
            )

        return self.resolve("tokenizer")

    # ==================================================
    # Prompt Builder
    # ==================================================

    def prompt_builder(self) -> PromptBuilder:

        if "prompt_builder" not in self._services:

            self.register(
                "prompt_builder",
                PromptBuilder()
            )

        return self.resolve("prompt_builder")

    # ==================================================
    # Conversation
    # ==================================================

    def conversation(self) -> Conversation:

        if "conversation" not in self._services:

            self.register(
                "conversation",
                Conversation()
            )

        return self.resolve("conversation")

    # ==================================================
    # Formatter
    # ==================================================

    def formatter(self) -> Formatter:

        if "formatter" not in self._services:

            self.register(
                "formatter",
                Formatter()
            )

        return self.resolve("formatter")

    # ==================================================
    # Inference
    # ==================================================

    def inference(self) -> InferenceEngine:

        if "inference" not in self._services:

            self.register(
                "inference",
                InferenceEngine(
                    self.model_loader()
                )
            )

        return self.resolve("inference")

    # ==================================================
    # Chat Manager
    # ==================================================

    def chat_manager(self) -> ChatManager:

        if "chat_manager" not in self._services:

            self.register(
                "chat_manager",
                ChatManager(
                    self.inference(),
                    self.tokenizer(),
                )
            )

        return self.resolve("chat_manager")

    # ==================================================
    # Shutdown
    # ==================================================

    def shutdown(self) -> Shutdown:

        if "shutdown" not in self._services:

            self.register(
                "shutdown",
                Shutdown(
                    self.model_loader()
                )
            )

        return self.resolve("shutdown")