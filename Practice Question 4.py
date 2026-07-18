# Food Bill Splitter

# Write a program to help a group of friends split a food bill evenly.
# Take the total bill amount from the user (this can have decimals, like 1450.50).
# Take the total number of people sharing the bill (this must be a whole number).
# Calculate each person's individual share by dividing the total bill by the number of people.

bill=float(input("Enter Total Bill:"))
people=int(input("Enter No. of People:"))
individual_share=bill/people
print("Each Individual Share:", individual_share)