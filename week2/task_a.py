
weekDay = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

day_input = input("Enter a day of the week: ").strip().lower()

if day_input in weekDay:
    day_title = day_input
    day_number = weekDay[day_input]
    print(f"{day_title} is day {day_number}")
else:
    print("Please enter a valid day")
