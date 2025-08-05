"""
🔹 HashMap Operations: Java vs Python 🔹

| **Operation**                | **Java (`HashMap<K, V>`)**                | **Python (`dict`)**                 |
| ---------------------------- | ----------------------------------------- | ----------------------------------- |
| **Create**                   | `Map<K, V> map = new HashMap<>();`        | `my_dict = defaultdict(int)`, or {} |
| **Insert / Add**             | `map.put(key, value);`                    | `my_dict[key] = value`              |
| **Update**                   | `map.put(key, newValue);`                 | `my_dict[key] = new_value`          |
| **Get value by key**         | `map.get(key);`                           | `my_dict.get(key)`                  |
| **Check key exists**         | `map.containsKey(key);`                   | `key in my_dict`                    |
| **Check value exists**       | `map.containsValue(value);`               | `value in my_dict.values()`         |
| **Remove a key**             | `map.remove(key);`                        | `my_dict.pop(key)`                  |
| **Get all keys**             | `map.keySet();`                           | `my_dict.keys()`                    |
| **Get all values**           | `map.values();`                           | `my_dict.values()`                  |
| **Get all entries**          | `map.entrySet();`                         | `my_dict.items()`                   |
| **Get size**                 | `map.size();`                             | `len(my_dict)`                      |
| **Clear all entries**        | `map.clear();`                            | `my_dict.clear()`                   |
| **Iterate (keys)**           | `for (K key : map.keySet())`              | `for key in my_dict:`               |
| **Iterate (key-value)**      | `for (Map.Entry<K,V> e : map.entrySet())` | `for key, value in my_dict.items()` |
| **Default value if missing** | `map.getOrDefault(key, default)`          | `my_dict.get(key, default)`         |
| **Put if absent**            | `map.putIfAbsent(key, value);`            | `my_dict.setdefault(key, value)`    |
| **Check if empty**           | `map.isEmpty();`                          | `not my_dict`                       |

# ✅ You can use Python’s collections default dict for most dictionary (hash map) operations — but with one key advantage:
# it automatically provides a default value for missing keys.
"""

my_dict = {}
# print(f"The value associated with this apple is {my_dict["apple"]} ")  # This will give KeyError

# ✅ That's why we use Python’s collections defaultdict for safe
from collections import defaultdict

d = defaultdict(int)  # Default value is 0

print(d["apple"])  # Outputs 0, instead of KeyError!

# Insert / Add a Key-Value Pair
my_dict["apple"] = 10
my_dict["banana"] = 11
my_dict["mango"] = 12
my_dict["orange"] = 13
my_dict["papaya"] = 14

# Update Value
my_dict["apple"] = 20  # Overwrites previous value

# Get Value by Key
val = my_dict.get("apple")  # Returns None if not found

# Check if Key Exists
if "apple" in my_dict:
    pass

# Check if Value Exists
if 20 in my_dict.values():
    pass

# Remove a Key
my_dict.pop("apple")

# Get All Keys
keys = my_dict.keys()

# Get All Values
values = my_dict.values()

# Get All Key-Value Pairs
entries = my_dict.items()

# Get Size
size = len(my_dict)

# Clear All Entries
my_dict.clear()

# Iterate Over Keys
for key in my_dict:
    print(key)

# Iterate Over Key-Value Pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Get with Default if Missing
val = my_dict.get("banana", 0)

# Put If Absent
my_dict.setdefault("banana", 15)

# Check if Empty
if not my_dict:
    pass
