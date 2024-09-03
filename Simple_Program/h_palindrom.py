# def palindrome(num):
   
#     num_str = str(num)
    
#     reverse_str = num_str[::-1]
    
#     if num_str == reverse_str:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))

# if palindrome(num):
#     print(f"{num} = palindrome")
# else:
#     print(f"{num} = no palindrome")

num = int(input("Enter the number to check palindrome: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")