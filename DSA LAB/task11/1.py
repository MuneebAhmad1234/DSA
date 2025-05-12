class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    # Chaining (Linked List) Collision Handling
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return

    # Open Addressing (Linear Probing) Collision Handling
    def insert_linear_probing(self, key, value):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if isinstance(self.table[index], list) and self.table[index][0] == key:
                self.table[index][1] = value
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("HashTable is full")
        self.table[index] = [key, value]

    def get_linear_probing(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if isinstance(self.table[index], list) and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete_linear_probing(self, key):
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            if isinstance(self.table[index], list) and self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break


# Testing the HashTable
if __name__ == "__main__":
    print("Testing Chaining:")
    ht = HashTable(10)
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("name", "Bob")  # Update value
    print(ht.get("name"))  # Output: Bob
    print(ht.get("age"))  # Output: 25
    ht.delete("age")
    print(ht.get("age"))  # Output: None

    print("\nTesting Linear Probing:")
    ht_lp = HashTable(10)
    ht_lp.insert_linear_probing("name", "Alice")
    ht_lp.insert_linear_probing("age", 25)
    ht_lp.insert_linear_probing("name", "Bob")  # Update value
    print(ht_lp.get_linear_probing("name"))  # Output: Bob
    print(ht_lp.get_linear_probing("age"))  # Output: 25
    ht_lp.delete_linear_probing("age")
    print(ht_lp.get_linear_probing("age"))  # Output: None