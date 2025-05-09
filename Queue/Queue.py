class QueueUsingArray:
    def __init__(self):
        self.QUEUE_SIZE = 100
        self.queue = [None] * self.QUEUE_SIZE
        self.front = 0
        self.rear = 0

    def enqueue(self):
        """Add an element to the rear of the queue"""
        if self.rear == self.QUEUE_SIZE - 1:
            print("Queue is full!")
        else:
            try:
                data = int(input("Enter the Element: "))
                self.queue[self.rear] = data
                self.rear += 1
            except ValueError:
                print("Please enter a valid integer!")

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            print(f"Element is deleted = {self.queue[self.front]}")
            self.queue[self.front] = None  # Optional: clear the position
            self.front += 1

    def display(self):
        """Display all elements in the queue"""
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            print("Queue elements:")
            for i in range(self.front, self.rear):
                print(f"→ {self.queue[i]}", end=" ")
            print()  # New line after display

def main():
    queue = QueueUsingArray()
    
    while True:
        print("\n" + "-" * 37)
        print("1-Insert From Rear")
        print("2-Delete From Front")
        print("3-Display")
        print("4-Exit")
        print("-" * 37 + "\n")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        print("-" * 37)
        
        if choice == 1:
            queue.enqueue()
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    """
    Queue Implementation Notes:
    - Linear queue using array (fixed size of 100)
    - Follows FIFO (First-In-First-Out) principle
    - Simple array-based implementation
    - Limitations:
      - Wasted space as elements are dequeued
      - Doesn't reuse empty spaces (unlike circular queue)
    - For better space utilization, consider circular queue implementation
    """
    main()