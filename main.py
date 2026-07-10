"""
==========================================================
Manoj AI

Entry Point

Author: Darshan
==========================================================
"""

from __future__ import annotations

from app.application import Application


def main() -> None:
    """
    Application entry point.
    """

    app = Application()

    app.run()


if __name__ == "__main__":

    main()