def main():
    greeting = input("Greeting: ")
    res = handle_greeting(greeting.strip().lower())
    print(f"${res}")

def handle_greeting(greeting):
    sub_greeting = greeting[0:5]
    print(sub_greeting)
    if sub_greeting == "hello":
        return 0
    elif sub_greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()