# Reversing a linked list
    # All the links start pointing in the opposite direction.
    # The head starts pointing to the last element of the list.
"""
1.  previous: Initially pointing at None, this variable points to the previous element so the node.
    next link can be reversed using it. This is then updated to the node next to it, i.e., current.

2.  current: Initially pointing to head, the node being pointed to by this variable gets its node.
    next set to the previous item in the list. This is then updated to the node next to it,​ i.e., following.

3.  temp: Initially pointing to the second node , this is used so the current pointer may move one 
    step ahead in each iteration.
   
"""
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

    def reverse(self, head):
        previous = None
        while head:
            temp = head
            head = head.next
            temp.next = previous
            previous = temp
        
        return previous
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

l = LinkedList()
l.insertInBeginning(1)
l.insertInBeginning(2)
l.insertInBeginning(3)
newHead = l.reverse(l.head)

print("Before Reverse")
l.printList()

print("After Revers")
while newHead:
    print(newHead.data, end=" ")
    newHead = newHead.next