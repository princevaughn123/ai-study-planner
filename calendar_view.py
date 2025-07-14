import pandas as pd
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

def show_study_details(date, df):
    selected = df[df["Date"] == date]
    if selected.empty:
        messagebox.showinfo("No Study", f"No study sessions on {date}")
    else:
        message = "\n".join([
            f"{row['Subject']} – {row['Duration (min)']} min (Score: {row['Productivity Score (1-10)']})"
            for _, row in selected.iterrows()
        ])
        messagebox.showinfo(f"📚 Sessions on {date}", message)

def open_calendar():
    try:
        df = pd.read_csv("data/study_log.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "No study log found.")
        return

    root = tk.Tk()
    root.title("📅 Study Calendar")
    root.geometry("300x300")

    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)

    def on_date_select():
        date = cal.get_date()
        show_study_details(date, df)

    tk.Button(root, text="View Logs", command=on_date_select).pack(pady=10)

    root.mainloop()
