import math
def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime(start, end):
    total = 0
    for num in range(start, end + 1):
        if prime(num):
            total += num
    return total

start = 10
end = 50
result = sum_of_prime(start, end)

print(f"Sum of prime number is {start} and {end}: {result}")

