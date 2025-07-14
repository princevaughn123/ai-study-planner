from utils import log_study_session

def main():
    print("🧠 AI Study Planner – CLI Mode")
    subject = input("What subject did you study? ")
    
    # Validate that duration is a number
    while True:
        try:
            duration = int(input("How many minutes did you study? "))
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    # Validate that productivity is between 1–10
    while True:
        try:
            productivity = int(input("Rate your productivity (1-10): "))
            if 1 <= productivity <= 10:
                break
            else:
                print("❌ Enter a number between 1 and 10.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # Log it
    log_study_session(subject, duration, productivity)

if __name__ == "__main__":
    main()
