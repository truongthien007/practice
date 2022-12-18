from prac_06.guitar import guitar

guitar_1 = guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = guitar("Another guitar", 2013, 10)


def main():
    print(guitar_1.get_age())
    print(guitar_2.get_age())
    print(guitar_1.is_vintage())
    print(guitar_2.is_vintage())


main()

