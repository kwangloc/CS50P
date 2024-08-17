# MEOW = 3

# for _ in range(MEOW):
#     print("meow")

class Cat:
    MEOW = 3 # class constant
    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")

cat = Cat()
cat.meow()

# # type hints

def meow(n: int) -> str:
    """
    meow n times
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n"*n

# number: int = int(input("Number: "))
# meow(number)