"""
Day 007: Input vaidation & error handling
Objective: Build resilient input handling for real world usage

"""
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be Non-Negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again")

def get_daily_hours():
    hours = []
    print("\nEnter coding hours for each day")
    for day in range(1,8):
        value = get_valid_float(f"Day {day}:")
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
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty. Exiting program.")
        return

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