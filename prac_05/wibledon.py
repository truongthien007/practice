champions = []
nations = []
with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    text = in_file.read()
    in_file.close()
    for line in text[1:]:
        items = line.strip().split(",")
        print(items)
        champions.append(items[2])
        nations.append(items[1])
    print(champions)
    print(nations)
