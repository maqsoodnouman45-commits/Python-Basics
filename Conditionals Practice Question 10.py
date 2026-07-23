# Online Order Shipping & Invoice Generator

bill=float(input("Enter total amount of order:"))
zone=input("Enter Shipping Zone(Local/National):")
if(bill>=5000):
    shipping_fee=0
    total_bill=bill+shipping_fee
    print("Note:You qualified for FREE SHIPPING!")
elif(bill>0 and bill<5000):
    if(zone=="Local"):
        shipping_fee=150
        total_bill=bill+shipping_fee
    elif(zone=="National"):
        shipping_fee=300
        total_bill=bill+shipping_fee
print("Order Amount:\t\t\t",total_bill,"\nShipping Fee:\t\t\t",shipping_fee,"\nTotal Bill:\t\t\t",total_bill)