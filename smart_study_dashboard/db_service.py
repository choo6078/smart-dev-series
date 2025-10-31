from  __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Optional, List, Tuple

DATA_DIR = Path(__file__).with_name("data")
DEFAULT_DB = DATA_DIR / "study_data.db"

def _connect(db_path: Optional[Path] = None) -> sqlite3.Connection:
    DATA_DIR.mkdir(exist_ok=True)
    db = (db_path or DEFAULT_DB)
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: Optional[Path] = None) -> None:
    with _connect(db_path) as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS sessions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        duration_sec INTEGER NOT NULL,
                        task TEXT,
                        category TEXT
                     );
                     """)
        conn.commit()

def insert_session(
        date_str: str,
        duration_sec: int,
        task: Optional[str] = None,
        category: Optional[str] = None,
        db_path: Optional[Path] = None
) -> None:
    
    with _connect(db_path) as conn:
        conn.execute(
            "INSERT INTO sessions (date, duration_sec, task, category) VALUES (?, ?, ?, ?)",
            (date_str, duration_sec, task, category)
        )
        conn.commit()

def fetch_sessions(
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        db_path: Optional[Path] = None
) -> List[sqlite3.Row]:
    
    query = "SELECT * FROM sessions"
    conds, params = [], []
    if date_from:
        conds.append("data >= ?"); params.append(date_from)
    if date_to:
        conds.append("data <= ?"); params.append(date_to)
    if conds:
        query += " WHERE " + " AND ".join(conds)
    query += " ORDER BY date DESC, id DESC"

    with _connect(db_path) as conn:
        rows = conn.execute(query, params).fetchall()
        return list(rows)
    
def fetch_daily_totals(
        week_start: str,
        week_end: str,
        db_path: Optional[Path] = None
) -> List[Tuple[str, int]]:
    sql = """
    SELECT date, SUM(duration_sec) AS total_sec
    FROM sessions
    WHERE date BETWEEN ? AND ?
    GROUP BY date
    ORDER BY date ASC
    """
    with _connect(db_path) as conn:
        rows = conn.execute(sql, (week_start, week_end)).fetchall()
        return [(r["date"], int(r["total_sec"])) for r in rows]