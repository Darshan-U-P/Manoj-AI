"""
==========================================================
Manoj AI
model_loader.py

Loads the local GGUF model.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from llama_cpp import Llama

from config.config import config
from system.logger import logger
from system.exceptions import (
    ModelLoadError,
    ModelNotFoundError,
)


class ModelLoader:
    """
    Loads and manages the local language model.

    This class is responsible only for loading the model.
    It does NOT perform inference.
    """

    def __init__(self) -> None:

        self._model: Optional[Llama] = None

    # ==================================================
    # Load Model
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
                    "context_size"
                ),

                n_gpu_layers=config.get(
                    "model",
                    "gpu_layers"
                ),

                n_threads=config.get(
                    "model",
                    "threads"
                ),

                n_batch=config.get(
                    "model",
                    "batch_size"
                ),

                verbose=config.get(
                    "model",
                    "verbose"
                ),

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
    # Unload
    # ==================================================

    def unload(self) -> None:

        logger.info("Unloading model.")

        self._model = None

    # ==================================================
    # Status
    # ==================================================

    @property
    def is_loaded(self) -> bool:

        return self._model is not None

    # ==================================================
    # Getter
    # ==================================================

    @property
    def model(self) -> Llama:

        if self._model is None:

            raise ModelLoadError(
                "Model has not been loaded."
            )

        return self._model