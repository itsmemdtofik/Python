##String Method

#Case conversion method

text = "hello world"

# capitalize() - First character uppercase, rest lowercase
print(text.capitalize())  # "Hello world"

# title() - First character of each word uppercase
print(text.title())      # "Hello World"

# upper() - All characters uppercase
print(text.upper())      # "HELLO WORLD"

# lower() - All characters lowercase
print("HELLO".lower())   # "hello"

# casefold() - More aggressive lowercase (for case-insensitive comparisons)
print("STRASSE".casefold())  # "strasse" (German ß becomes ss)

# swapcase() - Swaps cases
print("Hello World".swapcase())  # "hELLO wORLD"


##Search and check method
text = "Python is fun and Python is powerful"

# count() - Count occurrences
print(text.count("Python"))  # 2

# startswith()/endswith() - Check prefix/suffix
print(text.startswith("Python"))  # True
print(text.endswith("ful"))       # True

# find()/rfind() - Find first/last occurrence (-1 if not found)
print(text.find("is"))      # 7 (first occurrence)
print(text.rfind("is"))     # 21 (last occurrence)

# index()/rindex() - Like find() but raises error if not found
print(text.index("fun"))    # 12
# print(text.index("java")) # ValueError

# isalnum() - Alphanumeric check
print("abc123".isalnum())  # True
print("abc 123".isalnum()) # False (space not alnum)

# isalpha() - Alphabet characters only
print("abc".isalpha())     # True
print("abc1".isalpha())    # False

# isnumeric()/isdigit()/isdecimal() - Number checks
print("123".isnumeric())   # True
print("½".isnumeric())     # True (Unicode numeric)
print("123".isdigit())     # True
print("½".isdigit())       # False


##Formatting method

# center()/ljust()/rjust() - Padding
print("hello".center(11, "-"))  # "---hello---"
print("hello".ljust(10, "*"))   # "hello*****"
print("hello".rjust(10, "*"))   # "*****hello"

# zfill() - Zero padding
print("42".zfill(5))           # "00042"

# format() - String formatting
print("{} is {}".format("Python", "awesome"))  # "Python is awesome"
print("{1} before {0}".format("A", "B"))      # "B before A"

# expandtabs() - Tab expansion
print("a\tb".expandtabs(4))    # "a   b"


##Cleaning anf manipulation method

text = "   Hello World!   "

# strip()/lstrip()/rstrip() - Remove whitespace
print(text.strip())    # "Hello World!"
print(text.lstrip())   # "Hello World!   "
print(text.rstrip())   # "   Hello World!"

# replace() - Replace substrings
print("Hello World".replace("World", "Python"))  # "Hello Python"

# partition()/rpartition() - Split at first/last occurrence
print("hello.world.py".partition("."))  # ('hello', '.', 'world.py')
print("hello.world.py".rpartition(".")) # ('hello.world', '.', 'py')

##Splitting and joining method

# split()/rsplit() - Split string
print("a,b,c".split(","))      # ['a', 'b', 'c']
print("a b c".split())         # ['a', 'b', 'c'] (default split on whitespace)
print("a,b,c".rsplit(",", 1))  # ['a,b', 'c'] (maxsplit=1 from right)

# splitlines() - Split by lines
print("line1\nline2\r\nline3".splitlines())  # ['line1', 'line2', 'line3']

# join() - Join iterable with string
print("-".join(["a", "b", "c"]))  # "a-b-c"

##Advanced method

# maketrans()/translate() - Character translation
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans))  # "h2ll4"

# format_map() - Format with mapping
data = {'name': 'Alice', 'age': 25}
print("{name} is {age} years old".format_map(data))  # "Alice is 25 years old"

# isidentifier() - Check if valid Python identifier
print("var_name".isidentifier())  # True
print("123var".isidentifier())    # False

# isprintable() - Check if all characters printable
print("Hello".isprintable())      # True
print("Hello\n".isprintable())    # False (contains newline)