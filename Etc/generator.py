# sleep.py

def main():
    n = int(input("What's n? "))
    for s in sheep_yield(n):
        print(s)

# normal way
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock
# generator yield
def sheep_yield(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()