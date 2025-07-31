"""
Delete a Node from linked list without head pointer

You are given a singly linked list and pointer which is pointing to the node which is required to be deleted.
Any information about the head pointer or any other node is not given.
You need to write a function to delete that node from the linked list.
Your function will take only one argument, i.e., a pointer to the node which is to be deleted

Note: No head reference is given to you. It is guaranteed that the node to be deleted is not the last node:

"""

from Node import SingleLinkedList as Node


class DeleteNodeWithoutHead:

    def __init__(self):
        self.head = None

    def deleteNodeWithoutHead(self, current: Node):

        if current is None:
            return

        elif current.next is None:
            print("This is last node, require head, can not be freed\n")
            return

        # Copy data of the next node to current node
        current.data = current.next.data

        # Perform conventional deletion
        current.next = current.next.next

    def push(self, data: int):

        # Allocate node and put in the data
        newNode = Node(data)

        # Link the old list of the ned node
        newNode.next = self.head

        # Move the head to point to the new node
        self.head = newNode

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("NULL\n")


if __name__ == '__main__':
    llist = DeleteNodeWithoutHead()

    # create linked list 35->15->4->20
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)

    print("Initial Linked List : ")
    llist.print_list()

    # Delete 15 without sending head
    del_node = llist.head.next

    # Function call
    llist.deleteNodeWithoutHead(del_node)

    # Print the final Linked List
    print("Final Linked List after deletion of 15 : ")
    llist.print_list()
