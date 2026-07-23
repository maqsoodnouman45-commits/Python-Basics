# ATM Cash Withdrawal System

balance=10000.0
print("Current balance:",float(balance))
withdraw_amount=float(input("Enter amount you want to withdraw:"))
if(withdraw_amount>0):
    if(withdraw_amount<=balance):
        new_balance=balance-withdraw_amount
        print("New Balance:",new_balance)
    else:
        print("Insufficient funds in your account")
else:
    print("Invalid withdrawal amount")