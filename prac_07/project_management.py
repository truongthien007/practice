MENU = ['-(L)oad project', "-(S)ave project", "-(D)isplay project", "-(F)ilter project by date", "-(A)dd new project",
        "-(U)pdate project"]
for menu in MENU:
    print(menu)


def main():
    with open("projects.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)

def extract_data(data):
    def extract_data(data):
        projects = []
        for line in data[1:]:
            items = line.strip().split("\t")
            projects.append(items)
