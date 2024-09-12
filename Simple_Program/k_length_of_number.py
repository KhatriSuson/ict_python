number = 12345
length = 0
temp = abs(number)  # Handle negative numbers

while temp > 0:
    temp //= 10
    length += 1

# Edge case for 0
if number == 0:
    length = 1

print(length)