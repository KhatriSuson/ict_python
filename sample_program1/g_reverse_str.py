def reverser_str(str):
    reversed_str = ''
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

result = reverser_str('hello')
print(f'Reverse of hello is : {result}')