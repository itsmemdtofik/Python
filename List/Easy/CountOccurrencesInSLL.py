"""
Count Occurrences in a Linked List
Given a singly linked list and a key, the task is to count the number of occurrences of the given key in the linked list.

Example :

Input : head: 1->2->1->2->1->3->1 , key = 1
Output : 4

"""

from Node import SingleLinkedList as Node


def countFrequencyOfGivenKey(head: Node, key: int):
    currentNode = head
    count = 0
    while currentNode is not None:
        if currentNode.data == key:
            count += 1
        currentNode = currentNode.next
    return count


head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

key = 1

print(countFrequencyOfGivenKey(head, key))
