"""
     * <pre>
     * !Remove Duplicates from Un-Sorted List
     * Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
     * leaving only distinct numbers from the original list. Return the linked list sorted as well.
     *
     * Input: head = [1 -> 2 -> 5 -> 6 -> 5 -> 2 -> null]
     * Output: [1 -> 2 -> 5 -> 6 -> null]
     *
     * !Approach: Using Hashing Time Complexity: O(n) Space Complexity: O(n)
     * Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers.
     * </pre>
"""
from Node import SingleLinkedList as Node
from PrintList import printSLL


def removeDuplicatesFromUnSortedSingleLinkedList(head: Node):
    if head is None or head.next is None:
        return head

    seen = set()
    currentNode = head

    seen.add(currentNode.data)
    while currentNode.next is not None:
        if currentNode.next.data in seen:
            currentNode.next = currentNode.next.next  # Skip duplicates
        else:
            seen.add(currentNode.next.data)
            currentNode = currentNode.next
    return head



if __name__ == "__main__":
    # Creating linked list: 1 -> 2 -> 5 -> 6 -> 5 -> 2 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(2)

    print("Before Removing Duplicates:")
    printSLL(head)

    print("After Removing Duplicates:")
    removeDuplicatesFromUnSortedSingleLinkedList(head)
    printSLL(head)
