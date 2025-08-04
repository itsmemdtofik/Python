"""
| Operation / Feature            | Description                                    | `list`             | `tuple` | `set`                        | `dict`                    |
| ------------------------------ | ---------------------------------------------- | ------------------ | ------- | ---------------------------- | ------------------------- |
| **Ordered**                    | Elements maintain the order you insert them    | ✅                  | ✅       | ❌                            | ✅ (≥3.7)                  |
| **Mutable**                    | Can change (add/remove/update) after creation  | ✅                  | ❌       | ✅                            | ✅                         |
| **Duplicates allowed**         | Whether duplicate values are allowed           | ✅                  | ✅       | ❌                            | ❌ (keys)                  |
| **Indexing**                   | Can access elements by index like `x[0]`       | ✅                  | ✅       | ❌                            | ❌                         |
| **Slicing**                    | Can extract ranges like `x[1:3]`               | ✅                  | ✅       | ❌                            | ❌                         |
| **Iteration**                  | Can loop through using `for x in ...`          | ✅                  | ✅       | ✅                            | ✅                         |
| **Membership test**            | Use `in` to check presence                     | ✅                  | ✅       | ✅                            | ✅ (keys)                  |
| **Add element**                | Add single item (`append`, `add`, or assign)   | ✅ `append()`       | ❌       | ✅ `add()`                    | ✅ `dict[key] = value`     |
| **Update element**             | Modify an existing item                        | ✅                  | ❌       | ❌ (remove & re-add)          | ✅                         |
| **Remove element**             | Remove item using method like `remove()`       | ✅ `remove()`       | ❌       | ✅ `remove()`                 | ✅ `pop(key)`              |
| **Pop element**                | Remove and return last/random item             | ✅ `pop()`          | ❌       | ✅ `pop()`                    | ✅ `pop(key)`              |
| **Insert at position**         | Add item at specific index                      | ✅ `insert()`       | ❌       | ❌                            | ❌                         |
| **Sort**                       | Sort elements                                  | ✅ `sort()`         | ❌       | ❌ (use `sorted(set)`)        | ❌                         |
| **Merge / Combine**            | Combine two structures                         | ✅ `+` / `extend()` | ✅ `+`   | ✅ `union()`                  | ✅ `update()`              |
| **Length**                     | `len()` returns number of elements             | ✅                  | ✅       | ✅                            | ✅                         |
| **Immutability**               | Cannot change after creation                   | ❌                  | ✅       | ❌                            | ❌                         |
| **Hashable (can be dict key)** | Can be used as key in dict or element in a set | ❌                  | ✅       | ✅ (if elements are hashable) | ✅ (keys must be hashable) |


"""

# list
lst = [1, 2, 3]
lst.append(4)
print(lst[1])  # Access by index

# tuple
tpl = (1, 2, 3)
print(tpl[1])  # Immutable

# set
st = {1, 2, 3}
st.add(4)
print(2 in st)  # Membership test

# dict
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d['a'])  # Access by key
