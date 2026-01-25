"""
Day 014: Feature Engineering & derived metrics
Objective: Create model-readt feastures from cleaned data

"""

import pandas as pd
from colorama import Fore

def main():
    filepath = "daily/day_014/data/week.csv"
    df = pd.read_csv(filepath)

    print(Fore.GREEN + "n ---- Raw Data ----")
    print(df)

    # Feature 1 binary iondicator
    df["is_workday"] = df["category"].apply(lambda x: 1 if x == "work" else 0)

    # Feature 2 Non-Lineasr transformation
    df["hours_squared"] = df["hours"] ** 2

    # Feature 3: Bucketing
    df["hours_bucket"] = pd.cut(
        df["hours"],
        bins=[-1,1,2.5,10],
        labels=["Low", "Medium", "High"]
    )
    print("\n--- Feature-Enhanced Data ---")
    print(df)

    #aggregate features (category level)
    category_features = (
        df.groupby("category")
        .agg(
            total_hours=("hours", "sum"),
            avg_hours=("hours", "mean"),
            workday_ratio=("is_workday", "mean"),
        )
        .reset_index()
    )
    print("\n---- Category Level Features ----")
    print(category_features)

 
if __name__ == "__main__":
    main()

