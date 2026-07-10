"""
==========================================================
Manoj AI
exceptions.py

Custom exception hierarchy.

Author: Darshan
==========================================================
"""


# ==========================================================
# Base Exception
# ==========================================================

class ManojAIError(Exception):
    """
    Base exception for the Manoj AI project.

    Every custom exception should inherit from this class.
    """

    pass


# ==========================================================
# Configuration
# ==========================================================

class ConfigurationError(ManojAIError):
    """Raised when configuration loading or validation fails."""
    pass


class MissingConfigurationError(ConfigurationError):
    """Raised when a required configuration value is missing."""
    pass


class InvalidConfigurationError(ConfigurationError):
    """Raised when configuration values are invalid."""
    pass


# ==========================================================
# Model
# ==========================================================

class ModelError(ManojAIError):
    """Base model exception."""
    pass


class ModelNotFoundError(ModelError):
    """Raised when the model file cannot be located."""
    pass


class ModelLoadError(ModelError):
    """Raised when the model fails to load."""
    pass


class ModelInferenceError(ModelError):
    """Raised when inference fails."""
    pass


# ==========================================================
# Chat
# ==========================================================

class ChatError(ManojAIError):
    """Base chat exception."""
    pass


class PromptError(ChatError):
    """Raised when prompt creation fails."""
    pass


class ConversationError(ChatError):
    """Raised when conversation handling fails."""
    pass


# ==========================================================
# Logging
# ==========================================================

class LoggingError(ManojAIError):
    """Raised when the logging system fails."""
    pass


# ==========================================================
# File System
# ==========================================================

class FileSystemError(ManojAIError):
    """Base file system exception."""
    pass


class FileReadError(FileSystemError):
    """Raised when reading a file fails."""
    pass


class FileWriteError(FileSystemError):
    """Raised when writing a file fails."""
    pass


# ==========================================================
# Runtime
# ==========================================================

class StartupError(ManojAIError):
    """Raised during application startup."""
    pass


class ShutdownError(ManojAIError):
    """Raised during application shutdown."""
    pass


class InitializationError(ManojAIError):
    """Raised when a component fails to initialize."""
    pass