"""
==========================================================
Manoj AI
inference.py

Handles text generation using the loaded language model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from typing import Any

from llm.model_loader import ModelLoader
from config.config import config
from system.logger import logger
from system.exceptions import ModelInferenceError


class InferenceEngine:
    """
    Performs inference using the loaded model.

    This class does NOT:
        - Load models
        - Build prompts
        - Manage conversations

    It only generates responses.
    """

    def __init__(self, model_loader: ModelLoader) -> None:

        self._loader = model_loader

    # ==================================================
    # Generate Response
    # ==================================================

    def generate(
        self,
        messages: list[dict[str, str]]
    ) -> str:
        """
        Generate a response from the language model.

        Parameters
        ----------
        messages
            OpenAI-style chat messages.

        Returns
        -------
        str
            Assistant response.
        """

        if not self._loader.is_loaded:
            raise ModelInferenceError(
                "Model is not loaded."
            )

        logger.info("Starting inference...")

        try:

            response: dict[str, Any] = (
                self._loader.model.create_chat_completion(

                    messages=messages,

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

                    stream=False
                )
            )

            logger.info("Inference completed.")

            return (
                response["choices"][0]
                ["message"]
                ["content"]
                .strip()
            )

        except Exception as error:

            logger.exception(
                "Inference failed."
            )

            raise ModelInferenceError(
                str(error)
            ) from error