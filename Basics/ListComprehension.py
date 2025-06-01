#Performing mathmetical operations on lists using list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("Squared Numbers:", squared_numbers)


# List Comprehension for Filtering
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# List Comprehension for String Manipulation
words = ["hello", "world", "python"]
capitalized_words = [word.upper() for word in words]
print("Capitalized Words:", capitalized_words)

# List Comprehension for Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [num for sublist in nested_list for num in sublist]
print("Flattened List:", flattened_list)

# List Comprehension for Conditional Logic
numbers = [1, 2, 3, 4, 5]
conditional_list = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Conditional List:", conditional_list)

#Dictionary Comprehension
my_list = [1, 2, 3, 4, 5, 6]
squared_dict = {x:x**2 for x in my_list if x % 2 == 0}
print("Squared Dictionary:", squared_dict)