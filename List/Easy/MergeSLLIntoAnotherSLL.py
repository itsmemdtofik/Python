"""
     * <pre>
     * !Merges two linked lists at alternate positions.
     * Given two singly linked lists, The task is to insert nodes of the second list
     * into the first list at alternate positions of the first list and leave the
     * remaining nodes of the second list if it is longer.
     *
     * @param Example:
     * Input: head1: 1->2->3 , head2: 4->5->6->7->8
     * Output: head1: 1->4->2->5->3->6 , head2: 7->8
     *
     * !Approach: Using Iterative Method – O(n) Time and O(1) Space
     * The idea is to start traversing from the beginning of both lists.
     * For each step, take a node from the second list and insert it after a node from the first list.
     * This process continues until we reach the end of one or both lists.
     * If the second list is longer, remaining nodes will be kept as it is second list.
     * </pre>
"""
from Node import SingleLinkedList as Node
from PrintList import printSLL


def merge(head1: Node, head2: Node):

    # Initialize pointers to traverse the two lists
    currentNode1 = head1
    currentNode2 = head2

    while currentNode1 is not None and currentNode2 is not None:

        # Save the next nodes of the current
        temp1 = currentNode1.next
        temp2 = currentNode2.next

        currentNode2.next = currentNode1.next
        currentNode1.next = currentNode2

        currentNode1 = temp1
        currentNode2 = temp2

    return [head1, currentNode2]


if __name__ == "__main__":
    # Creating first linked list 1->2->3
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    # Creating second linked list 4->5->6->7->8
    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(8)

    # Store first and second head points in array
    ar = merge(head1, head2)
    printSLL(ar[0])
    printSLL(ar[1])
