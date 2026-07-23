# The 4-Function Calculator

num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
op=input("Choose operation(+,-,*,/):")
match op:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/" if(num2==0):
        print("Error! Division by zero is not allowed")
    case "/":
        print(num1/num2)
    case _:
        print("Invalid Operator selected")