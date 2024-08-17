## write to a file
## opt 1
# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()
## opt 2
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

## read a file
## store all lines to a list
# with open("names.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     # print(line, end = "")
#     print(line.rstrip())
## iterate all lines in file
# with open("names.txt", "r") as file:
#     for line in file:
#         print(line.rstrip())
## best practice
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(name)



