# ! Doubly Linked List
"""
#!Why do we need self?

#?Access Instance Variables: 
We need self to refer to instance-specific variables (like self.head, self.data, etc.) that are unique to each object. Without self, all variables would belong to the class itself, not specific instances.

#!Binding the Method to the Object: 
Using self allows each object to call methods and modify its own properties independently of other objects. Every time you call a method on an object, it knows which object it’s working with, thanks to self.

#!Understanding self
Instance Variables: Each object of the class may have different values for its properties (variables). To refer to these properties (like head, next, prev), we use self.

#!Methods and self: 
When you define a method inside a class, self allows that method to access and modify the properties of the object the method is called on. Without self, you wouldn't be able to refer to or modify the instance's state.
"""
from typing import Any
from PrintList import printDLL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):  # Initialize an empty list
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtMidOfEvenOdd(self, data: int) -> Node | None:
        new_node = Node(data)

        # Case: Empty list → return new_node as head
        if self.head is None:
            return new_node

        slow = fast = self.head

        # Find middle node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Insertion logic
        if fast is None:
            # EVEN-LENGTH: Insert BEFORE second middle (slow)
            # Example: [1 ⇄ 2 ⇄ 3 ⇄ 4] → Insert between 2 and 3
            new_node.next = slow
            new_node.prev = slow.prev
            slow.prev = new_node
            if new_node.prev is not None:
                new_node.prev.next = new_node
            else:
                # Only happens in 2-node lists: [A ⇄ B] → [new ⇄ A ⇄ B]
                self.head = new_node
        else:
            # ODD-LENGTH: Insert AFTER exact middle (slow)
            # Example: [1 ⇄ 2 ⇄ 3] → Insert after 2
            new_node.prev = slow
            new_node.next = slow.next
            slow.next = new_node
            if new_node.next is not None:
                new_node.next.prev = new_node

        return self.head

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

    def delete_from_beginning(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def deleteAtMidOfEvenOdd(self) -> Any | None:
        if not self.head or not self.head.next:
            return None  # Empty or single-node list

        slow = fast = self.head

        # Find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node (slow)
        if slow.prev is not None:
            slow.prev.next = slow.next  # Bypass slow
        else:
            self.head = slow.next  # Update head if deleting first node

        if slow.next is not None:
            slow.next.prev = slow.prev  # Update next node's prev

        slow.prev = slow.next = None  # Optional: Clean up references

        return self.head

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
        current.prev = None

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

        while current.prev is not None:
            current = current.prev
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


if __name__ == '__main__':
    # Create nodes and link forward and backward
    head = Node(20)
    node2 = Node(30)
    node3 = Node(40)
    node4 = Node(50)
    node5 = Node(60)
    node6 = Node(70)

    # Forward links
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # Backward links
    node2.prev = head
    node3.prev = node2
    node4.prev = node3
    node5.prev = node4
    node6.prev = node5

    # Proceed with function calls
    Dll = DoublyLinkedList()
    Dll.insert_at_beginning(head, 10)
    print(f"After inserting node {head.data} at beginning:")
    printDLL(head)

    Dll.insertAtMidOfEvenOdd(head)
    print(f"After inserting node 80 at mid (even/odd):")
    printDLL(head)

    Dll.insert_at_end(head)
    print(f"After inserting node 90 at end:")
    printDLL(head)

    print(f"Original List:")
    printDLL(head)

    Dll.delete_from_beginning(head)
    print(f"After deleting from beginning:")
    printDLL(head)

    print(f"Original List:")
    printDLL(head)

    Dll.deleteAtMidOfEvenOdd(head)
    print(f"After deleting from mid:")
    printDLL(head)

    Dll.delete_from_end(head)
    print(f"After deleting from mid:")
    printDLL(head)

    Dll.delete_from_end(head)
    print(f"After deleting from end:")
    printDLL(head)
