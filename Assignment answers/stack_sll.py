class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Points to the head (front) of the list
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Link new node to current top
        self.top = new_node       # Update top to new node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: The stack is empty.")
        popped_node = self.top
        self.top = self.top.next  # Move top to next node
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.data

    def stack_size(self):
        return self.size

    def display(self):
        current = self.top
        print("Stack (top -> bottom): ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()         # Output: Stack (top -> bottom): 30 -> 20 -> 10 -> None
    print("Popped:", stack.pop())  # Output: Popped: 30
    stack.display()         # Output: Stack (top -> bottom): 20 -> 10 -> None
    print("Peek:", stack.peek())   # Output: Peek: 20
    print("Size:", stack.stack_size())  # Output: Size: 2
