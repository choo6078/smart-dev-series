import tkinter as tk
import time
from .db_service import insert_session
from datetime import datetime

class PomodoroTimer:
    def __init__(self, root: tk.Tk, minutes: int = 1):
        self.root = root
        self.is_running = False
        self.total_seconds = minutes * 60
        self.time_left = self.total_seconds
        self.sessions_duration = self.total_seconds
        self._tick_job = None

        self.label = None
        self._btn_start = None
        self._btn_pause = None
        self._btn_reset = None

    def create_timer_frame(self) -> tk.Frame:
        frame = tk.Frame(self.root)

        self.label = tk.Label(frame, text=self.format_time(self.time_left), font=("Arial", 36))
        self.label.pack()

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        self._btn_start = tk.Button(btn_frame, text="Start", command=self.start_timer)
        self._btn_start.pack(side="left", padx=5)

        self._btn_pause = tk.Button(btn_frame, text="Pause", command=self.pause_timer)
        self._btn_pause.pack(side="left", padx=5)

        self._btn_reset = tk.Button(btn_frame, text="Reset", command=self.reset_timer)
        self._btn_reset.pack(side="left", padx=5)

        return frame

    @staticmethod
    def format_time(seconds: int) -> str:
        m, s = divmod(seconds, 60)
        return f"{m:02d}:{s:02d}"

    def _schedule_next_tick(self):
        self._tick_job = self.root.after(1000, self.update_timer)

    def update_timer(self):
        if not self.is_running:
            return

        if self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time(self.time_left))
            self._schedule_next_tick()
        else:
            self.label.config(text="Time's up!")
            self.is_running = False
            self._tick_job = None

            today = datetime.now().strftime("%Y-%m-%d")

            elapsed = self.sessions_duration - self.time_left
            insert_session(today, max(elapsed, 0), task="집중 세션", category="공부")
            print("[DB] 공부 기록 저장 완료")

    def start_timer(self):
        if self.is_running:
            return

        self.is_running = True
        if self.time_left <= 0:
            self.time_left = self.total_seconds
            self.label.config(text=self.format_time(self.time_left))
        self._schedule_next_tick()

    def pause_timer(self):
        self.is_running = False
        if self._tick_job is not None:
            try:
                self.root.after_cancel(self._tick_job)
            finally:
                self._tick_job = None

    def reset_timer(self):
        self.pause_timer()
        self.time_left = self.total_seconds
        if self.label is not None:
            self.label.config(text=self.format_time(self.time_left))
