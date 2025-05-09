class QueueUsingLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        """Add an element to the rear of the queue"""
        try:
            data = int(input("Enter the data: "))
            new_node = self.Node(data)
            
            if self.front is None and self.rear is None:
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node
        except ValueError:
            print("Please enter a valid integer!")

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.front is None and self.rear is None:
            print("Queue is empty!")
        else:
            if self.front == self.rear:
                # Only one element in queue
                print(f"Dequeued element: {self.front.data}")
                self.front = None
                self.rear = None
            else:
                print(f"Dequeued element: {self.front.data}")
                self.front = self.front.next

    def display(self):
        """Display all elements in the queue"""
        if self.front is None and self.rear is None:
            print("Queue is empty!")
        else:
            print("Queue elements:")
            current = self.front
            while current is not None:
                print(f"→ {current.data}", end=" ")
                current = current.next
            print()  # New line after display

def main():
    queue = QueueUsingLinkedList()
    
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
    - Linked List implementation of Queue
    - Follows FIFO (First-In-First-Out) principle
    - Dynamic size (no fixed capacity)
    - Advantages:
      - No size limitation (except memory)
      - Efficient enqueue/dequeue operations (O(1))
    - Uses inner Node class to represent elements
    """
    main()