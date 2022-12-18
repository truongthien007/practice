"""
estimate time:30 mins
actually time:25 mins
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        else:
            return True

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection {self.reflection}, First appear in {self.year}"
