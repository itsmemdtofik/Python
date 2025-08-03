"""
Delete N nodes after M nodes of a linked list

Given a linked list and two integers m and n, the task is to traverse the linked list such that you skip m nodes,
then delete the next n nodes, and continue the same till end of the linked list.

Note: m cannot be 0.

Example:
Input: Linked List: 9->1->3->5->9->4->10->1, n = 1, m = 2
Output: 9->1->5->9->10->1
Explanation: Deleting 1 node after skipping 2 nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.

Input: Linked List: 1->2->3->4->5->6, n = 1, m = 6
Output: 1->2->3->4->5->6
Explanation: After skipping 6 nodes for the first time , we will reach of end of the linked list, so, we will get the given linked list itself.
"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def skipMDeleteN(head: Node, m: int, n: int) -> Node:
    currentNode = head

    while currentNode is not None:
        # Skip m-1 nodes
        for i in range(1, m):
            if currentNode is None:
                return head
            currentNode = currentNode.next

        if currentNode is None:
            return head

        # Start deleting next n nodes
        nextNode = currentNode.next
        for i in range(n):
            if nextNode is None:
                break
            nextNode = nextNode.next

        # Link the m-th node to the (m+n+1)-th node
        currentNode.next = nextNode

        # Move currentNode to the next start point
        currentNode = nextNode

    return head


if __name__ == "__main__":
    # Create the following linked list: 1->2->3->4->5->6
    head = Node(9)
    head.next = Node(1)
    head.next.next = Node(3)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(9)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(10)
    head.next.next.next.next.next.next.next = Node(1)

    m = 2
    n = 1
    head = skipMDeleteN(head, m, n)
    printSLL(head)
