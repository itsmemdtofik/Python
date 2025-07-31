"""
✅ sorted():
Returns a new sorted list.
Works on any iterable (like lists, tuples, dictionaries, etc.).
Original iterable remains unchanged.
"""

numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 9]
print(numbers)  # [5, 2, 9, 1] (original remains unchanged)

words = ['banana', 'apple', 'cherry', 'kiwi']

sorted_numbers = sorted(words, key=len)
print(f"Sort by length: {sorted_numbers}")

sorted_numbers = sorted(words, key=lambda x: [-1])
print(f"Sorted by the last character: {sorted_numbers}")

list_data = [5, 2, 9, 1]
sorted_numbers = sorted(list_data, reverse=True)
print(f"In descending order: {sorted_numbers}")

data = [(2, 'b'), (1, 'a'), (3, 'c')]

# Sort by the first element
print(sorted(data, key=lambda x: x[0]))

# Sort by the second element
print(sorted(data, key=lambda x: x[1]))

"""
✅ .sort():
Modifies the list in place (does not return a new list).
Works only on lists.
Returns None.
"""

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # [1, 2, 5, 9]

nums = ['banana', 'apple', 'cherry', 'kiwi']
nums.sort(key=len)
print(f"Sort by length using sort(): {nums}")

list_data = [5, 2, 9, 1]
list_data.sort(reverse=True)
print(f"In descending order: {list_data}")
