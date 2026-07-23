# Number Classifier

num=int(input("Enter number:"))
if(num>0):
    if(num%2==0):
        print("Positive Even number")
    else:
        print("Positive Odd number")
elif(num<0):
    if(num%2==0):
        print("Negative Even number")
    else:
        print("Negative Odd number")
else:
    print("Number is 0")