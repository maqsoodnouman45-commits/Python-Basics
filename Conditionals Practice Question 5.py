# University Admission Eligibility

percent=float(input("Enter FSC Percentage:"))
if(percent>=60.0 and percent<=100.0):
    marks=int(input("Enter Entry-test marks:"))
    if(marks>=50 and marks<=100):
        print("Congratulations! You are eligible for admission")
    elif(marks>0 and marks<50):
        print("Ineligible: Entry Test score must be at least 50.")
    else:
        print("Invalid entry! Enter valid score")
elif(percent>0.0 and percent<60.0):
    print("Ineligible: FSc percentage must be at least 60%.")
else:
    print("Invalid entry! Enter valid percentage")