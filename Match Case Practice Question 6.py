# Restaurant Menu Order System

print("MENU\n1. BIRYANI\t\t\tRs.350\n2. Karahi\t\t\tRs.1200\n3. Burger\t\t\tRs.450")
choice=int(input("Enter Choice(1 for Biryani/2 for Karahi/3 for Burger):"))
quantity=int(input("Enter quantity:"))
match choice:
    case 1:
        total_price=quantity*350
        print("Total Amount:",total_price)
    case 2:
        total_price=quantity*1200
        print("Total Amount:",total_price)
    case 3:
        total_price=quantity*450
        print("Total Amount:",total_price)
    case _:
        print("Invalid Entry!")