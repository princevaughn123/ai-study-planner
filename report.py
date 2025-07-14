import pandas as pd
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ai_recommend import recommend_next_subject

def generate_weekly_report():
    try:
        df = pd.read_csv("data/study_log.csv")
    except FileNotFoundError:
        print("No study log found.")
        return

    if df.empty:
        print("No data to report.")
        return

    today = datetime.today()
    last_week = today - timedelta(days=7)

    # Filter last 7 days
    df["Date"] = pd.to_datetime(df["Date"])
    recent = df[df["Date"] >= last_week]

    if recent.empty:
        print("No study data in the last 7 days.")
        return

    # Summarize
    total_time = recent["Duration (min)"].sum()
    avg_productivity = recent["Productivity Score (1-10)"].mean()
    top_subject = recent.groupby("Subject")["Duration (min)"].sum().idxmax()
    suggestion = recommend_next_subject()

    # Generate PDF
    filename = "Weekly_Study_Report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(50, 750, "📊 Weekly Study Report")
    c.drawString(50, 720, f"Week Ending: {today.strftime('%Y-%m-%d')}")
    c.drawString(50, 690, f"Total Study Time: {total_time} minutes")
    c.drawString(50, 670, f"Average Productivity: {avg_productivity:.2f}/10")
    c.drawString(50, 650, f"Most Studied Subject: {top_subject}")
    c.drawString(50, 630, f"📌 AI Suggestion: Study more of {suggestion}")

    c.save()
    print(f"✅ Report saved as: {filename}")
