"""
Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

"""
from typing import Optional
from Node import SingleLinkedList as Node
from PrintList import printSLL


class ReverseNodeInKthGroup:

    def reverse(self, head: Node):
        previousNode = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        return previousNode

    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        dummy = Node(99)
        dummy.next = head
        previousNode = dummy

        while head:
            currentNode = head
            count = 0

            # Check if at least k nodes remain
            while count < k - 1 and currentNode:
                count += 1
                currentNode = currentNode.next

            if not currentNode:
                break

            nextNode = currentNode.next  # Store the next group's head
            currentNode.next = None  # Cut current group

            reversed_head = self.reverse(head)  # Reverse the current k-group
            previousNode.next = reversed_head  # Connect previous group to reversed

            previousNode = head  # After reversal, head is now the tail of the reversed group
            head.next = nextNode  # Connect tail to next part
            head = nextNode  # Move head forward

        return dummy.next


if __name__ == "__main__":
    # Manually create: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list:")
    printSLL(head)

    k = 2
    rev = ReverseNodeInKthGroup()
    new_head = rev.reverseKGroup(head, k)

    print(f"\nReversed in k-group (k={k}):")
    printSLL(new_head)
