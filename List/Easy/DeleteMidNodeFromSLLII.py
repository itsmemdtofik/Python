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
     * !Approach1: One-Pass Traversal with Slow and Fast Pointers - O(n) Time and O(1) Space
     * </pre>

"""

from List.Node import SingleLinkedList as Node
from List.PrintList import printSLL


def deleteMidNodeFromSingleLinkedList(head: Node):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    previousNode = None

    # Find middle node
    while fast and fast.next:
        fast = fast.next.next
        previousNode = slow
        slow = slow.next

    # 'slow' is now the middle node; 'prev' is the node before it
    if previousNode:
        previousNode.next = slow.next

    return head


if __name__ == "__main__":
    # Fixed linked list creation
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Original list:")
    printSLL(head)

    head = deleteMidNodeFromSingleLinkedList(head)

    print("After deleting middle node:")
    printSLL(head)
