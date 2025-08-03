"""
     * <pre>
     * !Reverse Linked List
     * Given a linked list, the task is to reverse the linked list by changing the links between nodes.
     * The idea is to reverse the links of all nodes using three pointers:
     *
     * Input: head: 1 -> 2 -> 3 -> 4 -> NULL
     * Output: head: 4 -> 3 -> 2 -> 1 -> NULL
     * Explanation: Reversed Linked List: 4 -> 3 -> 2 -> 1 -> null
     *
     * !Approach1: Using Iterative Method(two-pointer) - O(n) Time and O(1) Space
     * !Approach2: Using Stack - O(n) Time and O(n) Space
     * Push all nodes onto the stack
     * Pop the last node from the stack (which was the last in original list)
     * Start popping the nodes and push them at the end of the linked list in the same order until the stack is empty.
     * Update the current->next pointer of last node in the stack by NULL.
     * </pre>
"""
class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None


def reverseSingleLinkedListUsingStack(head:Node):

    # Create a stack to store the nodes
    stack = []
    currentNode = head

    # Push all nodes node into stack
    while currentNode is not None:
        stack.append(currentNode)
        currentNode = currentNode.next

    # Make the last node as new head of the linked list
    newHead = stack.pop()
    currentNode = newHead

    # Pop all the nodes and append to the linked list
    while stack:
        # append the top value of stack in list
        currentNode.next = stack.pop()

        # move to the next node in the list
        currentNode = currentNode.next

    # Update the next pointer of last node of stack to None or Terminate the list
    currentNode.next = None

    return newHead


def printList(node:Node):
    while node is not None:
        print(f" {node.data}", end=" ->")
        node = node.next
    print(f" NULL")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given Linked List:", end="")
printList(head)

head = reverseSingleLinkedListUsingStack(head)

print("Reversed Linked List:", end="")
printList(head)