class CircularQueueUsingArray:
    def __init__(self):
        self.QUEUE_SIZE = 1024
        self.front = 0
        self.rear = 0
        self.queue = [None] * self.QUEUE_SIZE

    def enqueue(self):
        """Add an element to the rear of the queue"""
        if self.front == (self.rear + 1) % self.QUEUE_SIZE:
            print("Queue is full!")
        else:
            data = int(input("Enter the element: "))
            self.rear = (self.rear + 1) % self.QUEUE_SIZE
            self.queue[self.rear] = data

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            self.front = (self.front + 1) % self.QUEUE_SIZE
            element = self.queue[self.front]
            print(f"Element deleted is: {element}")
            self.queue[self.front] = None  # Optional: clear the position

    def display(self):
        """Display all elements in the queue"""
        if self.front == self.rear:
            print("Queue is empty!")
        else:
            print("Queue elements:")
            i = (self.front + 1) % self.QUEUE_SIZE
            while True:
                print(f"→ {self.queue[i]}", end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.QUEUE_SIZE
            print()  # New line after display

def main():
    cq = CircularQueueUsingArray()
    
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
            cq.enqueue()
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    """
    Circular Queue Implementation Notes:
    - Uses fixed-size array (1024 elements)
    - Follows FIFO (First-In-First-Out) principle
    - Efficient space utilization via modulo arithmetic
    - Time complexity: O(1) for enqueue/dequeue operations
    - Avoids the problem of wasted space in linear queues
    """
    main()