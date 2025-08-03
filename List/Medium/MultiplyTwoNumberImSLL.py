"""
Multiply two numbers represented by Linked Lists
Given two numbers represented by linked lists, The task is to return the multiplication of these two linked lists.

Examples:

Input : head1 : 1->0->0 , head2 : 1->0
Output: 1000
Explanation: head1 represents 100 and head2 represents the number 10, 100 x 10 = 1000

Time Complexity: O(max(n1, n2)), where n1 and n2 represents the number of nodes present in the first and second linked list respectively.
Auxiliary Space: O(1)
"""
from Node import SingleLinkedList as Node

# MOD is used to preventing Integer Overflow
MOD = 10 ** 9 + 7  # Commonly used large prime


def multiplyTwoNumberInSingleLinkedList(head1: Node, head2: Node):
    num1 = 0
    num2 = 0

    firstNode = head1
    secondNode = head2

    while firstNode is not None:
        num1 = (num1 * 10 + firstNode.data) % MOD
        firstNode = firstNode.next

    while secondNode is not None:
        num2 = (num2 * 10 + secondNode.data) % MOD
        secondNode = secondNode.next

    return (num1 * num2) % MOD


if __name__ == "__main__":
    # Create first list 9->4->6
    head1 = Node(1)
    head1.next = Node(0)
    head1.next.next = Node(0)

    # Create second list 8->4
    head2 = Node(1)
    head2.next = Node(0)
    print(multiplyTwoNumberInSingleLinkedList(head1, head2))
