"""
    * !Detect and Remove Loop in Linked List
     * Given the head of a linked list that may contain a loop.
     * A loop means that the last node of the linked list is connected back to a node in the same list.
     * The task is to remove the loop from the linked list (if it exists).
     *
     * ! Approach: Using Floyd's Cycle Detection Algorithm - O(n) Time and O(1) Space

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL



class DetectAndRemoveLoop:
    @staticmethod
    def detectAndRemoveLoop(head: Node):
        if head is None or head.next is None:
            return

        slow = head
        fast = head
        loopExists = False

        # Step 1: Detect loop using Floyd's algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loopExists = True
                break

        # Step 2: If loop exists, find the start and remove it
        if loopExists:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None  # Remove loop

if __name__ == "__main__":
    # Create linked list: 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop: 4 -> 3
    head.next.next.next = head.next

    print("Original List with Loop (partial print to avoid infinite loop):")
    temp = head
    for _ in range(5):  # just print a few nodes to show the loop
        print(temp.data, end=" -> ")
        temp = temp.next
    print("...")

    DetectAndRemoveLoop.detectAndRemoveLoop(head)

    print("\nList after removing loop:")
    printSLL(head)
