
#! Stack using a class and built in list (append(), pop(), len())

class Stack:

    def __init__(self):
        self._stack = [] #Making private

    def is_empty(self):
        return len(self._stack) == 0
    
    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack!")
        return self._stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack!")
        else:
            return self._stack[-1]
    
    def size(self):
        return len(self._stack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack (top to bottom) :")
            for item in reversed(self._stack):
                print(item)
    
    def __repr__(self):
        return f"Stack ({self._stack})"
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.display()
print(f"The size of stack is : {stack.size()}")

stack.push(30)
stack.push(40)
stack.display()
print(f"The size of stack is : {stack.size()}")

stack.pop()
stack.display()
print(f"The size of stack is : {stack.size()}")
stack.pop()


print(f"The peek element from the stack is : {stack.peek()}")
stack.display()
print(f"The size of stack is : {stack.size()}")

print(repr(stack), type(stack))
