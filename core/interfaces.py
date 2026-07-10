"""
==========================================================
Manoj AI
interfaces.py

Abstract interfaces used throughout the project.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.models import (
    ChatRequest,
    ChatResponse,
)


# ==========================================================
# Language Model
# ==========================================================

class LLMInterface(ABC):
    """
    Base interface for every language model.
    """

    @abstractmethod
    def load(self) -> None:
        """
        Load the model.
        """
        raise NotImplementedError

    @abstractmethod
    def unload(self) -> None:
        """
        Unload the model.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        request: ChatRequest
    ) -> ChatResponse:
        """
        Generate a response.
        """
        raise NotImplementedError


# ==========================================================
# Memory
# ==========================================================

class MemoryInterface(ABC):
    """
    Base memory interface.
    """

    @abstractmethod
    def store(self, text: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        query: str
    ) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError


# ==========================================================
# User Interface
# ==========================================================

class UIInterface(ABC):
    """
    Base UI interface.
    """

    @abstractmethod
    def show_user(
        self,
        text: str
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_assistant(
        self,
        text: str
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_system(
        self,
        text: str
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_error(
        self,
        text: str
    ) -> None:
        raise NotImplementedError


# ==========================================================
# Voice
# ==========================================================

class VoiceInterface(ABC):
    """
    Base voice engine.
    """

    @abstractmethod
    def listen(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def speak(
        self,
        text: str
    ) -> None:
        raise NotImplementedError


# ==========================================================
# Vision
# ==========================================================

class VisionInterface(ABC):
    """
    Base vision engine.
    """

    @abstractmethod
    def analyze(
        self,
        image_path: str
    ) -> str:
        raise NotImplementedError


# ==========================================================
# Plugin
# ==========================================================

class PluginInterface(ABC):
    """
    Base plugin.
    """

    @abstractmethod
    def initialize(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        raise NotImplementedError


# ==========================================================
# Tool
# ==========================================================

class ToolInterface(ABC):
    """
    Base tool.
    """

    @abstractmethod
    def execute(
        self,
        *args,
        **kwargs
    ):
        raise NotImplementedError