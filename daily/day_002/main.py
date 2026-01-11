"""
Day 002 – User Input and Control Flow
Objective: Build an interactive commitment calculator
"""

def main():
    name = input("Enter your name: ")
    daily_hours = float(input("Enter daily coding hours: "))

    weekly_hours = daily_hours * 7
    monthly_hours = daily_hours * 30

    if daily_hours < 1:
        level = "Low"
    elif daily_hours <= 3:
        level = "Medium"
    else:
        level = "High"

    print("\n--- Commitment Summary ---")
    print(f"Name: {name}")
    print(f"Daily Hours: {daily_hours}")
    print(f"Weekly Hours: {weekly_hours}")
    print(f"Monthly Hours: {monthly_hours}")
    print(f"Commitment Level: {level}")

if __name__ == "__main__":
    main()
