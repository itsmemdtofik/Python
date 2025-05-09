# Create a sample list
fruits = ["apple", "banana", "cherry"]

# 1. append() - Adds an element at the end
fruits.append("orange")  # Now: ['apple', 'banana', 'cherry', 'orange']

# 2. clear() - Removes all elements
# fruits.clear()  # Now: []

# 3. copy() - Creates a copy
fruits_copy = fruits.copy()  # Same as fruits[:]

# 4. count() - Counts occurrences
apple_count = fruits.count("apple")  # Returns 1

# 5. extend() - Adds multiple elements
fruits.extend(["mango", "kiwi"])  # Now: ['apple', 'banana', 'cherry', 'orange', 'mango', 'kiwi']

# 6. index() - Finds position
banana_index = fruits.index("banana")  # Returns 1

# 7. insert() - Adds at specific position
fruits.insert(1, "pear")  # Inserts at position 1: ['apple', 'pear', 'banana', ...]

# 8. pop() - Removes by index
last_fruit = fruits.pop()  # Removes and returns 'kiwi'

# 9. remove() - Removes by value
fruits.remove("pear")  # Removes 'pear'

# 10. reverse() - Reverses the list
fruits.reverse()  # Now: ['mango', 'orange', 'cherry', 'banana', 'apple']

# 11. sort() - Sorts alphabetically
fruits.sort()  # Now: ['apple', 'banana', 'cherry', 'mango', 'orange']

print(fruits)  # Final list

'''
Each method modifies the original list (except copy() and count())

Methods like pop() and remove() return values while modifying the list

sort() and reverse() change the order permanently
'''