class StackArray:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Test cases for StackArray
print("Stack using Array:")
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)
print("Peek:", stack_array.peek())  # Output: 3
print("Size:", stack_array.size())  # Output: 3
print("Pop:", stack_array.pop())    # Output: 3
print("Is empty:", stack_array.is_empty())  # Output: False
print("Size:", stack_array.size())  # Output: 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.stack_size = 0
    
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.stack_size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.stack_size -= 1
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self.stack_size

# Test cases for StackLinkedList
print("\nStack using Linked List:")
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)
print("Peek:", stack_linked_list.peek())  # Output: 3
print("Size:", stack_linked_list.size())  # Output: 3
print("Pop:", stack_linked_list.pop())    # Output: 3
print("Is empty:", stack_linked_list.is_empty())  # Output: False
print("Size:", stack_linked_list.size())  # Output: 2
