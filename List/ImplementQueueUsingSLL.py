"""
Queue - Linked List Implementation

In this article, the Linked List implementation of the queue data structure is discussed and implemented. Print '-1' if the queue is empty.
Approach: To solve the problem follow the below idea:
we maintain two pointers, front and rear. The front points to the first item of the queue and rear points to the last item.

enQueue(): This operation adds a new node after the rear and moves the rear to the next node.
deQueue(): This operation removes the front node and moves the front to the next node.

"""

from Node import SingleLinkedList as Node


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data: int):
        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
            self.printQueue()
            return
        self.rear.next = newNode
        self.rear = newNode
        self.printQueue()

    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        self.printQueue()
        return temp.data

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        queue_string = "Current Queue: "
        while temp is not None:
            queue_string += str(temp.data) + " "
            temp = temp.next
        print(queue_string)


q = Queue()

# Enqueue elements into the queue
q.enqueue(10)
q.enqueue(20)

# Dequeue elements from the queue
q.dequeue()
q.dequeue()

# Enqueue more elements into the queue
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Dequeue an element from the queue
q.dequeue()
