MENU = ['-(L)oad project', "-(S)ave project", "-(D)isplay project", "-(F)ilter project by date", "-(A)dd new project",
        "-(U)pdate project"]
for menu in MENU:
    print(menu)


def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()

