"""
==========================================================
Manoj AI
inference.py

Inference engine for the language model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from typing import Any

from config.config import config

from core.interfaces import LLMInterface
from core.models import (
    ChatRequest,
    ChatResponse,
    Message,
)

from llm.model_loader import ModelLoader

from system.exceptions import (
    ModelInferenceError,
)

from system.logger import logger


class InferenceEngine(LLMInterface):
    """
    Handles all text generation.

    Responsibilities
    ----------------
    - Generate responses
    - Apply generation settings
    - Convert model output into ChatResponse

    Does NOT
    --------
    - Load models
    - Manage conversations
    - Build prompts
    """

    def __init__(
        self,
        model_loader: ModelLoader,
    ) -> None:

        self._loader = model_loader

    # ==================================================
    # Compatibility
    # ==================================================

    def load(self) -> None:
        """
        Forward to ModelLoader.
        """
        self._loader.load()

    def unload(self) -> None:
        """
        Forward to ModelLoader.
        """
        self._loader.unload()

    # ==================================================
    # Generate
    # ==================================================

    def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        if not self._loader.is_loaded:
            raise ModelInferenceError(
                "Model is not loaded."
            )

        logger.info(
            "Starting inference..."
        )

        try:

            response: dict[str, Any] = (
                self._loader.model.create_chat_completion(

                    messages=[
                        message.to_dict()
                        for message in request.messages
                    ],

                    temperature=config.get(
                        "model",
                        "temperature"
                    ),

                    top_p=config.get(
                        "model",
                        "top_p"
                    ),

                    top_k=config.get(
                        "model",
                        "top_k"
                    ),

                    repeat_penalty=config.get(
                        "model",
                        "repeat_penalty"
                    ),

                    max_tokens=config.get(
                        "model",
                        "max_tokens"
                    ),

                    stream=False,
                )
            )

            text = (
                response["choices"][0]
                ["message"]
                ["content"]
                .strip()
            )

            logger.info(
                "Inference completed."
            )

            return ChatResponse(
                message=Message(
                    role="assistant",
                    content=text,
                )
            )

        except Exception as error:

            logger.exception(
                "Inference failed."
            )

            raise ModelInferenceError(
                str(error)
            ) from error