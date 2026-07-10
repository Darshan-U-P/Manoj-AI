"""
==========================================================
Manoj AI
startup.py

Application startup sequence.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from llm.model_loader import ModelLoader
from system.logger import logger


class Startup:
    """
    Handles application startup.

    Responsibilities
    ----------------
    - Initialize components
    - Load model
    - Verify startup completed

    Does NOT
    --------
    - Perform inference
    - Manage conversations
    """

    def __init__(self) -> None:

        self._model_loader = ModelLoader()

    # ==================================================
    # Initialize
    # ==================================================

    def initialize(self) -> ModelLoader:
        """
        Initialize the application.

        Returns
        -------
        ModelLoader
            Loaded model loader.
        """

        logger.info("=" * 60)
        logger.info("Starting Manoj AI")
        logger.info("=" * 60)

        self._model_loader.load()

        logger.info("Startup completed successfully.")

        return self._model_loader