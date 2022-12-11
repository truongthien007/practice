NAME_TO_CODE = {"Absolute Zero": "0048ba", "Acid Green": "b0bf1a",
                "AliceBlue": "f0f8ff",
                "Alizarin crimson": "e32636",
                "Amaranth": "e52b50",
                "Amber": "ffbf00",
                "Amethyst": "9966cc",
                "Antiquewhite": "faebd7",
                "Antiquewhite1": "ffefdb",
                "Antiquewhite2": "eedfcc",
                "Antiquewhite3": "cdc0b0"}
print(NAME_TO_CODE)
name = input("Enter name color: ").title()
while name != "":
    if name in NAME_TO_CODE:
        print(name, 'is', NAME_TO_CODE[name])
    else:
        print("invalid name")
    name = input("Enter name color: ").title()
