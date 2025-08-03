"""
Merge Sort for Doubly Linked List
Given a doubly linked list, The task is to sort the doubly linked list in non-decreasing order using merge sort.

Examples:

Input: 10 <-> 8 <-> 4 <-> 2
Output: 2 <-> 4 <-> 8 <-> 10

Input: 5 <-> 3 <-> 2
Output: 2 <-> 3 <-> 5

Approach: Using Merge Sort Time Complexity: O(n Log n)  Space: O(1)
"""

from PrintList import printDLL


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def getMiddle(head: Node):
    if head is None or head.next is None:
        return head

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def getMerge(head1: Node, head2: Node):
    dummy = Node(0)
    currentNode = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            currentNode.next = head1
            head1.prev = currentNode  # Update prev pointer
            head1 = head1.next
        else:
            currentNode.next = head2
            head2.prev = currentNode  # Update prev pointer
            head2 = head2.next
        currentNode = currentNode.next

    # Attach remaining elements
    currentNode.next = head1 if head1 else head2

    if currentNode.next:
        currentNode.next.prev = currentNode  # Update prev for remaining nodes

    merged_head = dummy.next
    if merged_head is not None:
        merged_head.prev = None  # Ensure head's prev is None
    return merged_head


def getMergeSortDoublyLinkedList(head: Node):
    if head is None or head.next is None:
        return head

    # Split the list
    mid = getMiddle(head)
    left = head
    right = mid.next
    mid.next = None
    right.prev = None  # Break the link

    # Recursively sort
    left_sorted = getMergeSortDoublyLinkedList(left)
    right_sorted = getMergeSortDoublyLinkedList(right)

    # Merge and fix prev pointers
    return getMerge(left_sorted, right_sorted)


def createDoublyLinkedList(nums: list[int]):
    dummy = Node(0)
    currentNode = dummy

    for num in nums:
        newNode = Node(num)
        currentNode.next = newNode
        newNode.prev = currentNode
        currentNode = newNode

    head = dummy.next
    if head is not None:
        head.prev = None  # Detach dummy
    return head


def main():
    # Test case
    arr = [4, 2, 1, 3, -100, 1, 200, 10, 100]
    head = createDoublyLinkedList(arr)
    print("Original list:")
    printDLL(head)

    sorted_head = getMergeSortDoublyLinkedList(head)
    print("Sorted list:")
    printDLL(sorted_head)


if __name__ == '__main__':
    main()
