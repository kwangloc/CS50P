clubs = []
with open("clubs.csv") as file:
    for line in file:
        name, coach = line.rstrip().split(",")
        # club = {}
        # club["name"] = name
        # club["coach"] = coach
        club = {"name": name, "coach": coach}
        clubs.append(club)

def get_name(club):
    return club["name"]

def get_coach(club):
    return club["coach"]

# for club in sorted(clubs, key=get_name):
#     print(f"{club['name']} is coached by {club['coach']}")
for club in sorted(clubs, key=lambda club: club["name"]):
    print(f"{club['name']} is coached by {club['coach']}")