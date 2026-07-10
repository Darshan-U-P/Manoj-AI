"""
==========================================================
Manoj AI
application.py

Main application controller.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from app.startup import Startup
from app.shutdown import Shutdown

from core.container import Container
from core.lifecycle import Lifecycle

from system.logger import logger


class Application:
    """
    Main application controller.

    Responsibilities
    ----------------
    - Coordinate application lifecycle
    - Start services
    - Run chat
    - Shutdown services

    Does NOT
    --------
    - Create dependencies
    - Perform inference
    - Manage conversations
    """

    def __init__(self) -> None:

        self._container = Container()

        self._lifecycle = Lifecycle()

    # ==================================================
    # Run
    # ==================================================

    def run(self) -> None:

        try:

            self._lifecycle.initialize()

            startup: Startup = (
                self._container.startup()
            )

            startup.initialize()

            self._lifecycle.start()

            logger.info(
                "Application initialized."
            )

            chat = (
                self._container.chat_manager()
            )

            chat.run()

        except KeyboardInterrupt:

            logger.info(
                "Interrupted by user."
            )

        except Exception:

            self._lifecycle.error()

            logger.exception(
                "Fatal application error."
            )

        finally:

            self._lifecycle.stopping()

            shutdown: Shutdown = (
                self._container.shutdown()
            )

            shutdown.execute()

            self._lifecycle.stop()