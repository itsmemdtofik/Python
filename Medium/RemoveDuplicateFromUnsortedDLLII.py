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


def print_dll(head: Node):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "\n")
        current = current.next


def removeDuplicatesFromUnsortedDoublyLinkedList(head: Node):
    if head is None:
        return None

    seen = set()
    currentNode = head

    while currentNode is not None:
        if currentNode.data in seen:
            temp1 = currentNode.prev
            temp2 = currentNode.next

            if temp1:
                temp1.next = temp2
            if temp2:
                temp2.prev = temp1
            if currentNode == head:
                head = temp2

        else:
            seen.add(currentNode.data)

        currentNode = currentNode.next

    return head


def build_dll(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head


# Test the implementation
values = [1, 2, 3, 2, 4]
head = build_dll(values)
print("Original List:")
print_dll(head)

head = removeDuplicatesFromUnsortedDoublyLinkedList(head)
print("List after removing duplicates:")
print_dll(head)
