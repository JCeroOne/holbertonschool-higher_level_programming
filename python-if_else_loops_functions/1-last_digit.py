#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0:
    n = -(abs(number) % 10)
str = ""
if n > 5:
    str = " and is greater than 5"
elif n < 6 and n is not 0:
    str = " and is less than 6 and not 0"
elif n == 0:
    str = " and is 0"
print(f"Last digit of {number} is {n}{str}")
