class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def create_loop(self, position):
        current = self.head
        loop_node = None
        count = 0
        while current and current.next:
            if count == position:
                loop_node = current
            current = current.next
            count += 1
        if loop_node:
            current.next = loop_node
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_loop_start(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def remove_loop(self):
        loop_start = self.find_loop_start()
        if not loop_start:
            return
        current = loop_start
        while current.next != loop_start:
            current = current.next
        current.next = None
    
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.create_loop(2)

if sll.detect_loop():
    print("Loop detected at node:", sll.find_loop_start().data)
    sll.remove_loop()
    print("Loop removed, LinkedList:")
    sll.display()
else:
    print("No loop detected.")
