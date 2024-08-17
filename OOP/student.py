class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get(cls):
        while True:
            name = input("Name: ")
            house = input("House: ")
            try:
                return cls(name, house)
            except ValueError:
                pass

def main():
    student = Student.get()
    print(student)

# def get_student():
#     while True:
#         name = input("Name: ")
#         house = input("House: ")
#         try:
#             return Student(name, house)
#         except ValueError:
#             pass

if __name__ == "__main__":
    main()