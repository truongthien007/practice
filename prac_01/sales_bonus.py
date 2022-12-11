"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sale
while sale >=0
    if sale < 1000
        bonus = sale * SMALL_RATE
    else:
        bonus = sale * BIG_RATE
    display bonus
    get sale 
display end
"""
TARGET_SALE = 1000
# the target that can get more bonus if exceed
SMALL_RATE = 0.1
BIG_RATE = 0.15
sale = float(input("Enter your sales:$"))
while sale >= 0:
    if sale < TARGET_SALE:
        bonus = sale * SMALL_RATE
    else:
        bonus = sale * BIG_RATE
    print("Your bonus is $", bonus)
    sale = float(input("Enter your sales:$"))
print("end")
