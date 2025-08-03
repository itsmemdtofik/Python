"""
    * <pre>
     * !Remove Duplicates from Sorted List II
     * Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
     * Return the linked list sorted as well.
     *
     * Input: head = [1,2,3,3,4,4,5]
     * Output: [1, 2, 3, 4, 5]
     *
     * !Approach: Iterative Time Complexity: O(n) Space Complexity: O(1)
     *
     * </pre>
"""
from Node import SingleLinkedList as Node
from PrintList import printSLL


def removeDuplicatesFromSortedSingleLinkedList(head: Node):
    if head is None or head.next is None:
        return head

    dummy = Node(0)
    dummy.next = head
    previousNode = dummy
    currentNode = head

    while currentNode is not None:
        isDuplicate = False

        while currentNode.next is not None and currentNode.data == currentNode.next.data:
            currentNode = currentNode.next
            isDuplicate = True

        if isDuplicate:
            previousNode.next = currentNode.next
        else:
            previousNode = previousNode.next

        currentNode = currentNode.next

    return dummy.next


# Manually create: 1 -> 2 -> 3 -> 3 -> 3 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(5)

print("Before Removing Duplicates:")
printSLL(head)

head = removeDuplicatesFromSortedSingleLinkedList(head)

print("After Removing Duplicates:")
printSLL(head)
