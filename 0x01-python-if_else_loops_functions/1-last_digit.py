#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
last_character = string_number[-1]
lastdigit = int(last_character)
if lastdigit > 5:
    str = 'Last digit of {:d} is {:d} and is greater than 5'
    print(str.format(number, lastdigit))
elif lastdigit == 0:
    str = 'Last digit of {:d} is {:d} and is 0'
    print(str.format(number, lastdigit))
else:
    str = 'Last digit of {:d} is {:d} and is less than 6 and not 0'
    print(str.format(number, lastdigit))
