# import random


# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")

# run the sort function without creating a particular instance
import random


class Hat:
    # def __init__(self):
    #     self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    n = 1
    # @classmethod
    # def sort(cls, name):
    #     print(name, "is in", random.choice(cls.houses))


# Hat.sort("Harry")
hat_1 = Hat()
hat_2 = Hat()
print(hat_1.n)
print(hat_2.n)
hat_1.n += 1
print(hat_1.n)
print(hat_2.n)