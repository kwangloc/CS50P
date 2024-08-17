class Jar:
    # size = 0
    # capacity = 0
    def __init__(self, capacity = 12, size = 0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return("🍪"*self.size)

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size

def main():
    jar_1 = Jar()
    print(str(jar_1))
    jar_1.deposit(5)
    print(str(jar_1))

if __name__ == "__main__":
    main()