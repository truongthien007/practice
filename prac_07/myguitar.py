import csv
from prac_06.guitar import Guitar

guitars = []
guitar_class = []


def main():
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    guitar = csv.reader(in_file)
    for row in guitar:
        guitars.append(row)
    in_file.close()
    print("Guitars:")
    for guitar in guitars:
        guitar_class.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    guitar_class.sort()
    for i, guitar in enumerate(guitar_class, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:15,.2f} {vintage_string}")


main()
