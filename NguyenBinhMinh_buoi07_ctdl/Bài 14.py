class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


myQueue = Queue(4)
myQueue.printQueue()