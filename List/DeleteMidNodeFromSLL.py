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
    if head is None:
        return None

    if head.next is None:
        return None

    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    middleIndex = count // 2

    current = head
    for i in range(middleIndex - 1):
        current = current.next

    current.next = current.next.next

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)


    head = deleteMidFromSLL(head)
    printSLL(head)
