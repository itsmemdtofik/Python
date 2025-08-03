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

from PrintList import printSLL


class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev = None
        self.next = None


def getMiddle(head: Node):
    if head is None or head.next is None:
        return head

    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next
    return slow


def getMerge(head1: Node, head2: Node):
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


def getMergeSortSingleLinkedListII(head: Node):
    # Base case: Empty or single-node list
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    mid = getMiddle(head)
    left = head
    right = mid.next
    mid.next = None  # Break the link

    # Recursively sort both halves
    leftSort = getMergeSortSingleLinkedListII(left)
    rightSort = getMergeSortSingleLinkedListII(right)

    # Merge the sorted halves
    return getMerge(leftSort, rightSort)


def createSingleLinkedList(nums: int):
    dummy = Node(0)
    currentNode = dummy

    for num in nums:
        currentNode.next = Node(num)
        currentNode = currentNode.next
    return dummy.next


def main():
    nums: list[int] = [4, 2, 1, 3, -100, 1, 200, 10, 100]
    head = createSingleLinkedList(nums)
    print(f"Before Sorting the List is : ")
    printSLL(head)

    sortedHead = getMergeSortSingleLinkedListII(head)
    print(f"After Sorting the list is: ")
    printSLL(sortedHead)


if __name__ == '__main__':
    main()
