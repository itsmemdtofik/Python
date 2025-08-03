"""
     * !Detect and Remove Loop in Linked List
     * Given the head of a linked list that may contain a loop.
     * A loop means that the last node of the linked list is connected back to a node in the same list.
     * The task is to remove the loop from the linked list (if it exists).
     *
     * ! Approach: Detect and Remove Loop using Hashing - O(n) Time and O(n) Space

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


class DetectAndRemoveLoop:

    @staticmethod
    def detectAndRemoveLoopUsingHashing(head: Node):
        seen = set()
        currentNode = head
        previousNode = None
        while currentNode is not None:

            # If node is already in the set, remove the loop
            if currentNode in seen:
                previousNode.next = None
                return

            # Add node to the set and move forward
            seen.add(currentNode)
            previousNode = currentNode
            currentNode = currentNode.next

    @staticmethod
    def detectAndRemoveLoopUsingHashingII(head: Node):
        seen = set()
        currentNode = head
        previousNode = None

        while currentNode is not None:
            if currentNode in seen:
                # Case 1: Loop starts at a middle node
                if previousNode is not None:
                    previousNode.next = None
                # Case 2: Loop starts at head (entire list is a cycle)
                else:
                    # Find the last node before `head` and break the loop
                    temp = head
                    while temp.next != head:
                        temp = temp.next
                    temp.next = None
                return
            else:
                seen.add(currentNode)
                previousNode = currentNode
                currentNode = currentNode.next


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

    DetectAndRemoveLoop.detectAndRemoveLoopUsingHashing(head)

    print("\nList after removing loop:")
    printSLL(head)
