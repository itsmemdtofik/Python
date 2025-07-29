class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # 3. Insert after a node
    def insert_after(self, prev_data, data):
        current = self.head
        while current is not None and current.data != prev_data:
            current = current.next
        if current is not None:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        else:
            print(f"Node with data {prev_data} not found.")

    # 4. Delete by value
    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        else:
            print(f"Node with data {data} not found.")

    # 5. Delete from the beginning
    def delete_from_beginning(self):
        if self.head is not None:
            self.head = self.head.next

    # 6. Delete from the end
    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    # 7. Delete after a node
    def delete_after(self, prev_data):
        current = self.head
        while current is not None and current.data != prev_data:
            current = current.next
        if current is not None and current.next is not None:
            current.next = current.next.next
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

    # 9. Traverse the list
    def traverse(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    # 10. Reverse the list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

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

    # 14. Merge two sorted linked lists
    @staticmethod
    def merge_sorted(list1, list2):
        merged_list = SinglyLinkedList()
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

    # 15. Remove duplicates
    def remove_duplicates(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    # 16. Remove N-th node from the end
    def remove_nth_from_end(self, n):
        length = self.length()
        if n > length:
            return
        if n == length:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(1, length - n):
            current = current.next
        current.next = current.next.next

    # 17. Get N-th node from the end
    def get_nth_from_end(self, n):
        length = self.length()
        if n > length:
            return -1
        current = self.head
        for _ in range(1, length - n):
            current = current.next
        return current.data

    # 18. Check if the list is empty
    def is_empty(self):
        return self.head is None

    # 19. Get the head node
    def get_head(self):
        return self.head

    # 20. Clear the list
    def clear(self):
        self.head = None

    # 21. Clone the list
    def clone_list(self):
        cloned_list = SinglyLinkedList()
        current = self.head
        while current is not None:
            cloned_list.insert_at_end(current.data)
            current = current.next
        return cloned_list

    # 22. Swap nodes in pairs
    def swap_pairs(self):
        current = self.head
        while current is not None and current.next is not None:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next

    # 23. Flatten a multi-level linked list
    def flatten(self):
        pass  # Simplified version, no implementation

def main():
    sll = SinglyLinkedList()
    
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
        print("9. Traverse")
        print("10. Reverse")
        print("11. Length")
        print("12. Find middle")
        print("13. Detect loop")
        print("14. Merge two sorted lists")
        print("15. Remove duplicates")
        print("16. Remove N-th node from the end")
        print("17. Get N-th node from the end")
        print("18. Check if empty")
        print("19. Clear the list")
        print("20. Clone the list")
        print("21. Swap pairs")
        print("22. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            data = int(input("Enter data: "))
            sll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            sll.insert_at_end(data)
        elif choice == 3:
            prev = int(input("Enter node to insert after: "))
            data = int(input("Enter data: "))
            sll.insert_after(prev, data)
        elif choice == 4:
            data = int(input("Enter data to delete: "))
            sll.delete_by_value(data)
        elif choice == 5:
            sll.delete_from_beginning()
        elif choice == 6:
            sll.delete_from_end()
        elif choice == 7:
            prev = int(input("Enter node to delete after: "))
            sll.delete_after(prev)
        elif choice == 8:
            data = int(input("Enter data to search: "))
            print("Found:", sll.search(data))
        elif choice == 9:
            sll.traverse()
        elif choice == 10:
            sll.reverse()
        elif choice == 11:
            print("Length:", sll.length())
        elif choice == 12:
            print("Middle:", sll.find_middle())
        elif choice == 13:
            print("Loop detected:", sll.detect_loop())
        elif choice == 14:
            list2 = SinglyLinkedList()
            print("Merging two sorted lists...")
            merged_list = SinglyLinkedList.merge_sorted(sll, list2)
            merged_list.traverse()
        elif choice == 15:
            sll.remove_duplicates()
        elif choice == 16:
            n = int(input("Enter N: "))
            sll.remove_nth_from_end(n)
        elif choice == 17:
            n = int(input("Enter N: "))
            print("Nth from end:", sll.get_nth_from_end(n))
        elif choice == 18:
            print("Is empty:", sll.is_empty())
        elif choice == 19:
            sll.clear()
        elif choice == 20:
            cloned = sll.clone_list()
            cloned.traverse()
        elif choice == 21:
            sll.swap_pairs()
        elif choice == 22:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()