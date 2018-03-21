# Guilherme Paes Feb 2018

# GMIT Data Analytics Exercise 1:
# A program that displays Fibonacci numbers (Adapted from Ian McLoughlin)


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 12
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# My name is Guilherme, so the first and last letter of my name (G + E = 7 + 5) give the number 12. The 12th Fibonacci number is 144.


# GMIT Data Analytics Exercise 2:
"""The ord() method returns an integer representing Unicode code point for the given Unicode character.
In other words, it gives the ASCII code of the character.
Example: ord(‘d’) is 100"""

name = "Paes"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


"""My surname is Paes
The first letter P is number 80
The last letter s is number 115
Fibonacci number 195 is 25299086886458645685589389182743678652930"""
