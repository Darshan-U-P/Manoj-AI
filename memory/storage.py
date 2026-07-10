"""
==========================================================
Manoj AI
memory/storage.py

Memory storage backend.

Author: Darshan
==========================================================
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime

from memory.models import (
    MemoryEntry,
    MemoryType,
    MemoryCategory,
    MemoryPriority,
)

from system.logger import logger


class MemoryStorage:
    """
    Handles persistent memory storage.

    Responsibilities
    ----------------
    - Load memories
    - Save memories
    - Delete memories
    - Create storage files

    Does NOT
    --------
    - Decide what to remember
    - Search memories
    - Extract memories
    """

    def __init__(
        self,
        file_path: str | Path,
    ) -> None:

        self._path = Path(file_path)

        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._path.exists():

            self.save([])

    # ==================================================
    # Save
    # ==================================================

    def save(
        self,
        memories: list[MemoryEntry],
    ) -> None:

        data = []

        for memory in memories:

            data.append({

                "id": memory.id,

                "content": memory.content,

                "memory_type": memory.memory_type.value,

                "category": memory.category.value,

                "priority": memory.priority.value,

                "created_at": memory.created_at.isoformat(),

                "updated_at": memory.updated_at.isoformat(),

                "access_count": memory.access_count,

                "metadata": memory.metadata,

            })

        with open(
            self._path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        logger.info(
            f"Saved {len(memories)} memories."
        )

    # ==================================================
    # Load
    # ==================================================

    def load(
        self,
    ) -> list[MemoryEntry]:

        with open(
            self._path,
            "r",
            encoding="utf-8",
        ) as file:

            raw = json.load(file)

        memories: list[MemoryEntry] = []

        for item in raw:

            memories.append(

                MemoryEntry(

                    id=item["id"],

                    content=item["content"],

                    memory_type=MemoryType(
                        item["memory_type"]
                    ),

                    category=MemoryCategory(
                        item["category"]
                    ),

                    priority=MemoryPriority(
                        item["priority"]
                    ),

                    created_at=datetime.fromisoformat(
                        item["created_at"]
                    ),

                    updated_at=datetime.fromisoformat(
                        item["updated_at"]
                    ),

                    access_count=item[
                        "access_count"
                    ],

                    metadata=item[
                        "metadata"
                    ],

                )

            )

        logger.info(
            f"Loaded {len(memories)} memories."
        )

        return memories

    # ==================================================
    # Clear
    # ==================================================

    def clear(self) -> None:

        self.save([])

        logger.info(
            "Memory storage cleared."
        )

    # ==================================================
    # Exists
    # ==================================================

    @property
    def exists(self) -> bool:

        return self._path.exists()

    # ==================================================
    # Path
    # ==================================================

    @property
    def path(self) -> Path:

        return self._path