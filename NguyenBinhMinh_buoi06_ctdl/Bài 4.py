class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example Usage:
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()
print("Length:", linked_list.length)