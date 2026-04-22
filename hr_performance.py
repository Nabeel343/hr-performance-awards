# ---------------------------------------------
# NUMPY + PANDAS INDUSTRY MINI PROJECT 3(Full Stack Academy)
# HR Performance Awards RnR (Amazon-style metrics)
# Metrics: Accuracy, Productivity, Velocity
# ---------------------------------------------

#-----------------------------------------------
import numpy as np
import pandas as pd


def main():
    print("\n--- HR Performance Awards Project (Metrics Analysis) for monthly RnR(Rewards and recognition) ---\n")

    # ---------------------------------
    # PART 1: Create Employee Dataset
    # ---------------------------------
    data = {
        "Employee": ["Aijaz", "Faisal", "Riya", "Arjun", "Neha","Zainab", "Anwar", "Haroon"],
        "Accuracy": [96, 92, 88, 95, 90,97,98,100],         # percentage
        "Productivity": [85, 80, 78, 88, 82,89,99,99],      # score out of 100
        "Velocity": [70, 75, 68, 80, 72,84,98,72]           # tasks/hour (scaled)
    }

    df = pd.DataFrame(data)

    print("1) Raw Employee Dataset (DataFrame):")
    print(df)

    # ---------------------------------
    # PART 2: Data Inspection
    # ---------------------------------
    print("\n2) Data Preview (head):")
    print(df.head())

    print("\n3) Data Info (structure and types):")
    print(df.info())

    # ---------------------------------
    # PART 3: NumPy Arrays + Stats
    # ---------------------------------
    accuracy_arr = np.array(df["Accuracy"])
    productivity_arr = np.array(df["Productivity"])
    velocity_arr = np.array(df["Velocity"])

    print("\n4) NumPy Arrays created from DataFrame columns:")
    print("Accuracy:", accuracy_arr)
    print("Productivity:", productivity_arr)
    print("Velocity:", velocity_arr)

    print("\n5) Basic NumPy Statistics:")
    print("Average Accuracy:", round(np.mean(accuracy_arr), 2))
    print("Max Productivity:", np.max(productivity_arr))
    print("Min Velocity:", np.min(velocity_arr))

    # ---------------------------------
    # PART 4: Feature Engineering
    # ---------------------------------
    # Simple scoring method for demo:
    # TotalScore = Accuracy + Productivity + Velocity
    df["TotalScore"] = df["Accuracy"] + df["Productivity"] + df["Velocity"]
    df["AverageScore"] = df["TotalScore"] / 3

    print("\n6) New Columns Added (TotalScore, AverageScore):")
    print(df)

    # ---------------------------------
    # PART 5: Award Filtering Logic
    # ---------------------------------
    # Example rule: award candidates if TotalScore > 250
    print("\n7) Award Candidates (TotalScore > 250):")
    award_candidates = df[df["TotalScore"] > 250]
    print(award_candidates)

    # ---------------------------------
    # PART 6: Ranking for Awards
    # ---------------------------------
    print("\n10) Ranking Employees by TotalScore (Top to Bottom):")
    ranked_df = df.sort_values("TotalScore", ascending=False)
    print(ranked_df[["Employee", "TotalScore", "AverageScore"]])

    # Top 1 winner
    top_employee = ranked_df.iloc[0]["Employee"]
    top_score = ranked_df.iloc[0]["TotalScore"]
    print(f"\n11) Award Winner: {top_employee} (TotalScore: {top_score})")

    print("\n--- End of Analysis report(Monthly Rnr) ---\n")


if __name__ == "__main__":
    main()

