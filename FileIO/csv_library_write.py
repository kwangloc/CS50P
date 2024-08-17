import csv

name = input("What's the club name? ").rstrip()
coach = input("Who's the coach? ").rstrip()

# with open("csv_library.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, coach])

with open("csv_library.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "coach"])
    writer.writerow({"name": name, "coach": coach})