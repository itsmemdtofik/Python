"""
Deletion at beginning (Removal of first node) in a Linked List

Given a linked list, The task is to remove the first node from the given linked list.

Examples:

Input : head : 3 -> 12 -> 15 -> 18 -> NULL
Output : 12 -> 15 -> 18 -> NULL

Input : head : 2 -> 4 -> 6 -> 8 -> 33 -> 67 -> NULL
Output : 4 -> 6 -> 8 -> 33 -> 67 -> NULL

"""
from Node import SingleLinkedList as Node
from PrintList import printSLL


def deleteAtBeginningInLinkedList(head: Node):
    if head is None:
        return None

    head = head.next

    return head


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 3 -> 12 -> 15 -> 18
    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(15)
    head.next.next.next = Node(18)
    head = deleteAtBeginningInLinkedList(head)
    printSLL(head)
