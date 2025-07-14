import pandas as pd

def recommend_next_subject():
    try:
        df = pd.read_csv("data/study_log.csv")

        if df.empty:
            print("Not enough data to make a recommendation yet.")
            return "Not enough data."

        # Group by subject
        subject_stats = df.groupby("Subject").agg({
            "Duration (min)": "sum",
            "Productivity Score (1-10)": "mean"
        })

        # Calculate a score: less studied + lower productivity = higher priority
        subject_stats["Priority Score"] = (
            (subject_stats["Productivity Score (1-10)"].max() - subject_stats["Productivity Score (1-10)"])
            + (subject_stats["Duration (min)"].max() - subject_stats["Duration (min)"])
        )

        recommended = subject_stats["Priority Score"].idxmax()

        print(f"📚 Recommended Subject to Study Next: {recommended}")
        return recommended

    except FileNotFoundError:
        print("Study log not found.")
        return "No data found."
