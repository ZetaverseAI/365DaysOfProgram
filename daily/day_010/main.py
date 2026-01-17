"""
Day 010: Directory scanning and batch processing
Objective: Process Multiple CSV Files programatically

"""

import os
import csv
from colorama import Fore

def process_csv(filepath):
    hours = []

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            hours.append(float(row["hours"]))

    total = sum(hours)
    average = total / len(hours)

    return total, average

def main():
    data_dir = "daily/day_010/data"

    print("\n---- Batch Processing Summary ----")

    for filename in os.listdir(data_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(data_dir, filename)
            total, average = process_csv(filepath)

            print(Fore. BLUE + f"\nFile: {filename}")
            print(f"Total Hours: {total}")
            print(f"Averge hours / day: {average}")

if __name__ == "__main__":
    main()