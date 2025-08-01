# ✅  Code 1:
while current.next is not None:
    current = current.next
# current is now the last node
"""
✔️ Behavior:
Stops at the last node (i.e., where current.next == None)
This is the correct approach when you want to modify the last node, such as appending a new node at the end.
"""

"""
⏸️ Example:
For list: 10 → 20 → 30

Iteration 1: current = 10 → current.next = 20 → OK
Iteration 2: current = 20 → current.next = 30 → OK
Iteration 3: current = 30 → current.next = None → Stop
➡️ current is now at 30 (✅ last node)"""

# ❌ Code 2:

while current is not None:
    current = current.next
# current is now the last node (WRONG!)
"""
❗ Behavior:
This loop continues until current becomes None
It goes past the last node (since current = current.next where current.next = None)

"""


# ✅ 1. while current.next is not None:
# 🔧 Use Case: When you want to stop at the last node, usually to perform an operation on it — like inserting at the end, checking its value, etc.
# ✅ Common Examples:
# 🔹 Inserting at the end of a linked list:
def insertAtEnd(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next is not None:
        current = current.next

    current.next = new_node  # attach to last node
    return head


# 🔹 Getting the value of the last node:
while current.next is not None:
    current = current.next
print("Last node data:", current.data)

# ❗ 2. while current is not None:
# 🔎 Use Case: When you want to traverse the entire list, visiting every node, and you don’t care about doing anything after the loop.
# 🔹 Printing the entire list:
while current is not None:
    print(current.data)
    current = current.next

# 🔹 Counting nodes:
count = 0
while current is not None:
    count += 1
    current = current.next
print("Length of list:", count)

# 🔹 Searching for a value:
found = False
target = None
while current is not None:
    if current.data == target:
        found = True
        break
    current = current.next
"""
| Loop                             | Use When You Want To...                               | Stops At     |
| -------------------------------- | ----------------------------------------------------- | ------------ |
| `while current.next is not None` | Access/modify the **last node** (e.g., insert at end) | ✅ Last node  |
| `while current is not None`      | Visit **all nodes** (e.g., print, count, search)      | ❌ After last |

"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def insertAtMidOfEvenOdd(head: Node, data: int) -> Node:
    new_node = Node(data)

    # Empty list
    if not head:
        return new_node

    slow = fast = head
    prev = None

    # Find middle
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Insertion logic
    if not fast:  # Even-length: insert before second middle
        if not prev:  # Only 2 nodes
            new_node.next = head
            return new_node
        prev.next = new_node
        new_node.next = slow
    else:  # Odd-length: insert after middle
        new_node.next = slow.next
        slow.next = new_node

    return head
