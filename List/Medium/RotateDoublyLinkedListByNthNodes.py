"""
Rotate Doubly linked list by N nodes
Given a doubly-linked list, the task is to rotate the linked list counter-clockwise by p nodes. Here p is a given positive integer and is smaller than the count of nodes in the linked list.

Examples:

Input: 1 2 3 4 5, p = 2
Output: 3 4 5 1 2

"""

from Node import DoubleLinkedList as Node
from PrintList import printDLL


def rotateDoublyLinkedListClockWise(head: Node, position: int):
    currentNode = head

    # Find the last node
    while currentNode.next is not None:
        currentNode = currentNode.next

    # Make the list circular
    currentNode.next = head
    head.prev = currentNode

    # Move head and tail by the given position
    for i in range(p):
        head = head.next
        currentNode = currentNode.next

    # Break the circular connection
    currentNode.next = None
    head.prev = None

    return head


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(6)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    p = 3
    head = rotateDoublyLinkedListClockWise(head, p)
    printDLL(head)
