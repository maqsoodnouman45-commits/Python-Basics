# Restaurant Discount & Format Receipt

bill=float(input("Enter Total Bill:"))
age=int(input("Enter age:"))
if(age<12):
    discount_rate=0.3
elif(age>=60):
    discount_rate=0.2
else:
    discount_rate=0
    
discount_amount=bill*discount_rate
total_bill=bill-discount_amount
print("TOTAL BILL:\t\t\t",bill,"\nDISCOUNT:\t\t\t",discount_amount,"\nFINAL PAYABLE:\t\t\t",total_bill)