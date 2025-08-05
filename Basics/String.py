"""
✅ Python String Operations Summary Table:

| **Operation**           | **Syntax / Method**  | **Description**                        | **Example**                 |
| ----------------------- | -------------------- | -------------------------------------- | --------------------------- |
| **Create string**       | `s = "hello"`        | Declare a string                       | `"hello"`                   |
| **Access character**    | `s[0]`               | Get character at index                 | `'h'`                       |
| **Slice string**        | `s[1:4]`             | Substring from index 1 to 3            | `'ell'`                     |
| **Reverse string**      | `s[::-1]`            | Returns reversed string                | `'olleh'`                   |
| **Concatenate**         | `s + " world"`       | Combine strings                        | `'hello world'`             |
| **Repeat string**       | `s * 3`              | Repeat string 3 times                  | `'hellohellohello'`         |
| **Check membership**    | `'h' in s`           | Returns True if character is in string | `True`                      |
| **Length**              | `len(s)`             | Number of characters                   | `5`                         |
| **Convert to list**     | `list(s)`            | Converts string to list of characters  | `['h', 'e', 'l', 'l', 'o']` |
| **Join list to string** | `''.join(['h','e'])` | Combines list into string              | `'he'`                      |

"""

"""
🧹 String Methods (Modification & Query):

| **Method**                          | **Description**                       | **Example & Result**                      |
| ----------------------------------- | ------------------------------------- | ----------------------------------------- |
| `s.lower()`                         | Lowercase                             | `'HELLO'.lower()` → `'hello'`             |
| `s.upper()`                         | Uppercase                             | `'hello'.upper()` → `'HELLO'`             |
| `s.title()`                         | Title case                            | `'hello world'.title()` → `'Hello World'` |
| `s.capitalize()`                    | Capitalize first letter                | `'hello'.capitalize()` → `'Hello'`        |
| `s.strip()`                         | Remove leading/trailing whitespace    | `' hello '.strip()` → `'hello'`           |
| `s.lstrip()` / `s.rstrip()`         | Left/right strip                      | `' hello '.lstrip()` → `'hello '`         |
| `s.replace(a, b)`                   | Replace substring                     | `'hi hi'.replace('hi','ho')` → `'ho ho'`  |
| `s.find(x)`                          | First index of x or `-1`              | `'apple'.find('p')` → `1`                  |
| `s.index(x)`                        | Like `find()` but errors if not found  | `'apple'.index('p')` → `1`                |
| `s.count(x)`                        | Count occurrences                     | `'hello'.count('l')` → `2`                |
| `s.startswith(x)` / `s.endswith(x)` | Check prefix/suffix                     | `'hello'.startswith('he')` → `True`       |
| `s.isalpha()`                       | All letters                           | `'abc'.isalpha()` → `True`                |
| `s.isdigit()`                       | All digits                            | `'123'.isdigit()` → `True`                |
| `s.isalnum()`                       | Alphanumeric                          | `'abc123'.isalnum()` → `True`             |
| `s.isspace()`                       | All whitespace                        | `'   '.isspace()` → `True`                |
| `s.swapcase()`                      | Switch case                           | `'HeLLo'.swapcase()` → `'hEllO'`          |
| `s.zfill(n)`                         | Pad with zeros                        | `'7'.zfill(3)` → `'007'`                   |

"""
"""
🧪 String Testing:

| **Check**                | **Example**   | **Result**      |
| ------------------------ | ------------- | --------------- |
| Empty string             | `s == ''`     | `True` if empty |
| Contains only letters    | `s.isalpha()` | `True`/`False`  |
| Contains only digits     | `s.isdigit()` | `True`/`False`  |
| Contains only alphanum   | `s.isalnum()` | `True`/`False`  |
| Contains only whitespace | `s.isspace()` | `True`/`False`  |

"""
"""
🔍 Splitting and Joining:

| **Operation**       | **Syntax**            | **Example & Result**                           |
| ------------------- | --------------------- | ---------------------------------------------- |
| Split by space      | `s.split()`           | `'a b c'.split()` → `['a','b','c']`            |
| Split by delimiter  | `s.split(',')`        | `'a,b,c'.split(',')` → `['a','b','c']`         |
| Join with delimiter | `','.join(['a','b'])` | `'a,b'`                                        |
| Partition           | `s.partition('x')`    | `'a-x-b'.partition('-')` → `('a', '-', 'x-b')` |

"""

"""
✅ Advanced and Useful:
| **Operation**    | **Syntax**               | **Example & Result**        |
| ---------------- | ------------------------ | --------------------------- |
| String reverse   | `s[::-1]`                | `'hello'[::-1]` → `'olleh'` |
| Ordinal value    | `ord('A')`               | `65`                        |
| Char from ASCII  | `chr(65)`                | `'A'`                       |
| Check palindrome | `s == s[::-1]`           | `'madam'` → `True`          |
| Count characters | `collections.Counter(s)` | `{'a': 2, 'b': 1}`          |

"""
# String Indexing and slicing,
# String immutability→ Strings can't be changed in-place; you must create a new one.

string = "hello world"
print(f"Index Zero: {string[0]} and {string[-1]}")
print(f"{string[1:4]} and Reverse String is: {string[::-1]}")

# String method:  .upper(), .lower(), .strip(), .replace(), .find(), .split(), .join()
x = 'Hello, World!'

print(x.upper())
print(x.lower())
print(x.strip())
print(x.split(','))
print(x.replace('e', 'a'))

# Concatenating string

# This won't work
'''age = 25
txt = 'My name is Jhon, I am ' + age
print(txt)'''

# We use the F-String method to solve this issue
age = 34
txt = f'My name is Jhon, I am {age}'
print(txt)

x = 'abababa'

for i in x:
    print(i)

if 'z' not in x:
    print("Not there")

print(x[1])
print(len(x))
