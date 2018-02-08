# Guilherme Paes
# A program that displays Fibonacci numbers using people's names (Adapted from Ian McLoughlin)

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

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


#My surname is Paes
#The first letter P is number 80
#The last letter s is number 115
#Fibonacci number 195 is 25299086886458645685589389182743678652930


#The ord() method returns an integer representing Unicode code point for the given Unicode character.
#In other words, it gives the ASCII code of the character.
#Example: ord(‘d’) is 100

