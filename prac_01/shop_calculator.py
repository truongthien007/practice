"""
get number_of_item
total = 0
while number_of_item < 0:
    display invalid
    get number_of_item
for i in range(number_of_item):
    get price
    total = total + price
if total > 100:
    total = total - total * 0.1
display total
"""
number_of_item = int(input("Number of items: "))
total = 0
DISCOUNT_RATE = 0.1
SPEND_AT_LEAST = 100
# the at least money has to spend to get discount
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))
for i in range(number_of_item):
    price = float(input("Price of item: "))
    total += price
if total > SPEND_AT_LEAST:
    total = total - total * DISCOUNT_RATE
print(f"Total price for {number_of_item} items is ${total:.2f}")



