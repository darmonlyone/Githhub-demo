from model.Person import Person

people = []

while True:
    ip = input("A: add person\nL: list people\nF: change person\nE: exit\nEnter code: ")

    if ip == "E":
        break
    elif ip == "A":
        people.append(Person(
            input("Enter Name:"),
            int(input("Enter Age:"))))
    elif ip == "L":
        for person in people:
            print(person)
    elif ip == "F":
        old_name = input("Old Name:")
        for person in people:
            if person.name == old_name:
                new_name = input("input New Name:")
                new_age = int(input("input New Age:"))
                person.change_name(new_name)
                person.change_age(new_age)


    else:
        print("Invalid Input please try again")
