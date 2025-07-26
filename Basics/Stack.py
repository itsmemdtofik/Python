"""
In Python, a stack is typically implemented using a list, and yes, you use:

1. append() to push
2. pop() to pop

| Stack Operation | Java              | Python using list |
| --------------- | ----------------- | ----------------- |
| Push            | `stack.push(x)`   | `stack.append(x)` |
| Pop             | `stack.pop()`     | `stack.pop()`     |
| Peek            | `stack.peek()`    | `stack[-1]`       |
| Is Empty        | `stack.isEmpty()` | `len(stack) == 0` |
| Size            | `stack.size()`    | `len(stack)`      |

"""

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

top = stack.pop()
print(top)
print(stack)

