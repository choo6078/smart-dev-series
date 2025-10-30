import tkinter as tk
from smart_study_dashboard.timer import PomodoroTimer

def test_timer_initial_state():
    root = tk.Tk()
    timer = PomodoroTimer(root, minutes=25)
    assert timer.time_left == 25 * 60
    assert timer.is_running is False
    root.destroy()