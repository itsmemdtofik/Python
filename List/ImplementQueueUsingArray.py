"""
Array implementation of queue - Simple:

To implement a queue of size n using an array, the operations are as follows:
Enqueue: Adds new elements to the end of the queue. Checks if the queue has space before insertion, then increments the size.
Dequeue: Removes the front element by shifting all remaining elements one position to the left. Decrements the queue size after removal.
getFront: Returns the first element of the queue if it's not empty. Returns -1 if the queue is empty.
Display: Iterates through the queue from the front to the current size and prints each element.
"""


class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.is_empty():
            self.q.pop(0)

    def get_front(self):
        return -1 if self.is_empty() else self.q[0]

    def display(self):
        print(' '.join(map(str, self.q)))


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.get_front())
    q.dequeue()
    q.enqueue(4)
    q.display()
