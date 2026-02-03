from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable

DEFAULT_DB_PATH = Path.home() / ".invest-record" / "invest.db"

SCHEMA_STATEMENTS: Iterable[str] = (
    """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset TEXT NOT NULL,
        txn_type TEXT NOT NULL,
        quantity REAL NOT NULL,
        price REAL NOT NULL,
        currency TEXT NOT NULL,
        traded_at TEXT NOT NULL,
        notes TEXT
    )
    """,
)


def resolve_db_path(db_path: str | None) -> Path:
    if db_path:
        return Path(db_path).expanduser().resolve()
    return DEFAULT_DB_PATH


def connect(db_path: str | None = None) -> sqlite3.Connection:
    path = resolve_db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_schema(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()
    for statement in SCHEMA_STATEMENTS:
        cursor.execute(statement)
    connection.commit()
