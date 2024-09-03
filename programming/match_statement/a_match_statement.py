n = int(input("Any nuber from 1 to 7 :"))
match (n):
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thrusday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")

    case _:
        print("Invalid Input")