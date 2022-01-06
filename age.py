from datetime import datetime

# prompt for an integer
def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

# get the current age
def get_age(birthday: datetime, today: datetime) -> int:

    # get the difference between the two dates
    year = today.year - birthday.year
    month = today.month - birthday.month
    day = today.day - birthday.day

    # if the birthday has not yet occurred this year, subtract 1 from year
    if month < 0:
        year -= 1
        month += 12

    # if the birthday has not yet occurred this month, subtract 1 from month
    if day < 0:
        month -= 1
        day += 30
    
    print(f"You are {year} years, {month} months, and {day} days old.")

get_age(datetime(year=prompt("year > "), month=prompt("month > "), day=prompt("day > ")), datetime.now())
get_age(datetime(year=1953, month=9, day=23), datetime.now())
get_age(datetime(year=1987, month=1, day=6), datetime.now())