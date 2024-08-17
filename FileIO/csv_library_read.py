import csv

clubs = []

## reader
# with open("clubs.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         clubs.append({"name": row[0], "coach": row[1]})
        
## DictReader
with open("csv_library.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # clubs.append({"name": row["name"], "coach": row["coach"]})
        clubs.append(row)

for club in sorted(clubs, key=lambda club: club["name"]):
    print(f"{club['name']} is coached by {club['coach']}")