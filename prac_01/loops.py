for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
number = int(input("number: "))
for i in range(number):
    print("*", end='')

# d. print n lines of increasing stars.
number = int(input("number: "))
for i in range(number):
    for j in range(i + 1):
        print("* ", end='')
    print()


