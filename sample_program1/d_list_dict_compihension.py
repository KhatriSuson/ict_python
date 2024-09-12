list = [1,2,3,4,5]
square_of_even = [x**2 for x in list if x % 2 ==0]
print(f'square_of_even \t {square_of_even}')

square_of_dict = {x: x**2 for x in list}
print(square_of_dict)