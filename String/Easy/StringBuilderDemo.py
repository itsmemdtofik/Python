import sys
import time


class StringBuilderDemo:
    def __init__(self):
        print("\n=== Constructors ===")

        # Python strings are immutable, so we use lists for mutability
        self.sb1 = []  # Default empty list
        self.sb2 = []  # Python doesn't have pre-allocation like Java's capacity
        self.sb3 = list("Hello")
        self.sb4 = self.sb3.copy()

        print(f"sb1 (empty): {''.join(self.sb1)}")
        print(f"sb2 (empty): {''.join(self.sb2)}")
        print(f"sb3 (\"Hello\"): {''.join(self.sb3)}")
        print(f"sb4 (copy of sb3): {''.join(self.sb4)}")

        print("\n=== Modifying Content ===")

        self.sb = list("Hello")
        print(f"Original: {''.join(self.sb)}")

        # Append operations
        self.sb.extend(list(" World"))  # "Hello World"
        self.sb.extend(list(str(123)))  # "Hello World123"
        self.sb.extend(list(str(True).lower()))  # "Hello World123true"
        print(f"After append: {''.join(self.sb)}")

        # Insert operations
        self.sb.insert(5, ",")  # "Hello, World123true"
        print(f"After insert: {''.join(self.sb)}")

        # Replace operations (slice assignment)
        self.sb[7:12] = list("Java")  # "Hello, Java123true"
        print(f"After replace: {''.join(self.sb)}")

        # Delete operations
        del self.sb[5:6]  # "Hello Java123true"
        print(f"After delete: {''.join(self.sb)}")
        del self.sb[5]  # "HelloJava123true"
        print(f"After deleteCharAt: {''.join(self.sb)}")

        # Reverse operation
        self.sb.reverse()  # "eurt321avaJolleH"
        print(f"After reverse: {''.join(self.sb)}")
        self.sb.reverse()  # Back to "HelloJava123true"

        # Set character
        self.sb[0] = 'h'  # "helloJava123true"
        print(f"After setCharAt: {''.join(self.sb)}")

        print("\n=== Accessing Content ===")

        # Character access
        ch = self.sb[1]  # 'e'
        print(f"charAt(1): {ch}")

        # Substring operations
        sub1 = ''.join(self.sb[0:])  # Full string
        sub2 = ''.join(self.sb[0:5])  # "hello"
        print(f"substring(0): {sub1}")
        print(f"substring(0,5): {sub2}")

        # Index operations
        temp_str = ''.join(self.sb)
        index1 = temp_str.find("Java")
        index2 = temp_str.rfind("Java")
        print(f"indexOf(\"Java\"): {index1}")
        print(f"lastIndexOf(\"Java\"): {index2}")

        # Conversion to string
        final_string = ''.join(self.sb)
        print(f"toString(): {final_string}")

        print("\n=== Utility Methods ===")

        # Length
        length = len(self.sb)
        print(f"length(): {length}")

        # Python lists grow dynamically, no direct capacity concept
        # But we can check memory size
        size = sys.getsizeof(self.sb)
        print(f"memory size: {size} bytes")

        # Length management
        self.sb = self.sb[:10]  # Truncate to length 10
        print(f"After setLength(10): '{''.join(self.sb)}'")
        print(f"length after setLength: {len(self.sb)}")

        print("\n=== Performance Comparison ===")

        # String concatenation in loop (BAD)
        start_time = time.perf_counter_ns()
        s = ""
        for i in range(1000):
            s += str(i)
        end_time = time.perf_counter_ns()
        print(f"String concatenation time: {end_time - start_time} ns")

        # List append + join in loop (GOOD)
        start_time = time.perf_counter_ns()
        sb_perf = []
        for i in range(1000):
            sb_perf.append(str(i))
        ''.join(sb_perf)
        end_time = time.perf_counter_ns()
        print(f"List append + join time: {end_time - start_time} ns")


if __name__ == "__main__":
    StringBuilderDemo()