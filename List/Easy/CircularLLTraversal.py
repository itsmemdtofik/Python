"""
Given a circular linked list, the task is to print all the elements of this circular linked list.

Example:

Input: 1 2 3 4 5 6
Traversal-of-Circular-Linked-List
Output: 1 2 3 4 5 6

Input: 2 4 6 8 10
Traversal-of-Circular-Linked-List
Output: 2 4 6 8 10

"""

from Node import SingleLinkedList as Node


def printCLL(head: Node):
    if head is None:
        return

    currentNode = head
    while True:
        print(f"{currentNode.data}", end=" -> ")
        currentNode = currentNode.next

        if currentNode == head:
            break
    print("NULL")


if __name__ == "__main__":
    head = Node(11)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)
    head.next.next.next.next = head

    printCLL(head)
