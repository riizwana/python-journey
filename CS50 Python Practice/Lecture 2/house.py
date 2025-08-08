name = input("What is your name? ")
match name:
    # The straight line are to have them match together in the same case by stating various variables like the names on the bottom.
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")