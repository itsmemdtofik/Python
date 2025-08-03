"""
    /**
     * !Delete last occurrence of an item from linked list
     * Given a singly linked list and a key, the task is to delete the last occurrence of that key in the linked list.
     *
     * Input: head: 1 -> 2 -> 3 -> 1 -> 4 -> NULL, key = 1
     * Output: 1 -> 2 -> 3 -> 4 -> NULL
     *
     * Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> NULL , key = 3
     * Output: 1 -> 2 -> 4 -> 5 -> NULL
     *
     * !Approach: Approach Using Position Tracking (Traversing Twice)
     * Traverse the list to find the position of the last occurrence of the key.
     * Traverse the list again to delete the node at that position.
     */
"""
from typing import Any

from Node import SingleLinkedList as Node
from PrintList import printSLL


def deleteLastOccurrenceFromSLL(head: Node, key: int) -> Node | None | Any:
    if head is None:
        return None

    lastPosition = -1
    currentPosition = 0
    currentNode = head

    # First Pass: find last occurrence position
    while currentNode:
        if currentNode.data == key:
            lastPosition = currentPosition
        currentNode = currentNode.next
        currentPosition += 1

    if lastPosition == -1:
        return head  # Key not found

    if lastPosition == 0:
        return head.next  # Delete head

    # Second Pass: delete node at last position
    currentNode = head
    for _ in range(lastPosition - 1):
        currentNode = currentNode.next

    if currentNode.next is not None:
        currentNode.next = currentNode.next.next
    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(4)

    key = 1
    head = deleteLastOccurrenceFromSLL(head, key)
    printSLL(head)
