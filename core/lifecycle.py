"""
==========================================================
Manoj AI
lifecycle.py

Application lifecycle definitions.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


# ==========================================================
# Application State
# ==========================================================

class ApplicationState(Enum):
    """
    Represents the current state of the application.
    """

    CREATED = auto()

    INITIALIZING = auto()

    RUNNING = auto()

    PAUSED = auto()

    STOPPING = auto()

    STOPPED = auto()

    ERROR = auto()


# ==========================================================
# Lifecycle
# ==========================================================

@dataclass(slots=True)
class Lifecycle:

    """
    Tracks the current application lifecycle.
    """

    state: ApplicationState = ApplicationState.CREATED

    started_at: datetime | None = None

    stopped_at: datetime | None = None

    # ------------------------------------------------------

    def initialize(self) -> None:

        self.state = ApplicationState.INITIALIZING

    # ------------------------------------------------------

    def start(self) -> None:

        self.state = ApplicationState.RUNNING

        self.started_at = datetime.now()

    # ------------------------------------------------------

    def pause(self) -> None:

        self.state = ApplicationState.PAUSED

    # ------------------------------------------------------

    def resume(self) -> None:

        self.state = ApplicationState.RUNNING

    # ------------------------------------------------------

    def stop(self) -> None:

        self.state = ApplicationState.STOPPED

        self.stopped_at = datetime.now()

    # ------------------------------------------------------

    def stopping(self) -> None:

        self.state = ApplicationState.STOPPING

    # ------------------------------------------------------

    def error(self) -> None:

        self.state = ApplicationState.ERROR

    # ------------------------------------------------------

    @property
    def is_running(self) -> bool:

        return self.state == ApplicationState.RUNNING

    # ------------------------------------------------------

    @property
    def is_stopped(self) -> bool:

        return self.state == ApplicationState.STOPPED

    # ------------------------------------------------------

    @property
    def has_error(self) -> bool:

        return self.state == ApplicationState.ERROR