"""
==========================================================
Manoj AI
shutdown.py

Application shutdown sequence.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from llm.model_loader import ModelLoader

from system.logger import logger


class Shutdown:
    """
    Handles application shutdown.

    Responsibilities
    ----------------
    - Release resources
    - Unload model
    - Cleanup

    Does NOT
    --------
    - Create dependencies
    - Manage chat
    - Perform inference
    """

    def __init__(
        self,
        model_loader: ModelLoader,
    ) -> None:

        self._loader = model_loader

    # ==================================================
    # Execute
    # ==================================================

    def execute(self) -> None:

        logger.info("=" * 60)
        logger.info("Shutting down Manoj AI")

        if self._loader.is_loaded:

            self._loader.unload()

        logger.info(
            "Cleanup completed."
        )

        logger.info("Goodbye!")

        logger.info("=" * 60)