import tkinter as tk
from timer import PomodoroTimer

class StudyDashUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Study Dashboard")
        self.root.geometry("480x360")

        self.timer = PomodoroTimer(root)

        self.timer_frame = self.timer.create_timer_frame()
        self.timer_frame.pack(pady=30)

        self.status_label = tk.Label(
            root, text="Ready", font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyDashUI(root)
    root.mainloop()
