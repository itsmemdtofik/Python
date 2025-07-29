"""
Convert singly linked list into circular linked list

Given a singly linked list, the task is to convert it into a circular linked list.

Examples:

Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Explanation: Singly linked list is converted to circular by pointing last node to head.

Input: head: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> NULL
Output: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> NULL
Explanation: Singly linked list is converted to circular by pointing last node to head.

"""

from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None


def recursive(currentNode: Node, head: Node):
    if currentNode.next is None:
        currentNode.next = head
        return
    recursive(currentNode.next, head)


def iterative(head: Node):
    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next
    currentNode.next = head


def print_circular_list(head: Optional[Node]):
    if head is None:
        return
    currentNode = head
    while True:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
        if currentNode == head:
            break
    print(f"NULL")


# Example usage
if __name__ == "__main__":
    # Recursive approach
    head = Node(10)
    head.next = Node(12)
    head.next.next = Node(14)
    head.next.next.next = Node(16)

    recursive(head, head)
    print("Using Recursive Approach:")
    print_circular_list(head)

    # Iterative approach
    head1 = Node(11)
    head1.next = Node(12)
    head1.next.next = Node(13)
    head1.next.next.next = Node(14)

    iterative(head1)
    print("Using Iterative Approach:")
    print_circular_list(head1)

