"""
Docstring for daily.day_003.main
Loops and Aggregation
Objective: User ITeration to complete weeklty coding metrics
"""

def main():
    name        = input("Enter your name: ")
    daily_hours = float(input("Enter planned daily coding hours: "))

    total_hours = 0

    print("\n Daily Breakdown:")
    for day in range(1, 8):
        total_hours += daily_hours
        print(f"Day {day}: {daily_hours} hours")
    
    average_hours = total_hours/7

    if average_hours < 1.5:
        intensity = "Low"
    elif average_hours <= 3:
        intensity = "Medium"
    else:
        intensity = "High"

    print("\n----- Weekly summary -------")
    print(f"Name: {name}")
    print(f"Total Hours (week): {total_hours}")
    print(f"Average hours/day: {average_hours:.2f}")
    print(f"Intensity Level: {intensity}")


if __name__ == "__main__":
    main()

