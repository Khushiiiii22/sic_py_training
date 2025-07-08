class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class QueueDLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = DLLNode(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def size(self):
        return self._size

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
