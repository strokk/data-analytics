# Guilherme Paes
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


#My name is Guilherme, so the first and last letter of my name (G + E = 7 + 5) give the number 12. The 12th Fibonacci number is 144.
