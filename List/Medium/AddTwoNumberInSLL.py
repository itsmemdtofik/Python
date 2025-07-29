"""
Add Two Numbers Represented as Linked List
Given two numbers represented as two lists, the task is to return the sum of two lists.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Input: num1 = 4 -> 5, num2 = 3 -> 4 -> 5
Output: 3 -> 9 -> 0
Explanation: Sum of 45 and 345 is 390.

Time: O(n + m)
Space: O(n + m) due to call stack or auxiliary stacks.

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def listToNumber(head: Node) -> int:
    num = 0
    currentNode = head
    while currentNode is not None:
        num = num * 10 + currentNode.data
        currentNode = currentNode.next
    return num


def numberToList(num: int) -> Node:
    if num == 0:
        return Node(0)

    dummy = Node(0)
    currentNode = dummy

    for digit in str(num):
        currentNode.next = Node(int(digit))
        currentNode = currentNode.next

    return dummy.next


def addTwoLists(head1: Node, head2: Node) -> Node:
    num1 = listToNumber(head1)
    num2 = listToNumber(head2)
    total = num1 + num2
    return numberToList(total)


# ---------------------- Test -------------------------
if __name__ == "__main__":
    # num1 = 4 -> 5 (i.e., 45)
    num1 = Node(4)
    num1.next = Node(5)

    # num2 = 3 -> 4 -> 5 (i.e., 345)
    num2 = Node(3)
    num2.next = Node(4)
    num2.next.next = Node(5)

    result = addTwoLists(num1, num2)

    print("Input List 1:")
    printSLL(num1)

    print("Input List 2:")
    printSLL(num2)

    print("Result (Sum):")
    printSLL(result)
