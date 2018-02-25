"""Project Euler 5 - Guilherme Paes - 25/02/2018

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?"""

number = 1
for i in (range(1, 21)):
    if number % i > 0:
        for x in range(1, 21):
            if (number * x) % i == 0:
                number *= x
                break
print(number)