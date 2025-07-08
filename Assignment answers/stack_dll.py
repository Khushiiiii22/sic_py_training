class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class StackDLL:
    def __init__(self):
        self.head = None  # Points to the front of the list
        self.tail = None  # Points to the rear (top of stack)
        self._size = 0

    def is_empty(self):
        return self.tail is None

    def push(self, data):
        new_node = DLLNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: The stack is empty.")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.tail.data

    def size(self):
        return self._size

    def display(self):
        current = self.head
        print("Stack (bottom -> top): ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    stack = StackDLL()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()         # Output: Stack (bottom -> top): 10 <-> 20 <-> 30 <-> None
    print("Popped:", stack.pop())  # Output: Popped: 30
    stack.display()         # Output: Stack (bottom -> top): 10 <-> 20 <-> None
    print("Peek:", stack.peek())   # Output: Peek: 20
    print("Size:", stack.size())   # Output: Size: 2
