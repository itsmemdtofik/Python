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


def reverseDoublyLinkedListUsingStack(head: Node):
    if head is None or head.next is None:
        return head

    stack = []
    currentNode = head

    # Push all nodes onto the stack
    while currentNode is not None:
        stack.append(currentNode)
        currentNode = currentNode.next

    # Pop nodes from the stack and reverse the list
    newHead = stack.pop()
    currentNode = newHead

    while stack:  # True as long as stack is not empty
        nextNode = stack.pop()
        currentNode.next = nextNode
        nextNode.prev = currentNode
        currentNode = nextNode

    # Set the last nodes next to None
    currentNode.next = None
    return newHead


def printDLL(head: Node):
    currentNode = head
    while currentNode is not None:
        print(f" {currentNode.data}", end=" ->")
        currentNode = currentNode.next
    print(" NULL")


# Example usage
if __name__ == "__main__":
    # Create a sample doubly linked list: 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    print("Original list:")
    printDLL(head)

    head = reverseDoublyLinkedListUsingStack(head)

    print("Reversed list:")
    printDLL(head)
