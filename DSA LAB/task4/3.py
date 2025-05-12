class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
        else:
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.size  # Circular increment
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
        else:
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.size  # Circular increment
            return element
    
    def get_front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]
    
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[(self.rear - 1 + self.size) % self.size]
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)

print("Front element:", cq.get_front())  # Expected Output: 20
print("Rear element:", cq.get_rear())    # Expected Output: 60
