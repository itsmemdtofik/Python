from PrintList import printSLL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtBegining(head: Node, data: int):
    if head is None:
        return None

    new_node = Node(data)
    new_node.next = head
    head = new_node

    return head


def insertAtMidOfEvenOdd(head: Node, data: int):
    if head is None:
        return Node(data)

    new_node = Node(data)

    slow = head
    fast = head
    previousNode = None

    while fast is not None and fast.next is not None:
        previousNode = slow
        slow = slow.next
        fast = fast.next.next

    if fast is None:
        # Even length — insert **before** the second middle
        new_node.next = slow
        if previousNode is not None:
            previousNode.next = new_node
            return head
        else:
            # Only two nodes, insert at beginning
            new_node.next = head
            return new_node
    else:
        # Odd length — insert **after** the exact middle
        new_node.next = slow.next
        slow.next = new_node
        return head


def insertAtEnd(head: Node, data: int):
    if head is None:
        return None

    new_node = Node(data)

    currentNode = head
    while currentNode.next is not None:
        currentNode = currentNode.next

    currentNode.next = new_node

    return head


def deleteAtBeginning(head: Node):
    if head is None:
        return None

    return head.next


def deleteAtMidOfEvenOdd(head: Node) -> Node:
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node (works for both odd and even lengths)
    if prev:
        prev.next = slow.next

    return head


def deleteAtEnd(head: Node):
    if head is None:
        return None  # List is empty

    if head.next is None:
        return None  # Only one node — delete it by returning None

    currentNode = head
    previousNode = None

    while currentNode.next is not None:
        previousNode = currentNode
        currentNode = currentNode.next

    previousNode.next = None  # Unlink the last node
    return head


if __name__ == '__main__':
    head = Node(20)
    head.next = Node(30)
    head.next.next = Node(40)
    head.next.next.next = Node(50)
    head.next.next.next.next = Node(60)
    head.next.next.next.next.next = Node(70)

    head = insertAtBegining(head, 10)
    print(f"After inserting node {head.data} at beginning: ")
    printSLL(head)

    head = insertAtMidOfEvenOdd(head, 80)
    print(f"After inserting node 80 at even and odd: ")
    printSLL(head)

    head = insertAtEnd(head, 90)
    print(f"After inserting node 90 at ending: ")
    printSLL(head)

    print(f"Original List:")
    printSLL(head)

    head = deleteAtBeginning(head)
    print(f"After deleting from beginning:")
    printSLL(head)

    print(f"Original List:")
    printSLL(head)

    head = deleteAtMidOfEvenOdd(head)
    print(f"After deleting from Mid:")
    printSLL(head)

    head = deleteAtMidOfEvenOdd(head)
    print(f"After deleting from Mid:")
    printSLL(head)

    head = deleteAtEnd(head)
    print(f"After deleting from End:")
    printSLL(head)
