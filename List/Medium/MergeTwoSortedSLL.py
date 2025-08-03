"""
Merge two sorted linked lists
Given two sorted linked lists consisting of n and m nodes respectively.
The task is to merge both of the lists and return the head of the merged list.

!Approach: Using Iterative Merge - O(n+m) Time and O(1) Space

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


class MergeTwoSortedList:

    @staticmethod
    def merge(head1: Node, head2: Node):
        dummy = Node(0)
        currentNode = dummy

        while head1 is not None and head2 is not None:
            if head1.data <= head2.data:
                currentNode.next = head1
                head1 = head1.next
            else:
                currentNode.next = head2
                head2 = head2.next
            currentNode = currentNode.next

        currentNode.next = head1 if head1 is not None else head2
        return dummy.next


if __name__ == "__main__":
    # List 1: 1 -> 3 -> 5
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)

    # List 2: 2 -> 4 -> 6
    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    merged_head = MergeTwoSortedList.merge(l1, l2)

    print("Merged List:")
    printSLL(merged_head)
