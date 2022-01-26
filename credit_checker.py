# Filename:     credit_checker.py
# Date:         1/18/2022
# Purpose:      Simple algorithm to validate a credit card n
# Name:         Nathan Pham


digit_sum = lambda n : sum([int(i) for i in list(str(n))]); 
validate = lambda n: digit_sum(''.join(str(digit_sum(n[i]) * 2) if i % 2 == 0 else n[i] for i in range(len(n)))) % 10 == 0; print("Valid credit card" if validate(''.join("5424 1801 2445 6789".split(' '))) else "Invalid credit card")