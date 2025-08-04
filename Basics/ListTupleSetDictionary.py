"""
🔢 1. list
Ordered, mutable, allows duplicates
Think of it like a dynamic array.
✅ Supports: indexing, slicing, iteration, nesting
"""
print(f"List Operations:")
my_list: list[int] = [1, 2, 3, 2]

my_list.append(4)  # Add
my_list[0] = 10  # Modify
print(my_list[1])  # Access

"""
🧱 2. tuple
Ordered, immutable, allows duplicates
Like a list, but cannot be changed after creation.
✅ Often used for fixed data (like coordinates, database records)
"""
print(f"Tuple Operations:")
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Access
# my_tuple[1] = 4       ❌ Error (immutable)

"""
🔥 3. set
Unordered, mutable, no duplicates
Based on hash tables — fast membership tests.
✅ Good for uniqueness and set operations: union, intersection, etc.
✅ Set does not support accessing the element
❗ set in Python does not support indexing
"""
print(f"Set Operations:")
my_set = {1, 2, 3, 2}
my_set.add(4)  # Add
my_set.remove(1)  # Remove
print(2 in my_set)  # Membership test

# ❗ set in Python does not support indexing
my_set = {10, 20, 30}
print(my_set[0])  # ❌ Error: TypeError: 'set' object is not subscriptable

# ❗ It does Iterate over the set
for item in my_set:
    print(item)

# ❗ Convert it to a list or tuple (if you need indexing)
my_list = list(my_set)
print(my_list[0])  # Now works, but order is arbitrary

"""
🧠 4. dict (HashMap)
Unordered (pre-3.7), mutable, key-value pairs
Keys must be immutable (e.g., str, int, tuple)
✅ Fast lookups, updates, deletions by key

"""
print(f"Dictionary Operations:")
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3  # Add
print(my_dict["a"])  # Access value

"""

"""
