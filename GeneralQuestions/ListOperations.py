"""
✅ Python List Operations Summary Table:

| **Operation**             | **Syntax / Method**           | **Description**                       | **Example & Result**              |
| ------------------------- | ----------------------------- | ------------------------------------- | --------------------------------- |
| **Create list**           | `lst = [1, 2, 3]`             | Creates a list                        | `[1, 2, 3]`                       |
| **Access item**           | `lst[i]`                      | Gets item at index `i`                | `lst[0] → 1`                      |
| **Negative indexing**     | `lst[-1]`                     | Gets last item                        | `lst[-1] → 3`                     |
| **Slice**                 | `lst[1:3]`                    | Sublist from index 1 to 2             | `[2, 3]`                          |
| **Length**                | `len(lst)`                    | Number of elements                    | `3`                               |
| **Append**                | `lst.append(x)`               | Adds `x` to end                       | `[1, 2, 3] → [1, 2, 3, x]`        |
| **Extend**                | `lst.extend([4, 5])`          | Adds multiple items                   | `[1, 2] → [1, 2, 4, 5]`           |
| **Insert**                | `lst.insert(1, x)`            | Inserts `x` at index 1                | `[1, x, 2, 3]`                    |
| **Remove**                | `lst.remove(x)`               | Removes first `x`; error if not found  | `[1, 2, 2].remove(2) → [1, 2]`    |
| **Pop**                   | `lst.pop()` / `lst.pop(i)`    | Removes & returns last / i-th item    | `pop() → 3`                       |
| **Clear**                 | `lst.clear()`                 | Removes all elements                  | `[]`                              |
| **Index of item**         | `lst.index(x)`                | First index of `x`                    | `lst.index(2) → 1`                |
| **Count item**            | `lst.count(x)`                | Number of occurrences                 | `lst.count(2) → 2`                |
| **Reverse (in-place)**    | `lst.reverse()`               | Reverses list in-place                | `[1, 2] → [2, 1]`                 |
| **Sorted (new list)**     | `sorted(lst)`                 | Returns sorted copy                   | `[3, 1] → [1, 3]`                 |
| **Sort in-place**         | `lst.sort()`                  | Sorts the list                        | `[3, 1] → [1, 3]`                 |
| **Copy list**             | `lst.copy()` or `lst[:]`      | Shallow copy                          | `new = lst.copy()`                |
| **Join list of strings**  | `' '.join(lst)`               | Joins list into string                | `['a','b'] → 'a b'`               |
| **Repeat list**           | `lst * 3`                     | Repeats contents                      | `[1, 2] * 3 → [1, 2, 1, 2, 1, 2]` |
| **Membership**            | `x in lst`                    | True if `x` in list                   | `2 in [1,2,3] → True`             |
| **Loop through list**     | `for item in lst:`            | Iterate each item                     | prints all                        |
| **Enumerate items**       | `for i, v in enumerate(lst):` | Index + value pair                    | `i, v`                            |
| **List comprehension**    | `[x*x for x in lst]`          | Transform items                       | `[1, 4, 9]`                       |
| **Filter with list comp** | `[x for x in lst if x > 2]`   | Conditional list                      | `[3, 4]`                          |
| **Nested list access**    | `lst[0][1]`                   | Access inner list elements            | `[[1,2],[3,4]] → 2`               |

"""

"""
🔢 Math/Conversion Utilities:

| **Function**     | **Description**               | **Example**                |
| ---------------- | ----------------------------- | -------------------------- |
| `sum(lst)`       | Sum of all elements           | `[1,2,3] → 6`              |
| `min(lst)`       | Minimum element               | `[1,2,3] → 1`              |
| `max(lst)`       | Maximum element               | `[1,2,3] → 3`              |
| `list(str)`      | Convert to list of characters | `'abc' → ['a','b','c']`    |
| `list(range(n))` | Create numeric list           | `list(range(3)) → [0,1,2]` |

"""
"""
✅ Advanced Tricks:

| **Trick**    | **Code**                      | **Result**                      |
| ------------ | ----------------------------- | ------------------------------- |
| Reverse copy | `lst[::-1]`                   | Returns reversed list           |
| Unique items | `list(set(lst))`              | Removes duplicates (unordered)  |
| Flatten list | `[y for x in lst for y in x]` | Flattens 2D list                |
| Zip lists    | `zip(list1, list2)`           | Pairs items from both lists     |
| Unpack list  | `a, b, c = lst`               | Assign each element to variable |

"""

print(f"All List Operations:\n")

# Create a list
nums: list[int] = [1, 2, 3]

# Access item (Indexing)
print(f"First Element: {nums[0]}")

# Negative indexing
print(f"Last element in the list: {nums[-1]}")

# List slicing
print(nums[1:3])  # Output: [2, 3]

# Insert an item from end
nums.append(4)

# Adds multiple item at once
nums.extend([5, 6])  # Output: [1, 2, 3, 4, 5, 6]
print(nums)

# Insert item on index to remember the ordering
nums.insert(2, 10)
print(nums)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Remove : Removes the first occurrence of 10. Raises an error if not found.
nums.remove(10)
print(nums)  # Output: [1, 2, 3, 4, 5, 6]

# Pop element from the list, Removes and returns the last element. lst.pop(i) removes by index.
x = nums.pop()
print(x)  # Output: 6
print(nums)  # Output: [1, 2, 3, 4, 5]

# Clear the list
nums.clear()
print(nums)  # Output: []

# Index: Returns the first index of 2.
nums = [1, 2, 3, 2]
print(nums.index(2))  # Output: 1

# Count: Counts how many times 2 occurs in the list.
print(nums.count(2))  # Output: 2

# Reverse list in-place
nums.reverse()
print(nums)  # Output: [2, 3, 2, 1]

# Sort list in-place
nums.sort()
print(nums)  # Output: [1, 2, 2, 3]

# Sorted(new_list): Returns a new sorted list; original remains unchanged.
lst = [3, 1, 2]
new_lst = sorted(lst)
print(new_lst)  # Output: [1, 2, 3]

# Copy the list
copy_lst = lst.copy()
print(copy_lst)  # Output: [3, 1, 2]

# Join list of string
words = ['hello', 'world']
print(' '.join(words))  # Output: 'hello world'

# Multiply List: Repeats list contents.
print([0] * 5)  # Output: [0, 0, 0, 0, 0]

# Membership: Checks if value exists in the list.
print(2 in lst)  # Output: True

# Loop through list: Iterates over each element.
for item in lst:
    print(item)

# Enumerate (Index + Value): Returns both index and value.
for index, value in enumerate(lst):
    print(f"Index is: {index}, Value is: {value}")

# List comprehension: Creates a list using a single-line loop
squares = [x * x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Filter with List Comprehension: Includes elements conditionally.
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Nested List: Accesses an item from a list inside a list.
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Output: 3

# Flatten a List: Flattens 2D list into 1D
flat = [y for x in matrix for y in x]
print(flat)  # Output: [1, 2, 3, 4]

# Zip two list: Pairs items from both lists into tuples.
names = ['a', 'b']
ages = [10, 20]
print(list(zip(names, ages)))  # Output: [('a', 10), ('b', 20)]

# Unpack list: Assigns elements to individual variables.
a, b, c = [1, 2, 3]
print(a, b, c)  # Output: 1 2 3

# Reverse copy (Not in-place)
lst = [1, 2, 3]
rev = lst[::-1]
print(rev)  # Output: [3, 2, 1]
