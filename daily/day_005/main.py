"""
Day 005 - Dictionaries and dtructured data
Objective: Model coding data using key-value structures
"""

def main():
    name = input("Enter your name: ")

    daily_hours = []

    print(f"Enter coding hours for each day:")
    for day in range(1,8):
        hours = float(input(f"Day {day}: "))
        daily_hours.append(hours)

    profile = {
        "name": name,
        "daily_hours": daily_hours,
        "total_hours": sum(daily_hours),
        "average_hours": sum(daily_hours) / len(daily_hours),
        "min_hours": min(daily_hours),
        "max_hours": max(daily_hours)
    }

    if profile["average_hours"] <=1.5:
        intensity = "Low"
    elif profile["average_hours"] <= 3.0:
        intensity = "Medium"
    else:
        intensity = "High"
    
    print("\n ---- Weekly Coding Profile ----")
    for key,value in profile.items():
        print(f"{key}: {value}")
    

if __name__ == "__main__":
    main()

