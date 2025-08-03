"""
Merge Sort for Linked Lists:

Given a singly linked list, The task is to sort the linked list in non-decreasing order using merge sort.

Examples:

Input: 40 -> 20 -> 60 -> 10 -> 50 -> 30 -> NULL
Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> NULL

Input: 9 -> 5 -> 2 -> 8 -> NULL
Output: 2 -> 5 -> 8 -> 9 -> NULL

Approach: Using Merge Sort Time Complexity: O(n * log n) and Space: O(n)
"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def getMiddle(head):
    if head is None or head.next is None:
        return head

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:  # Modified condition
        slow = slow.next
        fast = fast.next.next
    return slow


def getMerge(head1: Node, head2: Node):
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    current.next = head1 if head1 else head2
    return dummy.next


def getMergeSortSingleLinkedList(head: Node):
    # Base case: empty or single-node list
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    mid = getMiddle(head)
    left = head
    right = mid.next
    mid.next = None  # Break the link

    # Recursively sort both halves
    left_sorted = getMergeSortSingleLinkedList(left)
    right_sorted = getMergeSortSingleLinkedList(right)

    # Merge the sorted halves
    return getMerge(left_sorted, right_sorted)


def createSingleLinkedList(nums: int):
    dummy = Node(0)
    currentNode = dummy

    for num in nums :
        currentNode.next = Node(num)
        currentNode = currentNode.next

    return dummy.next


def main():
    nums: list[int] = [4, 2, 1, 3, -100, 1, 200, 10, 100]
    head = createSingleLinkedList(nums)
    print("Original list:")
    printSLL(head)

    sorted_head = getMergeSortSingleLinkedList(head)
    print("Sorted list:")
    printSLL(sorted_head)

if __name__ == '__main__':
    main()