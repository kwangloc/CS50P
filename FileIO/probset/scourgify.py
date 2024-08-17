import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # if get_extension(sys.argv[1]) != ".csv":
    #     sys.exit("Not a CSV file")
    try:
        students = []
        with open(sys.argv[1], newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        with open(sys.argv[2], "w", newline='') as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for student in students:
                last, first = student["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": student["house"]})
        # for student in students:
        #     print(f"{student['name']}, {student['house']}")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

# def get_extension(file_name):
#     try:
#         for i in range(len(file_name)-1, -1, -1):
#             if file_name[i] == ".":
#                 extension = file_name[i:]
#                 return extension
#         return None
#     except IndexError:
#         pass

if __name__ == "__main__":
    main()