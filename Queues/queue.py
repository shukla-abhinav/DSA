"""
enqueue
dequeue
rear
front
isEmpty
"""
class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self,data):
        self.elements.append(data)
    
    def dequeue(self):
        # [1,2,3,4]
        return self.elements.pop(0)

    def rear(self):
        return self.elements[-1]

    def front(self):
        return self.elements[0]

    def isEmpty(self):
        return len(self.elements) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print("front: ",q.front())
print("rear: ",q.rear())

q.dequeue()

print("front: ",q.front())
print("rear: ",q.rear())