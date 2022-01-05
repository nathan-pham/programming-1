# prompt for an integer
def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

# prompt for 2 numbers
number_1 = prompt("Enter a number: ")
number_2 = prompt("Enter another number: ")

# if number_1 is greater than number_2 then print "number_1 is greater than number_2"
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")

# if number_1 is less than number_2 then print "number_1 is less than number_2"
if number_1 < number_2:
    print(f"{number_1} is less than {number_2}")

# if number_1 is equal to number_2 then print "number_1 is equal to number_2"
if number_1 == number_2:
    print(f"{number_1} is equal to {number_2}")