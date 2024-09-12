def palindrom(str):
    s = str.lower()
    return s == s[::-1]

print(palindrom('aaaaa'))
print(palindrom('apple'))