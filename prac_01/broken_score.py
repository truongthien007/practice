"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
"""
get score 
while 0 <= score <= 100
    if score < 50
        display bad
    else if score < 90
        display pass
    else 
        display excellent
    get score
display invalid                    
"""
# TODO: Fix this!

score = float(input("Enter score: "))
while 0 <= score <= 100:
    # to get valid score
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Pass")
    else:
        print("Excellent")
    score = float(input("Enter score: "))
print("Invalid score")
