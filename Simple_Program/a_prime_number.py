n = int(input("Enter any nuber:"))
count = 0
for j in range(1,n+1):
    if n % j == 0:
        count += 1
if count == 2:
    print(f"{n} is prime")

else:
    print(f"{n} is not prime")


