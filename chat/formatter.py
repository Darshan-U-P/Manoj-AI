"""
==========================================================
Manoj AI
formatter.py

Console formatter.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from colorama import (
    Fore,
    Style,
    init,
)

from core.models import Message

from config.config import config

# Initialize Colorama
init(autoreset=True)


class Formatter:
    """
    Formats console output.

    Responsibilities
    ----------------
    - Display messages
    - Display errors
    - Display system messages
    - Display banner

    Does NOT
    --------
    - Manage conversations
    - Generate responses
    """

    def __init__(self) -> None:

        self._use_color = config.get(
            "console",
            "colored_output"
        )

    # ==================================================
    # Internal
    # ==================================================

    def _color(
        self,
        color: str,
        text: str,
    ) -> str:

        if not self._use_color:
            return text

        return color + text + Style.RESET_ALL

    # ==================================================
    # Display Message
    # ==================================================

    def message(
        self,
        message: Message,
    ) -> None:

        role = message.role.lower()

        if role == "user":

            color = Fore.CYAN
            prefix = "You"

        elif role == "assistant":

            color = Fore.GREEN
            prefix = "Manoj"

        elif role == "system":

            color = Fore.YELLOW
            prefix = "System"

        else:

            color = Fore.WHITE
            prefix = role.capitalize()

        print(
            self._color(
                color,
                f"\n{prefix}: {message.content}"
            )
        )

    # ==================================================
    # Error
    # ==================================================

    def error(
        self,
        text: str,
    ) -> None:

        print(
            self._color(
                Fore.RED,
                f"\nError: {text}"
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