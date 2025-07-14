import tkinter as tk
from tkinter import messagebox
from utils import log_study_session
from analyze import analyze_study_data
from ai_recommend import recommend_next_subject
from calendar_view import open_calendar
from report import generate_weekly_report

# === Colors & Fonts ===
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#3a3a3a"
FONT = ("Segoe UI", 10)

# === Submit function ===
def submit_form():
    subject = subject_entry.get()
    try:
        duration = int(duration_entry.get())
        productivity = int(productivity_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Duration and Productivity must be numbers.")
        return

    if not (1 <= productivity <= 10):
        messagebox.showerror("Error", "Productivity must be between 1 and 10.")
        return

    log_study_session(subject, duration, productivity)
    messagebox.showinfo("Success", "Study session logged!")
    subject_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    productivity_entry.delete(0, tk.END)

def show_recommendation():
    subject = recommend_next_subject()
    messagebox.showinfo("🤖 AI Suggestion", f"You should study: {subject}")

# === Window setup ===
root = tk.Tk()
root.title("AI Study Planner")
root.configure(bg=BG_COLOR)
root.resizable(False, False)
root.geometry("400x400")

# === Labels & Entries ===
tk.Label(root, text="Subject:", fg=FG_COLOR, bg=BG_COLOR, font=FONT).pack(pady=(10, 0))
subject_entry = tk.Entry(root, font=FONT, bg=BTN_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
subject_entry.pack(padx=20, pady=5, fill="x")

tk.Label(root, text="Duration (minutes):", fg=FG_COLOR, bg=BG_COLOR, font=FONT).pack()
duration_entry = tk.Entry(root, font=FONT, bg=BTN_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
duration_entry.pack(padx=20, pady=5, fill="x")

tk.Label(root, text="Productivity (1-10):", fg=FG_COLOR, bg=BG_COLOR, font=FONT).pack()
productivity_entry = tk.Entry(root, font=FONT, bg=BTN_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
productivity_entry.pack(padx=20, pady=5, fill="x")

# === Buttons ===
tk.Button(root, text="✅ Log Session", command=submit_form, font=FONT, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=10, fill="x", padx=50)
tk.Button(root, text="📊 View Progress", command=analyze_study_data, font=FONT, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=5, fill="x", padx=50)
tk.Button(root, text="🤖 What Should I Study?", command=show_recommendation, font=FONT, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=5, fill="x", padx=50)
tk.Button(root, text="🗓️ View Calendar", command=open_calendar, font=FONT, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=5, fill="x", padx=50)
tk.Button(root, text="📄 Generate Weekly Report", command=generate_weekly_report, font=FONT, bg=BTN_COLOR, fg=FG_COLOR).pack(pady=5, fill="x", padx=50)

# === Enter Key Binding ===
root.bind('<Return>', lambda event: submit_form())

# === Run ===
root.mainloop()
