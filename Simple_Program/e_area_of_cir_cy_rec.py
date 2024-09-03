import math
ch = int(input("Enter choice: \n 1. Rectangle \n 2. Circle \n 3. Cylinder \n 4. Square\n"))
match(ch):
    case 1:
        l = int(input("Enter L:"))
        b = int(input("Enter B:"))
        area = l * b
        print(f"Area of Rectange = {area}")

    case 2:
        r = int(input("Enter radious"))
        area = 3.14*r*r
        # area = math.pie*r*r
        print(f"Area of circle = {area}")
    case 3:
        r = int(input("Enter r:"))
        h = int(input("Enter h:"))
        area = 2*3.14*r(r+h)
        # area = math.pie*r(r+h)
        print(f"Area of circle = {area}")
    case 4:
        l = int(input("Enter L:"))
        area = l * l
        print(f"Area of circle = {area}")

    case _:
        print("hehe! sorry Invalid input")
