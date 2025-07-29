"""
     * <pre>
     * !Detect Loop or Cycle in Linked List
     * Given a singly linked list, check if the linked list has a loop (cycle) or not.
     * A loop means that the last node of the linked list is connected back to a node in the same list.
     *
     * Input: head: 1 -> 3 -> 4 -> 3
     * Output: true
     *
     * !Approach: Using Floyd's Cycle-Finding Algorithm - O(n) Time and O(1) Space
     * </pre>

"""

from Node import SingleLinkedList as Node


def detectLoopII(head: Node):
    slow = head
    fast = head

    while slow is not None and fast and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop
    head.next.next.next = head.next

    if detectLoopII(head):
        print("true")
    else:
        print("false")
