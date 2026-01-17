"""
Day 009: CSV & JSON data formats
Objective: persist and reload structured data using standard formats

Docstring for daily.day_009.main
"""

import csv
import json
from colorama import Fore

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def get_daily_hours():
    hours = []
    print("\nEnter coding hours for each day:")
    for day in range(1, 8):
        hours.append(get_valid_float(f"Day {day}: "))
    return hours


def calculate_metrics(daily_hours):
    return {
        "total_hours": sum(daily_hours),
        "average_hours": sum(daily_hours) / len(daily_hours),
        "min_hours": min(daily_hours),
        "max_hours": max(daily_hours),
    }


def classify_intensity(avg_hours):
    if avg_hours < 1.5:
        return "Low"
    elif avg_hours <= 3:
        return "Medium"
    return "High"

def save_to_csv(daily_hours, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["day", "hours"])
        for i, hours in enumerate(daily_hours, start=1):
            writer.writerow([i, hours])

def save_to_json(profile, filepath):
    with open(filepath, "w") as f:
        json.dump(profile, f, indent=4)      

def load_to_print_file(filepath):
    print(f"\n---- contents of {filepath} ----")
    with open(filepath, "r") as f:
        print(f.read())

def main():
    name = input("Enter your name: ").strip()
    if not name:
        print(Fore.RED + "Name cannot be empty. Exiting")
        return
    daily_hours = get_daily_hours()
    metrics = calculate_metrics(daily_hours)

    profile = {
        "name"          : name,
        "daily_hours"   : daily_hours,
        **metrics,
        "intensity"     : classify_intensity(metrics["average_hours"]),
    }

    csv_path = "daily/day_009/daily_hours.csv"
    json_path = "daily/day_009/profile.json"

    save_to_csv(daily_hours, csv_path)
    save_to_json(profile, json_path)

    print("\n Files sabes Successfully")
    load_to_print_file(csv_path)
    load_to_print_file(json_path)

if __name__ == "__main__":
    main()


