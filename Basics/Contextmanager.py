
#! Context Manager in Python

'''
Context managers in Python are used to manage resources, ensuring that they are properly acquired and released.
The most common use of context managers is the with statement.
'''

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
    
with FileManager("data.txt", "w") as f:
    f.write('Hello, World!')

'''
In this example, the FileManager class is a context manager that ensures the file is properly closed after it is used within the with statement.
'''