"""
Intersection point of two Linked Lists

Given two singly linked lists that merge into a single Y-shaped list.
The two lists initially have distinct paths but eventually converge at a common node,
forming a Y-shape, the task is to find and return the node where the two lists merge.


"""

from Node import SingleLinkedList as Node


def getIntersectionPointOfTwoLinkedListUsingNestedLoop(head1: Node, head2: Node):
    while head2 is not None:
        currentNode = head1
        while currentNode is not None:

            # If both node are same
            if currentNode == head2:
                return head2
            currentNode = currentNode.next
        head2 = head2.next

    return None


def getIntersectionPointOfTwoLinkedListUsingHashing(head1: Node, head2: Node):
    seen = set()
    currentNode1 = head1

    while currentNode1 is not None:
        seen.add(currentNode1)
        currentNode1 = currentNode1.next

    currentNode2 = head2
    while currentNode2 is not None:
        if currentNode2 in seen:
            return currentNode2  # Intersection point found
        currentNode2 = currentNode2.next
    return None


def getCount(head: Node):
    count = 0
    currentNode = head
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next
    return count


def getIntersectionByDifference(difference: int, head1: Node, head2: Node):
    currentNode1 = head1
    currentNode2 = head2

    for _ in range(difference):
        if not currentNode1:
            return None
        currentNode1 = currentNode1.next

    while currentNode1 is not None and currentNode2 is not None:
        if currentNode1 == currentNode2:
            return currentNode1
        currentNode1 = currentNode1.next
        currentNode2 = currentNode2.next

    return None


def getIntersectionPointOfTwoLinkedListUsingDifference(head1: Node, head2: Node):
    length1 = getCount(head1)
    length2 = getCount(head2)

    if length1 > length2:
        difference = length1 - length2
        return getIntersectionByDifference(difference, head1, head2)
    else:
        difference = length2 - length1
        return getIntersectionByDifference(difference, head2, head1)


def getIntersectionPointOfTwoLinkedListUsingTwoPointer(head1: Node, head2: Node):
    currentNode1 = head1
    currentNode2 = head2

    # If any of the heads is None, there is no intersection
    if not currentNode1 or not currentNode2:
        return None

    # Traverse the lists until both pointers meet
    while currentNode1 != currentNode2:
        currentNode1 = currentNode1.next if currentNode1 is not None else head2
        currentNode2 = currentNode2.next if currentNode2 is not None else head1

    return currentNode1


# -------- Test --------
if __name__ == "__main__":
    # List A: 10 -> 15 -> 30
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    # List B: 3 -> 6 -> 9
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    # Connecting B to A at node 15 (shared reference)
    head2.next.next.next = head1.next

    intersectionPoint = getIntersectionPointOfTwoLinkedListUsingTwoPointer(head1, head2)
    print("Intersection Point:", intersectionPoint.data if intersectionPoint else "No intersection")
