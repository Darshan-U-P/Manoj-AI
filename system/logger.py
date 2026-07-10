"""
==========================================================
Manoj AI
logger.py

Central logging system.

Author: Darshan
==========================================================
"""

from __future__ import annotations

import logging
from pathlib import Path

from config.config import config
from config.constants import (
    LOG_FILE,
    LOG_FORMAT,
    DATE_FORMAT,
)


class Logger:
    """
    Central logger for Manoj AI.

    Features:
    - Console logging
    - File logging
    - Configurable log level
    - Singleton instance
    """

    def __init__(self) -> None:

        self._logger = logging.getLogger("ManojAI")

        if self._logger.handlers:
            return

        self._logger.setLevel(
            getattr(
                logging,
                config.get("logging", "level", default="INFO").upper()
            )
        )

        formatter = logging.Formatter(
            fmt=LOG_FORMAT,
            datefmt=DATE_FORMAT
        )

        # ----------------------------------------
        # Console Handler
        # ----------------------------------------

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self._logger.addHandler(console_handler)

        # ----------------------------------------
        # File Handler
        # ----------------------------------------

        if config.get("logging", "save_to_file"):

            Path(LOG_FILE).parent.mkdir(
                parents=True,
                exist_ok=True
            )

            file_handler = logging.FileHandler(
                LOG_FILE,
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            self._logger.addHandler(file_handler)

        self._logger.propagate = False

    # ==================================================
    # Public Logging Methods
    # ==================================================

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def critical(self, message: str) -> None:
        self._logger.critical(message)

    def exception(self, message: str) -> None:
        self._logger.exception(message)


# ==========================================================
# Singleton Logger
# ==========================================================

logger = Logger()