def main():
    n = int(input("n = "))
    # print_column(n)
    # print_row(n)
    print_square(n)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        print("#" * size, end = "\n")

main()