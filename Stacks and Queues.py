class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push_to_stack(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.is_empty():
            self.head = value
        else:
            old = self.head
            self.head = value
            self.head.next = old

    def pop(self):
        if not self.is_empty():
            old = self.head
            self.head = self.head.next
            old.next = None
            return old.data
        else:
            return "Stack is empty"

    def is_empty(self):
        return self.head is None  # Returns boolean True or False

    # function to return head/ stack pointer of stack
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "Stack is empty"

    def __str__(self):
        print("--Stack--")
        output = ""
        current = self.head
        while current is not None:
            output += str(current.data) + "->"
            current = current.next
        if output:
            return "[" + output[:-2] + "]"
        return "[]"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Append value to the tail of queue
    def append_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.is_empty():
            self.head = value
        else:
            self.tail.next = value
        self.tail = value

    # Remove first value in queue
    def remove(self):
        if not self.is_empty():
            old = self.head
            self.head = self.head.next
            old.next = None
            return old.data
        else:
            return "Queue is empty"

    def is_empty(self):
        return self.head is None  # Returns boolean True or False

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "Queue is empty"

    def __str__(self):
        print("--Queue--")
        output = ""
        current = self.head
        while current is not None:
            output += str(current.data) + "->"
            current = current.next
        if output:
            return "[" + output[:-2] + "]"
        return "[]"


my_stack = Stack()
my_queue = Queue()

for i in range(1, 6):
    my_stack.push_to_stack(i)
    my_queue.append_value(i)

my_stack.pop()
my_queue.remove()

print(my_stack)
print(my_queue)
