# Birth-Year Finder

# write a script that acts as a simple birth-year finder.
# Ask the user to enter their current age.
# Typecast that input into a whole number.
# Subtract their age from 2026 to find their approximate birth year.

age=int(input("Enter current age: "))
birth_year=2026-age
print("Your approximate birth year is:",birth_year)