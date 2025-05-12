import time
import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def display(self):
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")

class HashTableLinearProbing:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

    def display(self):
        for i, pair in enumerate(self.table):
            if pair is not None:
                print(f"Index {i}: ({pair[0]}, {pair[1]})")
            else:
                print(f"Index {i}: None")

def compare_methods():
    keys = [random.randint(1, 10000) for _ in range(1000)]
    values = [random.randint(1, 10000) for _ in range(1000)]

    chaining_table = HashTableChaining(size=200)
    start_time = time.time()
    for key, value in zip(keys, values):
        chaining_table.insert(key, value)
    chaining_insert_time = time.time() - start_time

    start_time = time.time()
    for key in keys:
        chaining_table.get(key)
    chaining_search_time = time.time() - start_time

    probing_table = HashTableLinearProbing(size=2000)
    start_time = time.time()
    for key, value in zip(keys, values):
        probing_table.insert(key, value)
    probing_insert_time = time.time() - start_time

    start_time = time.time()
    for key in keys:
        probing_table.get(key)
    probing_search_time = time.time() - start_time

    print("Performance Comparison:")
    print(f"Chaining - Insert Time: {chaining_insert_time:.6f}s, Search Time: {chaining_search_time:.6f}s")
    print(f"Linear Probing - Insert Time: {probing_insert_time:.6f}s, Search Time: {probing_search_time:.6f}s")

if __name__ == "__main__":
    print("Testing Separate Chaining:")
    chaining_table = HashTableChaining(size=10)
    chaining_table.insert("a", 1)
    chaining_table.insert("b", 2)
    chaining_table.insert("c", 3)
    chaining_table.display()
    print("Get 'b':", chaining_table.get("b"))
    chaining_table.delete("b")
    chaining_table.display()

    print("\nTesting Linear Probing:")
    probing_table = HashTableLinearProbing(size=10)
    probing_table.insert("a", 1)
    probing_table.insert("b", 2)
    probing_table.insert("c", 3)
    probing_table.display()
    print("Get 'b':", probing_table.get("b"))
    probing_table.delete("b")
    probing_table.display()

    print("\nComparing Methods:")
    compare_methods()
