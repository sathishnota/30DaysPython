class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Error: {exc_value}")
        # Return False to propagate the exception, True to suppress it
        return False
with SafeFileHandler("example.txt", "w") as f:
    f.write("This file is safely managed!\n")
    # Uncomment the next line to test error handling
    # raise ValueError("Something went wrong!")
