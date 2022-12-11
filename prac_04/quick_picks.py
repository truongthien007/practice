import random

quick_pick = int(input("How many quick pick you want to generate? "))


def formatList(values):
    for j in range(len(values)):
        if len(values[j]) == 1:
            values[j] = " " + values[j]


for i in range(0, quick_pick):
    values = []
    while len(values) != 6:
        value = random.randint(1, 45)
        if value not in values:
            values.append(value)
    values.sort()
    values = [str(value) for value in values]
    formatList(values)
    print(' '.join(values))
    print()

