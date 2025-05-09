# Program to display each character and count characters manually

def display_character(string):
    # Convert the string to lowercase
    lowercase_str = ''
    for ch in string:
        # Manual lowercase conversion (only for letters)
        if 'A' <= ch <= 'Z':
            lowercase_str += chr(ord(ch) + 32)
        else:
            lowercase_str += ch

    # Manually convert string to list of characters
    ch_list = []
    for c in lowercase_str:
        ch_list.append(c)

    count = 0

    for i in range(0, len(ch_list)):
        count += 1
        print(ch_list[i], end=", ")

    if count > 0:
        print("\nThe number of characters is:", count)

def main():
    print("Enter the string:")
    string = input()
    display_character(string)

if __name__ == "__main__":
    main()
