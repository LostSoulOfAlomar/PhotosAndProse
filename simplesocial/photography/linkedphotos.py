class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def InsertStart(self, data):

        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size1(self):
        return self.size

    def insertEnd(self, data):

        self.size = self.size+1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self, data):
        if self.head == None:
            pass

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


linked_list = LinkedList()

# linked_list.InsertStart(12)
# linked_list.InsertStart(122)
# linked_list.InsertStart(3)
linked_list.insertEnd(31)

# linked_list.traverseList()
# print(linked_list.size)
# linked_list.remove(31)
# linked_list.remove(3)
linked_list.traverseList()

print(linked_list.size)
