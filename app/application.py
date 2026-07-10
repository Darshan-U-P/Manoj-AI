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

from llm.inference import InferenceEngine
from llm.tokenizer import Tokenizer

from chat.chat_manager import ChatManager

from system.logger import logger


class Application:
    """
    Main application controller.

    Responsibilities
    ----------------
    - Startup
    - Dependency wiring
    - Chat loop
    - Shutdown

    Does NOT
    --------
    - Perform inference
    - Build prompts
    - Store conversations
    """

    def __init__(self) -> None:

        self._startup = Startup()

        self._shutdown = None

        self._model_loader = None

        self._tokenizer = None

        self._inference = None

        self._chat = None

    # ==================================================
    # Run
    # ==================================================

    def run(self) -> None:
        """
        Run Manoj AI.
        """

        try:

            # ----------------------------------------
            # Startup
            # ----------------------------------------

            self._model_loader = (
                self._startup.initialize()
            )

            # ----------------------------------------
            # Core Components
            # ----------------------------------------

            self._tokenizer = Tokenizer(
                self._model_loader
            )

            self._inference = InferenceEngine(
                self._model_loader
            )

            self._chat = ChatManager(
                self._inference,
                self._tokenizer
            )

            self._shutdown = Shutdown(
                self._model_loader
            )

            logger.info(
                "Application initialized."
            )

            # ----------------------------------------
            # Start Chat
            # ----------------------------------------

            self._chat.run()

        except KeyboardInterrupt:

            logger.info(
                "Interrupted by user."
            )

        except Exception:

            logger.exception(
                "Fatal application error."
            )

        finally:

            if self._shutdown is not None:

                self._shutdown.execute()