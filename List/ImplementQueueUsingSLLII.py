class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class ImplementQueueUsingLList:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

    def enqueue(self, data: int):
        new_node = ListNode(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        print("Queue: ", end="")
        while current:
            print(current.data, end=" -> " if current.next else " -> null")
            current = current.next
        print()


# Example usage
if __name__ == "__main__":
    queue = ImplementQueueUsingLList()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()

    print("Dequeued:", queue.dequeue())
    queue.display()

    print("Front element:", queue.peek())
    print("Queue size:", queue.size())
