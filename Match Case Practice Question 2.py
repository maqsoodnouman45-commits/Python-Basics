# Season Finder

month=input("Enter month name:").lower()
match month:
    case "december"|"january"|"februay":
        print("Season is Winter")
    case "march"|"april"|"may":
        print("Season is Spring")
    case "june"|"july"|"august":
        print("Season is Summer")
    case "september"|"october"|"november":
        print("Season is Autumn")
    case _:
        print("Invalid month name entered!")