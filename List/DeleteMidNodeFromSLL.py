"""
     * <pre>
     * !Delete middle of linked list
     * Given a singly linked list, the task is to delete the middle node of the list.
     * If the list contains an even number of nodes, there will be two middle nodes. In this case, delete the second middle node.
     * If the linked list consists of only one node, then return NULL.
     *
     * @param Example:
     * Input: LinkedList: 1->2->3->4->5
     * Output: 1->2->4->5
     *
     * !Approach1: Using Two-Pass Traversal - O(n) Time and O(1) space
     * </pre>

"""
from typing import Any

from List.Linkedlist import Node
from List.PrintList import printSLL


def deleteMidFromSLL(head: Node) -> Node | None | Any:
    if head.next is None:
        return None

    count = 0
    currentNode = head
    nextNode = head

    while currentNode is not None:
        count += 1
        currentNode = currentNode.next

    middleIndex = count // 2

    for i in range(middleIndex - 1):
        nextNode = nextNode.next

    nextNode.next = nextNode.next.next

    return head


if __name__ == "__main__":
    # Create a static hardcoded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5.
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
   # head.next.next.next.next.next = Node(6)

    print("Original Linked List:", end=" ")
    printSLL(head)

    # Delete the middle node.
    head = deleteMidFromSLL(head)

    print("Linked List after deleting the middle node:", end=" ")
    printSLL(head)
