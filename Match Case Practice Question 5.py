# Vowel or Consonant Checker

alphabet=input("Enter any single English alphabet:").lower()
vowel="a","e","i","o","u"
match alphabet:
    case "a"|"e"|"i"|"o"|"u":
        print("Entered character is a vowel")
    case c if(len(c)==1 and c.isalpha()):
        print("It is a consonant")
    case _:
        print("Invalid entry!")