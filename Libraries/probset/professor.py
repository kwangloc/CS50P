import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        num_1 = generate_integer(level)
        num_2 = generate_integer(level)
        res = num_1 + num_2
        for i in range(3):
            try:
                ans = int(input(f"{num_1} + {num_2} = "))
            except ValueError:
                print("EEE")
            else:
                if ans != res:
                    print("EEE")
                else:
                    score += 1
                    break
            if i == 2:
                print(f"{num_1} + {num_2} = {res}")
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()