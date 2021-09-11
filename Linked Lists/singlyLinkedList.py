class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insertInBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


    def insertAfter(self,node,data):
        if node is None:
            print("Node is not in the Linked List!")
            return
        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode


    def insertLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    def deleteNodeBeginning(self):
        if self.head is None:
            print("Linked List Empty")
            return
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            print("Linked List Empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next.next is None:
                temp.next = None
                
    def deleteMiddle(self,pos):
        if self.head is None:
            print("Linked List Empty")
            return
        if pos == 0:
            self.deleteNodeBeginning()
            return
        
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == pos:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def reverse(self, head):
        previous = None
        
        while head:
            
            temp = head
            head = head.next
            temp.next = previous
            previous = temp
        
        return previous

l = LinkedList()
l.insertInBeginning(1)
l.insertInBeginning(2)
l.insertInBeginning(3)
# l.insertLast("A")
# l.insertLast("B")
# l.insertLast(10)
# l.insertAfter(l.head.next,5)
# l.insertAfter(l.head.next.next.next,"Apple")
# # l.deleteNodeBeginning()
# # l.deleteNodeBeginning()
# # l.deleteLast()
# # l.deleteLast()
# l.deleteMiddle(2)
# l.deleteMiddle(3)

# l.printList()

