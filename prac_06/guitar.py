"""
estimate time: 40 min
actually time: 25 min
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        guitar_age = 2022 - self.year
        return guitar_age

    def is_vintage(self):
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year
