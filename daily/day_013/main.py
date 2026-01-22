"""
Day 013 - Handling Missing data and transformation
Objective: Clean and transform imperfect datasets

"""

import pandas as pd
from colorama import Fore

def main():
    filepath = "daily/day_013/data/week.csv"
    df = pd.read_csv(filepath)

    print(Fore.GREEN +"\n---- Raw Data ----")
    print(df)

    print(Fore.RED +"\n---- Missing Data Summary ----")
    print(df.isna().sum())

    # Handle missing numberical value
    mean_hours = df["hours"].mean()
    df["hours"] = df["hours"].fillna(mean_hours)

    print(Fore.GREEN + "\n---- After Filling missing values")
    print(mean_hours)
    print(df)

    # handling missing categorical values
    df["category"] = df["category"].fillna("Unknown")
    print(df)

    #Transformation: Normalize hours (0-1 scale)
    max_hours = df["hours"].max()
    df["normalized_hours"] = df["hours"] / max_hours

    print(Fore.BLUE + "\n---- After transformation (Normalized hours)----" )
    print(df)

    # Aggregation After Cleaning
    grouped = df.groupby("category")["hours"].sum().reset_index()
    print("n----Total hours by category (Cleaned Data)----")
    print(grouped)




if __name__ == "__main__":
    main()
