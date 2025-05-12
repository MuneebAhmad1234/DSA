class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_head(new_node)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    print(cache.get(1))
    cache.put(3, "C")
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, "D")
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
