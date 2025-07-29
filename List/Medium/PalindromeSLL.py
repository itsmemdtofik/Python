"""
     * <pre>
     * !Palindrome Linked List
     * Given a singly linked list. The task is to check if the given linked list is palindrome or not.
     *
     * ! Approach1: Using Stack - O(n) Time and O(n) Space
     * ! Approach2: Using Iterative Method - O(n) Time and O(1) Space
     * </pre>
"""

from Node import SingleLinkedList as Node

class PalindromeLinkedList:

    @staticmethod
    def stack(head: Node) -> bool:
        stack = []
        currentNode = head
        while currentNode is not None:
            stack.append(currentNode.data)
            currentNode = currentNode.next

        currentNode = head
        while currentNode:
            if currentNode.data != stack.pop():
                return False
            currentNode = currentNode.next

        return True

    @staticmethod
    def iterative(head: Node) -> bool:

        if head is None or head.next is None:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        previousNode = None
        currentNode = slow
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        # Step 3: Compare both halves
        first_half = head
        second_half = previousNode
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    @staticmethod
    def twoPointer(head: Node) -> bool:
        if head is None or head.next is None:
            return True

        # Convert to list
        values = []
        currentNode = head
        while currentNode:
            values.append(currentNode.data)
            currentNode = currentNode.next

        # Two-pointer check
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    # Create a list: 1 -> 2 -> 3 -> 2 -> 1 -> 10
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(10)

    result = PalindromeLinkedList.twoPointer(head)

    if result:
        print("List is Palindrome")
    else:
        print("List is not Palindrome")
