email_to_name = {}


def main():
    email = input("Email: ")
    while email != "":
        get_name(email)
        validate_name(email)
        print(email_to_name)
        email = input("Email: ")


def validate_name(email):
    request = input(f"Is your name {get_name(email)}? (y/n)")
    if request.lower() in ["n", "no"]:
        correct_name = input("Name: ")
        email_to_name[email] = correct_name
    elif request.lower() in ["y", "yes"]:
        email_to_name[email] = get_name(email)


def get_name(email):
    emails = email.split("@")
    name = emails[0].title().split(".")
    result_name = " ".join(name)
    return result_name


main()
