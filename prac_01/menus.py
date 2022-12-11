name = input("Enter name: ")
for i in ["(H)ello", "(G)oodbye", "(Q)uit"]:
    print(i)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    for i in ["(H)ello", "(G)oodbye", "(Q)uit"]:
        print(i)
    choice = input(">>>").upper()
print("Finished")



