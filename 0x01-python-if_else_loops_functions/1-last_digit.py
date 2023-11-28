#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    talk = f"Last digit of {number} is -{last_digit}"
    print(f"{talk} and is less than 6 and not 0")
else:
    talk = f"Last digit of {number} is {last_digit}"
    if last_digit > 5:
        print(f"{talk} and is greater than 5")
    elif last_digit == 0:
        print(f"{talk} and is 0")
    else:
        print(f"{talk} and is less than 6 and not 0")
