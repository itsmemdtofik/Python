from Node import SingleLinkedList as Node


def detectLoopIII(head: Node):
    slow = head
    fast = head

    # First phase: detect if there's a loop
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Second phase: find the start of the loop
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # or return True if you just want to confirm existence
    return None  # or return False if you just want to confirm existence


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop
    head.next.next.next = head.next

    if detectLoopIII(head):
        print("True")
    else:
        print("False")
