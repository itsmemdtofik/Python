# ************************************
# Binary Tree Creation and Traversal
# ************************************

# Problem Description:
# --------------------
# Create a binary tree by taking user input. 
# If the user inputs -1, it means the node is NULL.
# After creating the tree, allow the user to perform:
# 1. Inorder Traversal (Left, Root, Right)
# 2. Preorder Traversal (Root, Left, Right)
# 3. Postorder Traversal (Left, Right, Root)
# 4. Exit the program.

# The tree should be created dynamically by asking for each node's data, 
# and its left and right children recursively.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to create the binary tree
def create():
    data = int(input("\nEnter the data: "))
    if data == -1:
        return None

    root = Node(data)
    print(f"Enter the left child of {root.data}: ")
    root.left = create()
    print(f"Enter the right child of {root.data}: ")
    root.right = create()
    return root

# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" -> ")
    inorder(root.right)

# Preorder Traversal (Root -> Left -> Right)
def preorder(root):
    if root is None:
        return
    print(root.data, end=" -> ")
    preorder(root.left)
    preorder(root.right)

# Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" -> ")

# Main function to drive the menu
def main():
    root = None

    while True:
        print("\nSelect the operation:")
        print("------------------------------")
        print("1. Create Binary Tree")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Exit")
        print("------------------------------")
        choice = int(input("Enter your choice: "))
        print("------------------------------")

        if choice == 1:
            root = create()
        elif choice == 2:
            if root is None:
                print("Tree is empty. Please create a tree first.")
            else:
                print("\nInorder Traversal:")
                inorder(root)
                print()
        elif choice == 3:
            if root is None:
                print("Tree is empty. Please create a tree first.")
            else:
                print("\nPreorder Traversal:")
                preorder(root)
                print()
        elif choice == 4:
            if root is None:
                print("Tree is empty. Please create a tree first.")
            else:
                print("\nPostorder Traversal:")
                postorder(root)
                print()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()