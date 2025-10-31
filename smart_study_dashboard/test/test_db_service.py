from pathlib import Path
from ..db_service import init_db, insert_session, fetch_sessions, fetch_daily_totals

def test_insert_and_fetch(tmp_path):
    db_path = tmp_path / "test.db"

    init_db(db_path)

    insert_session("2025-10-31", 1500, "Pomodoro #1", "Study", db_path)
    insert_session("2025-10-31", 600, "Quick review", "Study", db_path)

    rows = fetch_sessions(db_path=db_path)

    assert len(rows) == 2
    durations = {row["duration_sec"] for row in rows}
    assert {1500, 600}.issubset(durations)

def test_weekly_totals(tmp_path):
    db_path = tmp_path / "test.db"

    init_db(db_path)

    insert_session("2025-10-27", 1200, "Day1", "Study", db_path)
    insert_session("2025-10-29", 1800, "Day3", "Study", db_path)
    insert_session("2025-10-29", 600, "Day3", "Study", db_path)

    totals = fetch_daily_totals("2025-10-27", "2025-11-02", db_path)
    totals_dict = dict(totals)

    assert totals_dict["2025-10-29"] == 2400

    assert totals_dict["2025-10-27"] == 1200
    