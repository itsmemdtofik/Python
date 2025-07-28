"""
Deletion from a Circular Linked List

In this article, we will learn how to delete a node from a circular linked list.
In a circular linked list, the last node connects back to the first node, creating a loop.

There are three main ways to delete a node from circular linked list:

1. Deletion at the beginning
2. Deletion at specific position
3. Deletion at the end
Now, let’s look at the methods and steps for these three deletion operations.

Deletion from a Circular Linked List:
Deletion involves removing a node from the linked list.
The main difference is that we need to ensure the list remains circular after the deletion.
We can delete a node in a circular linked list in three ways:
"""

from CircularLLTraversal import printCLL
from Node import SingleLinkedList as Node


def deleteFirstNode(last: Node):
    if last is None:
        print(f"List is empty!")
        return None

    head = last.next

    if head == last:
        last = None
    else:
        last.next = head.next
    return last

def print_list(last):
    if last is None:
        return

    head = last.next
    while True:
        print(head.data, end=" -> ")
        head = head.next
        if head == last.next:
            break
    print("NULL")


first = Node(2)
first.next = Node(3)
first.next.next = Node(4)

last = first.next.next
last.next = first

print("Original list: ", end="")
print_list(last)

# Delete the first node
last = deleteFirstNode(last)

print("List after deleting first node: ", end="")
print_list(last)
