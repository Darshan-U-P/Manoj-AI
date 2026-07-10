"""
==========================================================
Manoj AI
models.py

Core data models shared across the application.

Author: Darshan
==========================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


# ==========================================================
# Message
# ==========================================================

@dataclass(slots=True)
class Message:
    """
    Represents a single chat message.
    """

    role: str
    content: str

    timestamp: datetime = field(
        default_factory=datetime.now
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # --------------------------------------------------

    def to_dict(self) -> dict[str, str]:
        """
        Convert to OpenAI/llama.cpp format.
        """

        return {
            "role": self.role,
            "content": self.content
        }


# ==========================================================
# Chat Request
# ==========================================================

@dataclass(slots=True)
class ChatRequest:
    """
    Request sent to the inference engine.
    """

    messages: list[Message]


# ==========================================================
# Chat Response
# ==========================================================

@dataclass(slots=True)
class ChatResponse:
    """
    Response returned by the inference engine.
    """

    message: Message


# ==========================================================
# Generation Configuration
# ==========================================================

@dataclass(slots=True)
class GenerationConfig:
    """
    Runtime generation settings.
    """

    temperature: float

    top_p: float

    top_k: int

    max_tokens: int

    repeat_penalty: float


# ==========================================================
# Model Information
# ==========================================================

@dataclass(slots=True)
class ModelInfo:
    """
    Information about the loaded model.
    """

    name: str

    path: str

    context_size: int

    gpu_layers: int

    loaded: bool = False