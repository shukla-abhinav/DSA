class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def Pop(self):
        self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def isEmpty(self):
        return len(self.elements) == 0

    def printStack(self):
        for i in self.elements:
            print(i,end=" ")

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.peek())
# stack.Pop()
# print(stack.peek())
# # stack.printStack()