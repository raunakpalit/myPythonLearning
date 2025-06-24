class MyCustomError(Exception):
    def __init__(self, message, error_code):
        # self.message = message
        super().__init__(message, error_code)

def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 300)
    return a/b

print(divide(4, 0))