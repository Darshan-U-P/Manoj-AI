"""
==========================================================
Manoj AI
config.py

Loads, validates and provides application configuration.

Author: Darshan
==========================================================
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from config.constants import SETTINGS_FILE


class Config:
    """
    Central configuration manager.

    Loads settings.json once and provides
    read-only access to configuration values.
    """

    def __init__(self, config_path: Path = SETTINGS_FILE) -> None:
        self._config_path = config_path
        self._data: dict[str, Any] = {}

        self.load()

    # --------------------------------------------------
    # Load Configuration
    # --------------------------------------------------

    def load(self) -> None:
        """
        Load configuration from JSON file.
        """

        if not self._config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found:\n{self._config_path}"
            )

        with open(self._config_path, "r", encoding="utf-8") as file:
            self._data = json.load(file)

    # --------------------------------------------------
    # Reload Configuration
    # --------------------------------------------------

    def reload(self) -> None:
        """
        Reload configuration from disk.
        """

        self.load()

    # --------------------------------------------------
    # Generic Getter
    # --------------------------------------------------

    def get(
        self,
        *keys: str,
        default: Any = None
    ) -> Any:
        """
        Retrieve nested configuration values.

        Example:

        config.get("model", "temperature")

        config.get("logging", "level")
        """

        value = self._data

        for key in keys:

            if not isinstance(value, dict):
                return default

            value = value.get(key)

            if value is None:
                return default

        return value

    # --------------------------------------------------
    # Generic Setter
    # --------------------------------------------------

    def set(
        self,
        *keys: str,
        value: Any
    ) -> None:
        """
        Update configuration in memory.

        Does NOT automatically save to disk.
        """

        data = self._data

        for key in keys[:-1]:

            if key not in data:
                data[key] = {}

            data = data[key]

        data[keys[-1]] = value

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save(self) -> None:
        """
        Save configuration back to settings.json.
        """

        with open(
            self._config_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self._data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    # --------------------------------------------------
    # Properties
    # --------------------------------------------------

    @property
    def data(self) -> dict[str, Any]:
        """
        Return complete configuration.
        """

        return self._data.copy()


# ======================================================
# Singleton
# ======================================================

config = Config()