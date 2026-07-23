# Login System Simulator

correct_username="maliknoumanmaqsood45"
correct_pin=6179
username=input("Enter username:")
pin=int(input("Enter PIN:"))
if(username==correct_username):
    if(pin==correct_pin):
        print("Welcome to your Dashboard!")
    else:
        print("Incorrect PIN! Access Denied")
else:
    print("Incorrect Username! Access Denied")