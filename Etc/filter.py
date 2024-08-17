students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindor_only = list(filter(is_gryffindor, students))
for gryffindor in gryffindor_only:  
    print(gryffindor["name"])
