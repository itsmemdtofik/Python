"""
     * <pre>
     * !Remove duplicates from an unsorted doubly linked list
     * Given an unsorted doubly linked list containing n nodes, the task is to remove duplicate nodes while preserving the original order.
     *
     * Examples:
     * Input: Doubly Linked List = 1 <-> 2 <-> 3 <-> 2 <-> 4
     * Output: Doubly Linked List = 1 <-> 2 <-> 3 <-> 4
     *
     * !Approach:Using HashSet - O(n) Time and O(n) Space
     * </pre>

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_dll(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data, end=" <-> " if currentNode.next else "\n")
        currentNode = currentNode.next


def removeDuplicatesFromUnsortedDoublyLinkedList(head: Node):
    if head is None or head.next is None:
        return head

    seen = set()
    currentNode = head
    previousNode = None

    while currentNode is not None:
        if currentNode.data in seen:
            # Remove current node
            previousNode.next = currentNode.next
            if currentNode.next is not None:
                currentNode.next.prev = previousNode
            currentNode = currentNode.next
        else:
            seen.add(currentNode.data)
            previousNode = currentNode
            currentNode = currentNode.next

    return head


# Helper to build doubly linked list from list
def createDoublyLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    currentNode = head
    for val in values[1:]:
        new_node = Node(val)
        currentNode.next = new_node
        new_node.prev = currentNode
        currentNode = new_node
    return head


# Test cases
test_lists = [
    [1, 2, 3, 2, 4],
    [1, 1, 1, 1],
    [1, 2, 3, 4]
]

for i, values in enumerate(test_lists, 1):
    print(f"\nOriginal List {i}:")
    head = createDoublyLinkedList(values)
    print_dll(head)
    head = removeDuplicatesFromUnsortedDoublyLinkedList(head)
    print("List after removing duplicates:")
    print_dll(head)
