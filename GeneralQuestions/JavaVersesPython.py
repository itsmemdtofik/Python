"""
🔹 1. Java Stack Operations 🔹

| **Operation**          | **Java (Legacy Stack)** | **Modern Java (Deque - Preferred)**          |
| ---------------------- | ----------------------- | -------------------------------------------- |
| **Push**               | `stack.push(item)`      | `deque.push(item)` or `deque.addFirst(item)` |
| **Pop**                | `stack.pop()`           | `deque.pop()` or `deque.removeFirst()`       |
| **Peek (top element)** | `stack.peek()`          | `deque.peek()` or `deque.peekFirst()`        |
| **Check if empty**     | `stack.isEmpty()`       | `deque.isEmpty()`                            |
| **Size**               | `stack.size()`          | `deque.size()`                               |

| Term     | Meaning                                                             |
| -------- | ------------------------------------------------------------------- |
| **Top**  | The most recently added element (last in) — top of the stack        |
| **Peek** | An operation to **look at the top** element **without removing** it |


Modern Java (Preferred: Deque for Stack):
"""

"""
📚 1. Python Stack Operations(Option: 1):
# Python does not have a dedicated Stack class, but list or deque can be used.

| **Operation**          | **Using `list`**     | **Using `collections.deque`** |
| ---------------------- | -------------------- | ----------------------------- |
| **Push**               | `stack.append(item)` | `stack.append(item)`          |
| **Pop**                | `stack.pop()`        | `stack.pop()`                 |
| **Peek (top element)** | `stack[-1]`          | `stack[-1]`                   |
| **Check if empty**     | `len(stack) == 0`    | `len(stack) == 0`             |
| **Size**               | `len(stack)`         | `len(stack)`                  |

| Term     | Meaning                                                             |
| -------- | ------------------------------------------------------------------- |
| **Top**  | The most recently added element (last in) — top of the stack        |
| **Peek** | An operation to **look at the top** element **without removing** it |

# Modern Python (Preferred: Deque for Stack): Since deque is optimized for fast appends/pops from both ends, it can also be used for stacks.
# In Python, we use collections.deque (double-ended queue) for efficient LIFO operations.

"""

stack = []
stack.append(10)  # Push to the stack
stack.append(20)  # Push to the stack
stack.append(30)  # Push to the stack
stack.append(40)  # Push to the stack

print(f"Stack Operations using List:")
length = len(stack)  # Find the length of the stack
print(f"The size of the stack is : {length}")

top = stack.pop()  # Pop from the stack
print(f"The top element of the stack is : {top}")

peek = stack[-1]  # Find peek element from the stack
print(f"The peek element of the stack is : {peek}")

isEmpty = not stack  # Check if ths stack is empty or not
print(f"Check whether the stack is empty or not: {isEmpty}")
print("\n")

"""
📚 Using collections.deque (More Efficient for Large Stacks): Option 2

| **Operation**      | **Python (`deque`)** |
| ------------------ | -------------------- |
| **Push**           | `stack.append(item)` |
| **Pop**            | `stack.pop()`        |
| **Peek**           | `stack[-1]`          |
| **Check if empty** | `not stack`          |
| **Size**           | `len(stack)`         |

# Modern Python (Preferred: Deque for Stack): Since deque is optimized for fast appends/pops from both ends, it can also be used for stacks.
# In Python, we use collections.deque (double-ended queue) for efficient LIFO operations.
"""
from collections import deque

stack = deque()
stack.append(10)  # Push to the stack
stack.append(20)  # Push to the stack
stack.append(30)  # Push to the stack
stack.append(40)  # Push to the stack

print(f"Stack Operations using Dequeue:")

length = len(stack)  # Find the length of the stack
print(f"The size of the stack is : {length}")

peek = stack[-1]  # Find peek element from the stack
print(f"The peek element of the stack is : {peek}")

top = stack.pop()  # Pop from the stack
print(f"The top element of the stack is : {top}")

peek = stack[-1]  # Find peek element from the stack
print(f"The peek element after popping of the stack is : {peek}")

isEmpty = not stack  # Check if ths stack is empty or not
print(f"Check whether the stack is empty or not: {isEmpty}")
print("\n")

"""
📚 Queue Operations in Python(FIFO) Order:

| **Operation**      | **Python (`deque`)** | **Description**                                    |
| ------------------ | -------------------- | -------------------------------------------------- |
| **Enqueue**        | `queue.append(item)` | Adds an element to the end (rear) of the queue.    |
| **Dequeue**        | `queue.popleft()`    | Removes and returns the front element (head).      |
| **Peek**           | `queue[0]`           | Retrieves (but does not remove) the front element. |
| **Check if empty** | `not queue`          | Returns `True` if the queue is empty.              |
| **Size**           | `len(queue)`         | Returns the number of elements in the queue.       |

# In Python, we use collections.deque (double-ended queue) for efficient FIFO operations.
"""

from collections import deque

queue = deque()

queue.append(11)
queue.append(12)
queue.append(13)
queue.append(14)

front = queue[0]  # Peek (check front element), Raises Index Error if empty

if queue:  # Check if not empty to avoid errors
    removed_item = queue.popleft()
    print(removed_item)

isEmpty = not queue  # Check if empty
print(f"Check whether the queue is empty or not : {isEmpty}")

size = len(queue)
print(f"The size of the queue is : {size}")

"""
🔑 Key Differences Between Java Queue and Python deque:

| **Feature**        | **Java (`Queue`)**             | **Python (`deque`)**                          |
| ------------------ | ------------------------------ | --------------------------------------------- |
| **Implementation** | `LinkedList` (or `ArrayDeque`) | `collections.deque`                           |
| **Enqueue**        | `add()` / `offer()`            | `append()`                                    |
| **Dequeue**        | `remove()` / `poll()`          | `popleft()`                                   |
| **Peek**           | `element()` / `peek()`         | `queue[0]`                                    |
| **Empty Check**    | `isEmpty()`                    | `not queue`                                   |
| **Thread Safety**  | Not thread-safe by default     | Not thread-safe (`use queue.Queue` if needed) |
| **Performance**    | O(1) for all operations        | O(1) for all operations                       |

"""

