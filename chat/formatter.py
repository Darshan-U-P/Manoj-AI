"""
==========================================================
Manoj AI
formatter.py

Console output formatter.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from colorama import Fore, Style, init

from config.config import config

# Initialize colorama
init(autoreset=True)


class Formatter:
    """
    Formats and prints chat messages.

    Responsibilities
    ----------------
    - Display user messages
    - Display assistant messages
    - Display system messages
    - Display errors

    Does NOT
    --------
    - Store conversations
    - Generate AI responses
    """

    def __init__(self) -> None:

        self._use_color = config.get(
            "console",
            "colored_output"
        )

    # ==================================================
    # Internal Helper
    # ==================================================

    def _color(self, color: str, text: str) -> str:

        if not self._use_color:
            return text

        return color + text + Style.RESET_ALL

    # ==================================================
    # User
    # ==================================================

    def user(self, message: str) -> None:

        print(
            self._color(
                Fore.CYAN,
                f"\nYou: {message}"
            )
        )

    # ==================================================
    # Assistant
    # ==================================================

    def assistant(self, message: str) -> None:

        print(
            self._color(
                Fore.GREEN,
                f"\nManoj: {message}"
            )
        )

    # ==================================================
    # System
    # ==================================================

    def system(self, message: str) -> None:

        print(
            self._color(
                Fore.YELLOW,
                f"\nSystem: {message}"
            )
        )

    # ==================================================
    # Error
    # ==================================================

    def error(self, message: str) -> None:

        print(
            self._color(
                Fore.RED,
                f"\nError: {message}"
            )
        )

    # ==================================================
    # Banner
    # ==================================================

    def banner(self) -> None:

        if not config.get(
            "console",
            "show_banner"
        ):
            return

        print(
            self._color(
                Fore.MAGENTA,
                "=" * 60
            )
        )

        print(
            self._color(
                Fore.MAGENTA,
                "               Manoj AI"
            )
        )

        print(
            self._color(
                Fore.MAGENTA,
                "=" * 60
            )
        )