"""
Day 006 - Functions and modular designs
Objective: refactor logic into reusable functions
"""

def get_daily_hours():
    hours = []
    print("\nEnter coding hours for each day")
    for day in range(1,8):
        value = float(input(f"Day {day}:"))
        hours.append(value)
    return hours

def calculate_metrics(daily_hours):
    return {
        "total_hours": sum(daily_hours),
        "average_hours": sum(daily_hours)/len(daily_hours),
        "min_hours": min(daily_hours),
        "max_hours": max(daily_hours)
    }

def classify_intensity(avg_hours):
    if avg_hours <= 1.5:
        return "Low"
    elif avg_hours <= 3:
        return "Medium"
    else:
        return "High"

def print_profile(profile):
    print("\n---- Weekly Coding Profile ----")
    for key, value in profile.items():
        print(f"{key}: {value}")
    


def main():
    name = input("Enter your name: ")

    daily_hours = get_daily_hours()

    metrics = calculate_metrics(daily_hours)
    intensity = classify_intensity(metrics["average_hours"])

    profile = {
        "Name": name,
        "daily_hours": daily_hours,
        **metrics,
        "intensity": intensity
    } 

    print_profile(profile)

if __name__ == "__main__":
    main()