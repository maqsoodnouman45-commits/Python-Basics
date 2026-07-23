# Cinema Ticket System

age=int(input("Enter age:"))
if(age>=18):
    seat=input("Enter seat preference(Standard/VIP):")
    if(seat=="VIP"):
        print("Ticket price is 1500 PKR")
    elif(seat=="Standard"):
        print("Ticket price is 1000 PKR")
    else:
        print("Invalid entry.Enter 'Standard' or 'VIP' ")
elif(age<18):
    adult_accompanied=input("Are you accompanied with any adult?(Yes/No):")
    if(adult_accompanied=="Yes"):
        print("Ticket price is 500 PKR")
    elif(adult_accompanied=="No"):
        print("Entry Denied: Minors must be accompanied by an adult.")
    else:
        print("Invalid entry. Enter Yes/No")