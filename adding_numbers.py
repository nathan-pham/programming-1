number = "5424 1801 2345 6789".replace(' ', '')
total = 0


def digit_sum(n): return sum([int(i) for i in list(str(n))])


for i in range(len(number)):
    digit = int(number[i])

    if i % 2 == 0:
        digit *= 2

        if digit >= 10:
            total += digit_sum(digit)
        else:
            total += digit
    else:
        total += digit

print(total % 10 == 0)
