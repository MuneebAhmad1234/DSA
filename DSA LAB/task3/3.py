class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def delete_at_position(self, position):
        if not self.head:
            return "List is empty"
        current = self.head
        count = 0
        while current:
            if count == position:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                current = None
                return
            current = current.next
            count += 1
        return "Position out of bounds"
    
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")
    
    def traverse_reverse(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ← ")
            current = current.prev
        print("None")

# Testing the Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_beginning(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)

print("Doubly Linked List (Forward Traversal):")
dll.traverse_forward()  # Expected Output: 1 → 2 → 3 → 4 → 5 → None

print("Doubly Linked List (Reverse Traversal):")
dll.traverse_reverse()  # Expected Output: 5 ← 4 ← 3 ← 2 ← 1 ← None

dll.delete_at_position(2)
print("\nAfter deleting the node at position 2 (0-indexed):")
dll.traverse_forward()  # Expected Output: 1 → 2 → 4 → 5 → None
