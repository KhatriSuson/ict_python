a, b , c = 1, 2,3
ch = int(input("Enter YOur Choice form 1 to 3 :"))

match(ch):
    case 1:
        area = a * b
        print("Area = ", area)
    case 2:
        vol = a * b * c
        print("vol = ", vol)
    case 3:
        perimeter = 2(a + b)
        print("Perimeter = ", perimeter)

    case _:
        print("Invalid INput")
