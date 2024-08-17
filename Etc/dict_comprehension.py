students = ["Hermione", "Harry", "Ron"]

## traditional way
# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

## dictionary comprehension

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

