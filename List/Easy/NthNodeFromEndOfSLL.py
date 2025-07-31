"""
     * <pre>
     * !Program for Nth node from the end of a Linked List
     * Given a Linked List of M nodes and a number N,
     * find the value at the Nth node from the end of the Linked List.
     * If there is no Nth node from the end, print -1.
     *
     * @param Examples:
     * Input: 1 -> 2 -> 3 -> 4, N = 3
     * Output: 2
     * Explanation: Node 2 is the third node from the end of the linked list.
     *
     * Input: 35 -> 15 -> 4 -> 20, N = 4
     * Output: 35
     * Explanation: Node 35 is the fourth node from the end of the linked list.
     *
     * !Approach: By Finding the length of list - Two Pass - O(M) Time and O(1) Space
     * The idea is to count the number of nodes in linked list in the first pass, say len.
     * In the second pass, return the (len - n + 1)th nodes from beginning of the Linked List.
     * </pre>
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to append a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to find Nth node from the end using two-pass approach
    def get_nth_from_end(self, n):
        length = 0
        temp = self.head

        # First pass: find length of list
        while temp:
            length += 1
            temp = temp.next

        # If n is greater than length, return -1
        if n > length:
            return -1

        # Second pass: get (length - n + 1)th node from start
        temp = self.head
        for _ in range(length - n):
            temp = temp.next

        return temp.data


# --------- Test the Code ---------

# Example 1
llist1 = LinkedList()
for value in [1, 2, 3, 4]:
    llist1.append(value)
print("Output:", llist1.get_nth_from_end(3))  # Output: 2

# Example 2
llist2 = LinkedList()
for value in [35, 15, 4, 20]:
    llist2.append(value)
print("Output:", llist2.get_nth_from_end(4))  # Output: 35
