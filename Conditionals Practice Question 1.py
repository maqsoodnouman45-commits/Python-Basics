#Pass/Fail & Merit Scholarship Checker

marks=int(input("Enter your marks:"))
if(marks>=50 and marks<=100):
    print("Result: Pass")
    if(marks>=80 and marks<=100):
        print("You are eligible for scholarship")
    elif(marks>=50 and marks<80):
        print("You are not eligible for scholarship")
elif(marks>=0 and marks<50):
    print("Result: Fail")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")