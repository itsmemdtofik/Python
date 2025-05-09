
#! Doubly Linked List
'''
#!Why do we need self?

#?Access Instance Variables: 
We need self to refer to instance-specific variables (like self.head, self.data, etc.) that are unique to each object. Without self, all variables would belong to the class itself, not specific instances.

#!Binding the Method to the Object: 
Using self allows each object to call methods and modify its own properties independently of other objects. Every time you call a method on an object, it knows which object it’s working with, thanks to self.

#!Understanding self
Instance Variables: Each object of the class may have different values for its properties (variables). To refer to these properties (like head, next, prev), we use self.

#!Methods and self: 
When you define a method inside a class, self allows that method to access and modify the properties of the object the method is called on. Without self, you wouldn't be able to refer to or modify the instance's state.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):#Initialize an empty list
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # 3. Insert after a node
    def insert_after(self, prev_data, data):
        current = self.head
        while current is not None and current.data != prev_data:
            current = current.next
        if current is not None:
            new_node = Node(data)
            new_node.next = current.next
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        else:
            print(f"Node with data {prev_data} not found.")

    # 4. Delete by value
    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        current = self.head
        while current is not None and current.data != data:
            current = current.next
        if current is not None:
            if current.next is not None:
                current.next.prev = current.prev
            if current.prev is not None:
                current.prev.next = current.next
        else:
            print(f"Node with data {data} not found.")

    # 5. Delete from the beginning
    def delete_from_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    # 6. Delete from the end
    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None

    # 7. Delete after a node
    def delete_after(self, prev_data):
        current = self.head
        while current is not None and current.data != prev_data:
            current = current.next
        if current is not None and current.next is not None:
            to_delete = current.next
            current.next = to_delete.next
            if to_delete.next is not None:
                to_delete.next.prev = current
        else:
            print(f"No node found to delete after {prev_data}")

    # 8. Search an element
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # 9. Traverse the list from head to tail
    def traverse_forward(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # 10. Traverse the list from tail to head
    def traverse_backward(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    # 11. Find the length of the list
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # 12. Find the middle element
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow is not None else -1

    # 13. Detect a loop
    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 14. Find the intersection of two linked lists
    @staticmethod
    def get_intersection(list1, list2):
        current1 = list1.head
        current2 = list2.head
        while current1 is not None:
            while current2 is not None:
                if current1 == current2:
                    return current1
                current2 = current2.next
            current2 = list2.head
            current1 = current1.next
        return None

    # 15. Merge two sorted doubly linked lists
    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = DoublyLinkedList()
        current1 = list1.head
        current2 = list2.head
        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next
        while current1 is not None:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        while current2 is not None:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        return merged_list

    # 16. Remove duplicates
    def remove_duplicates(self):
        current = self.head
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if current.data == next_node.data:
                    if next_node.next is not None:
                        next_node.next.prev = current
                    current.next = next_node.next
                next_node = next_node.next
            current = current.next

    # 17. Remove N-th node from the end
    def remove_nth_from_end(self, n):
        length = self.length()
        if n > length:
            return
        if n == length:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        current = self.head
        for _ in range(1, length - n):
            current = current.next
        to_delete = current.next
        current.next = to_delete.next
        if to_delete.next is not None:
            to_delete.next.prev = current

    # 18. Get N-th node from the end
    def get_nth_from_end(self, n):
        length = self.length()
        if n > length:
            return -1
        current = self.head
        for _ in range(1, length - n):
            current = current.next
        return current.data

    # 19. Check if the list is empty
    def is_empty(self):
        return self.head is None

    # 20. Get the head node
    def get_head(self):
        return self.head

    # 21. Clear the list
    def clear(self):
        self.head = None

    # 22. Clone the list
    def clone_list(self):
        cloned_list = DoublyLinkedList()
        current = self.head
        while current is not None:
            cloned_list.insert_at_end(current.data)
            current = current.next
        return cloned_list

    # 23. Swap nodes in pairs
    def swap_pairs(self):
        current = self.head
        while current is not None and current.next is not None:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next

    # 24. Flatten a multi-level linked list
    def flatten(self):
        pass  # Simplified version, no implementation

def main():
    dll = DoublyLinkedList()
    
    while True:
        print("\nChoose an operation:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert after a node")
        print("4. Delete by value")
        print("5. Delete from the beginning")
        print("6. Delete from the end")
        print("7. Delete after a node")
        print("8. Search an element")
        print("9. Traverse forward")
        print("10. Traverse backward")
        print("11. Length")
        print("12. Find middle")
        print("13. Detect loop")
        print("14. Find intersection")
        print("15. Merge two sorted lists")
        print("16. Remove duplicates")
        print("17. Remove N-th node from the end")
        print("18. Get N-th node from the end")
        print("19. Check if empty")
        print("20. Clear the list")
        print("21. Clone the list")
        print("22. Swap pairs")
        print("23. Flatten list")
        print("24. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insert_at_end(data)
        elif choice == 3:
            prev = int(input("Enter node to insert after: "))
            data = int(input("Enter data: "))
            dll.insert_after(prev, data)
        elif choice == 4:
            data = int(input("Enter data to delete: "))
            dll.delete_by_value(data)
        elif choice == 5:
            dll.delete_from_beginning()
        elif choice == 6:
            dll.delete_from_end()
        elif choice == 7:
            prev = int(input("Enter node to delete after: "))
            dll.delete_after(prev)
        elif choice == 8:
            data = int(input("Enter data to search: "))
            print("Found:", dll.search(data))
        elif choice == 9:
            dll.traverse_forward()
        elif choice == 10:
            dll.traverse_backward()
        elif choice == 11:
            print("Length:", dll.length())
        elif choice == 12:
            print("Middle:", dll.find_middle())
        elif choice == 13:
            print("Loop detected:", dll.detect_loop())
        elif choice == 14:
            pass  # Implement intersection if needed
        elif choice == 15:
            list2 = DoublyLinkedList()
            print("Merging two sorted lists...")
            merged_list = DoublyLinkedList.merge_sorted(dll, list2)
            merged_list.traverse_forward()
        elif choice == 16:
            dll.remove_duplicates()
        elif choice == 17:
            n = int(input("Enter N: "))
            dll.remove_nth_from_end(n)
        elif choice == 18:
            n = int(input("Enter N: "))
            print("Nth from end:", dll.get_nth_from_end(n))
        elif choice == 19:
            print("Is empty:", dll.is_empty())
        elif choice == 20:
            dll.clear()
        elif choice == 21:
            cloned_list = dll.clone_list()
            cloned_list.traverse_forward()
        elif choice == 22:
            dll.swap_pairs()
        elif choice == 23:
            dll.flatten()
        elif choice == 24:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()