"""
     * <pre>
     * !Detect Loop or Cycle in Linked List
     * Given a singly linked list, check if the linked list has a loop (cycle) or not.
     * A loop means that the last node of the linked list is connected back to a node in the same list.
     *
     * Input: head: 1 -> 3 -> 4 -> 3
     * Output: true
     * Input: head: 1 -> 8 -> 3 -> 4 -> NULL
     * Output: false
     * !Approach: Using HashSet - O(n) Time and O(n) Space
     * </pre>

"""
from Node import SingleLinkedList as Node


def detectLoop(head: Node):
    seen = set()

    currentNode = head
    while currentNode is not None:
        if currentNode in seen:
            return True

        seen.add(currentNode)
        currentNode = currentNode.next

    return False


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop
    head.next.next.next = head.next

    if detectLoop(head):
        print("true")
    else:
        print("false")
