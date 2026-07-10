"""
==========================================================
Manoj AI
constants.py

Application-wide immutable constants.

Do NOT place configurable values here.
User-configurable settings belong in settings.json.
==========================================================
"""

from pathlib import Path

# ==========================================================
# Application Information
# ==========================================================

APP_NAME: str = "Manoj AI"
APP_VERSION: str = "0.1.0"
APP_AUTHOR: str = "Darshan"

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

# ==========================================================
# Directories
# ==========================================================

CONFIG_DIR: Path = PROJECT_ROOT / "config"

MODELS_DIR: Path = PROJECT_ROOT / "models"

BASE_MODELS_DIR: Path = MODELS_DIR / "base"

LORA_MODELS_DIR: Path = MODELS_DIR / "loras"

TOKENIZER_DIR: Path = MODELS_DIR / "tokenizer"

LOGS_DIR: Path = PROJECT_ROOT / "logs"

TESTS_DIR: Path = PROJECT_ROOT / "tests"

# ==========================================================
# Files
# ==========================================================

SETTINGS_FILE: Path = CONFIG_DIR / "settings.json"

LOG_FILE: Path = LOGS_DIR / "manoj.log"

# ==========================================================
# Logging
# ==========================================================

LOG_FORMAT: str = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)

DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

# ==========================================================
# Supported Model Formats
# ==========================================================

SUPPORTED_MODEL_EXTENSIONS = (
    ".gguf",
)

SUPPORTED_LORA_EXTENSIONS = (
    ".gguf",
)

# ==========================================================
# Console
# ==========================================================

SEPARATOR = "=" * 70

WELCOME_MESSAGE = """
==========================================
        Welcome to Manoj AI
==========================================
"""

EXIT_COMMANDS = (
    "exit",
    "quit",
    "bye",
)

# ==========================================================
# Environment
# ==========================================================

DEFAULT_ENCODING = "utf-8"

JSON_INDENT = 4