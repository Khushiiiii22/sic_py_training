class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            # Queue has only one element, reset after dequeue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No peek value.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("No element in the circular queue")
            return
        print("Circular Queue:", end=" ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

# Example usage
if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()  # Output: Circular Queue: 1 2 3 4 5
    cq.dequeue()
    cq.display()  # Output: Circular Queue: 2 3 4 5
    cq.enqueue(6)
    cq.display()  # Output: Circular Queue: 2 3 4 5 6
    print("Front element:", cq.peek())  # Output: Front element: 2
