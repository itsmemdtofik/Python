def reverse_file_content(file_path: str) -> None:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Original content:\n{content}")

            # Reverse the string
            reversed_content = content[::-1]
            print(f"\nThe reversed string is:\n{reversed_content}")

    except FileNotFoundError:
        print("File does not exist")
        print("You need to create a file")


if __name__ == "__main__":
    file_path = "/Users/itsmemdtofik/Downloads/DSA-Java-Solutions/String/file1.java"
    reverse_file_content(file_path)
