"""
Day 11: Introduction to Pandas
Objective: Peform basic data annalysis using dataframes
"""

import pandas as pd
from colorama import Fore

def main():
    filepath ="daily/day_011/data/week.csv"

    df = pd.read_csv(filepath)

    print(Fore.BLUE + "\n ---- Raw Data ----")
    print(df)

    total_hours = df["hours"].sum()
    average_hours = df["hours"].mean() 
    min_hours = df["hours"].min()
    max_hours = df["hours"].max()

    print("\n ---- Describe() Output ----")
    print(f"Total Hours: {total_hours}")
    print(f"Average Hours: {average_hours:.2f}")
    print(f"Min Hours: {min_hours}")
    print(f"Max Hours: {max_hours}")
    
    t_hours = df.min()["hours"]
    print(f"Total Hours1: {t_hours}")
    

if __name__ == "__main__":
    main()