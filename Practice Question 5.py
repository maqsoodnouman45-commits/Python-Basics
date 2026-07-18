#Windows Path Builder

# Write a script that:
# Asks the user to type in a name for a new project folder.
# Combines their input with a base directory to create this exact Windows path layout: C:\Users\Admin\Documents\[User's Input]
# Prints the final path string.

folder=input("Enter new folder name:")
final_directory="C:\\Users\\Admin\\Documents\\" + folder
print("Final Path:", final_directory)