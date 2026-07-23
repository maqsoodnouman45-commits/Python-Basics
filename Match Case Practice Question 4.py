# Age Group Ticket Pricer

age=int(input("Enter age:"))
match age:
    case age if(age<5 and age>0):
        print("Ticket price is FREE")
    case age if(age>=5 and age<18):
        print("Child Ticket price is: 500")
    case age if(age>=18 and age<60):
        print("Adult Ticket price is: 1000")
    case age if(age>=60):
        print("Senior Citizen Ticket is: 400")
    case _:
        print("Invalid Entry")