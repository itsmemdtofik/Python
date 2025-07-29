"""
     * <pre>
     * !Intersection of two Sorted Linked Lists
     * Given two lists sorted in increasing order, create and return a new list representing the intersection of the two lists.
     * The new list should be made with its own memory — the original lists should not be changed.
     * Input:
     * First linked list: 1->2->3->4->6
     * Second linked list be 2->4->6->8,
     * Output: 2->4->6.
     * The elements 2, 4, 6 are common in
     * both the list so they appear in the
     * intersection list.
     *
     * !Approach:  Two Pointer Switching Technique Time: O(n) Space: O(1)
     * </pre>
"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def getIntersectionOfTwoSortedSingleLinkedListII(head1: Node, head2: Node):
    dummy = Node(0)
    currentNode = dummy

    while head1 is not None and head2 is not None:
        if head1.data == head2.data:
            currentNode.next = Node(head1.data)
            currentNode = currentNode.next
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next

    return dummy.next


if __name__ == "__main__":
    # List 1: 1 -> 2 -> 3 -> 4 -> 6
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(6)

    # List 2: 2 -> 4 -> 6 -> 8
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)
    head2.next.next.next = Node(8)

    print("First List:")
    printSLL(head1)

    print("Second List:")
    printSLL(head2)

    intersection = getIntersectionOfTwoSortedSingleLinkedListII(head1, head2)

    print("Intersection of the two lists:")
    printSLL(intersection)
