"""
! Stack:
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
This means that the last element added to the stack is the first one to be removed.

? Operations on a Stack:
* 1. Push(): Add an item to the top of stack.
* 2. Pop(): Remove an item from the top of stack.
* 3. Peek(): Returns the top without removing it.
* 4. isEmpty(): Check if stack is empty or not.
* 5. size(): Returns the number of elements in the stack.

TODO: Real world example: 1. Browser History, 2. Undo Functions in text editor.

@param Application: Depth First Search in graphs.
"""

class StackUsingArray:
    def __init__(self):
        self.top = -1
        self.MAX_SIZE = 10
        self.arr = [0] * self.MAX_SIZE

    def overflow(self):
        print("Overflow Condition: Stack is full.")

    def underflow(self):
        print("Underflow Condition: Stack is empty.")

    def push(self):
        if self.top == self.MAX_SIZE - 1:
            self.overflow()
        else:
            element = int(input("Enter the element to insert into the stack: "))
            self.top += 1
            self.arr[self.top] = element
            print(f"Element pushed: {element}")

    def pop(self):
        if self.top == -1:
            self.underflow()
        else:
            print(f"Element popped: {self.arr[self.top]}")
            self.top -= 1

    def display(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.arr[i])

def main():
    stack = StackUsingArray()

    while True:
        print("--------------------------")
        print("1 - Push")
        print("2 - Pop")
        print("3 - Display")
        print("4 - Exit")
        print("--------------------------")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            stack.push()
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
