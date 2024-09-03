count = 0
for n in range(1,101):
    for i in range(1,101):
        if n % i == 0:
            count = count+i
    if (n == count):
        print(f"{n} is perfetct")
    else:
        print(f"{n}, is not perfect")