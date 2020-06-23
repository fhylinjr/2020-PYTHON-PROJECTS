class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
        else:
            self.tail.next = value
        self.tail = value

    def __str__(self):
        output = ""
        current = self.head
        while current is not None:
            output += str(current.data) + "->"
            current = current.next
        if output:
            return "[" + output[:-2] + "]"
        return "[]"

    def left_append_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
        else:
            old = self.head
            self.head = value
            self.head.next = old

    def search_value(self, index):
        current = self.head
        position = 0
        while position != index:
            current = current.next
            position += 1
        if position == index:
            return f"{current.data} found at index {index}"
        else:
            return f"No value at index {index}"

    def remove_value(self, index):
        current = self.head
        position = 0
        while position != index:
            last = current
            current = current.next
            position += 1
        if position == index:
            last.next = current.next
        return

    def length_list(self):
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length += 1
        return f"length of linked list is {length}"

    def reverse_list_recursively(self, current, previous):
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recursively(next, current)


my_list = LinkedList()
my_list.append_value(1)
my_list.append_value(2)
my_list.append_value(3)
my_list.append_value(4)
my_list.append_value(5)
print(my_list)
my_list.left_append_value(6)
#print(my_list.length_list())
#print(my_list.search_value(2))
#print(my_list.remove_value(3))
print(my_list)

my_list.reverse_list_recursively(my_list.head, None)
print(my_list)

