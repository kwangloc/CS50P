import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if get_extension(sys.argv[1]) != ".csv":
        sys.exit("Not a CSV file")
    try:
        pizzas = []
        with open(sys.argv[1], newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append(row)
        print(tabulate(pizzas, headers = "keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def get_extension(file_name):
    try:
        for i in range(len(file_name)-1, -1, -1):
            if file_name[i] == ".":
                extension = file_name[i:]
                return extension
        return None
    except IndexError:
        pass

if __name__ == "__main__":
    main()