def gcd(a,b):
    while b != 0:
        a, b = b, a % b
        
    return a

resut = gcd(48, 18)
print(f' the gcd is : {resut}')