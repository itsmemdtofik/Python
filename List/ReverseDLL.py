"""
Given a Doubly Linked List, the task is to reverse the Doubly Linked List.

Examples:

Input: Doubly Linked List = 1 <-> 2 <-> 3 -> NULL
Output: Reversed Doubly Linked List = 3 <-> 2 <-> 1 -> NULL

Input: Doubly Linked List = 1 ->NULL
Output: Reversed Doubly Linked List = 1 ->NULL

Approach: Using Two Pointers - O(n) Time and O(1) Space

"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def reverseDoublyLinkedList(head: Node):
    # If the list is empty or has only one node, then return the head as it is
    if head is None or head.next is None:
        return head

    previousNode = None
    currentNode = head

    while currentNode is not None:
        # Swap the next and previous
        previousNode = currentNode.prev
        currentNode.prev = currentNode.next
        currentNode.next = previousNode

        currentNode = currentNode.prev

    return previousNode.prev


def printDLL(head: Node):
    currentNode = head
    while currentNode is not None:
        print(f" {currentNode.data}", end=" ->")
        currentNode = currentNode.next
    print(" NULL")


if __name__ == "__main__":
    # Create a doubly linked list:
    # 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print("Original Doubly Linked List")
    printDLL(head)
    head = reverseDoublyLinkedList(head)
    print("Reversed Doubly Linked List")
    printDLL(head)
