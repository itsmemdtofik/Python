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


def reverseDoublyLinkedListUsingTwoPointer(head: Node):
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

        # Move in the original forward direction using the updated prev (which was originally next)
        currentNode = currentNode.prev

    # previousNode is now the old head's previous node, which is the new head of the reversed list.
    if previousNode is not None:
        return previousNode.prev
    return head


def reverseDoublyLinkedListSwapping(head: Node):
    if head is None or head.next is None:
        return head

    currentNode = head
    # previousNode = None

    while currentNode is not None:
        currentNode.prev, currentNode.next = currentNode.next, currentNode.prev
        head = currentNode
        currentNode = currentNode.prev

    return head


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
    head = reverseDoublyLinkedListSwapping(head)
    print("Reversed Doubly Linked List")
    printDLL(head)
