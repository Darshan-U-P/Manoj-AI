"""
==========================================================
Manoj AI
model_loader.py

Loads and manages the local language model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from llama_cpp import Llama

from config.config import config
from core.interfaces import LLMInterface
from core.models import (
    ChatRequest,
    ChatResponse,
    Message,
    ModelInfo,
)
from system.exceptions import (
    ModelLoadError,
    ModelNotFoundError,
)
from system.logger import logger


class ModelLoader(LLMInterface):
    """
    Loads and manages the language model.

    Responsibilities
    ----------------
    - Load model
    - Unload model
    - Hold model information

    Does NOT
    --------
    - Build prompts
    - Manage conversations
    - Handle UI
    """

    def __init__(self) -> None:

        self._model: Optional[Llama] = None

        self._info = ModelInfo(
            name="",
            path="",
            context_size=0,
            gpu_layers=0,
            loaded=False,
        )

    # ==================================================
    # Load
    # ==================================================

    def load(self) -> None:

        model_path = Path(
            config.get("model", "path")
        )

        if not model_path.exists():
            raise ModelNotFoundError(
                f"Model not found:\n{model_path}"
            )

        logger.info("Loading language model...")

        try:

            self._model = Llama(
                model_path=str(model_path),
                n_ctx=config.get(
                    "model",
                    "context_size",
                ),
                n_gpu_layers=config.get(
                    "model",
                    "gpu_layers",
                ),
                n_threads=config.get(
                    "model",
                    "threads",
                ),
                n_batch=config.get(
                    "model",
                    "batch_size",
                ),
                verbose=config.get(
                    "model",
                    "verbose",
                ),
            )

            self._info = ModelInfo(
                name=model_path.stem,
                path=str(model_path),
                context_size=config.get(
                    "model",
                    "context_size",
                ),
                gpu_layers=config.get(
                    "model",
                    "gpu_layers",
                ),
                loaded=True,
            )

            logger.info("Model loaded successfully.")

        except Exception as error:

            logger.exception(
                "Failed to load model."
            )

            raise ModelLoadError(
                str(error)
            ) from error

    # ==================================================
    # Generate
    # ==================================================

    def generate(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Generate a response from the model.

        NOTE:
        In Phase 0.5 this method simply delegates to
        llama.cpp. Advanced generation remains in
        InferenceEngine.
        """

        if self._model is None:
            raise ModelLoadError(
                "Model has not been loaded."
            )

        response = self._model.create_chat_completion(
            messages=[
                message.to_dict()
                for message in request.messages
            ]
        )

        text = (
            response["choices"][0]
            ["message"]
            ["content"]
            .strip()
        )

        return ChatResponse(
            message=Message(
                role="assistant",
                content=text,
            )
        )

    # ==================================================
    # Unload
    # ==================================================

    def unload(self) -> None:

        logger.info("Unloading model.")

        self._model = None

        self._info.loaded = False

    # ==================================================
    # Properties
    # ==================================================

    @property
    def model(self) -> Llama:

        if self._model is None:
            raise ModelLoadError(
                "Model has not been loaded."
            )

        return self._model

    @property
    def info(self) -> ModelInfo:
        return self._info

    @property
    def is_loaded(self) -> bool:
        return self._info.loaded