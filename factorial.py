#Guilherme Paes - March 2018
#Funcion that takes an input and return its factorial number

def factorial(f):
    fact = 1
    for i in range(f):
        fact = fact * (i + 1)
    return fact

#Testing the function:
print("The Factorial of 5 is: " + str(factorial(5)))
print("The Factorial of 7 is: " + str(factorial(7)))
print("The Factorial of 10 is: " + str(factorial(10)))
