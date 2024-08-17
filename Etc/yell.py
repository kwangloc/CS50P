def main():
    # yell("This", "is", "cs50")
    # yell_map("This", "is", "cs50") # map
    # yell_list_comprehension("This", "is", "cs50") # list comprehension
    # cond_in_list_comp()
    filter_func()
    

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

# map
def yell_map(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

# list comprehensions
def yell_list_comprehension(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

# condition in list comprehension
def cond_in_list_comp():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    print(gryffindors)

# filter(function, iterable)
def is_gryffindor(student):
    return student["house"] == "Gryffindor"

def filter_func():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]
    # gryffindors = filter(is_gryffindor, students)
    gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

    # for gryffindor in gryffindors:  
    #     print(gryffindor["name"])

    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])

if __name__ == "__main__":
    main()