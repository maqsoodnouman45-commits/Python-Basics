#String Operations

a="Nouman"
print(a.upper()) # variable.upper() method converts the string to uppercase letters.
print(a.lower()) # variable.lower() method converts the string to lowercase letters.
print(a.replace("Nouman","Nouman Awan")) # variable.replace() method replaces a specified phrase with another specified phrase.

b="  Nouman  "
print(b.strip()) # variable.strip() method removes whitespaces from the beginning or the end of the string.
print(b.rstrip()) # variable.rstrip() method removes whitespaces from the right side of the string.
print(b.rstrip("n   ")) # variable.rstrip() method removes specified characters from the right side of the string.
print(b.lstrip()) # variable.lstrip() method removes whitespaces from the left side of the string.
print(b.lstrip("  N")) # variable.lstrip() method removes specified characters from the left side of the string.

c="My name is Malik Nouman Maqsood"
print(c.split()) # variable.split() method splits the string into a list where each word is a list item.
print(c.capitalize()) # variable.capitalize() method converts the first character of the string to uppercase. Rest is converted to lowercase.
print(c.center(50)) # variable.center() method returns a centered string of a specified length.
print(c.center(50,"-")) # variable.center() method returns a centered string of a specified length and fills the remaining space with a specified character.
print(c.title()) # variable.title() method converts the first character of each word to uppercase and the rest to lowercase.
print(c.istitle()) # variable.istitle() method returns True if the string follows the rules of a title, otherwise False.

d="My name is Malik Nouman Maqsood. I am an AI Engineer. I am a Python Developer. I am still learning."
print(d.count("I")) # variable.count() method returns the number of times a specified value occurs in a string.
print(c.startswith("My")) # variable.startswith() method returns True if the string starts with the specified value, otherwise False.
print(d.endswith("."))
print(d.endswith("learning")) # variable.endswith() method returns True if the string ends with the specified value, otherwise False.
print(d.find("I")) # variable.find() method returns the index of the first occurrence of the specified value.If not found, it returns -1.
print(d.index("I")) # variable.index() method returns the index of the first occurrence of the specified value. If not found, it raises a ValueError.

e="maqsoodnouman45@gmail.com"
print(e.isalnum()) # variable.isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers), otherwise False.
print(e.isalpha()) # variable.isalpha() method returns True if all characters in the string are alphabetic, otherwise False.
print(e.isdigit()) # variable.isdigit() method returns True if all characters in the string are digits, otherwise False.
print(e.islower()) # variable.islower() method returns True if all characters in the string are lowercase, otherwise False.
print(e.isupper()) # variable.isupper() method returns True if all characters in the string are uppercase, otherwise False.

f="Nouman\n"
print(f.isprintable())
g="Nouman Awan"
print(g.isprintable()) # variable.isprintable() method returns True if all characters in the string are printable, otherwise False.
print(g.isspace()) # variable.isspace() method returns True if all characters in the string are whitespaces, otherwise False.
print(g.swapcase()) # variable.swapcase() method converts uppercase characters to lowercase and lowercase characters to uppercase.