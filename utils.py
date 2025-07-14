import pandas as pd
from datetime import datetime

def log_study_session(subject, duration, productivity_score):
    # Create a new entry with the current date and user input
    entry = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Subject": subject,
        "Duration (min)": duration,
        "Productivity Score (1-10)": productivity_score
    }

    try:
        # Try to load the existing CSV file
        df = pd.read_csv("data/study_log.csv")
        # Add new entry to the existing dataframe
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    except FileNotFoundError:
        # If file doesn't exist, create a new dataframe
        df = pd.DataFrame([entry])

    # Save updated data back to CSV
    df.to_csv("data/study_log.csv", index=False)
    print("✅ Study session logged.")
