"""
Remove every k-th node of the linked list
Given a singly linked list, the task is to remove every kth node of the linked list. Assume that k is always less than or equal to the length of the Linked List.

Examples :

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
Output: 1 -> 3 -> 5
Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def deleteKthNodeFromSLL(head: Node, k: int):
    if head is None or k <= 0:
        return head

    currentNode = head
    previousNode = None
    count = 0

    while currentNode is not None:
        count += 1

        # If count is multiple of k, remove current node
        if count % k == 0:

            # Bypass the current node
            if previousNode is not None:
                previousNode.next = currentNode.next
            else:
                # If removing the head node
                head = currentNode.next
        else:
            # Update previous node pointer only if we do not remove the node
            previousNode = currentNode

        currentNode = currentNode.next

    return head


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    k = 2
    head = deleteKthNodeFromSLL(head, k)
    printSLL(head)
