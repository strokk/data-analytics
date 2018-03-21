# Guilherme Paes, Feb-2018
# The Collatz conjecture exercise
# https://en.wikipedia.org/wiki/Collatz_conjecture

n = 21

print(n)
while n > 1:
  if n % 2 == 0:
    # if number is even divide by 2
    n = n / 2
    print(n)
  else:
    # if number is odd multiply by 3 and subtract 1
    n = (n*3) + 1
    print(n)
