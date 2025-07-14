import pandas as pd
import matplotlib.pyplot as plt

def analyze_study_data():
    try:
        df = pd.read_csv("data/study_log.csv")

        if df.empty:
            print("No data to analyze yet.")
            return

        # Group by subject and sum duration
        subject_totals = df.groupby("Subject")["Duration (min)"].sum()

        # Average productivity
        avg_productivity = df["Productivity Score (1-10)"].mean()

        print(f"\n📊 Total Time Spent Per Subject:\n{subject_totals}")
        print(f"\n🧠 Average Productivity Score: {avg_productivity:.2f}/10")

        # Plot the graph
        subject_totals.plot(kind="bar", title="Total Study Time per Subject", ylabel="Minutes")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Study log not found. Try logging some sessions first!")

if __name__ == "__main__":
    analyze_study_data()
