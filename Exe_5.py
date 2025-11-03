monthndays = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
month = int(input("Enter a month number (1-12): "))
if month in monthndays:

    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"The month {month} has {monthndays[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")