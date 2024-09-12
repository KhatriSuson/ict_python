import math

def factorial(n):
    if n<0:
        return "Factorial does not exit"
    return math.factorial(n)

print(factorial(5))