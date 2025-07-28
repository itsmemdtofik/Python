"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
Note that pos is not passed as a parameter.

Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

"""

from Node import SingleLinkedList as Node
from PrintList import printSLL


def detectCycleII(head: Node):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:

            temp1 = head
            temp2 = slow

            while temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1
    return None


if __name__ == '__main__':
    # Create a cycle: 3 -> 2 -> 0 -> -4 -> points back to node with value 2
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    head.next.next.next.next = head.next  # cycle here

    cycle_start = detectCycleII(head)

    if cycle_start:
        print("Cycle starts at node with value:", cycle_start.data)
    else:
        print("No cycle")
