# create node class with basic features: data and reference pointer
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

# create basic linkedlist which we will be tracking both the head and tail
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #funtion for adding nodes to end of list
    def append_value(self, value):
        if not isinstance(value, Node): # this checks if value passed is a node or not.
            value = Node(value)
        if self.head == None: # checks if head node is empty to indicate empty list or not
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
    
    # function to add nodes to beginning of linked list
    def left_append_value(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head = value
        else:
            old = self.head
            self.head = value
            self.head.next = old # references head pointer to the previous head value
    
    # function to search for node in list by passing index as parameter
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
    
    # function to remove node from list by passing index as parameter.
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

    # function to determine length of linked list.
    def length_list(self):
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length += 1
        return f"length of linked list is {length}"

    # EXTRA FEATURE- WITH UPCOMING APPLICATIONS (palidrome, etc). 
    # This function reverses list recursively.
    def reverse_list_recursively(self, current, previous):
        if self.head == None:  # checks for empty list
            return
        elif current.next == None:  # checks if at last node in list
            self.tail = self.head
            current.next = previous  # references the pointer of the current node to the previous instead of the next one.
            self.head = current  # sets current (last node) as head
        else:
            next = current.next  # stores value of next node (node to the right of current) in a variable
            current.next = previous  # sets pointer of current node to previous node instead of next
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

