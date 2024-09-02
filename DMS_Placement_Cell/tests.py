from django.test import TestCase

# Create your tests here.

# Note: Python 3.11 introduces fine-grained error locations in tracebacks, 
# which provide specific line numbers and code snippets in error messages.
# This feature is automatically utilized when running tests with Django's TestCase.

# Example of handling multiple exceptions using exception groups in Python 3.11
def example_function():
    try:
        # Some code that may raise multiple exceptions
        pass
    except* (ValueError, TypeError) as e:
        # Handle ValueError and TypeError exceptions
        e.add_note("This exception was raised due to invalid value or type.")
        print(f"Handled exceptions: {e}")
    except Exception as e:
        # Handle any other exceptions
        e.add_note("An unexpected exception occurred.")
        print(f"Unhandled exception: {e}")

# Implementing a class with Self type hint for methods returning an instance of the class
from typing import Self

class ExampleClass:
    def __init__(self, value: int):
        self.value = value

    def increment(self) -> Self:
        self.value += 1
        return self

    def decrement(self) -> Self:
        self.value -= 1
        return self
