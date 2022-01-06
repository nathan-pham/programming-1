from datetime import datetime

# prompt for an integer
def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

def compare_age(date1: datetime, date2: datetime) -> int:
    if date1 > date2: return 1
    elif date1 < date2: return -1
    return 0

def get_age(birthday: datetime, today: datetime) -> int:
    compare = compare_age(birthday, today)
    age = -1

    if compare < 0:
        age = today.year - birthday.year

        if (today.month < birthday.month) or (today.month == birthday.month and today.day < birthday.day):
            age -= 1

    elif compare == 0: age = 0
    else: print("[error] birthday is in the future!")
    
    return age

print(get_age(datetime(year=prompt("year > "), month=prompt("month > "), day=prompt("day > ")), datetime.now()))
print(get_age(datetime(year=1953, month=9, day=23), datetime.now()))
print(get_age(datetime(year=1987, month=1, day=6), datetime.now()))