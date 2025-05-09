#How python code works
def greet(name):
            print(f"Hello {name} !")


'''if __name__ == "__main__":
    user = "Alice"
    greet(user)'''

user = 'Alice'
greet(user)

'''
Step1: The interpreter reads from top to bottom.

Step2: It defines the greet() function but doesn't execute it yet.

Step3: Checks if this is the main program being run (__name__ == "__main__").

Step4: Creates a variable user with value "Alice".

Step5: Calls the greet() function with user as argument.

Step6: Executes the print() statement inside the function.
'''