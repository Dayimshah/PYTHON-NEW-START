COVID Daily Cases - Data Processing Script
------------------------------------------

This is a beginner-friendly Python script that reads a CSV file containing total COVID-19 cases and calculates the daily new cases.

It uses the pandas library to load and process the data.

What It Does:
-------------
- Loads a CSV with two columns: Date and Total_Cases
- Calculates the number of new cases each day using the difference between consecutive days.
- Outputs a clean table with the results.

What You Need:
--------------
- Python 3
- pandas library

To install pandas:
------------------
Open your terminal or command prompt and run:

    pip install pandas

CSV File Format:
----------------
Make sure your CSV file (named `covid_data.csv`) looks like this:

    Date,Total_Cases
    2020-01-01,0
    2020-01-02,2
    2020-01-03,5
    2020-01-04,7

How To Use:
-----------
1. Save the script as: covid_daily_cases.py
2. Place your `covid_data.csv` file in the same folder.
3. Open terminal in the folder and run:

    python covid_daily_cases.py

4. The script will read the CSV, calculate the daily new cases, and display the result.

Output Example:
---------------
    Date        Total_Cases  Daily_New_Cases
    2020-01-01       0              0.0
    2020-01-02       2              2.0
    2020-01-03       5              3.0
    2020-01-04       7              2.0

Notes:
------
- The first row of daily new cases will be 0 because there's no previous day to compare.
- Make sure the column names in your CSV exactly match: `Date` and `Total_Cases`.

File Structure:
---------------
- covid_daily_cases.py  → the Python script
- covid_data.csv        → your input data file
