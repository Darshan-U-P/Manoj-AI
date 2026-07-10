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
    - Validate startup
    - Initialize services
    - Load the language model

    Does NOT
    --------
    - Create dependencies
    - Manage conversations
    - Perform inference
    """

    def __init__(
        self,
        model_loader: ModelLoader,
    ) -> None:

        self._loader = model_loader

    # ==================================================
    # Initialize
    # ==================================================

    def initialize(self) -> None:
        """
        Initialize the application.
        """

        logger.info("=" * 60)
        logger.info("Starting Manoj AI")
        logger.info("=" * 60)

        if not self._loader.is_loaded:
            self._loader.load()

        logger.info(
            "Startup completed successfully."
        )