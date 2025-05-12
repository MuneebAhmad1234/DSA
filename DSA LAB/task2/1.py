class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert_end(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def display(self):
        print(self.array[:self.size])


dynamic_array = DynamicArray()

dynamic_array.insert_end(10)
dynamic_array.insert_end(20)
dynamic_array.insert_end(30)

dynamic_array.display()

dynamic_array.insert_at(1, 15)
dynamic_array.display()

dynamic_array.delete_at(2)
dynamic_array.display()

print(dynamic_array.search(15))
print(dynamic_array.search(100))
