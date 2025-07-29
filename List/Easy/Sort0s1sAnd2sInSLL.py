"""
Sort a linked list of 0s, 1s and 2s
Given a linked list of 0s, 1s and 2s, The task is to sort the list in non-decreasing order.

Examples:

Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL

Approach: By Maintaining Frequency - O(n) Time and O(1) Space
"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def sort0s1sAnd2sInSingleLinkedList(head: Node):
    # Initialize count of '0', '1' and '2' as 0
    count = [0, 0, 0]
    currentNode = head

    while currentNode is not None:
        count[currentNode.data] += 1
        currentNode = currentNode.next

    index = 0
    currentNode = head

    while currentNode is not None:
        if count[index] == 0:
            index += 1
        else:
            currentNode.data = index
            count[index] -= 1
            currentNode = currentNode.next

    return head


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 1 -> 1 -> 2 -> 1 -> 0 -> NULL
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print(f"Linked List before Sorting : ", end='')
    printSLL(head)

    sort0s1sAnd2sInSingleLinkedList(head)

    print(f"Linked List after Sorting : ", end='')
    printSLL(head)
