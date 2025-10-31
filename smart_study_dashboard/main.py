import tkinter as tk
from ui import StudyDashUI
from datetime import datetime
from db_service import init_db, insert_session

init_db()

def on_timer_finished(elapsed_seconds: int, task_name: str | None = None, category: str | None = None) -> None:

    today = datetime.now().strftime("%Y-%m-%d")
    insert_session(today, elapsed_seconds, task_name, category)
    print(f"[DB] 세션 저장 완료 | {today=} {elapsed_seconds=} {task_name=} {categor=}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyDashUI(root)
    root.mainloop()
