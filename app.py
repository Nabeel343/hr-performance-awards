
# -----------------------------------------------------------
# HR Performance Awards Dashboard
# NumPy + Pandas + Streamlit
# Metrics: Accuracy, Productivity, Velocity
# -----------------------------------------------------------

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# -----------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------

st.set_page_config(
    page_title="HR Performance Awards",
    page_icon="🏆",
    layout="wide"
)


# -----------------------------------------------------------
# DATASET
# -----------------------------------------------------------

data = {
    "Employee": [
        "Aijaz", "Faisal", "Riya", "Arjun",
        "Neha", "Zainab", "Anwar", "Haroon"
    ],
    "Accuracy": [96, 92, 88, 95, 90, 97, 98, 100],
    "Productivity": [85, 80, 78, 88, 82, 89, 99, 99],
    "Velocity": [70, 75, 68, 80, 72, 84, 98, 72]
}

df = pd.DataFrame(data)


# -----------------------------------------------------------
# FEATURE ENGINEERING
# -----------------------------------------------------------

df["TotalScore"] = (
    df["Accuracy"]
    + df["Productivity"]
    + df["Velocity"]
)

df["AverageScore"] = df["TotalScore"] / 3

ranked_df = df.sort_values(
    "TotalScore",
    ascending=False
).reset_index(drop=True)

ranked_df["Rank"] = ranked_df.index + 1

award_candidates = ranked_df[
    ranked_df["TotalScore"] > 250
]


# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------

st.title("🏆 HR Performance Awards Dashboard")

st.markdown(
    """
    **Monthly Rewards & Recognition (RnR) Analysis**

    This dashboard evaluates employee performance using three
    key metrics: **Accuracy, Productivity, and Velocity**.
    """
)

st.divider()


# -----------------------------------------------------------
# KEY PERFORMANCE METRICS
# -----------------------------------------------------------

average_accuracy = round(np.mean(df["Accuracy"]), 2)
max_productivity = int(np.max(df["Productivity"]))
min_velocity = int(np.min(df["Velocity"]))

top_employee = ranked_df.iloc[0]["Employee"]
top_score = int(ranked_df.iloc[0]["TotalScore"])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📊 Average Accuracy",
        f"{average_accuracy}%"
    )

with col2:
    st.metric(
        "⚡ Max Productivity",
        f"{max_productivity}/100"
    )

with col3:
    st.metric(
        "🏃 Min Velocity",
        f"{min_velocity}"
    )

with col4:
    st.metric(
        "🏆 Top Performer",
        top_employee
    )


st.divider()


# -----------------------------------------------------------
# AWARD WINNER
# -----------------------------------------------------------

st.subheader("🥇 Monthly Award Winner")

winner_col1, winner_col2 = st.columns(2)

with winner_col1:
    st.success(
        f"🏆 **{top_employee}** is the top performer!"
    )

with winner_col2:
    st.metric(
        "Total Performance Score",
        top_score
    )


# -----------------------------------------------------------
# EMPLOYEE PERFORMANCE TABLE
# -----------------------------------------------------------

st.subheader("👥 Employee Performance")

display_df = ranked_df[
    [
        "Rank",
        "Employee",
        "Accuracy",
        "Productivity",
        "Velocity",
        "TotalScore",
        "AverageScore"
    ]
].copy()

display_df["AverageScore"] = display_df[
    "AverageScore"
].round(2)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# -----------------------------------------------------------
# AWARD CANDIDATES
# -----------------------------------------------------------

st.subheader("🏅 Award Candidates")

st.write(
    "Employees with a **Total Score greater than 250** "
    "qualify for monthly recognition."
)

candidate_df = award_candidates[
    [
        "Rank",
        "Employee",
        "Accuracy",
        "Productivity",
        "Velocity",
        "TotalScore",
        "AverageScore"
    ]
].copy()

candidate_df["AverageScore"] = candidate_df[
    "AverageScore"
].round(2)

st.dataframe(
    candidate_df,
    use_container_width=True,
    hide_index=True
)


st.divider()


# -----------------------------------------------------------
# EMPLOYEE SEARCH
# -----------------------------------------------------------

st.subheader("🔎 Employee Performance Details")

selected_employee = st.selectbox(
    "Select an employee",
    df["Employee"].tolist()
)

employee_data = df[
    df["Employee"] == selected_employee
].iloc[0]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Accuracy",
        f"{employee_data['Accuracy']}%"
    )

with c2:
    st.metric(
        "Productivity",
        f"{employee_data['Productivity']}"
    )

with c3:
    st.metric(
        "Velocity",
        f"{employee_data['Velocity']}"
    )

with c4:
    st.metric(
        "Total Score",
        int(employee_data["TotalScore"])
    )


# -----------------------------------------------------------
# PERFORMANCE CHART
# -----------------------------------------------------------

st.subheader("📈 Employee Performance Comparison")

chart_df = df.set_index("Employee")[
    ["Accuracy", "Productivity", "Velocity"]
]

st.bar_chart(chart_df)


# -----------------------------------------------------------
# TOTAL SCORE CHART
# -----------------------------------------------------------

st.subheader("🏆 Total Performance Score")

fig, ax = plt.subplots()

ax.bar(
    ranked_df["Employee"],
    ranked_df["TotalScore"]
)

ax.set_xlabel("Employee")
ax.set_ylabel("Total Score")
ax.set_title("Employee Total Performance Score")

plt.xticks(rotation=45)

st.pyplot(fig)


# -----------------------------------------------------------
# NUMPY STATISTICS
# -----------------------------------------------------------

st.subheader("🧮 Performance Statistics")

stat_col1, stat_col2, stat_col3 = st.columns(3)

with stat_col1:
    st.write("**Average Accuracy**")
    st.write(
        f"{np.mean(df['Accuracy']):.2f}%"
    )

with stat_col2:
    st.write("**Maximum Productivity**")
    st.write(
        int(np.max(df["Productivity"]))
    )

with stat_col3:
    st.write("**Minimum Velocity**")
    st.write(
        int(np.min(df["Velocity"]))
    )


# -----------------------------------------------------------
# DOWNLOAD REPORT
# -----------------------------------------------------------

st.subheader("📥 Download Performance Report")

csv_data = display_df.to_csv(index=False)

st.download_button(
    label="Download Employee Report",
    data=csv_data,
    file_name="hr_performance_awards_report.csv",
    mime="text/csv"
)


# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------

st.divider()

st.caption(
    "HR Performance Awards | "
    "NumPy + Pandas + Streamlit | "
    "Monthly Rewards & Recognition Analysis"
)
```
