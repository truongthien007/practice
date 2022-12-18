from prac_06.guitar import Guitar
guitars = []


def main():
    print("My guitar!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        name = input("Name: ")
        print(guitars)
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth ${guitar.cost} {vintage}")


main()
