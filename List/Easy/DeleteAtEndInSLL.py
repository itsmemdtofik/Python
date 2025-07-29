from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None


def printSLL(head: Optional[Node]):
    if not head:
        print("List is empty.")
        return
    current = head
    while current:
        print(current.data, end=" -> " if current.next else " -> None\n")
        current = current.next


def deleteAtEnd(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        print("List is empty. Nothing to delete.")
        return None

    # Case 1: Only one node
    if head.next is None:
        return None

    # Case 2: Multiple nodes
    previousNode = None
    currentNode = head
    while currentNode.next:
        previousNode = currentNode
        currentNode = currentNode.next

    previousNode.next = None
    return head


# Example usage
if __name__ == "__main__":
    # Create a linked list: 3 -> 12 -> 15 -> 18 -> None
    head = Node(3)
    head.next = Node(12)
    head.next.next = Node(15)
    head.next.next.next = Node(18)

    print("Original List:")
    printSLL(head)

    # Delete last node
    head = deleteAtEnd(head)
    print("\nAfter deleting last node:")
    printSLL(head)

    # Delete again
    head = deleteAtEnd(head)
    print("\nAfter deleting last node again:")
    printSLL(head)

    # Delete again
    head = deleteAtEnd(head)
    print("\nAfter deleting last node again:")
    printSLL(head)

    # Delete again - should become empty
    head = deleteAtEnd(head)
    print("\nAfter deleting last node again:")
    printSLL(head)
