"""
     * <pre>
     * ! Linked List Cycle II
     * Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
     * Detect the start node of a cycle in a linked list, if one exists. Otherwise, return null.
     * @param Note: Do not modify the linked list.
     * </pre>
"""
from Node import SingleLinkedList as Node


class LinkedListCycleII:
    @staticmethod
    def getStartNodeOfCycleInSingleLinkedList(head: Node):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head

        # Step 1: Detect if there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Cycle detected, find the start of the loop
                currentNode = head
                while currentNode != slow:
                    currentNode = currentNode.next
                    slow = slow.next
                return currentNode  # Start of cycle

        return None  # No cycle

    @staticmethod
    def printCycleStart(head: Node):
        if head:
            print(f"Cycle starts at node with data: {head.data}")
        else:
            print("No cycle detected")


if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle starts again at 3)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next  # Creating cycle at node 3

    start_node = LinkedListCycleII.getStartNodeOfCycleInSingleLinkedList(head)
    LinkedListCycleII.printCycleStart(start_node)
