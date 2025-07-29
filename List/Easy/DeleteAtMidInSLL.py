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


def deleteInMiddle(head: Optional[Node], key: int) -> Optional[Node]:
    if head is None:
        return None

    # Case 1: Deletion at head
    if head.data == key:
        return head.next

    # Case 2: Search for node to delete
    previousNode = head
    currentNode = head.next

    while currentNode:
        if currentNode.data == key:
            previousNode.next = currentNode.next
            return head  # Return unchanged head
        previousNode = currentNode
        currentNode = currentNode.next

    # If key not found, return original head
    print(f"Value {key} not found in the list.")
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

    # Delete value in the middle
    head = deleteInMiddle(head, 15)
    print("\nAfter deleting 15:")
    printSLL(head)

    # Try to delete a non-existent value
    head = deleteInMiddle(head, 99)
    print("\nAfter attempting to delete 99:")
    printSLL(head)

    # Delete head value
    head = deleteInMiddle(head, 3)
    print("\nAfter deleting 3 (head):")
    printSLL(head)
