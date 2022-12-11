"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    the_amount_of_month = int(input("How many months? "))

    for month in range(1, the_amount_of_month + 1):
        """ use f-string to get input """
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    indicate_report(incomes, the_amount_of_month)


def indicate_report(incomes, the_amount_of_month):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, the_amount_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
