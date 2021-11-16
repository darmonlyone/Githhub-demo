from model.Person import Person

names = []

while True:
    ip = input("A: add person\nL: list people\nE: exit\nEnter code: ")

    if ip == "E":
        break
    elif ip == "A":
        names.append(Person(
            input("Enter Name:"),
            int(input("Enter Age:"))))
    elif ip == "L":
        for name in names:
            print(name)
    else:
        print("Invalid Input please try again")
