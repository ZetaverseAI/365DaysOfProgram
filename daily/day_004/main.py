"""
Day 004 - Lists and Basic Analytics 
Objective: Store and Analyze daily coding data
Docstring for daily.day_004.main
"""

def main():
    name = input("Enter your name: ")

    daily_hours = []

    print("n Enter coding hours for each day:")
    for day in range(1,8):
        hours = float(input(f"Day {day}: "))
        daily_hours.append(hours)
    
    total_hours = sum(daily_hours)
    average_hours = total_hours/ len(daily_hours)
    min_hours = min(daily_hours)
    max_hours = max(daily_hours)

    if average_hours < 1.5:
        intensity = "Low"
    elif average_hours < 3:
        intensity = "Medium"
    else:
        intensity = "High"
    
    print("\n ---- Weekly Analys ----")
    print(f"Name: {name}")
    print(f"Daily Hours: {daily_hours}")
    print(f"Total Hours: {total_hours}")
    print(f"Average hours/day: {average_hours} ")
    print(f"Min Hours (day): {min_hours}")
    print(f"Max hours (day): {max_hours}")
    print(f"intensity Level: {intensity}")

if __name__ == "__main__":
    main()
