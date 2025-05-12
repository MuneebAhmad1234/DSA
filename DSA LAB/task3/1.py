class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
    
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        current_position = 0
        while current and current_position < position - 1:
            current = current.next
            current_position += 1
        if current is None:
            print("Position out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node
    
    def delete_by_value(self, data):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            print(f"Value {data} not found in the list.")
        else:
            current.next = current.next.next
    
    def search_by_value(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

sll = SinglyLinkedList()

sll.insert_at_beginning(1)
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
sll.display()

sll.insert_at_end(4)
sll.display()

sll.insert_at_position(5, 2)
sll.display()

sll.delete_by_value(5)
sll.display()

position = sll.search_by_value(4)
print(f"Found 4 at position: {position}")

position = sll.search_by_value(6)
print(f"Found 6 at position: {position}")
