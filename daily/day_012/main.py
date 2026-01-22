"""
Day 012: Filtering, Sorting and Grouping wth pandas
Objective: Share and aggregate data intentionally

"""

import pandas as pd
from colorama import Fore

def main():
    filepath = "daily/day_012/data/week.csv"
    df = pd.read_csv(filepath)

    print(Fore.GREEN + "n ---- Raw Data ----")
    print(df)

    # Filering
    work_days = df[df["category"] == "work"]
    print(Fore.RED +"\n")
    print(work_days)
    
    # Sort
    sort_by_hours = df.sort_values(by="hours", ascending=True)
    print(Fore.BLUE +"\n")
    print(sort_by_hours)

    # Grouping
    grouped = df.groupby("category")["hours"].sum().reset_index()
    print("\n---- Total hours by category ----\n")
    print(grouped)

    max_category = grouped.loc[grouped["hours"].idxmax()]
    print(
        f"\n Category with highest totol hours: "
        f"{max_category['category']} with {max_category['hours']} hrs"
    )
 
if __name__ == "__main__":
    main()

