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


def getIntersectionOfTwoSortedSingleLinkedList(head1: Node, head2: Node):
    temp1 = head1
    temp2 = head2

    while temp1 != temp2:
        if temp1 is not None:
            temp1 = temp1.next
        else:
            temp1 = head2

        if temp2 is not None:
            temp2 = temp2.next
        else:
            temp2 = head1
    return temp1


def getIntersectionOfTwoSortedSingleLinkedListII(head1: Node, head2: Node):
    temp1 = head1
    temp2 = head2
    while temp1 != temp2:
        temp1 = head2 if temp1 is None else temp1.next
        temp2 = head1 if temp2 is None else temp2.next
    return temp1


if __name__ == "__main__":
    # Creating common part: 6 -> 8
    common = Node(6)
    common.next = Node(8)

    # First list: 1 -> 2 -> 3 -> 4 -> [6 -> 8]
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = common

    # Second list: 2 -> 4 -> [6 -> 8]
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = common

    print("First List:")
    printSLL(head1)

    print("Second List:")
    printSLL(head2)

    intersection = getIntersectionOfTwoSortedSingleLinkedList(head1, head2)

    print("Intersection of the two lists:")
    printSLL(intersection)
