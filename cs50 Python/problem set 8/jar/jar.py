class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for i in range(self._size):
            cookies += "🍪"
        return f"{cookies}"

    def deposit(self, n):
        if n > (self._capacity - self._size):
            raise ValueError(
                "Cannot deposit more cookies than what jar's capacity allows"
            )
        else:
            self._size = self._size + n

    def withdraw(self, n):
        if n > self._size or n > self._capacity:
            raise ValueError("Cannot withdraw more cookies than what is in the jar")
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a positive integer")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Size cannot exceed jar's capacity")
        else:
            self._size = size
