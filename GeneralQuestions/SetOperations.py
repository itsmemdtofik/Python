"""
✅ Python Set Operations Summary Table:

| Operation                                  | Syntax                                     | Description                                         | Example                                 |          |                      |
| ------------------------------------------ | ------------------------------------------ | --------------------------------------------------- | --------------------------------------- | -------- | -------------------- |
| **Create a set**                           | `s = {1, 2, 3}` or `set([1, 2, 3])`        | Creates a set                                       | `s = {1, 2, 3}`                         |          |                      |
| **Add an element**                         | `s.add(x)`                                 | Adds element `x` to the set                         | `s.add(4)` → `{1, 2, 3, 4}`             |          |                      |
| **Remove an element (error if not found)** | `s.remove(x)`                              | Removes element `x`; raises `KeyError` if not found | `s.remove(2)`                           |          |                      |
| **Remove an element (safe)**               | `s.discard(x)`                             | Removes element `x`; does nothing if not found      | `s.discard(100)`                        |          |                      |
| **Pop random element**                     | `s.pop()`                                  | Removes and returns an arbitrary element            | `s.pop()`                               |          |                      |
| **Clear all elements**                     | `s.clear()`                                | Empties the set                                     | `s.clear()` → `set()`                   |          |                      |
| **Set length**                             | `len(s)`                                   | Number of elements in the set                       | `len({1,2,3})` → `3`                    |          |                      |
| **Membership check**                       | `x in s`                                   | Checks if `x` is in the set                         | `2 in s` → `True`                       |          |                      |
| **Union**                                  | \`s1                                       | s2`or`s1.union(s2)\`                                | Combines elements from both sets        | \`{1, 2} | {2, 3}`→`{1, 2, 3}\` |
| **Intersection**                           | `s1 & s2` or `s1.intersection(s2)`         | Elements common to both sets                        | `{1, 2} & {2, 3}` → `{2}`               |          |                      |
| **Difference**                             | `s1 - s2` or `s1.difference(s2)`           | Elements in `s1` but not in `s2`                    | `{1, 2} - {2, 3}` → `{1}`               |          |                      |
| **Symmetric difference**                   | `s1 ^ s2` or `s1.symmetric_difference(s2)` | Elements in either set but not both                 | `{1, 2} ^ {2, 3}` → `{1, 3}`            |          |                      |
| **Subset check**                           | `s1 <= s2` or `s1.issubset(s2)`            | Checks if `s1` is a subset of `s2`                  | `{1, 2} <= {1, 2, 3}` → `True`          |          |                      |
| **Proper subset**                          | `s1 < s2`                                  | True if `s1` is a proper subset                     | `{1, 2} < {1, 2, 3}` → `True`           |          |                      |
| **Superset check**                         | `s1 >= s2` or `s1.issuperset(s2)`          | Checks if `s1` is a superset of `s2`                | `{1, 2, 3} >= {2}` → `True`             |          |                      |
| **Proper superset**                        | `s1 > s2`                                  | True if `s1` is a proper superset                   | `{1, 2, 3} > {2}` → `True`              |          |                      |
| **Equality**                               | `s1 == s2`                                 | True if both sets have the same elements            | `{1, 2} == {2, 1}` → `True`             |          |                      |
| **Inequality**                             | `s1 != s2`                                 | True if sets are not equal                          | `{1, 2} != {1, 3}` → `True`             |          |                      |
| **Set comprehension**                      | `{x*x for x in range(5)}`                  | Creates a set with logic                            | `{x*x for x in range(3)}` → `{0, 1, 4}` |          |                      |
| **Immutable set**                          | `frozenset([1, 2, 3])`                     | Creates an immutable set                            | `fs = frozenset([1, 2, 3])`             |          |                      |

"""

# Creating a Set, or seen = set([1, 2]), or seen = set()
seen = set()

# Add elements
seen.add(10)
seen.add(20)
seen.add(30)
seen.add(40)

# Remove Elements
# seen.remove(2)  # raises KeyError if not present
seen.discard(2)  # It does not raise KeyError if not present
seen.clear()  # removes all

seen.add(10)
seen.add(20)
seen.add(30)
seen.add(40)

# Check Membership
for i in seen:
    pass

# Update the set: Adds multiple elements from any iterable.
seen.update([5, 6])
print(seen)  # {10, 20, 30, 40, 5, 6}

# Size of set
len(seen)

# Iteration
for val in seen:
    print(val)

# Set Union
set1 = set()
set2 = set()

union = set1 | set2

# Or
union_all = set1.union(set2)

# Set Intersection
intersection = set1 & set2

# OR
intersection_set = set1.intersection(set2)

# Set Difference
difference = set1 - set2

# OR
difference_set = set1.difference(set2)

# Symmetric Difference ( Manual Implementation)
sym_diff = set1 ^ set2

# OR
sym_diff_set = set1.symmetric_difference(set2)

# Subset or Superset
var1 = set2 <= set1  # Subset
var2 = set1 >= set2  # Superset

# Equality check
var3 = set1 == set2

# Immutable Sets
frozen_set = frozenset(["a", "b", "c"])

# Covert list to set (Deduplication)
nums: list[int] = [1, 2, 2, 3]
nums_set = set(nums)

print(f"Original List: {nums}")
print(f"After list converted into set: {nums_set}")

# Set comprehension
squared = {x * x for x in nums_set}
print(f"Set comprehension: {squared}")

# Subset Check: Checks if all elements of one set are in another.
print({1, 2} <= {1, 2, 3})  # True
# or
print({1, 2}.issubset({1, 2, 3}))  # True

# Superset Check: Checks if the set contains all elements of another set.
print({1, 2, 3} >= {1, 2})  # True
# or
print({1, 2, 3}.issuperset({1, 2}))  # True

# Set equality: Order does not matter in sets.
print({1, 2} == {2, 1})  # True

# Set Inequality: Order does not matter in sets.
print({1, 2} != {1, 3})  # True

# Convert List to Set (Remove Duplicates)
lst = [1, 2, 2, 3]
unique = set(lst)
print(unique)  # {1, 2, 3}

# Immutable set: Immutable version of a set. Cannot be changed after creation.
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# Iterate through a set: Set iteration order is unpredictable.
for item in {1, 2, 3}:
    print(item)

"""
| **Operation**               | **Java Syntax**                                                     | **Python Syntax**                          | **Description**                                             |                    |
| --------------------------- | ------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------- | ------------------ |
| **Create a Set**            | `Set<Integer> s = new HashSet<>();`                                 | `s = set()` or `s = {1, 2}`                | Creates an empty or populated set                           |                    |
| **Add an element**          | `s.add(1);`                                                         | `s.add(1)`                                 | Adds an element                                             |                    |
| **Remove an element**       | `s.remove(1);`                                                      | `s.remove(1)` / `s.discard(1)`             | Removes element (KeyError in Python if not using `discard`) |                    |
| **Clear set**               | `s.clear();`                                                        | `s.clear()`                                | Empties the set                                             |                    |
| **Set size**                | `s.size();`                                                         | `len(s)`                                   | Returns number of elements                                  |                    |
| **Check membership**        | `s.contains(1);`                                                    | `1 in s`                                   | Checks if element exists                                    |                    |
| **Union**                   | `Set<T> u = new HashSet<>(s1); u.addAll(s2);`                       | \`s1                                       | s2`or`s1.union(s2)\`                                        | Combines both sets |
| **Intersection**            | `Set<T> i = new HashSet<>(s1); i.retainAll(s2);`                    | `s1 & s2` or `s1.intersection(s2)`         | Common elements                                             |                    |
| **Difference**              | `Set<T> d = new HashSet<>(s1); d.removeAll(s2);`                    | `s1 - s2` or `s1.difference(s2)`           | Elements in `s1` not in `s2`                                |                    |
| **Symmetric difference**    | `Set<T> sd = new HashSet<>(s1); sd.addAll(s2); sd.removeAll(temp);` | `s1 ^ s2` or `s1.symmetric_difference(s2)` | Elements in either set, but not both                        |                    |
| **Subset check**            | `s1.containsAll(s2);`                                               | `s2 <= s1` or `s2.issubset(s1)`            | True if `s2` is a subset of `s1`                            |                    |
| **Superset check**          | `s2.containsAll(s1);`                                               | `s2 >= s1` or `s2.issuperset(s1)`          | True if `s2` is a superset of `s1`                          |                    |
| **Equality check**          | `s1.equals(s2);`                                                    | `s1 == s2`                                 | True if both sets are equal                                 |                    |
| **Iterate over set**        | `for (T item : s) { ... }`                                          | `for item in s:`                           | Loop over each element                                      |                    |
| **Convert list to set**     | `Set<T> s = new HashSet<>(list);`                                   | `s = set(list)`                            | Removes duplicates from list                                |                    |
| **Set comprehension / map** | `list.stream().map(...).collect(Collectors.toSet());`               | `{x*x for x in iterable}`                  | Create a set with logic                                     |                    |
| **Immutable set**           | `Set<T> s = Set.of(1, 2, 3);` (Java 9+)                             | `frozenset([1, 2, 3])`                     | Read-only / unchangeable set                                |                    |

"""
