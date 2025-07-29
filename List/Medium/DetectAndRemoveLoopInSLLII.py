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


def detectAndRemoveLoop(head: Node):
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


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop
    head.next.next.next = head.next

    detectAndRemoveLoop(head)
    printSLL(head)
