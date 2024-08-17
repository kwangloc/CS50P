import random
import sys
    
def main():
    n = get_int("Level: ")
    number = random.randint(1,n)
    while True:
        guess = get_int("Guess: ")
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            sys.exit("Just right!")

def get_int(statement):
    while True:
        try:
            n = int(input(statement))
        except ValueError:
            pass
        else:
            if n > 0:
                return n    

main()