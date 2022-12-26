from prac_07.project import Project

MENU = ['-(L)oad project', "-(S)ave project", "-(D)isplay project", "-(F)ilter project by date", "-(A)dd new project",
        "-(U)pdate project"]
class_project = []


def main():
    with open("project.txt", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
    choice = get_choice()
    while choice != "Q":
        if choice == "S":
            filename = input("Filename: ")
            output_file = open(f"{filename}.txt", "w")
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
            output_file.close()
        elif choice == "D":
            class_project.sort()
            print("Incomplete Project: ")
            for project in class_project:
                if project.is_complete():
                    print(project)
            print("Completed Projects: ")
            for project in class_project:
                if project.is_complete():
                    print(project)


def get_choice():
    for menu in MENU:
        print(menu)
    choice = input(">>>").upper()
    return choice


def extract_data(data):
    projects = []
    for line in data[1:]:
        items = line.strip().split("\t")
        projects.append(items)
    for project in projects:
        class_project.append(Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4])))


main()
