# Match case statement 

# day = 2
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Invalid day!")

#Same using match case statement
day = int(input("Enter a day number (1-3): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day!")