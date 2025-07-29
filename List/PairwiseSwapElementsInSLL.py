"""
Pairwise Swap Elements of a given Linked List

Given a singly linked list, the task is to swap linked list elements pairwise.

Examples:

Input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output : 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL

Reverse-a-Linked-List-in-groups-of-given-size-1

Input : 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output : 2 -> 1 -> 4 -> 3 -> 5 -> NULL
"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def pairwiseSwapInSingleLinkedList(head: Node):
    currentNode = head
    while currentNode is not None and currentNode.next is not None:
        currentNode.data, currentNode.next.data = currentNode.next.data, currentNode.data
        currentNode = currentNode.next.next


if __name__ == "__main__":
    # Creating the linked list:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    pairwiseSwapInSingleLinkedList(head)

    printSLL(head)
