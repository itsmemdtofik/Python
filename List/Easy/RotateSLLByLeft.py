"""
     * <pre>
     * !Rotate a Singly Linked List
     * Given a singly linked list and an integer k, the task is to rotate the linked list to the left by k places.
     *
     * @param Examples:
     * Input: 10 -> 20 -> 30 -> 40 -> 50, K = 2
     * Output: 30 → 40 → 50 → 10 → 20
     *
     * Input: linked list = 10 -> 20 -> 30 -> 40, k = 6
     * Output: 30 -> 40 -> 10 -> 20
     *
     * !Approach: By changing pointer of kth node - O(n) Time and O(1) Space
     * The idea is to first convert the linked list to circular linked list by updating
     * the next pointer of last node to the head of linked list.
     * Then, traverse to the kth node and update the head of the linked list to the (k+1)th node.
     * Finally, break the loop by updating the next pointer of kth node to NULL..
     * </pre>
"""
from PrintList import printSLL


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def rotateSingleLinkedList(head: Node, k: int):
    if k == 0 or head is None:
        return head

    # Find the length of the list and the last node
    currentNode = head
    length = 1
    while currentNode.next is not None:
        currentNode = currentNode.next
        length += 1

    # Connect the last node to the head to make it circular
    currentNode.next = head

    # Modulo k with length to handle large values
    k = k % length
    if k == 0:
        currentNode.next = None  # Break the circle
        return head

    # Traverse to the new tail: (length - k - 1) steps from head
    currentNode = head
    for _ in range(length - k - 1):
        currentNode = currentNode.next

    # Set the new head and break the circle
    newHead = currentNode.next
    currentNode.next = None

    return newHead


if __name__ == "__main__":

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    head = rotateSingleLinkedList(head, 6)
    printSLL(head)

