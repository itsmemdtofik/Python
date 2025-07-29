"""
Given a sorted doubly linked list of positive distinct elements,
the task is to find pairs in a doubly-linked list whose sum is equal to the given value x in sorted order.

Input: 1 -> 2 -> 4 -> 5 -> 6 -> 8 -> 9, target = 7
Output: (1, 6), (2,5)
Explanation: We can see that there are two pairs (1, 6) and (2, 5) with sum 7.

Approach1: Using Hashing - O(n log n) Time and O(n) Space
Approach2: Using Two Pointer Technique - O(n) Time and O(1) Space
"""

from Node import DoubleLinkedList as Node


def getPairsFromDoublyLinkedListUsingHashing(head: Node, target: int):
    result = []
    seen = set()

    currentNode = head
    while currentNode is not None:
        complement = target - currentNode.data

        # Check is the target exists in the visited set
        if complement in seen:
            # Pair found, add it to the target
            result.append([complement, currentNode.data])

        # Add the current node's value to the visited set
        seen.add(currentNode.data)
        currentNode = currentNode.next

    # Sort the pairs by the first element of the pair
    result.sort(key=lambda pair: pair[0])
    return result


def getPairsFromDoublyLinkedListUsingTwoPointer(head: Node, target: int):
    result = []
    firstNode = secondNode = head

    # Move the second pointer to the end of the list
    while secondNode.next is not None:
        secondNode = secondNode.next

    # The loop terminates when two pointers cross each other (second.next == first),
    # or they become the same (first == second)
    while firstNode != secondNode and secondNode.next != firstNode:
        if (firstNode.data + secondNode.data) == target:

            # Add pairs the result list
            result.append([firstNode.data, secondNode.data])

            # Move first pointer in forward direction
            firstNode = firstNode.next

            # Move second pointer in the backword direction
            secondNode = secondNode.prev
        elif (firstNode.data + secondNode.data) < target:
            firstNode = firstNode.next
        else:
            secondNode = secondNode.prev

    result.sort(key=lambda pair: pair[0])
    return result


if __name__ == "__main__":
    # Values: 1 -> 2 -> 4 -> 5 -> 6 -> 8 -> 9
    values = [1, 2, 4, 5, 6, 8, 9]

    # Create doubly linked list
    head = Node(values[0])
    current = head
    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node

    target = 7
    pairs = getPairsFromDoublyLinkedListUsingTwoPointer(head, target)

    if not pairs:
        print("No pairs found.")
    else:
        for pair in pairs:
            print(pair[0], pair[1])
