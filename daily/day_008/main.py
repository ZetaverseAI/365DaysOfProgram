"""
Docstring for daily.day_008.main
"""

from colorama import Fore

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError(Fore.RED + "Value must be Non-Negative.")
            return value
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}. Please try again")


def get_daily_hours():
    hours = []
    print("\nEnter coding hours for each day:")
    for day in range(1, 8):
        hours.append(get_valid_float(Fore.WHITE + f"Day {day}: "))
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

def save_profile_to_file(profile, filepath):
    with open(filepath, "w") as f:
        for key, value in profile.items():
            f.write(f"{key}: {value}\n")

def load_profile_from_file(filepath):
    print(Fore.BLUE + "\n---- Loaded profile ----")
    with open(filepath, "r") as f:
        print(Fore.BLUE + f.read())

def main():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Exiting.")
        return

    daily_hours = get_daily_hours()
    metrics = calculate_metrics(daily_hours)
    intensity = classify_intensity(metrics["average_hours"])

    profile = {
        "name": name,
        "daily_hours": daily_hours,
        **metrics,
        "intensity": intensity
    }

    filepath = "daily/day_008/profile.txt"
    save_profile_to_file(profile, filepath)
    print(f"\nProfile saved to {filepath}")

    load_profile_from_file(filepath)


if __name__ == "__main__":
    main()