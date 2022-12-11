"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

# for k, v in CODE_TO_NAME.items():
# k is key, v is value in dictionaries
# print(f'{k: <3} is {v}')

# use EAFP
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        # state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Error")
    state_code = input("Enter short state: ").upper()
