"""
    /**
     * <pre>
     * !Reverse Linked List
     * Given a linked list, the task is to reverse the linked list by changing the links between nodes.
     * The idea is to reverse the links of all nodes using three pointers:
     *
     * Input: head: 1 -> 2 -> 3 -> 4 -> NULL
     * Output: head: 4 -> 3 -> 2 -> 1 -> NULL
     * Explanation: Reversed Linked List: 4 -> 3 -> 2 -> 1 -> null
     *
     * !Approach1: Using Iterative Method - O(n) Time and O(1) Space
     * !Approach2: Using Stack - O(n) Time and O(n) Space
     * prev: pointer to keep track of the previous node
     * temp1: pointer to keep track of the current node
     * temp2: pointer to keep track of the next node
     * </pre>
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def reverseSingleLinkedListUsingTwoPointer(head: Node):
    if head is None or head.next is None:
        return head

    currentNode = head
    previousNode = None

    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode


def printSLL(head: Node):
    currentNode = head
    while currentNode is not None:
        print(f" {currentNode.data}", end=" ->")
        currentNode = currentNode.next
    print(" NULL")


if __name__ == "__main__":
    # Create a hard-coded linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printSLL(head)

    head = reverseSingleLinkedListUsingTwoPointer(head)

    print("Reversed Linked List:", end="")
    printSLL(head)
