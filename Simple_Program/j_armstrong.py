num = int(input("Enter the number to check armstrong: "))
length = 0
var = abs(num)
# ct = len(str(num))

while var > 0:
    var //= 10
    length += 1
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
    
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

print(length)