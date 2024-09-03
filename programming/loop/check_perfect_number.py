count = 0
n = int(input("Etner any nuber:"))
for i in range(1,n):
    if n % i == 0:
        count = count+i

if (n == count):
        print(f'{n}, is perfetct')

else:
        print(f"{n} is not perfetc")