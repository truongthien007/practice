champions = []
times_to_champions = {}
nations = []
count_to_nations = []


def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        text = in_file.readlines()
        in_file.close()
        split_data(text)
        number_of_times_champion()
        number_of_nations()


def split_data(text):
    for line in text[1:]:
        items = line.strip().split(",")
        champions.append(items[2])
        nations.append(items[1])


def number_of_times_champion():
    for i in range(0, len(champions)):
        if champions[i] not in times_to_champions:
            # count_to_champions[champions[i]] is value
            times_to_champions[champions[i]] = 1
        else:
            times_to_champions[champions[i]] += 1
    for champion in times_to_champions:
        print(f"{champion}: {times_to_champions[champion]}")


def number_of_nations():
    for nation in nations:
        if nation not in count_to_nations:
            count_to_nations.append(nation)
    print(f'These {len(count_to_nations)} countries have won Wimbledon: ')
    result = sorted(count_to_nations)
    print(", ".join(result))


main()
