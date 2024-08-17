import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if get_extension(sys.argv[1]) != ".py":
        sys.exit("Not a Python file")
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        print(count_lines(lines))
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

def count_lines(lines):
    count = 0
    for line in lines:
        # if line.startswith("#") == False and line.isspace() == False:
        if line.strip().startswith("#") == False and line.strip() != "":
            count += 1
    return count

if __name__ == "__main__":
    main()