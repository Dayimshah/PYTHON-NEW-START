
import pandas as pd
import numpy as np

# 🧾 Step 1: Load the dataset


# We tell pandas to read the file
data = pd.read_csv("covid_data.csv")
# This helps us work with dates more easily
data["Date"] = pd.to_datetime(data["Date"])

 Look at the first few rows to see what our data looks like
print("First 5 rows of the dataset:")
print(data.head())

# This makes sure the dates are in order from oldest to newest
data = data.sort_values("Date")


# We subtract each day's total cases from the previous day's total
data["Daily_New_Cases"] = data["Total_Cases"].diff()

# The first row will have a missing value (because there's no previous day), so we fill it with 0
data["Daily_New_Cases"] = data["Daily_New_Cases"].fillna(0)

 Basic statistics
print("\n--- COVID-19 Case Summary ---")
print(f"Total Days Recorded: {len(data)}")
print(f"Total Cases Overall: {data['Total_Cases'].iloc[-1]:,.0f}")
print(f"Average Daily New Cases: {data['Daily_New_Cases'].mean():,.2f}")
print(f"Highest Single-Day Cases: {data['Daily_New_Cases'].max():,.0f}")
print(f"Lowest Non-Zero Daily Cases: {data['Daily_New_Cases'][data['Daily_New_Cases'] > 0].min():,.0f}")

#  Show the day with the highest new cases
worst_day = data[data["Daily_New_Cases"] == data["Daily_New_Cases"].max()]
print("\nDay with highest cases:")
print(worst_day)

#  Save this updated table to a new file
data.to_csv("covid_case_analysis.csv", index=False)
