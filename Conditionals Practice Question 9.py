# Electricity Bill Slab Calculator

units=int(input("Enter electricity unit consumed:"))
if(units<=0):
    print("Invalid Unit consumption")
else:
    if(units>0 and units<=100):
        base_bill=units*15
    elif(units>100 and units<=200):
        base_bill=units*20
    else:
        base_bill=units*25

    if(base_bill>3000):
        total_bill=base_bill*1.10
    else:
        total_bill=base_bill
    print("Total Bill:",total_bill)