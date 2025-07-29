class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class ImplementStackUsingLList:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def push(self, data: int):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack: null")
            return

        current = self.top
        print("Stack:")
        while current:
            print(current.data, end=" -> " if current.next else " -> null ")
            current = current.next
        print()


# Example usage
if __name__ == "__main__":
    stack = ImplementStackUsingLList()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    print("Popped:", stack.pop())
    stack.display()

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())
