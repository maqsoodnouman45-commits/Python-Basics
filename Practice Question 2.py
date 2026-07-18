#Strike-Rate Calculator

#Write a program that:
#Asks the user to input the total runs scored.
#Asks the user to input the total balls faced.
#Calculates the strike rate.
#Prints the final strike rate out

runs= int(input("Enter Runs scored: "))
balls= int(input("Enter Balls faced: "))
strike_rate=runs/balls*100
print("Strike Rate: ",strike_rate)