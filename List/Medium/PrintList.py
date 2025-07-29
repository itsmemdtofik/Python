from typing import Optional
from Node import SingleLinkedList, DoubleLinkedList


def printSLL(head: Optional[SingleLinkedList]) -> None:
    """Prints a singly linked list (e.g., 1 -> 2 -> null)."""
    if not head:
        print("null")
        return

    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")


def printDLL(head: Optional[DoubleLinkedList]) -> None:
    """Prints a doubly linked list (same as singly for forward traversal)."""
    if not head:
        print("null")
        return
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")