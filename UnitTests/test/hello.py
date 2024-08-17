def main():
    name = input("What's your name?")
    print(hello(name))

def say_hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()